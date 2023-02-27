#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
import subprocess
from rosbridge_library.srv import LaunchFile, LaunchFileRequest, LaunchFileResponse

def run_roslaunch(req):
    print('cwh', req.filename)

    rospy.loginfo("Starting roslaunch file...")
    # 启动 roslaunch 文件

    launch_files =[
    "/home/cwh/autoware.ai/src/autoware/utilities/runtime_manager/scripts/setup_tf.launch",
    "/home/cwh/autoware.ai/src/autoware/documentation/autoware_quickstart_examples/launch/tf_local.launch"
    ]

    for launch_file in  launch_files:
        cmd = ['roslaunch', launch_file]
        subprocess.Popen(cmd)
    
    # subprocess.call(["roslaunch", launch_file])
    rospy.loginfo("Launch file started.")
    return {'success': True, 'message': 'setup_tf launch finish'}

if __name__ == '__main__':
    rospy.init_node('run_roslaunch_node')
    # 创建 ROS 服务
    s = rospy.Service('/run_roslaunch', LaunchFile, run_roslaunch)
    rospy.loginfo("Ready to run roslaunch file.")
    rospy.spin()
