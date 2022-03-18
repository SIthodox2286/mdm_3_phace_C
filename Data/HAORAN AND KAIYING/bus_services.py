# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


'''
1.Load the data
'''
data=pd.read_excel('bus_services.xlsx')


'''
'''
plt.figure(dpi=200)

#(1) Get the regions' names
region_names=data.iloc[0:5,0]

#(2) Start a loop for plotting the data from Month: 1-3, 4-6, 7-9
xlabel_names=['1','2','3','4','5','6','7','8','9','10','11'] #Because the xlabel should be the month ranges
colors=['y','b','k','r','b']#Set the colors for 3 regions
legends=[];

for i in range(0,5):
    region_now=region_names[i]
    
    #<1> Plot the region's data of 'Total owed a prevention or relief duty'
    y=data.iloc[i,range(2,13,1)]#Get the data of 'Total owed a prevention or relief duty'
    x = range(0,len(xlabel_names),1)
    plt.plot(x, y, color=colors[i],marker="o",markersize=12)
    
    
    # Generate the legends for the lines
    k=len(legends)
    legends[k:k+2]=[region_now+': Total owed a prevention or relief duty',region_now+': Homeless - Relief duty owed']
    
plt.ylabel('Number')
plt.xlabel('Month')
plt.legend(legends,bbox_to_anchor=(2.1,1))
plt.xticks(x, xlabel_names, rotation=45)
plt.show()



'''
'''
