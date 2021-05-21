import pandas as pd
import numpy as np
# to load json files
import json
# datetime oprations
from datetime import timedelta
import datetime as dt
import plotly.express as px
import plotly.graph_objs as go
# import plotly.figure_factory as ff
from plotly.subplots import make_subplots
# for offline ploting
from plotly.offline import plot, iplot, init_notebook_mode
init_notebook_mode(connected=True)

country=pd.read_csv('country_wise_latest.csv')
full_grouped = pd.read_csv('full_grouped.csv')

def plot_map(df, col, pal):
    df = df[df[col]>0]
    fig = px.choropleth(df, locations="Country/Region", locationmode='country names', 
                  color=col, hover_name="Country/Region", 
                  title=col, hover_data=[col], color_continuous_scale=pal)
#     fig.update_layout(coloraxis_showscale=False)
    fig.show()

plot_map(country, 'Confirmed', 'matter')