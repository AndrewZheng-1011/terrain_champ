#!/bin/bash


for i in {0..1}
do
        echo "Running instance $j"
        for speedMult in {0..2}
        do
                roslaunch impact_listener start.launch
        done
done