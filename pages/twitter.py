import twint
import streamlit as st
st.set_page_config(layout='wide')
c = twint.Config() # Настроить
#c.Lang = "en" 
#c.Hide_output = True
cut1= st.selectbox('Интервал2:', ['elonmusk','VitalikButerin','BarrySilbert'])
c.Username = cut1 
#c.Search = ['India','bjp'] 
c.Limit = 10 
st.write(twint.run.Search(c))# Запустить
