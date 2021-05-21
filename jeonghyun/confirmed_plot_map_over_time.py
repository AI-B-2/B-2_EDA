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

full_grouped = pd.read_csv('full_grouped.csv')
full_grouped["Date"].dt.strftime('%Y-%m-%d')

def confirmed_over_time():
    df= pd.read_csv('full_grouped.csv')
    df["Date"].dt.strftime('%Y-%m-%d')
    frame = df["Date"].dt.strftime('%Y-%m-%d')

    fig = px.choropleth(df, locations="Country/Region", 
                    color=np.log(df["Confirmed"]),
                    locationmode='country names', hover_name="Country/Region", 
                    animation_frame=frame,
                    title='Cases over time', color_continuous_scale=px.colors.sequential.matter)
    fig.update(layout_coloraxis_showscale=False)
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

