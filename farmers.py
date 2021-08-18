import streamlit as st

import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.title("Smart Farmer")
st.markdown("The dashboard will help a researcher to get to know \
more about the given datasets and it's output")
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

data = pd.read_csv("counties.csv")



chart_visual = st.sidebar.selectbox('Select Charts/Plot type',
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))

st.sidebar.checkbox("Show Analysis of Price", True)
selected_status = st.sidebar.selectbox('Select Category',
                                       options=['County',
                                                'CROPS'])

fig = go.Figure()

if chart_visual == 'Line Chart':
    if selected_status == 'County':
        fig.add_trace(go.Scatter(x=data.CROPS, y=data.county,
                                 mode='lines',
                                 name='Crops per county'))
    if selected_status == 'CROPS':
        fig.add_trace(go.Scatter(x=data.County, y=data.CROPS,
                                 mode='lines', name='County'))
#     #if selected_status == 'Unit':
#         #fig.add_trace(go.Scatter(x=data.Values_in_Ksh, y=data.Unit,
#                                  #mode='lines',
#                                  #name='Unit'))

# elif chart_visual == 'Bar Chart':
#     if selected_status == 'Produce_Variety':
#         fig.add_trace(go.Bar(x=data.Values_in_Ksh, y=data.Produce_Variety,
#                              name='Produce_Variety'))
#     if selected_status == 'Commodity_Type':
#         fig.add_trace(go.Bar(x=data.Values_in_Ksh, y=data.Commodity_Type,
#                              name='Commodity_Type'))
#     if selected_status == 'Unit':
#         fig.add_trace(go.Bar(x=data.Values_in_Ksh, y=data.Unit,
#                              name='Unit'))

# elif chart_visual == 'Bubble Chart':
#     if selected_status == 'Produce_Variety':
#         fig.add_trace(go.Scatter(x=data.Values_in_Ksh,
#                                  y=data.Produce_Variety,
#                                  mode='markers',
#                                  marker_size=[40, 60, 80, 60, 40, 50],
#                                  name='Produce_Variety'))

#     if selected_status == 'Commodity_Type':
#         fig.add_trace(go.Scatter(x=data.Values_in_Ksh, y=data.Commodity_Type,
#                                  mode='markers',
#                                  marker_size=[40, 60, 80, 60, 40, 50],
#                                  name='Commodity_Type'))

#     if selected_status == 'Unit':
#         fig.add_trace(go.Scatter(x=data.Values_in_Ksh,
#                                  y=data.Unit,
#                                  mode='markers',
#                                  marker_size=[40, 60, 80, 60, 40, 50],
#                                  name='Unit'))

st.plotly_chart(fig, use_container_width=True)
