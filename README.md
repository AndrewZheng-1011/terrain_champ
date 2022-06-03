# terrain_champ
Simulation of champ quadruped on different ground parameters/terrain

Modification of champ installation procedure

## Installation (To be tested): ##
### Install Dependencies ###
```
sudo apt install -y python-rosdep
cd <your_ws>/src
git clone --recursive https://github.com/AndrewZheng-1011/terrain_champ.git
git clone https://github.com/chvmp/champ_teleop
cd ..
rosdep install --from-paths src --ignore-src -r -y
```
### Build workspace ###
```
cd <your_ws>
catkin_make
source <your_ws>/devel/setup.bash
```

## Quick Start ##
```
roscd impact_listener/script/
./start_experiment.sh
```



## Notes/To Do: ##
- Apply rosbag to record states
- Work on making plots on the trajectory difference of different terrains
- Make impact_listener/src files robust when no data directory (i.e. try: os.mkdir  (...) except (...))
- Add gazebo model path to ~/.bashrc file:
```
export GAZEBO_MODEL_PATH=~/<workspace_direction>/src/terrain_champ/impact_listener/models:${GAZEBO_MODEL_PATH}
```
