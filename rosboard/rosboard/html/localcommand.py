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

import time
import os
import rospy
import subprocess
# from rosbridge_library.srv import LaunchFile, LaunchFileRequest, LaunchFileResponse
from rosbridge_library.srv import Command, CommandRequest, CommandResponse

rosbag_proc = None
rosbag_filename = ""

def run_callback(req):
    # rospy.loginfo("Starting roslaunch file...")
    global rosbag_proc, rosbag_filename
    # 启动ndt相关命令
    if "ndt_mapping" == req.tag:
        pass
        # launch_files =[
        #     "/home/cwh/autoware.ai/src/autoware/utilities/runtime_manager/scripts/setup_tf.launch",
        #     "/home/cwh/autoware.ai/src/autoware/documentation/autoware_quickstart_examples/launch/tf_local.launch"
        # ]
        # for launch_file in  launch_files:
        #     cmd = ['roslaunch', launch_file]
        #     subprocess.Popen(cmd)
        # subprocess.Popen('roslaunch lidar_localizer ndt_mapping.launch', shell=True)
    
    if "rosbag_start" == req.tag:
        try:
            rosbag_filename = req.cmd[0]
            rosbag_proc = subprocess.Popen('rosbag record -a -O' + rosbag_filename + ' __name:=my_bag', shell=True)
            rospy.loginfo("启动成功")
        except Exception as e:
            rospy.loginfo("启动失败")
            print(str(e))

    if "rosbag_stop" == req.tag:
        try:
            if rosbag_proc is not None:
                print(rosbag_filename + "===========")
                subprocess.call(["rosnode", "kill", "/my_bag"])
                # rosbag_proc.terminate()
                # rosbag_proc.kill()
                # os.kill(rosbag_proc.pid, subprocess.signal.SIGINT)
                # rosbag_proc.send_signal()
                # os.rename(rosbag_filename + ".active", rosbag_filename)
                # subprocess.Popen('rosbag reindex' + rosbag_filename, shell=True)
                rosbag_proc = None
                rosbag_filename = ""
                rospy.loginfo("停止成功")
            else:
                rospy.loginfo("停止失败　还没开始录制")
        except Exception as e:
            rospy.loginfo("停止失败")
            print(str(e))
        

    return {'success': True, 'message': req.tag}

if __name__ == '__main__':
    rospy.init_node('run_roslaunch_node')
    # 创建 ROS 服务
    s = rospy.Service('/run_localcommand', Command, run_callback)

    # 预启动launch
    rospy.loginfo("Ready to run roslaunch file.")
    rospy.spin()
