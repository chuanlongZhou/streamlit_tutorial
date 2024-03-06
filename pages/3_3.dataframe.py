import streamlit as st
import pandas as pd
import numpy as np
import random

df = pd.read_csv('data\GEM_Coalpowerplant.csv')
st.markdown("### 1. Nothing special")
st.dataframe(df) 


st.markdown("### 2. Highlight max")
st.write("Height and width is set to 300 and 500, respectively. use_container_width is set to False.")
df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0), 
             height=300, 
             width=500, 
             use_container_width=False)


st.markdown("### 3. You can display charts")
df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
    use_container_width=True,
)


st.markdown("### 4. You can make interactive tables with selectbox and dynamic size")
df = pd.DataFrame(
    [
       {"fruit": "apple", "rating": 4, "selected": True},
       {"fruit": "banana", "rating": 5, "selected": False},
       {"fruit": "orange", "rating": 3, "selected": True},
   ]
)
edited_df = st.data_editor(df,
                           num_rows="dynamic")
st.markdown(f"Total rows: **{len(edited_df)}**")

st.markdown("### 5. You can make fancy metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.markdown("### 6. More fancy dataframes by configure [column types](https://docs.streamlit.io/library/api-reference/data/st.column_config)")
from components.fancy_table import fancy_table