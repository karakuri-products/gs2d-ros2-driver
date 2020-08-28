import rclpy
from rclpy.node import Node
from gs2d_ros2_driver_msg.msg import TargetPosition, TorqueEnable


class Gs2dRos2Driver(Node):
    def __init__(self):
        super().__init__('gs2d_ros2_driver')

        self.get_logger().info('Yes! initializing...')

        # self.pub_current_position = self.create_publisher(Float32, '/gs2d_ros2_driver/current_position', 10)

        self.sub_target_position = self.create_subscription(
            TargetPosition,
            '/gs2d_ros2_driver/target_position',
            self.target_position_callback,
            10
        )

        self.sub_torque_enable = self.create_subscription(
            TorqueEnable,
            '/gs2d_ros2_driver/torque_enable',
            self.torque_enable_callback,
            10
        )

        # timer_period = 0.5
        # self.timer = self.create_timer(timer_period, self.timer_callback)

    def target_position_callback(self, msg):
        self.get_logger().info('subscribe target position: {} (id: {})'.format(msg.data, msg.servo_id))

    def torque_enable_callback(self, msg):
        self.get_logger().info('subscribe torque enable: {} (id: {})'.format(msg.data, msg.servo_id))

    # def timer_callback(self):
    #     self.get_logger().info('Yes! initializing...')


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
