import streamlit as st
import joblib


model=joblib.load('placement.pkl')

def main():
    st.title("welcome to placement predictor")
    cgpa=st.slider("choose your package from slider ",min_value=0.0,max_value=10.0,step=0.1)
    st.write("enter cgpa",cgpa)


    if st.button("predict"):
        result=model.predict([[cgpa]])
        st.success(f"you package would be{result}")


if __name__=='__main__':
    main()       
    