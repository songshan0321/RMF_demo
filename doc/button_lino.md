# Demo: ROS 2 buttons trigger ROS 1 Linorobot

### Step1: start a button hub
ssh into raspi, allows permission to arduino port, run multi_button package:
```
raspi
arduino
multi_button
```
### Step2: start a ROS 1 roscore
Because part of this system uses ROS 1, we need a `roscore` running.
In another terminal, run a ROS1 roscore.
```
rmf_ros1
roscore
```

### Step3: start call_center server
Subscribe CallButtonState() and publish CallButtonStateArray in ROS 2
```
rmf_ros2
call_center
```

### Step4: translate ROS 2 messages to ROS 1
In another terminal, source the SOSS libraries and start a SOSS instance:
```
soss
cd ~/rmf/src/soss/soss
./soss.py ../configs/call_ros2_ros1.yaml
```

### Step5: receive messages in ROS 1
In another terminal, run the `rostopic echo` command:
```
rmf_ros1
rostopic echo /call_button_state_array
```










