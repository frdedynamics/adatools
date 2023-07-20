import dynamixel_sdk as dxl

portHandler = dxl.PortHandler("/dev/ttyUSB0")
packetHandler = dxl.PacketHandler(2.0)  # Protocol version  2.0

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:  
    print("Failed to open the port")
    quit()

# Set port baudrate
if portHandler.setBaudRate(57600):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()

# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, 1, 64, 1)
if dxl_comm_result != dxl.COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    quit()
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
    quit()
else:
    print("Dynamixel has been successfully connected")


dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, 1, 116, 2000)