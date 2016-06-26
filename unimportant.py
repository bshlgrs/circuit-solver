from circuits import *

#circuit3 = [(1,0,[Resistor(2),Resistor(2)]),
            #(0,1,[Resistor(4)])]

#print solveCurrents(circuit3)

#print findResistanceAtNodes(circuit3,1,0)

#circuit4 = [(1,0,[Battery(2)]),
            #(1,0,[Resistor(2),Resistor(2)]),
            #(0,1,[Resistor(4)])]

#print solveCurrents(circuit4)

#print findResistanceOverEdge(circuit4,0)

#circuit=[(0,1,[Battery(5),Resistor(1)]),
        #(1,0,[Capacitor_With_Breakdown(1,showing=True)])]

#evolve(circuit,4,0.001,0.005)


#circuit4 = [(0,0,[Battery(1),Resistor(1),Capacitor(1,1)])]

#evolve(circuit4,3,0.001,0.01)

circuit=[(0,1,[IncreasingVoltage(),Battery(5),Resistor(1)]),
            (1,0,[Non_Ohmic_Resistor(1,1)])]

evolve(circuit,4,0.01,0.01)

#circuit=[(0,0,[Inductor(1,1),Capacitor(0.01)])]

#evolve(circuit,0.1,0.0001,0.0001,True)


#mycircuit= [(0,0,[Resistor(2),Battery(1),CurrentSource(7)])]

#print circuitToDetailsList(mycircuit)
#print solveCurrents(mycircuit)
