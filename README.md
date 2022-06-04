# terrain_champ
Dataset of champ quadruped on different ground parameters/terrain simulated on the Gazebo platform. Different gait patterns (forward, left, right, backward), commanded velocities, ground parameters, and terrain profiles are simulated within this dataset. The goal of this repository is to provide a dataset of quadruped locomotion on different terrain profiles/paramters.


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
### Add mesh files to Gazebo model path ###
```
gedit ~/.bashrc
export GAZEBO_MODEL_PATH=~/<workspace_direction>/src/terrain_champ/impact_listener/models:${GAZEBO_MODEL_PATH}
```

## Quick Start ##
Quick start will run the champ simulator across default terrain (specified in the shell file) for different gaits and commanded velocity
```
roscd impact_listener/script/
./start_experiment.sh
```
## Data
The data that can be collected through the shell script ranges by changing these parameters:
- World - Currently support planar world and a ramp world
- Stiffness factor - Stiffness parameter defined in the model (plane/ramp)
- Damping factor - Damping parameter defined in the model (plane/ramp)
- Action - Shell script loops through forward, left, right, and backward gait motion
- Commanded velocity - Shell script loops through velocities ranging from 0.1m/s to 0.7 m/s
**The interpretation of these graphs can be summarized by the following:**
- Increased velocity of champ increases the rate of swing phase for quadruped. Stance phase is neglected here as champ controller defines a fixed stance duration
![lowerLegPosGraph](doc/cmdLowerLegPos.png)
![lowerLegVelGraph](doc/cmdLowerLegVelGraph.png)
- Different gait motions can be identified. Additionally, it is trivial to see the inherent hybrid system of quadruped locomotion
![gaitPatternLowerLegGraph](doc/gaitPatternLowerLegPos.png)
- Terrain parameters will affect the swing and stance gait motion of quadruped. For damping parameters, increase in damping affects the hinders the quadruped's swing and stance duration
![kp_graph](doc/varying_kp_LowerLegPos.png)
![kd_graph](doc/varying_kd_LowerLegPos.png)
- Different initial condition during rest phase is inherent. However, any distinct qualitative observations between the two terrain profiles cannot be concluded
![terrain_graph](doc/diff_Terrain_LowerLegPos.png)

Quantitative analysis is left to be done in future works.

## Notes/To Do: ##
- Apply rosbag to record states
- Work on making plots on the trajectory difference of different terrains
- Make impact_listener/src files robust when no data directory (i.e. try: os.mkdir  (...) except (...))
