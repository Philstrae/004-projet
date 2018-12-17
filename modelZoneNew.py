# -*- coding:utf8 -*-

import json
import math

class Agent:

    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name

    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
                setattr(self, attr_name, attr_value)

class Position:                

    def __init__(self, longitude_degrees, latitude_degrees):
        self.longitude_degrees = longitude_degrees
        self.latitude_degrees = latitude_degrees 

    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        return self.latitude_degrees * math.pi / 180          

class Zone:
    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabi

def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop('latitude')
        longitude = agent_attributes.pop('longitude')
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        print(agent.position.longitude_degrees, agent.position.latitude_degrees)

main()            