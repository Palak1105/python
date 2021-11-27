from pandas.io.parsers import read_csv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import datetime

plt.style.use('seaborn')

@st.cache
def load_data():
    df= pd.read_csv("data.csv",encoding='latin1',parse_dates=['date'],dtype={'stn_code':str},dayfirst=True)
    cols_to_drop = ['stn_code','sampling_date','agency','location_monitoring_station']
    df.drop(cols_to_drop,axis=1,inplace=True)
    city_day = pd.read_csv('city_day.csv',dayfirst=True).sort_values(by = ['Date', 'City'])
    city_day.Date = city_day.Date.apply(lambda x : datetime.datetime.strptime(x, '%Y-%m-%d'))
    city_day = city_day.sort_values(by = 'Date')
    city_day['B_X_O3_NH3'] = city_day['Benzene'] +  city_day['Xylene'] + city_day['O3'] + city_day['NH3']
    city_day['ParticulateMatters'] = city_day['PM2.5'] + city_day['PM10']
    df.set_index('date',inplace=True)
    return df,city_day

st.header("Project Options")

options = ['About the project',
            'Year wise Pollution Concentration',
             'Pollution in each city',
             'State wise Pollution timeline',
             'State vs rspm',
             'State vs spm ', 
             'Location vs no2',
             'Location vs spm',
             'Location vs rspm',
             ]

choice = st.selectbox("select an option",options)
df,city_df = load_data()

if choice == options[0]:
    st.image("project.jpg")
    st.info('''A report by the Health Effects Institute on air pollution in India (2018) reports that air pollution
     was responsible for 1.1 million deaths in India in 2015''')

    

elif choice == options[1]:
    period = st.select_slider("select graph period",['Y','M','2M','3M'])
    year_wise_df = df.resample(period).mean()
    pollution_component = st.select_slider("Select a pollution component",year_wise_df.columns.tolist())
    fig = px.bar(year_wise_df,x=year_wise_df.index,y=pollution_component,title='Year wise SO2 concentration')
    st.plotly_chart(fig)


elif choice == options[2]:
    most_polluted = city_df[['City', 'AQI', 'PM10', 'CO']].groupby(['City']).mean().sort_values(by = 'AQI', ascending = False)
    plt.style.use('seaborn-whitegrid')
    f, ax_ = plt.subplots(1, 3, figsize = (15,20))

    bar1 = sns.barplot(x = most_polluted.AQI,
                    y = most_polluted.index,
                    palette = 'Reds_r',
                    ax = ax_[0]);

    bar1 = sns.barplot(x = most_polluted.PM10,
                    y = most_polluted.index,
                    palette = 'RdBu',
                    ax = ax_[1]);

    bar1 = sns.barplot(x = most_polluted.CO,
                    y = most_polluted.index,
                    palette = 'RdBu',
                    ax = ax_[2]);

    titles = ['AirQualityIndex', 'ParticulateMatter10', 'CO']
    st.subheader("Pollution data for each city")
    for i in range(3) :
        ax_[i].set_ylabel('')   
        ax_[i].set_yticklabels(labels = ax_[i].get_yticklabels(),fontsize = 14);
        ax_[i].set_title(titles[i])
        f.tight_layout()
        st.pyplot(f)
    

elif choice == options[3]:
    states_df = df.groupby(['state',df.index]).sum().reset_index()
    state = st.selectbox("select a state", states_df.state.unique().tolist())
    period = st.select_slider("select graph period",['Y','M','2M','3M'])
    state_df = states_df[states_df['state']==state]
    state_df = state_df.set_index('date')  
    state_pollution = state_df.resample(period).mean()
    pol =  st.selectbox("select a pollutant",['so2','no2','rspm','spm','pm2_5'])
    fig = px.bar(state_pollution,x=state_pollution.index,y=pol,title='Year wise SO2 concentration')
    st.plotly_chart(fig)


elif choice == options[4]:
    st.header(" Comparison Of States VS RSPM")
    color = st.color_picker("select graph color")
    fig,ax = plt.subplots()
    state_limit = st.number_input("How many states",3,25,10)
    fig,ax = plt.subplots()
    df[['rspm','state']].groupby(["state"]).median().sort_values(by='rspm',ascending=False).head(state_limit).plot(
                   kind='bar', 
                    figsize=(15,10),
                    ax=ax,
                    color=color)
    plt.title(" Comparison of states vs rspm")               
    st.pyplot(fig)
    st.info('From the above figure, we concluded that RSPM level is highest in Delhi')


elif choice == options[5]:
    st.header("Comparison of States VS SPM")
    color = st.color_picker("select graph color")
    fig,ax = plt.subplots()
    state_limit = st.number_input("How many states",3,25,10)
    fig,ax = plt.subplots()
    df[['spm','state']].groupby(["state"]).median().sort_values(by='spm',ascending=False).head(state_limit).plot(
                    kind='bar', 
                    figsize=(15,10),
                    ax=ax,
                    color=color)
    plt.title(" Comparison of states vs spm")
    st.pyplot(fig)
    st.info('From the above figure, we concluded that SPM level is highest in Uttar Pradesh ')



  
elif choice== options[6]:
      st.header("Comparison of City no2")
      location_limit = st.number_input("How many location",3,25,10)
      fig,ax = plt.subplots()
      df[['no2','location']].groupby(["location"]).median().sort_values(by='no2',ascending=False).head(location_limit).plot(
                    kind='barh', 
                    figsize=(5,7),
                    ax=ax,)
      st.pyplot(fig)
      st.info('From the above figure, we concluded that NO2 level is highest in Hawroh ')
      
      
    
elif choice == options[7]:
        st.header("Comparison of City vs spm")
        
        fig,ax = plt.subplots()
        location_limit = st.sidebar.number_input("How many location",3,25,10)
        fig,ax = plt.subplots()
        df[['spm','location']].groupby(["location"]).median().sort_values(by='spm',ascending=False).head(location_limit).plot(
                    kind='barh', 
                    figsize=(5,7),
                    ax=ax,)
        st.pyplot(fig)
        st.info('From the above figure, we concluded that SPM level is highest in Meerut ')
        

     
elif choice== options[8]:
        st.header("Comparisopn of  City vs  rspm")
        fig,ax = plt.subplots()
        location_limit = st.sidebar.number_input("How many location",3,25,10)
        fig,ax = plt.subplots()
        df[['rspm','location']].groupby(["location"]).median().sort_values(by='rspm',ascending=False).head(location_limit).plot(
                    kind='barh', 
                    figsize=(5,7),
                    ax=ax,)
        st.pyplot(fig)
        st.info('From the above figure, we concluded that RSPM level is highest in Gaziabad')







    

    
