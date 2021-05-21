import pandas as pd
import numpy as np
# to load json files
import json
# datetime oprations
import plotly.express as px
import plotly.graph_objs as go
# import plotly.figure_factory as ff
from plotly.subplots import make_subplots
# for offline ploting
from plotly.offline import plot, iplot, init_notebook_mode
init_notebook_mode(connected=True)


def tree_map(df,val_list):
    df=pd.read_csv('country_wise_latest.csv')
    val_list = ['Country/Region','Deaths', 'Recovered', 'Active']
 
    temp = df[val_list]
    temp = temp.melt(id_vars=val_list[0], value_vars=val_list[1:])
    fig = px.treemap(temp, path=["variable"], values="value", height=225, 
                     color_discrete_sequence=[act, rec, dth])
    fig.data[0].textinfo = 'label+text+value'

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON