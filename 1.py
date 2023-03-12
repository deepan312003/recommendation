import numpy as np 
import pandas as pd 
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.write("Welcome to the new recommendation system")
st.markdown("""
         # Recommendation System

Machine learning solves many problems but making product recommendations is a widely known application of machine learning. There are three main types of recommendation systems

### Plan:
```
Recommendation system
    |
    |
    |-----> Collaborative filtering
    |       |
    |       |------> User-User collaborative filtering : User-Item Collaborative Filtering : “Users who are similar to you also liked …”
    |       |
    |       |------>Item-Item collaborative filtering : “Users who liked this item also liked …”
    |
    |
    |-----> Content Based Filtering
    |
    |
    |------>Hybrid Recommendation Systems

```
""")
rawdata = pd.read_csv("u.data",sep="\t",names=["user_id","item_id","rating","timestamp"])

st.table(rawdata.head())