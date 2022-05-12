# terrain_champ
Simulation of champ quadruped on different ground parameters/terrain


Notes:
- Work on making plots on the trajectory difference of different terrains
- Make impact_listener/src files robust when no data directory (i.e. try: os.mkdir  (...) except (...))
- Add gazebo model path:
```
export GAZEBO_MODEL_PATH=~/champ_ws/src/terrain_champ/impact_listener/models:${GAZEBO_MODEL_PATH}
```
