# things that don't work

from circuits import *

circuit= [(0,0,[Battery(1),Resistor(1),Inductor(1)])]

evolve(circuit,0.01,0.0001,0.0001,False)


# Things below here are things that used to break but don't anymore.

circuit2 = [(0,0,[Battery(5),Resistor(10000),Capacitor(0.00001,showing=True)])]

evolve(circuit2,0.5,0.0001,0.005)
