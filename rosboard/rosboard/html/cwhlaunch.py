#!/usr/bin/env python2
# -*- coding: utf-8 -*-



'''

launch_files = ["file1.launch", "file2.launch", "file3.launch"]

for launch_file in launch_files:
    subprocess.run(["roslaunch", launch_file])

为每个roslaunch文件启动一个独立的子进程
这可能会导致资源消耗较大
特别是在启动大量文件时。
如果需要更好地控制子进程的数量和资源消耗
可以使用并发编程库
如concurrent.futures或multiprocessing模块来实现更高效的启动方式。

'''


import rospy
import subprocess
from rosbridge_library.srv import LaunchFile, LaunchFileRequest, LaunchFileResponse

def run_roslaunch(req):
    rospy.loginfo("Starting roslaunch file...")

    if "ndt_mapping" == req.filename:
        subprocess.Popen('roslaunch lidar_localizer ndt_mapping.launch', shell=True)
    
    
    rospy.loginfo("Launch file started.")
    return {'success': True, 'message': req.filename + 'Launch file started'}

if __name__ == '__main__':
    rospy.init_node('run_roslaunch_node')
    # 创建 ROS 服务
    s = rospy.Service('/run_roslaunch', LaunchFile, run_roslaunch)

    # 预启动launch
    launch_files =[
    "/home/cwh/autoware.ai/src/autoware/utilities/runtime_manager/scripts/setup_tf.launch",
    "/home/cwh/autoware.ai/src/autoware/documentation/autoware_quickstart_examples/launch/tf_local.launch"
    ]

    for launch_file in  launch_files:
        cmd = ['roslaunch', launch_file]
        subprocess.Popen(cmd)

    rospy.loginfo("Ready to run roslaunch file.")
    rospy.spin()
