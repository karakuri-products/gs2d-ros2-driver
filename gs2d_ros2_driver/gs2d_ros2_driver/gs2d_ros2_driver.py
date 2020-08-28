import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class Gs2dRos2Driver(Node):
    def __init__(self):
        super().__init__('gs2d_ros2_driver')

        self.pub_current_position = self.create_subscription(Float32, '/gs2d_ros2_driver/current_position')
        self.sub_target_position = self.create_subscription(Float32, '/gs2d_ros2_driver/target_position')


def main(args=None):
    rclpy.init(args=args)
    node = Gs2dRos2Driver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
