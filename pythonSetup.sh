#!/bin/bash

#Maybe Run chmod +x ./pythonSetup.sh
#Run sudo-root ./pythonSetup.sh

ISAACPATH="/pvc/isaac-sim"
ISAAC_PYTHON="$ISAACPATH/python.sh"

export ISAACPATH=$ISAACPATH
export ISAAC_PYTHON=$ISAAC_PYTHON

ipython="sudo-root $ISAAC_PYTHON"

# ipython -m pip install --upgrade pip
$ipython -m pip install -e source/b1_walk
$ipython scripts/list_envs.py

alias ipython="$ipython"
# $ipython scripts/skrl/train.py --task=Template-B1-Walk-v0