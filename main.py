import streamlit as st

st.markdown(
    "<style>"
    ".gradient-text {"
    "background-image: linear-gradient(135deg, #1a006e, #ffa1ee);"
    "-webkit-background-clip: text;"
    "-webkit-text-fill-color: transparent;"
    "font-weight: bold; /* Make text bold if desired */"
    "}"
    "</style>",
    unsafe_allow_html=True)

st.markdown("<h1 class='gradient-bg'></h1>",
            unsafe_allow_html=True)

st.markdown("<h1 class='gradient-text' style='text-align: center;'>KeepOn</h1>",
            unsafe_allow_html=True)

st.markdown("<h4 class='gradient-text' style='text-align: center;'>For when you need help fueling the flame</h3>",
            unsafe_allow_html=True)

if "motivation_needs" not in st.session_state:
    st.session_state.motivation_needs = ["Exercise", "Cleaning", "Cooking", "Shopping", "General Pick-Me-Up"]

dropdown_box = st.selectbox("What do you need to be motivated to do?",
                            st.session_state.motivation_needs,
                            index=None,
                            placeholder="Click one of the options or enter your own (using more than 1 word)...",
                            accept_new_options=True)

if dropdown_box not in st.session_state.motivation_needs and dropdown_box is not None:
    st.write(f"You made a new option: {dropdown_box}. NOTE: This option will not save!")
    st.session_state.motivation_needs.append(dropdown_box)
