import roboticstoolbox as rtb
from math import pi


def get_robot_config_1(link1 = 0.3, link2 = 0.3, link3 = 0.3, link4 = 0.14,
                       link1_offset = 0.0, link2_offset = 0.0, link3_offset = 0.0, 
                       link4_offset = 0.0):
    """
    Create and return a DHRobot object representing a robot configuration.

    Parameters:
        link1 (float): Length of link 1.
        link2 (float): Length of link 2.
        link3 (float): Length of link 3.
        link4 (float): Length of link 4.
        link1_offset (float): Offset of link 1 along the X-axis of the first joint.
        link2_offset (float): Offset of link 2 along the Z-axis of the second joint.
        link3_offset (float): Offset of link 3 along the Z-axis of the third joint.
        link4_offset (float): Offset of link 4 along the X-axis of the fourth joint.

    Returns:
        DHRobot: Robot object representing the specified configuration.

    """
    return rtb.DHRobot(
        [
            rtb.RevoluteDH(d=link1, a=link1_offset, alpha=pi/2, qlim=[-90 *pi/180, 90 *pi/180]), 
            rtb.RevoluteDH(a=link2, d=link2_offset, qlim=[-90 *pi/180, 90 *pi/180]),
            rtb.RevoluteDH(a=link3, d=link3_offset, qlim=[-90 *pi/180, 90 *pi/180]),
            rtb.RevoluteDH(alpha=pi/2,          qlim=[-90 *pi/180, 90 *pi/180]),
            rtb.RevoluteDH(d=link4, a=link4_offset, qlim=[-180 *pi/180, 180 *pi/180]),
        ], name="My Config 1 Robot")

