import streamlit as st

st.title("Meu primeiro deploy")


slider = st.slider("Selecione um ano: ", min_value=1995, max_value=2024)

st.write(f'O ano selecionado foi: {slider}')


st.select_slider("Selecione um ano: ", options = [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024])

