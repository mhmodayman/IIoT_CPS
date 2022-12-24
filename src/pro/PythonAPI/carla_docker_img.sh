#!/bin/sh

#sudo docker run -d -p 2000-2002:2000-2002 --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 carlasim/carla:0.9.13 /bin/bash CarlaUE4.sh -RenderOffScreen -quality-level=Low
sudo docker run -d -p 2000-2002:2000-2002 --gpus all -e NVIDIA_VISIBLE_DEVICES=0 carlasim/carla:0.9.13 /bin/bash CarlaUE4.sh -RenderOffScreen -quality-level=Low

#source ~/carla-ros-bridge/catkin_ws/devel/setup.bash

# Option 1: start the ros bridge
#roslaunch carla_ros_bridge carla_ros_bridge.launch

# Option 2: start the ros bridge together with an example ego vehicle
#roslaunch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch

#sudo docker run -d -p 2000-2002:2000-2002 --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 carlasim/carla:0.9.13 /bin/bash CarlaUE4.sh -RenderOffScreen -quality-level=Low

#sudo docker run -e SDL_VIDEODRIVER=x11 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -d -p 2000-2002:2000-2002 -it --gpus all carlasim/carla:0.9.13 ./CarlaUE4.sh -RenderOffScreen -quality-level=Low
