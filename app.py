import streamlit as st
import pandas as pd

st.title("Test")
st.write("Hello !")
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
st.dataframe(df)