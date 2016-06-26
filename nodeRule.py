# Node rule

def maxnode(shape):
    return max(max(a,b) for (a,b) in shape)

def findCurrentEquivalences(shape):
    outlist=[]
    for node in range(maxnode(shape)+1):
        currentsIn = [pos for (pos,(a,b)) in enumerate(shape) if a==node]
        currentsOut = [pos for (pos,(a,b)) in enumerate(shape) if b==node]
        
        currentsInCopy= currentsIn
        
        currentsIn = [x for x in currentsIn if x not in currentsOut]
        currentsOut = [x for x in currentsOut if x not in currentsInCopy]
        
        outlist.append((node,currentsIn,currentsOut))
    return outlist

def nodeToEquation(inlist,outlist,length):
    def assign(x):
        if x in inlist:
            return 1.0
        elif x in outlist:
            return -1.0
        else:
            return 0.0
    return [assign(x) for x in range(length)]

