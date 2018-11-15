cmake_minimum_required(VERSION 2.8.3)
project(rplidar_ros)

set(RPLIDAR_SDK_PATH "./sdk/")

FILE(GLOB RPLIDAR_SDK_SRC 
  "${RPLIDAR_SDK_PATH}/src/arch/linux/*.cpp"
  "${RPLIDAR_SDK_PATH}/src/hal/*.cpp"
  "${RPLIDAR_SDK_PATH}/src/*.cpp"
)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rosconsole
  sensor_msgs
  
  rospy
  std_msgs
  message_generation
)

include_directories(
  ${RPLIDAR_SDK_PATH}/include
  ${RPLIDAR_SDK_PATH}/src
  ${catkin_INCLUDE_DIRS}
)


add_service_files(
   FILES
   angle.srv
#   Service2.srv
 )

# Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES entrainement
  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)



include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)



add_executable(rplidarNode src/node.cpp ${RPLIDAR_SDK_SRC})
target_link_libraries(rplidarNode ${catkin_LIBRARIES})

add_executable(rplidarNodeClient src/client.cpp)
target_link_libraries(rplidarNodeClient ${catkin_LIBRARIES})

install(TARGETS rplidarNode rplidarNodeClient
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch rviz sdk
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
)
