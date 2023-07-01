#!/usr/bin/env python

# ------------------------------------------------------------------------ #
# This example script shows how to generate a kinematic configuration
# for your robot with the config_generator. The config_generator is a helper
# function that exposes the parameters of a DHRobot (-> roboticstoolbox) that
# you are supposed to modify and returns the DHRobot object.
# ------------------------------------------------------------------------ #

from adatools import config_generator as cg


my_conf1_robot = cg.get_robot_config_1(link1=0.3, link1_offset=0.0,
                                       link2=0.3, link2_offset=0.0,
                                       link3=0.3, link3_offset=0.0,
                                       link4=0.2, link4_offset=0.0)

print(my_conf1_robot)   # prints the DHParameters of the robot
my_conf1_robot.teach(my_conf1_robot.q)  # shows the robot in a plot with sliders to drive the joints