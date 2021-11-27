from pandas.io.parsers import read_csv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


plt.style.use('seaborn')


@st.cache
def load_data():
    df = read_csv("data.csv",index_col=0,encoding='latin1')
    return df

st.sidebar.header("Project Options")


options = ['About the project',
            'Types of Areas',
             'State vs so2',
             'State vs no2',
             'State vs rspm',
             'State vs spm ',
              
             'Location vs so2',
             'Location vs no2',
             'Location vs spm',
             'Location vs rspm',
             ]

choice = st.sidebar.selectbox("select an option",options)

df = load_data()

if choice == options[0]:
    st.image("project.jpg")
    st.info('''A report by the Health Effects Institute on air pollution in India (2018) reports that air pollution
     was responsible for 1.1 million deaths in India in 2015''')

    
    


elif choice == options[1]:
    
    color = st.sidebar.color_picker("select graph color")
    st.title=("Types of areas")
    fig,ax = plt.subplots()
    df['type'].value_counts().head().plot.pie(
                                          figsize=(5,5), 
                                         wedgeprops={'width':.5},
                                         radius=1,
                                         title="Types of areas",
                                         autopct='%.1f%%',
                                         pctdistance =.9,
                                        
                                          textprops={'color':'black'})
    st.pyplot(fig)

elif choice == options[2]:
    st.header("Comparison of States VS SO2")
    color = st.sidebar.color_picker("select graph color")
    fig,ax = plt.subplots()
    state = st.sidebar.radio("select the state",df.state.unique().tolist())

    try:
       fig,ax=plt.subplots()
       df[df['state']==state].set_index('so2')['Estimated level of so2 (%)'].plot(kind='bar',figsize=(5,15),ax=ax,color=color)
       plt.title(f'so2 in {state}',fontsize="11",color='c')
       st.pyplot(fig)
    except Exception as e:
        st.error(f"Please ask the admin {e}")

    

elif choice == options[3]:
    st.header("Comparison of States VS NO2")
    color = st.sidebar.color_picker("select graph color")
    fig,ax = plt.subplots()
    state_limit = st.sidebar.number_input("How many states",3,25,10)
    fig,ax = plt.subplots()
    df[['no2','state']].groupby(["state"]).median().sort_values(by='no2',ascending=False).head(state_limit).plot(
                    kind='bar', 
                    figsize=(15,10),
                    ax=ax,
                    color=color)
    plt.title(" Comparison of states vs no2")
    st.pyplot(fig)
    st.info('From the above figure, we concluded that NO2 level is West Bengal ')

elif choice == options[4]:
    st.header(" Comparison Of States VS RSPM")
    color = st.sidebar.color_picker("select graph color")
    fig,ax = plt.subplots()
    state_limit = st.sidebar.number_input("How many states",3,25,10)
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
    color = st.sidebar.color_picker("select graph color")
    fig,ax = plt.subplots()
    state_limit = st.sidebar.number_input("How many states",3,25,10)
    fig,ax = plt.subplots()
    df[['spm','state']].groupby(["state"]).median().sort_values(by='spm',ascending=False).head(state_limit).plot(
                    kind='bar', 
                    figsize=(15,10),
                    ax=ax,
                    color=color)
    plt.title(" Comparison of states vs spm")
    st.pyplot(fig)
    st.info('From the above figure, we concluded that SPM level is highest in Uttar Pradesh ')



elif choice == options[6]:
      st.header("Comparison OF  City vs so2")
      fig,ax = plt.subplots()
      color = st.sidebar.color_picker("select graph color")
      location = st.sidebar.radio("select the state",df.location.unique().tolist())

      try:
       fig,ax=plt.subplots()
       df[df['location']==location].set_index('so2')['Estimated level of so2 (%)'].plot(kind='bar',figsize=(5,15),ax=ax,color=color)
       plt.title(f'so2 in {location}',fontsize="11",color='c')
       st.pyplot(fig)
      except Exception as e:
        st.error(f"Please ask the admin {e}")
      st.info('From the above figure, we concluded that SO2 level is highest in Dharuhera ')
      
elif choice== options[7]:
      st.header("Comparison of City no2")
      location_limit = st.sidebar.number_input("How many location",3,25,10)
      fig,ax = plt.subplots()
      df[['no2','location']].groupby(["location"]).median().sort_values(by='no2',ascending=False).head(location_limit).plot(
                    kind='barh', 
                    figsize=(5,7),
                    ax=ax,)
      st.pyplot(fig)
      st.info('From the above figure, we concluded that NO2 level is highest in Hawroh ')
      
      
    
elif choice == options[8]:
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
        

     
elif choice== options[9]:
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

else :
    pass
      
    





    

    
