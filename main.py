import streamlit as st
from motivational_speech_maker import speech

st.set_page_config(page_title="KeepOn", page_icon="./YourIconFileName.ico", layout="wide")

st.markdown(
    "<style>"
    ".gradient-text {"
    "background-image: linear-gradient(135deg, #1a006e, #ffa1ee);"
    "-webkit-background-clip: text;"
    "-webkit-text-fill-color: transparent;"
    "font-weight: bold;"
    "}"
    "</style>",
    unsafe_allow_html=True)

st.markdown("<h1 class='gradient-bg'></h1>",
            unsafe_allow_html=True)

st.markdown("<h1 class='gradient-text' style='text-align: center;'>KeepOn</h1>",
            unsafe_allow_html=True)

st.markdown("<h2 class='gradient-text' style='text-align: center;'>For when you need help fueling the flame</h2>",
            unsafe_allow_html=True)

st.markdown("<br><br><h5 style='text-align: center;'>What do you need to be motivated to do?</h5>",
            unsafe_allow_html=True)

motivation = st.text_input("",
                           value=None,
                           help="This will be used to create a personalized motivational message, so be sure to use "
                                "more than one word in your response.",
                           placeholder="\"I need motivation to...\"")

if motivation:
    st.markdown(f"{speech(motivation)}")
