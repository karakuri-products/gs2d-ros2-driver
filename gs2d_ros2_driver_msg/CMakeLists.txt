find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "msg/TargetPosition.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
 )
