cmake_minimum_required(VERSION 2.8.3)
project(rosboard)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  sensor_msgs
  # message_generation #自定义消息类型依赖  自定义重点
)

# add_service_files(
#   FILES
#   LaunchFile.srv
# )

catkin_python_setup()

# generate_messages(
#   DEPENDENCIES
#   std_msgs #自定义重点
# )

catkin_package(
  # CATKIN_DEPENDS message_runtime
)


catkin_install_python(PROGRAMS
  nodes/rosboard_node
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
