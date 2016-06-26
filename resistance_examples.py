# Cool stuff with resistance

from circuits import *

def resistanceListToDetails(inlist):
    return [(x,y,z,0,0,0) for (x,y,z) in inlist]

def graphToDetails(inlist):
    return [(x,y,1,0,0,0) for (x,y) in inlist]

#square_circuit=[(0,1),(0,2),(1,3),(2,3)]

#circuit1 = graphToDetails(square_circuit)

#cube_circuit=[(0,1),(0,2),(1,3),(2,3),
              #(4,5),(4,6),(5,7),(6,7),
              #(0,4),(1,5),(2,6),(3,7)]
 
#circuit2 = graphToDetails(cube_circuit)
 
#print findResistanceBetweenNodes(circuit2,0,7)

def coords_to_point(x,y,width):
    return x+y*(width+1)

def make_lattice(width,height):
    outlist=[]
    
    for a in range((width+1)*(height+1)):
        if a%(width+1)!=width:
            outlist.append((a,a+1))
        if a<((width+1)*height):
            outlist.append((a,a+width+1))
    return outlist

if __name__ == "__main__":
    circuit3=graphToDetails(make_lattice(10,10))

    print circuit3
    print findResistanceBetweenNodes(circuit3,coords_to_point(5,5,10),
                coords_to_point(6,7,10))
    # this returns 0.7981
    
    circuit3=graphToDetails(make_lattice(14,14))

    print circuit3
    print findResistanceBetweenNodes(circuit3,coords_to_point(7,7,14),
                coords_to_point(8,9,14))
    
    # this returns 0.7860
        
    circuit3=graphToDetails(make_lattice(18,18))

    print circuit3
    print findResistanceBetweenNodes(circuit3,coords_to_point(8,8,18),
                coords_to_point(9,10,18))
    # this returns 0.7809
    
    # Correct answer is 4/pi-0.5, or about 0.773, according to the internet.
