import dynamixel_sdk as dxl
import numpy as np

ADDR_TORQUE_ENABLE          = 64
ADDR_GOAL_POSITION          = 116
LEN_GOAL_POSITION           = 4         # Data Byte Length
ADDR_PRESENT_POSITION       = 132
LEN_PRESENT_POSITION        = 4         # Data Byte Length
DXL_MOVING_STATUS_THRESHOLD = 2        # Dynamixel moving status threshold
BAUDRATE                    = 57600
PROTOCOL_VERSION            = 2.0
PORT                        = "/dev/ttyUSB0"
DXL_IDS                     = [1, 2, 3]  # [1, 2, 3, 4, 5]


def to4bytes(num):
    """
    Convert an integer or a NumPy array of integers to a list of four bytes.

    Parameters:
        num (int or numpy.ndarray): The input integer or NumPy array of integers.

    Returns:
        list: A list of four bytes, where each byte is represented as an integer.

    Examples:
        >>> to4bytes(4095)
        [255, 15, 0, 0]

        >>> import numpy as np
        >>> to4bytes(np.array([4095, 4000]))
        array([[255,  15,   0,   0],
               [160,  15,   0,   0]])
    """

    # Convert the input to a NumPy array if it's not already
    num_array = np.asarray(num)

    low_word = np.bitwise_and(num_array, 0xFFFF)
    high_word = np.right_shift(num_array, 16)
    low_byte = np.bitwise_and(low_word, 0xFF)
    high_byte = np.bitwise_and(high_word, 0xFF)
    return np.column_stack([
        dxl.DXL_LOBYTE(low_word),
        dxl.DXL_HIBYTE(low_word),
        dxl.DXL_LOBYTE(high_word),
        dxl.DXL_HIBYTE(high_word)
    ]).tolist()
    
# Initialize PortHandler and PacketHandler instance
portHandler = dxl.PortHandler(PORT)
packetHandler = dxl.PacketHandler(PROTOCOL_VERSION)  # Protocol version  2.0

# Initialize GroupSyncWrite instance
groupSyncWrite = dxl.GroupSyncWrite(portHandler, packetHandler, ADDR_GOAL_POSITION, LEN_GOAL_POSITION)

# Initialize GroupSyncRead instace for Present Position
groupSyncRead = dxl.GroupSyncRead(portHandler, packetHandler, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:  
    print("Failed to open the port")
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()

# Enable Dynamixel Torque
for id in DXL_IDS:
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, id, ADDR_TORQUE_ENABLE, 1)
    if dxl_comm_result != dxl.COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        quit()
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
        quit()
    else:
        print("Dynamixel has been successfully connected")


# Sending goal positions
# Add parameter storage for present position value
for id in DXL_IDS:
    dxl_addparam_result = groupSyncRead.addParam(id)
    if dxl_addparam_result != True:
        print("[ID:%03d] groupSyncRead addparam failed" % id)
        quit()

index = 1
dxl_goal_position_limits = [0, 4095]         # Goal position limits
random_goal_positions_np = np.random.randint(dxl_goal_position_limits[0], dxl_goal_position_limits[1], size=(len(DXL_IDS))) # Generate random goal position for each servo
random_goal_positions = to4bytes(random_goal_positions_np) # Convert to 4 byte array

# Add goal position values to the Syncwrite parameter storage
i=0
for id in DXL_IDS:
    dxl_addparam_result = groupSyncWrite.addParam(id, random_goal_positions[i])
    if dxl_addparam_result != True:
        print("[ID:%03d] groupSyncWrite addparam failed" % id)
        quit()
    i = i + 1

# Syncwrite goal position
dxl_comm_result = groupSyncWrite.txPacket()
if dxl_comm_result != dxl.COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

# Clear syncwrite parameter storage
groupSyncWrite.clearParam()


# Reading servo positions
while 1:
    # Syncread present position
    dxl_comm_result = groupSyncRead.txRxPacket()
    if dxl_comm_result != dxl.COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

    # Check if groupsyncread data of Dynamixel#1 is available
    for id in DXL_IDS:
        dxl_getdata_result = groupSyncRead.isAvailable(id, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
        if dxl_getdata_result != True:
            print("[ID:%03d] groupSyncRead getdata failed" % id)
            quit()

    # Get Dynamixel#1 present position value
    i=0
    dxl_present_position = np.array([])
    for id in DXL_IDS:
        dxl_present_position = np.append(dxl_present_position, groupSyncRead.getData(id, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION))
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d\t" % (id, random_goal_positions_np[i], dxl_present_position[-1]), end="")
        i = i + 1
    print("")

    if ((abs(random_goal_positions_np - dxl_present_position) < DXL_MOVING_STATUS_THRESHOLD).all()):
        break

