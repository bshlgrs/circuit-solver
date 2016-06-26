import nodeRule
import loopRule
import circuitSolve
import plot_data
import time as timemodule
from components import *
from helpers import *

def printCircuit(circuit):
    for (a,b,contents) in circuit:
        print "Connection from node %s to node %s. Contents: %s"%(a,b,", ".join(
                            [x.show() for x in contents]))

# We turn a circuit into a list of tuples (start node, end node, 
#        resistance, voltage, current, inductance)

def circuitToDetailsList(circuit):
    detailslist=[]
    for (a,b,items) in circuit:
        detailslist.append((a,b,sum(item.getResistance() for item in items),
                sum(item.getVoltage() for item in items),
                sum(item.getCurrent() for item in items),
                sum(item.getInductance() for item in items)))
    #print detailslist
    return detailslist
    
def justTheShape(circuit):
    return [(x,y) for (x,y,z,w,q,u) in circuit]

def allEquations(detailsList):
    shape=justTheShape(detailsList)

    loops = loopRule.allLoops(shape)
    nodes = nodeRule.findCurrentEquivalences(shape)
    
    #print loops
    #print nodes
    
    numCurrents=len(detailsList)
    
    
    loopInductance = []
    nodeMatrix = []
    loopVoltages = []
    loopResistances = []
    
    
    for loop in loops:
        resistanceList,inductanceList,totalVoltage= \
                loopRule.loopToEquation(loop,detailsList,numCurrents)
        loopInductance.append(inductanceList)
        loopResistances.append(resistanceList)
        loopVoltages.append([totalVoltage])

    for (a,b,c) in nodes:
        nodeVector= nodeRule.nodeToEquation(b,c,numCurrents)
        nodeMatrix.append(nodeVector)

    return (loopInductance,nodeMatrix,loopVoltages,
                                        loopResistances)

def finalCurrents(circuit,final=True):
    
    def changeEdge(stuff):
        outstuff=[]
        for a in stuff:
            if isinstance(a,Capacitor) and final \
                    or isinstance(a,Inductor) and not final:
                return [Resistor(1e100)]
            if isinstance(a,Inductor) or isinstance(a,Capacitor):
                pass
            else:
                outstuff.append(a)
        return outstuff
    
    newcircuit=[(a,b,changeEdge(stuff)) for (a,b,stuff) in circuit]
    
    stuff = allEquations(circuitToDetailsList(newcircuit))

    return circuitSolve.findEquilibriumCurrents(stuff)


def findResistanceOverEdge(circuit,edgenum):
    detailsList= circuitToDetailsList(circuit)
    detailsList = [(x,y,z,0.,0.,0.) for (x,y,z,w,q,s) in detailsList]
    
    (a,b,c,d,e) = detailsList[edgenum]
    
    detailsList[edgenum]=(a,b,0.,1.,0.,0.)
    
 #   print detailsList
    
    equations = allEquations(detailsList)

    currents=circuitSolve.findEquilibriumCurrents(equations)
    
 #   print currents
    
    return 1.0/currents[0]        

def findResistanceBetweenNodes(circuit,node1,node2):
    
   # print circuit
    try:
        detailsList= circuitToDetailsList(circuit)
    except ValueError:
      #  print "assuming that was a detailsList you just gave me..."
        detailsList = circuit
     
    #print detailslist
    
    detailsList = [(x,y,z,0.,0.,0.) for (x,y,z,w,q,s) in detailsList]
    
    detailsList.append((node1, node2, 0., 1., 0., 0.))
    
  #  print detailsList
    
    equations = allEquations(detailsList)

    currents=circuitSolve.findEquilibriumCurrents(equations)
    
  #  print currents
    
    return 1.0/currents[-1]

def evolve(circuit,startState,timelimit,timestep,printtimes,plotting=True):
    
    time=0
    nextprinttime=0
    
    if startState==None:
        inductorMode = False
    else:
        currentsList = startState
        inductorMode = True
    
    if plotting:
        plotlist=[]
    
    while time<timelimit:
        
      #  print circuit
        
        stuff = allEquations(circuitToDetailsList(circuit))
        
    #    print stuff
        
        if inductorMode:
            currentsList=circuitSolve.solveCurrents( \
                    stuff,currentsList,timestep)
        else:
            currentsList=circuitSolve.findEquilibriumCurrents(stuff)
        
     #   print "lol",currentsList
        
        #timemodule.sleep(0.01)
        
     #   print "HOLY FUCKING SHIT"
      #  print currentsList
    
        if time>nextprinttime:
            if not plotting:
                print "\t".join(str(x) for x in 
                    format_data(circuit,currentsList,time))
            else:
                plotlist.append(format_data(circuit,currentsList,time))
                
            nextprinttime+=printtimes

        for (pos,connection) in enumerate(circuit):
            for item in connection[2]:
                item.updateSelf(timestep,currentsList[pos])
        
        time += timestep
    
    if not plotting:
        print "\t".join(str(x) for x in 
                format_data(circuit,currentsList,time))
    else:
        
        plot_data.plot_data(plotlist)
        

def format_data(circuit,currentsList,time):
    currentPrint = [round(x,rounding_length) 
    for x in currentsList]

    objectShowList = []
    for a in circuit:
        objectShowList.extend(x.data() for x in a[2] if x.data())
    
    return [time] + currentPrint + objectShowList

if __name__=="__main__":

  #  circuit1=[(0,1,[Battery(12),Inductor(3)]),(1,0,[Resistor(6)]),(1,0,[Resistor(6)])]

    circuit2 = [(0,0,[Battery(1),Inductor(1),Resistor(1)])]

    evolve(circuit2,[0],30,3,0.01,True)
    
   # print finalCurrents(circuit2)
    
    #print solveCurrents(circuit3)
#    evolve(circuit3,10,0.001,1)
