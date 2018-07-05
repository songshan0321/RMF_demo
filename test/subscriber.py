import rclpy

from rmf_msgs.msg import CallButtonState

g_node = None
state_dict = {}

def chatter_callback(msg):
    global g_node
    # g_node.get_logger().info(
        # 'I heard: "%s,%s"' % (msg.id,msg.pressed))
    state_dict[msg.id] = msg.pressed
    print(state_dict)

def main(args=None):
    global g_node
    rclpy.init(args=args)

    g_node = rclpy.create_node('subscriber_node')

    subscription = g_node.create_subscription(CallButtonState, 'call_button_state', chatter_callback)
    subscription  # prevent unused variable warning

    while rclpy.ok():
        rclpy.spin_once(g_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    g_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()