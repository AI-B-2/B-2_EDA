import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.controllers import Controller
import seaborn as sns
import json

covid_df = pd.read_csv("./country_all.csv")
covid_df['critical'] = covid_df['Deaths'] / covid_df['Confirmed']

def drw_GDP(): #GDP와 확진자당 사망의 관계 lineplot
    sorted_data = covid_df.sort_values(by=['GDP ($ per capita)'], axis=0)

    
    plt.xlabel("GDP ($ per capita)")
    plt.ylabel("Critical")

    GDP_per_Death = plt.plot(sorted_data['GDP ($ per capita)'], sorted_data['critical'])
    
    object_plot = Controller.to_json(GDP_per_Death)

    return object_plot

def drw_Density(): #인구밀도와 확진자당 사망의 관계 lineplot
    sorted_data = covid_df.sort_values(by=['Pop. Density (per sq. mi.)'], axis=0)
    
    
    plt.xlabel("Pop. Density (per sq. mi.)")
    plt.ylabel("Critical")
    plt.xticks([i for i in range(0, 1, 100)])

    densty_per_death = plt.plot(sorted_data['Pop. Density (per sq. mi.)'], sorted_data['critical'])
    
    object_plot = Controller.to_json(densty_per_death)

    return object_plot

drw_GDP()
drw_Density()
