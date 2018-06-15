import time
import RPi.GPIO as GPIO

# ROS library
import rclpy
from std_msgs.msg import String

# GPIO declaration
LED_PIN = 7
BTN_PIN_1 = 12
BTN_PIN_2 = 16
BTN_PIN_3 = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(BTN_PIN_1,GPIO.IN)
GPIO.setup(BTN_PIN_2,GPIO.IN)
GPIO.setup(BTN_PIN_3,GPIO.IN)

btn_state_1 = False
btn_state_2 = False
btn_state_3 = False
bed_dict = {12:"B01", 16:"B02", 18:"B03"}
logic_dict = {True:"S1", False:"S0"}

def led_update():
	if btn_state_1 == True or btn_state_2 == True or btn_state_3 == True:
		GPIO.output(LED_PIN,True)
	else:
		GPIO.output(LED_PIN,False)

def main(args=None):
    # ROS init
    rclpy.init(args=args)
    node = rclpy.create_node('button_node')
    publisher = node.create_publisher(String, 'button')
    msg = String()    

    while rclpy.ok():
        btn_state_1 = GPIO.input(BTN_PIN_1)
        btn_state_2 = GPIO.input(BTN_PIN_2)
        btn_state_3 = GPIO.input(BTN_PIN_3)
        
        msg.data = bed_dict[BTN_PIN_1] + logic_dict[btn_state_1] + " " + bed_dict[BTN_PIN_2] + logic_dict[btn_state_2] + " " + bed_dict[BTN_PIN_3] + logic_dict[btn_state_3]
        print("msg: " + msg.data)
        node.get_logger().info("%s" % msg.data)
        publisher.publish(msg)
        time.sleep(0.1)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()