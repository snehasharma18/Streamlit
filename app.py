import streamlit as st
import seaborn as sns
import pandas as pd

#make containers
header = st.container()
data_set = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("This is my app - Sneha")
    st.text("In this project we will work on a dataset")

with data_set:
    st.header("Dataset")
    st.text("this is my dataset")
    df = sns.load_dataset('titanic')
    df = df.dropna()
    st.write(df.head(10))
    st.text("This is a countplot between Males and Females")
    st.bar_chart(df['sex'].value_counts())
    st.subheader("This is a countplot between Different Classes")
    st.bar_chart(df['class'].value_counts())
    st.bar_chart(df['age'].sample(10))  #for head(10)

with features:
    st.header("These are our app features")
    st.text("Features of our app are")
    st.markdown("1. **Feature 1 :** This will tell us something")
    st.markdown("2. **Feature 1 :** This will tell us something")
    st.markdown("3. **Feature 1 :** This will tell us something")
    st.markdown("4. **Feature 1 :** This will tell us something")
    st.markdown("5. **Feature 1 :** This will tell us something")


with model_training:
    st.header("This is my model")
    st.text("hello world")
    #making columns
    input, display = st.columns(2)
    #adding list of features
    input.write(df.columns)
  
   








