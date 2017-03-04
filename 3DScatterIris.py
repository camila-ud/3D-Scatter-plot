"""
Plot 3D scatter example iris dataset
It works with .xls .xlsx or csv, using Pandas to load
dataset. Function scatter_plot group data by argument Name, plot and edit labels

Note: for install Pandas on Ubuntu: sudo apt-get install python-pandas
Run python 2.7.12
_____________________________________________________________________

Autor: Camila Arias
Universidad Distrital FJC
bog, colombia
"""

#import libraries
import pandas as pd  #Data analysis   
import matplotlib.pyplot as plt        #plot
from mpl_toolkits.mplot3d import Axes3D

#load dataset csv
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris.csv')

#load dataset excel
"""
excel = pd.ExcelFile('/home/user/documents/dataset_archive.xlsx') #ruta 
data = pd.read_excel(excel,sheetname=1)      #(sheetname: sheet to load) e.i: 1
"""
global grafico #figure
#Function scatter_plot group data by argument name, plot and edit labels
def scatter_plot(x_label,y_label,z_label,clase,c,m,label):
    x = data[ data['Name'] == clase ][x_label] #groupby Name column x_label
    y = data[ data['Name'] == clase ][y_label]
    z = data[ data['Name'] == clase ][z_label]
    # s: size point; alpha: transparent 0, opaque 1; label:legend
    grafico.scatter(x,y,z,color=c, edgecolors='k',s=50, alpha=0.9, marker=m,label=label)
    grafico.set_xlabel(x_label)
    grafico.set_ylabel(y_label)
    grafico.set_zlabel(z_label)
    return 

grafico = plt.figure().gca(projection='3d')  #new figure
scatter_plot('SepalLength','SepalWidth','PetalLength','Iris-virginica','g','o','Iris-virginica')
scatter_plot('SepalLength','SepalWidth','PetalLength','Iris-versicolor','b','o','Iris-versicolor')
scatter_plot('SepalLength','SepalWidth','PetalLength','Iris-setosa','r','o','Iris-setosa')
plt.legend()
plt.show()
