# Collision Avoidance Example

This is an example of using a Salty synthesized controller to control unmanned air vehicles (UAVs) following the collision avoidance protocol for UAVs in an airspace with multiple altitude layers.

## Prerequisite

- Python 2
- Salty
- Pygame
`sudo pip install pygame`
- Jinja2
`sudo pip install jinja2`

## Steps:
- Generate the controller
`./gen_ctrl.sh`
First, this script will generate ctrl.salt by running the script gen_ltl.py which uses ltl_temp.tl as a template. then will invoke salty on ctrl.salt and generate a concrete implementation of the controller in python.
- Run the simulation
`python simulation.py`
