# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:06:12 2022

@author: an
"""


class Oven:
    # Attributes
    color: str
    material: str
    temperature: int
    weight: int
    
    # Methods
    def init(self) -> None:

    def door_open(self):
        
    def door_close(self):
        
    def fuel_add(self):
        self.door_open()
        fuel = fuel + x
        self.door_close()
        
    def fuel_get(self):
        
    def ashes_remove(self):
        
        self.door_open()
        ashes = ashes - y
        self.door_close()
        
    def temperature_check(self):
        if self.temperature < 35:
            return "cold"
        elif self.temperature < 55:
            return "warm"
        elif self.temperature >= 55:
            return "hot!"
            
        