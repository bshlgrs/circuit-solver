from helpers import *
import math


class Component:
    def __init__():
        pass
    def show(self):
        pass
    def data(self):
        pass
    def getResistance(self):
        return 0.0
    def getVoltage(self):
        return 0.0
    def getCurrent(self):
        return 0.0
    def getInductance(self):
        return 0.0
    def updateSelf(self,timestep,current):
        pass

class Battery(Component):
    def __init__(self,voltage):
        self.voltage=float(voltage)
    def show(self):
        return "%s V battery"%self.voltage
    def getVoltage(self):
        return self.voltage
    def updateSelf(self,timestep,current):
        pass

class Resistor(Component):
    def __init__(self,resistance):
        self.resistance=float(resistance)
    def show(self):
        return "%s Ohm resistor"%self.resistance
    def getResistance(self):
        return self.resistance
    def updateSelf(self,timestep,current):
        pass

class Non_Ohmic_Resistor(Component):
    def __init__(self,resistance,maxVoltage,pastCurrent=0):
        self.resistance=float(resistance)
        self.maxVoltage=float(maxVoltage)
        self.pastCurrent=pastCurrent
        self.maxCurrent = maxVoltage/resistance
        print self.maxCurrent
    def show(self):
        return "%s Ohm resistor with max voltage %s" \
            %(self.resistance, self.maxVoltage)
    def getResistance(self):
        return self.resistance
    def getCurrent(self):
        #if self.pastCurrent < - self.maxCurrent:
            #return (-self.maxCurrent+self.pastCurrent)/3
        if self.pastCurrent > self.maxCurrent:
            return (self.maxCurrent - self.pastCurrent)/1.3
        return 0
    def updateSelf(self,timestep,current):
        self.pastCurrent=current

class Capacitor(Component):
    def __init__(self,capacitance,charge=0,showing=False):
        self.capacitance=float(capacitance)
        self.charge=float(charge)
        self.showing=showing
    def show(self):
        return "%s Farad capacitor, with %s Coulombs of charge"% \
                (self.capacitance,self.charge)
    def data(self):
        return self.charge
    def getVoltage(self):
        return self.charge/self.capacitance
    def updateSelf(self,timestep,current):
        self.charge-= current*timestep

class Capacitor_With_Breakdown(Component):
    def __init__(self,capacitance,charge=0,breakdown=1,showing=False):
        self.capacitance=float(capacitance)
        self.charge=float(charge)
        self.showing=showing
        self.breakdown=breakdown
        self.current=0
    def show(self):
        return "%s Farad capacitor, with %s Coulombs of charge"% \
                (self.capacitance,self.charge)
    def data(self):
        return self.charge
    def getVoltage(self):
        if self.charge< -self.breakdown:
            return 0
        if self.charge> self.breakdown:
            return 0
        return self.charge/self.capacitance

    def updateSelf(self,timestep,current):
        self.charge-= current*timestep
        self.current=current
        if self.charge< -self.breakdown:
            self.charge= -self.breakdown
        if self.charge> self.breakdown:
            self.charge= self.breakdown
        
class IncreasingVoltage(Component):
    def __init__(self):
        self.voltage=0
    def show(self):
        return "Increasing voltage"
    def getVoltage(self):
        return self.voltage
    def updateSelf(self,timestep,current):
        self.voltage+=timestep

class CurrentSource(Component):
    def __init__(self,current):
        self.current=current
    def show(self):
        return "%s A current source"%self.current
    def getCurrent(self):
        return self.current

class Inductor(Component):
    def __init__(self,inductance,current=0):
        self.inductance=inductance
        self.current=0
    def show(self):
        return "%s Henry inductor"%self.inductance
    def getInductance(self):
        return self.inductance
