# Demo: Call Button with raspi and arduino IO pins

### Step1: Upload code to arduino
[Arduino code](/multi_button/button_control/button_control.io) 

### Step2: start a button hub
On Raspi
Change permission to arduino port, run multi_button package. 
```
. ~/rmf/build/ros2/setup.bash
sudo chmod 777 /dev/ttyACM0
multi_button
```
