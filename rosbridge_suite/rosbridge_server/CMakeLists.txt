cmake_minimum_required(VERSION 3.0.2)
project(rosbridge_server)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS
  scripts/rosbridge_websocket.py
  scripts/rosbridge_websocket
  scripts/rosbridge_tcp.py
  scripts/rosbridge_tcp
  scripts/rosbridge_udp
  scripts/rosbridge_udp.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(FILES
  launch/rosbridge_websocket.launch
  launch/rosbridge_tcp.launch
  launch/rosbridge_udp.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

if (CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(test/websocket/test_smoke.test)
endif()
