import streamlit as st

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
