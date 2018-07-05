import serial
import time

# ROS library
import rclpy
from rmf_msgs.msg import CallButtonState

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=3.0)
state_dict = {}
bool_state = {False:0, True:1}

def main(args=None):
    # ROS init
    rclpy.init(args=args)
    node = rclpy.create_node('button_node')
    publisher = node.create_publisher(String, 'call_button_state')
    
    for i in range(16):
        # set all button state to False
        state_dict[i] = False

    try:
        while rclpy.ok():
            # Read serial msg from Arduino
            serial = port.readline()
            print("Read: " + repr(serial))

            for i in range(len(serial)):
                if serial[i] != bool_state[state_dict[i]]: # button state change
                    # Update msg
                    msg.id = "bed_" + str(i) + "_button"
                    msg.pressed = bool(state_dict[i])
                    # Log & publish msg
                    node.get_logger().info("%s,%s" % (msg.id,msg.pressed))
                    publisher.publish(msg)
                    
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()