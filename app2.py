import streamlit as st
st.title("BMI calculator")

with st.form("BMI calculator"):
    col1,col2,col3=st.columns([3,2,1])
with col1:
    weight=st.number_input("enter your weight in KGs", min_value=0)
with col2:
    height=st.number_input("Enter your age in Height in meters", min_value=0)
with col3:
    submit=st.form_submit_button("calculate")

if submit:
    BMI=round(weight/(height**2),2)

    if BMI <=18.5:
        st.error("UNDERWEIGHT")
    if BMI >18.5 and BMI<=24.9:
        st.success("HEALTHY/NORMAL")
    if BMI>=25 and BMI <=29.9:
        st.warning("OVERWEIGHT")
    elif BMI>=30.0:
        st.error("OBESS")
