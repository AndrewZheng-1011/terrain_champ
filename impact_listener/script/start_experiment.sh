#!/bin/bash


# Notes:
#       1) Representing more action (side to side or left and then right repeated)
#               - Or clockwise and counterclockwise
#       2) Modify xacro file of champ s.t. can change kp and kd values through script
environment='rampWorld'
worldFilePath="$HOME/champ_ws/src/terrain_champ/impact_listener/worlds/rampWorld_kp_100e10_kd_100.world"
#"/home/andrewzheng1011/champ_ws/src/impact_listener/worlds/planeWorld.world"

time2Term="7" # seconds
actions=('forward' 'backward' 'left' 'right')
gui="false" # false to run in "headless" mode
spawnHeight="0.6" # Spawn height for plane > 1.0m and < 1.5m (#1.2 seems good for blue plane and 0.6 for empty world)


for action in "${actions[@]}"
do
        for speedMult in {1..2} # Base speed: 0.1 with speed_mult --> speed = base * speedMult
        do
                if [ $speedMult -eq 1 ]
                then
                        gui="true"
                fi
                #echo $gui
                echo "Running action $action with environment: $environment"
                echo "---------------------------------------------------"
                echo "Speed Multipler: $speedMult"
                roslaunch impact_listener start.launch suffix_2:=$environment quad_cmd:=$action \
                speed_mult:=$speedMult time2Terminate:=$time2Term height_spawn:=$spawnHeight worldFile:=$worldFilePath \
                gui:=$gui
                gui="false"
        done
done
