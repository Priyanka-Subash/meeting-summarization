import streamlit as st
from transformers import pipeline

# Title
st.title("Meeting Summarization using AI")

st.write("Upload a meeting transcript file to generate summary")

# Load summarization model
@st.cache_resource
def load_model():
    summarizer = pipeline("summarization")
    return summarizer

summarizer = load_model()

# File upload
uploaded_file = st.file_uploader(
    "Upload meeting transcript (.txt)",
    type=["txt"]
)

if uploaded_file is not None:

    text = uploaded_file.read().decode("utf-8")

    st.subheader("Meeting Content")
    st.write(text)

    if st.button("Generate Summary"):

        with st.spinner("Summarizing..."):

            summary = summarizer(
                text,
                max_length=130,
                min_length=30,
                do_sample=False
            )

        st.subheader("Summary")
        st.success(summary[0]["summary_text"])
