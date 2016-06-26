import matplotlib.pyplot as plt

def plot_data(matrix):

    #print matrix
    
    plt.plot([x[0] for x in matrix],[x[1:] for x in matrix])
    
    plt.xlabel('time (s)')
    
    plt.xlim(-0,matrix[-1][0])
    
    plt.show()
