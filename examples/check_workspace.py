#!/usr/bin/env python

from adatools import config_generator as cg
from adatools import plotting_tools as pt
from spatialmath import SE3
import numpy as np  
import time

# This example shows how to check if your robot can reach all the corners of the base plate.
# If you see that the translational o andular distance is too large, the manipulability is close to zero or the Jacobian of the robot loses rank (rank < 5), you should consider changing the robot's link lengths and offsets.

# Create a robot based on config1
robot = cg.get_robot_config_1(link1=0.3, link1_offset=0.0,
                              link2=0.3, link2_offset=0.0,
                              link3=0.2, link3_offset=0.0,
                              link4=0.1, link4_offset=0.0)

robot_plot = robot.plot(robot.qr, backend='pyplot') # plot the robot in its home position
pt.plot_baseplate(robot_plot)  # plot the base plate

# Define the goal poses
Tgoals = SE3([SE3(0.3, 0, 0.2),
              SE3(0.3, 0, 0),
              SE3(0, 0.55/2, 0.2),
              SE3(0, 0.55/2, 0),
              SE3(0, -0.55/2, 0.2),
              SE3(0, -0.55/2, 0),
              SE3(0.6, 0.55/2, 0.2),
              SE3(0.6, 0.55/2, 0),
              SE3(0.6, -0.55/2, 0.2),
              SE3(0.6, -0.55/2, 0)]) * SE3.Rx(180, 'deg')

Tgoals.plot(ax=robot_plot.ax, length=0.1, style='rgb') # plot all goal poses

# Check if robot can reach the goal poses
sol = []
i = 0
for Tg in Tgoals:
    sol.append(robot.ikine_LM(Tg, q0=robot.qr, mask=[1,1,1,0.5,0.5,1])) # inverse kinematics
    robot.q = sol[i].q
    robot_plot.step()

    T = robot.fkine(robot.q) # forward kinematics
    angular_distance = Tg.angdist(T)
    trans_distance = np.linalg.norm(Tg.t - T.t)
    manip = robot.manipulability(robot.q, method='minsingular', axes='all')
    J_rank = np.linalg.matrix_rank(robot.jacob0(robot.q))
    print("Pose %03d : Translational distance (norm): %0.4f, Angular distance (geodesic norm): %0.4f, Manipulability: %.4g, Jacobian Rank: %d" \
           %(i, trans_distance, angular_distance, manip, J_rank))
    i = i + 1
    input("Press Enter in terminal to continue...")
    #time.sleep(2)

