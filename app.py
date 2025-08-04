import streamlit as st
from joblib import load

# Load the pipeline
pipeline = load("spam_pipeline.pkl")

# Streamlit UI
st.set_page_config(page_title="Spam Detector", page_icon="📬")
st.title("📬 Spam Message Detector")
st.markdown("🚀 Enter a message below and let the model predict whether it's **Spam** or **Ham**.")

user_input = st.text_area("📝 Your Message", height=150)

if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message first.")
    else:
        prediction = pipeline.predict([user_input])[0]
        if prediction == 1:
            st.error("🛑 It's a Spam message!")
        else:
            st.success("✅ It's a Ham message!")
