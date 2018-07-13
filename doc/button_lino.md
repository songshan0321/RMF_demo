# Demo: ROS 2 buttons trigger ROS 1 Linorobot

Please follow the Arduino setup instruction by following step1 from [this instruction](doc/multi_button).

### Step1: start a button hub

ssh into raspi, allows permission to arduino port, run multi_button package:
```bash
$ rpi
$ . ~/rmf/build/ros2/install/setup.bash
$ sudo chmod 777 /dev/ttyACM0
$ multi_button
```
### Step2: start a ROS 1 roscore

Because part of this system uses ROS 1, we need a `roscore` running.
In another terminal, run a ROS1 roscore.
```bash
$ . ~/rmf/build/ros1/setup.bash
$ roscore
```

### Step3: start call_center server
Subscribe CallButtonState() and publish CallButtonStateArray in ROS 2
```bash
$ . ~/rmf/build/ros2/setup.bash
$ call_center
```

### Step4: translate ROS 2 messages to ROS 1
In another terminal, source the SOSS libraries and start a SOSS instance:
```bash
$ soss
$ cd ~/rmf/src/soss/soss
$ ./soss.py ../configs/call_ros2_ros1.yaml
```

### Step5: receive messages in ROS 1
In another terminal, run the `rostopic echo` command:
```bash
$ . ~/rmf/build/ros1/setup.bash
$ rostopic echo /call_button_state_array
```

### Step6: Create a fake turtlebot node

In another terminal,

```bash
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

### Step7: Run navigation stack
In another terminal,
```bash
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
```

### Step9: Open rviz GUI (Optional)
In another terminal,
```bash
$ roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch
```

### Step10: Run action client
In another terminal, it will trigger robot to move 1 meter once the msg changed to true.
```bash
$ rosrun simple_navigation_goals simple_navigation_goals
```











