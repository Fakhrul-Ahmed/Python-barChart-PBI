# To get the data inside Power BI:
# Command prompt --> python path --> pip install openpyxl
# Home --> Get data --> Moer --> (write) python --> (select) Python script --> Connect

# (Writing the code)
# import pandas as pd
        # Telling panda to read my excel or csv file
# mydata = pd.read_excel("file location/ file path")
# mydata = pd.read_csv("file location/ file path")

#(Personal learning only: how to aggragate summary
        # I need a summary from mydata, and I am using the aggregate function,
        # and setting the labels in the chart by index function (.reset_index())
# summary = pd.pivot_table(mydata, index = 'Year', aggfunc='sum').reset_index()  
# Still learning: found problem here!!!)

import matplotlib as mb
import matplotlib.pyplot as plt
mb.rcParams['font.size']=19.0

# Calling the data
names = dataset.loc[0:5,'Bears'].tolist()
y = dataset.loc[0:5,'Year'].tolist()

plt.bar(y,names,color='red',width=0.5)

# Creating different colors
#colors = ['blue','red','green','yellow','violet','#ff6666']
# for bar chart color = colors but for pi chart colors = colors
#plt.bar(y,names,color=colors,width=0.5) 

plt.show()

