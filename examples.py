# Examples.py
from __future__ import print_function

from circuits import *
from resistance_examples import *



circuit1 = [(0,0,[Battery(6),Resistor(2)])]

print("Solving the following circuit:")

printCircuit(circuit1)

print("The current is as follows:")

print(finalCurrents(circuit1))

wait()

circuit2 = [(0,0,[Battery(4),Battery(3),Resistor(2),Resistor(2)])]

print("Resistors and batteries behave properly in series. This prints out " +
"the currents in the one connection in the circuit.")

printCircuit(circuit2)

print(finalCurrents(circuit2))

wait()

circuit3 = [(0,1,[Battery(4)]),
            (1,0,[Resistor(4)]),
            (1,0,[Resistor(4)])]

print("Resistors behave properly in parallel. The three numbers printed out " +
    "are the three different currents in the respective connections.")


printCircuit(circuit3)

print(finalCurrents(circuit3))

wait()

print("The function which finds resistance works in complex situations, like a cube of resistors. "
     + "See http://web.physics.ucsb.edu/~lecturedemonstrations/Composer/Pages/64.42.html")

cube_circuit=[(0,1),(0,2),(1,3),(2,3),
              (4,5),(4,6),(5,7),(6,7),
              (0,4),(1,5),(2,6),(3,7)]

circuit2 = graphToDetails(cube_circuit)

print(findResistanceBetweenNodes(circuit2,0,7))

wait()

print("I can approximate the knight's move problem (http://xkcd.com/356/). " +
 "According to the internet, the correct answer is about 0.773.")

circuit3=graphToDetails(make_lattice(10,10))

    # print(circuit3)
# print(findResistanceBetweenNodes(circuit3,coords_to_point)
  #      (5,5,10), coords_to_point(6,7,10))

wait()

circuit4 = [(0,0,[Battery(1),Resistor(1),Capacitor(1)])]

print("Capacitors work properly. This graphs the current in the circuit and the charge in the capacitor over time.")

printCircuit(circuit4)

evolve(circuit4,None,2,0.001,0.1)

wait()

circuit5 = [(0,0,[Battery(2),Resistor(2),Capacitor(1)])]

print("The prediction of RC time constant holds. Again, the graph is of current and charge in the capacitor.")


printCircuit(circuit5)

evolve(circuit5,None,2,0.001,0.1)

wait()

print("Capacitors work properly in series.")

circuit6 = [(0,0,[Battery(2),Resistor(2),Capacitor(1),Capacitor(1)])]

printCircuit(circuit6)

evolve(circuit6,None,2,0.001,0.1)

wait()

print("Capacitors work properly in parallel")

circuit7 = [(0,1,[Battery(2),Resistor(1)]),
            (1,0,[Capacitor(1)]),
            (1,0,[Capacitor(1)])]

printCircuit(circuit7)

evolve(circuit7,None,2,0.001,0.1)

wait()

print("Capacitors with breakdown work properly.")

circuit=[(0,1,[Battery(5),Resistor(1)]),
        (1,0,[Capacitor_With_Breakdown(1,showing=True)])]

evolve(circuit,None,2,0.001,0.005)
