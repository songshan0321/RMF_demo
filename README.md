# raspi version
#ssh into raspi

ssh songshan@10.12.60.1

#On Raspi

cd ~/ros2_ws && . install/local_setup.bash

cd ~/Downloads/RMF_demo && python3 ./one_button.py




# nanopi and comp version, connect nanopi to comp using USB to UART converter

#ssh into nanopi

ssh root@192.168.1.21

#On nanoPi

cd ~/demo && python3 ./serialButton.py

#On COM

cd ~/ros2_ws && . install/local_setup.bash

cd ~/Downloads/RMF_demo && python3 ./button_pub.py
