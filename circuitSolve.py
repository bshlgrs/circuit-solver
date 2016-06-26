# circuitSolve.py

import scipy
import scipy.linalg
import numpy as np
from scipy.integrate import odeint


def findEquilibriumCurrents(matrices):
    (loopInductance,nodeMatrix,loopVoltages,
                loopResistances) = matrices
    
    # A I = X
    
    A = np.matrix(loopResistances+nodeMatrix)
    
  #  print "c",loopVoltages
    
   # print loopVoltages
    
    X = np.copy(np.matrix(loopVoltages))
  #  print X
    X.resize(A.shape[0],1)
    
  #  print A
   # print X
    
    finalCurrents=scipy.linalg.lstsq(A,X)[0]
    return finalCurrents


# A dI/dt = B I + y
def solveCurrents(matrices, initialCurrents, timestep):
    (loopInductance,nodeMatrix,loopVoltages,
                loopResistances) = matrices
    
    # A I = X
    
    A = np.matrix(loopResistances+nodeMatrix)
    
  #  print "c",loopVoltages
    
   # print loopVoltages
    
    X = np.copy(np.matrix(loopVoltages))
  #  print X
    X.resize(A.shape[0],1)
    
  #  print A
   # print X
    
    finalCurrents=scipy.linalg.lstsq(A,X)[0]

 #   print finalCurrents
    
    # B dI/dt = CI_0 + X
    
    B = np.matrix(loopInductance+ nodeMatrix)
    C = np.copy(np.matrix(loopResistances))
    C.resize (B.shape[0],B.shape[1])
    
 #   print initialCurrents
    
    I_0 = np.copy(np.matrix(initialCurrents))
    I_0.resize(B.shape[0],1)

   # print "\n\n"
    
  #  print B
  #  print C
  #  print I_0
    
    changeInCurrents= scipy.linalg.lstsq(B,-C*I_0+X)[0]
    
  #  print finalCurrents
   # print "cc1",changeInCurrents
   # print "ic",np.array(initialCurrents)
    
    iCArray=np.copy(np.matrix(initialCurrents))
   # iCArray.transpose()
    
    iCArray.resize(B.shape[1],1)
    
   # print "ic",iCArray
    
    changedCurrent = np.add(changeInCurrents*timestep,
        iCArray)
    
   # print "cc",changedCurrent
    
    outlist=[]
    
   # print changedCurrent,"lol",initialCurrents
    
    for a in range(changedCurrent.shape[0]):
        
    #    print changedCurrent[a],finalCurrents[a]
        
        if changeInCurrents[a][0]>0:
            outlist.append(min(changedCurrent[a][0],finalCurrents[a][0]))
        else:
            outlist.append(max(changedCurrent[a][0],finalCurrents[a][0]))
  #  print outlist
   # print [changedCurrent[a][0] for a in range(changedCurrent.shape[0])]
   # print
    return [changedCurrent[a][0] for a in range(changedCurrent.shape[0])]


if __name__ == "__main__":
    
    loopInductance = [[0, 0.00001]]
    nodeMatrix = [[1,-1]]
    loopCurrents = [[0]]
    loopVoltages = [[-1]]
    loopResistances = [[2,0]]
    
    initialCurrents=[[0],[0]]
    
    mymatrix=(loopInductance,nodeMatrix,loopCurrents,loopVoltages,
                loopResistances)
    
    print solveCurrents(mymatrix, initialCurrents,0.1)
