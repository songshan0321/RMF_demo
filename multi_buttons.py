import serial
import time

# ROS library
import rclpy
from rmf_msgs.msg import CallButtonState

port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3.0)
state_dict = {}
bool_state = {False:0, True:1}

def main(args=None):
    # ROS init
    rclpy.init(args=args)
    node = rclpy.create_node('button_node')
    publisher = node.create_publisher(CallButtonState, 'call_button_state')
    msg = CallButtonState()

    for i in range(16):
        # set all button state to False
        state_dict[i] = False

    try:
        while rclpy.ok():
            # Read serial msg from Arduino
            serial = repr(port.readline())[2:-5]
            print("Read: " + serial)
            # print("length: " + str(len(serial)))

            length = len(serial)
            
            # handle serial input error
            if length != 16:
                print("Wrong Serial Length, ignore the msg")
            else:
                for i in range(length):
                    serial_binary = int(serial[i])
                    state_binary = int(bool_state[state_dict[i]])

                    if serial_binary != state_binary: # button state change

                        # Update state_dict
                        state_dict[i] =  bool(serial_binary)

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
        print("Quit")

if __name__ == '__main__':
    main()
