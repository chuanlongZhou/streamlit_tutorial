import streamlit as st
import pandas as pd
import numpy as np

st.markdown('### Streamlit Chart')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)
st.bar_chart(chart_data)
st.line_chart(chart_data)
st.scatter_chart(chart_data)
st.markdown('---')


import matplotlib.pyplot as plt
st.markdown('### Matplotlib Chart')
fig, ax = plt.subplots()
chart_data.plot(ax=ax)
st.pyplot(fig)
st.markdown('---')


import altair as alt
from vega_datasets import data
cars = data.cars.url
st.markdown('### [Altair Chart](https://altair-viz.github.io/index.html)')
brush = alt.selection_interval()
points = alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N'
).add_params(
    brush
)
bars = alt.Chart(cars).mark_bar().encode(
    x='count()',
    y='Origin:N',
    color='Origin:N'
).transform_filter(
    brush
)
st.altair_chart(points & bars, use_container_width=True)
st.markdown('---')


import plotly.figure_factory as ff
import plotly.express as px
st.markdown('### [Plotly](https://plotly.com/python/)')
# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
# Group data together
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']
# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])
# Plot!
st.plotly_chart(fig, use_container_width=True)


earthquakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')
fig_earthquakes = px.density_mapbox(earthquakes, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="open-street-map")
st.plotly_chart(fig_earthquakes, use_container_width=True)
st.markdown('---')

from pyecharts import options as opts
from pyecharts.charts import Geo, Bar, Map3D
from pyecharts.faker import Faker
from pyecharts.globals import ChartType
from streamlit_echarts import st_echarts, st_pyecharts
st.markdown('### [Echarts](https://echarts.apache.org/en/index.html)')
options = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}
    ],
}
st_echarts(options=options)

st.markdown('### [PyEcharts](https://gallery.pyecharts.org/#/README_EN)')
b = (
    Bar()
    .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_yaxis(
        "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
        toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)
st.markdown('---')

import folium
from streamlit_folium import st_folium
import geopandas as gpd
st.markdown('### [Folium](https://folium.streamlit.app/)')
st.markdown('Best option for Geopandas, but it keeps reloading...')
df = pd.read_csv('data\GEM_Coalpowerplant.csv')
# convert Latitude,Longitude to geometry
gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
# set crs
gdf.crs = "EPSG:4326"
# plot the map, the scatter size is based on the Capacity (MW)
m = gdf.explore(column='Capacity (MW)', cmap='Reds', as_layer=True, tooltip=True, legend=True)
folium.LayerControl().add_to(m)

st_folium(
    m,
    key="old",
    # height=800,
    # width=1000,
)