import yaml
from world import World

def create_world ():
    with open('config.yaml') as cfgfile:
        cfg = yaml.load(cfgfile)
    return World(cfg)
