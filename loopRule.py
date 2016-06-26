import helpers # This has the max loop length in it


# This does the graph algorithm to come up with the list of loops.

# So allLoops of [(0,1),(0,1),(0,1)] is
# [[(0, True), (1, False)], [(0, True), (2, False)], 
#    [(1, True), (2, False)]]

def allLoops(graph):
    outlist=[]
    for (pos,edge) in enumerate(graph):
        continuePath([(pos,True)],edge[0],[],graph,outlist)
    return outlist

def normalizeLoop(inlist):
    minimumElement = min(inlist)
    
    pivot= inlist.index(minimumElement)
    
    outlist= inlist[pivot:]+inlist[:pivot]
    
    if outlist[0][1] == False:
        outlist = [(x,not y) for (x,y) in outlist]
    
    return outlist

def continuePath(pathSoFar,start,visitedSoFar,graph,outlist):

    
    currentEdge = graph[pathSoFar[-1][0]]

    pos= graph[pathSoFar[-1][0]][pathSoFar[-1][1]]

    if pos==start:
        if pathSoFar==normalizeLoop(pathSoFar):
            outlist.append(pathSoFar)
        return
    elif pos in visitedSoFar:
        return

    if len(pathSoFar)>helpers.max_loop_length:
        return
    
    for (num,edge) in enumerate(graph):
        if num not in [x for (x,y) in pathSoFar]:
            if edge[0]==pos:
                continuePath(pathSoFar+[(num,True)],start,visitedSoFar+[pos],
                    graph,outlist)
            if edge[1]==pos:
                continuePath(pathSoFar+[(num,False)],start,visitedSoFar+[pos],
                    graph,outlist)
    return

def loopToEquation(loop,detailsList,length):
    
    totalVoltage=0.
    resistanceList=[]
    inductanceList=[]
    
    for x in range(length):
        if (x,True) in loop: # This next bit is V + RA
            totalVoltage+=detailsList[x][3]+detailsList[x][2]* \
                                    detailsList[x][4]
            resistanceList.append(detailsList[x][2])
            if abs(detailsList[x][5])<0.000001:
                inductanceList.append(0.00000001)
            else:
                inductanceList.append(detailsList[x][5])
        elif (x,False) in loop:
            totalVoltage-=detailsList[x][3]+detailsList[x][2]* \
                                    detailsList[x][4]
            resistanceList.append(-detailsList[x][2])
            if abs(detailsList[x][5])<0.000001:
                inductanceList.append(0.00000001)
            else:
                inductanceList.append(-detailsList[x][5])
        else:
            resistanceList.append(0.)
            inductanceList.append(0.)
    
    return (resistanceList,inductanceList,totalVoltage)

if __name__=="__main__":
    print allLoops([(0,1),(0,1),(0,1)])
    print
    print allLoops([(0,1),(0,1),(0,1),(1,2),(2,0)])
