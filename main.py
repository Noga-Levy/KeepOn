import streamlit as st
from motivational_speech_maker import speech

# We start by setting what the website's tab looks like on the browser
st.set_page_config(page_title="KeepOn", page_icon="./fire_icon.ico", layout="wide")

# Next, we create a text-style (using HTML, as streamlit supports it with the unsage_allow_html parameter set to true).
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

# Now, we can create text with this style, though we first want to create a black line for formatting.
st.markdown("<h1 class='gradient-bg'></h1>",
            unsafe_allow_html=True)

# Now, we have the actual text:

# Title
st.markdown("<h1 class='gradient-text' style='text-align: center;'>KeepOn</h1>",
            unsafe_allow_html=True)

# Moto
st.markdown("<h2 class='gradient-text' style='text-align: center;'>For when you need help fueling the flame</h2>",
            unsafe_allow_html=True)

# User prompt
st.markdown("<br><br><h5 style='text-align: center;'>What do you need to be motivated to do?</h5>",
            unsafe_allow_html=True)

# Textbox, for which we will send the inputted request to our speech-maker program.
motivation = st.text_input("",
                           value=None,
                           help="This will be used to create a personalized motivational message, so be sure to use "
                                "more than one word in your response.",
                           placeholder="\"I need motivation to...\"")

# If the user responded, create the speech.
if motivation:
    st.markdown(f"{speech(motivation)}")
