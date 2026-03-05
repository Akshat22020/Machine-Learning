import streamlit as st
import pickle

@st.cache_resource
def load_model():
    with open("classifier.pkl", "rb") as file:
        return pickle.load(file)

classifier = load_model()

import pandas as pd

def predict_note_authentication(variance, skewness, curtosis, entropy):
    input_df = pd.DataFrame({
        "variance": [float(variance)],
        "skewness": [float(skewness)],
        "curtosis": [float(curtosis)],
        "entropy": [float(entropy)]
    })
    
    prediction = classifier.predict(input_df)
    return prediction[0]

def main():
    st.title("Bank Authenticator")

    variance = st.text_input("Variance")
    skewness = st.text_input("Skewness")
    curtosis = st.text_input("Curtosis")
    entropy = st.text_input("Entropy")

    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        st.success(f"Prediction: {result}")

if __name__ == "__main__":
    main()