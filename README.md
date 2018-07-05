# raspi-arduino version
#run buttons_control.io on arduino
#On raspi

cd ~/ && git clone https://github.com/songshan0321/RMF_demo.git
. ~/rmf/build/ros2/install/setup.bash
cd ~/rmf/build/ros2 && ament build --symlink-install --only-packages one_button
sudo chmod 777 /dev/ttyACM0

multi_button


# raspi version
#On Raspi
cd ~/rmf/src && git clone https://github.com/songshan0321/RMF_demo.git
cd ~/rmf_ws && . install/setup.bash
cd ~/rmf_ws && ament build --symlink-install --only-packages one_button

one_button

# nanopi and comp version, connect nanopi to comp using USB to UART converter

#On nanoPi
cd ~/demo && python3 ./serialButton.py

#On COM
cd ~/ros2_ws && . install/local_setup.bash
cd ~/Downloads/RMF_demo && python3 ./button_pub.py