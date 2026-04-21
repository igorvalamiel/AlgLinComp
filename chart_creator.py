import matplotlib.pyplot as plt
import numpy as np

def create_chart(dataX, dataY, title, xname, yname, graphsize=(12,6), save_chart=0):
    
    #tamanho do grafico
    plt.figure(figsize=graphsize)

    #plotting the chart
    plt.plot(dataX, dataY, color='green')

    # enfeites do chart
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title(title)
    plt.grid(True, axis='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    #usando log
    plt.yscale('log')

    if save_chart:
        plt.savefig(f'{title}.png', dpi=150, bbox_inches='tight')
    else:
        plt.show()


#x = [1, 2, 3, 4.8, 5]
#y = [9, 8, 7.5, 6, 5]
#
#create_chart(x, y, "teste", "eixo x", "eixo y")
