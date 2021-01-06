import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
def Setcolor(z):
    if(z<0):
        return 'red'
    elif(z>=0 | z<1000):
        return 'green'
    elif(z>=1000):
        return 'yellow'
df=pd.read_excel('C:/Users/mramesh26/Desktop/Scorecard.xls',skiprows=1,nrows=16)
#set the index to Dept
df.set_index('Dept', inplace=True)
#grab just the week columns
df = df[[col for col in df.columns if col.startswith('QWeek')]].astype(int)
df.columns=['W1','W2','W3','W4','W5','W6','W7','W8','W9','W10','W11']
print(df.dtypes)
print(type('z'))
color=df.applymap(Setcolor)
#print(color.loc[name] for name in df.index)
print(color)
trace0=[go.Scatter(
    x = df.columns,
    y = df.loc[name],
    mode = 'markers+lines',
    marker=dict(
         color=color.loc[name],
           size=5,
                ),
    line=dict(
         width=0.1,
         ),
        name = name) for name in df.index]

layout=go.Layout(title='Score Card',
                 showlegend=True,
                 xaxis={'title': 'Weekly'},
                 yaxis=dict(title='Deviation'),
                )
fig = go.Figure(data=trace0,layout=layout)
pyo.plot(fig, filename='line3.html')








