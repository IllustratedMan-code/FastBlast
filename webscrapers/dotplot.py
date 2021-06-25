#%%
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

os.chdir("/home/david/Documents/BenoitLab/FastBlast/datafiles/")

data = pd.read_csv("downPermLeg.csv", sep="\t", skiprows=11)
print(data.columns)




def data_condensor(data, dataslice=None):
    
    if dataslice is None:
        dataslice = data.copy()
        dataslice.drop(str(data.columns[0]),1,inplace=True)

    y = list(data.iloc[:,0]) * (len(dataslice.columns))
    data_array = []
    name_array = []
    
    for col in dataslice.columns:
        data_array += list(dataslice[col])
        #print(list(data[col]))
        name_array += list([col]*len(dataslice.index))
    print(len(y), len(name_array), len(data_array))

    return (pd.DataFrame(dict(annotation = y, name = name_array, data=data_array)))

d = data_condensor(data, dataslice=data.iloc[:, 1:4])
    
fig = px.scatter(
            d,
            y="annotation", 
            x="data", 
            color="name", 
            width=1000, 
            height=600, 
            template="ggplot2",
            labels={
                    'annotation':'',
                    'data':'Value',
                    }
            
            )

fig.write_html("plotlyfigure.html")
fig.show()
