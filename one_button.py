#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

# ROS library
import rclpy
from std_msgs.msg import String
from rmf_msgs.msg import CallButtonState

# GPIO declaration
LED_PIN = 7
BTN_PIN_1 = 12
# BTN_PIN_2 = 16
# BTN_PIN_3 = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(BTN_PIN_1,GPIO.IN)
# GPIO.setup(BTN_PIN_2,GPIO.IN)
# GPIO.setup(BTN_PIN_3,GPIO.IN)

btn_state_1 = False
# btn_state_2 = False
# btn_state_3 = False
bed_dict = {12:"bed_0_button", 16:"bed_1_button", 18:"bed_2_button"}

# def led_update():
#     # if btn_state_1 == True or btn_state_2 == True or btn_state_3 == True:
#     if btn_state_1 == True:
#         GPIO.output(LED_PIN,GPIO.HIGH)
#     else:
#         GPIO.output(LED_PIN,GPIO.LOW)

def main(args=None):
    # ROS init
    rclpy.init(args=args)
    node = rclpy.create_node('button_node')
    publisher = node.create_publisher(CallButtonState, 'call_button_state')
    msg = CallButtonState()

    while rclpy.ok():
        btn_state_1 = GPIO.input(BTN_PIN_1)
        # btn_state_2 = GPIO.input(BTN_PIN_2)
        # btn_state_3 = GPIO.input(BTN_PIN_3)

        msg.id = bed_dict[BTN_PIN_1]
        msg.pressed = bool(btn_state_1)
        print("msg: " + msg.id + ", " +  str(msg.pressed))
        node.get_logger().info("%s,%s" % (msg.id,msg.pressed))
        publisher.publish(msg)
        if btn_state_1 == True:
            GPIO.output(LED_PIN,GPIO.HIGH)
        else:
            GPIO.output(LED_PIN,GPIO.LOW)
        time.sleep(0.1)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
