import twint
import streamlit as st
st.set_page_config(layout='wide')
c = twint.Config() # Настроить
"""
#c.Lang = "en" 
#c.Hide_output = True
cut1= st.selectbox('Интервал2:', ['elonmusk','VitalikButerin','BarrySilbert'])
c.Search = "#python"
#c.Username = cut1 
#c.Search = ['India','bjp'] 
c.Limit = 10
"""
c.Username = "noneprivacy"
c.Limit = 10
#c.Store_csv = True
#c.Output = "none.csv"
c.Lang = "en"
c.Translate = True
c.TranslateDest = "ru"
#st.write(twint.run.Search(c))# Запустить
