# Installation of ROS_Button

Download ROS_Button
```
cd ~/rmf/build/ros2/src
git clone https://github.com/songshan0321/ROS_Button.git
```

Install ROS_Button
```
. ~/rmf/build/ros2/install/setup.bash
cd ~/rmf/build/ros2
ament build --symlink-install --only-packages multi_button --only-packages one_button
```
