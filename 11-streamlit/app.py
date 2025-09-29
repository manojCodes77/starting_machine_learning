# command used to run the app
# streamlit run app.py
import streamlit as st
import pandas as pd
import numpy as np

# title of the app
st.title("Simple Streamlit App")

# display a simple text
st.write("Hello, welcome to the Streamlit app!")

df=pd.DataFrame({
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[24,30,22,35]
})

# display the dataframe
st.write("Here is a sample dataframe:")
st.write(df)

# creating a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)