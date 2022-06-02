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
cd .. # Go to source file
rosdep install --from-paths src --ignore-src -r -y
```
### Build workspace ###
```
cd <your_ws>
catkin_make
source <your_ws>/devel/setup.bash
```

### Launch demo ###
Launches a demo of champ walking forward on a plane with specified ground parameters and records in /data folder
```
roslaunch impact_listener start.launch
```

### Launch Script ###
Launches a shell script to recurseively record data of champ walking on different terrains at different gaits (forward,left,right,backwards)

```
roscd impact_listener/script
./start_experiment.sh
```


## Notes: ##
- Work on making plots on the trajectory difference of different terrains
- Make impact_listener/src files robust when no data directory (i.e. try: os.mkdir  (...) except (...))
- Add gazebo model path:
```
export GAZEBO_MODEL_PATH=~/champ_ws/src/terrain_champ/impact_listener/models:${GAZEBO_MODEL_PATH}
```
