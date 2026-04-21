import matplotlib.pyplot as plt
import numpy as np

def create_chart(dataX, dataY, title, xname, yname, graphsize=(12,6), save_chart=0):
    
    #plotting the chart
    plt.plot(dataX, dataY)

    #chart config
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title(title)

    if save_chart:
        plt.savefig(f'{title}.png', dpi=150, bbox_inches='tight')
    else:
        plt.show()


x = [1, 2, 3, 4, 5]
y = [9, 8, 7, 6, 5]

create_chart(x, y, "teste", "eixo x", "eixo y")
