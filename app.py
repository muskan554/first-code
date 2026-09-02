import streamlit as st

st.set_page_config(page_title="MindMate", page_icon="🧠")

st.title("🧠 MindMate - AI Psychology Assistant")
st.write("Your thought ko better thinking me badlo")

user_thought = st.text_area("Apna thought / problem yaha likho (English me):", 
                            placeholder="Ex: I feel everyone is judging me...")

if st.button("Analyze"):
    if user_thought:
        with st.spinner("Thinking..."):
            st.subheader("1. Psychology Analysis")
            st.write("**Possible Bias:** Mind Reading / Negative Bias. We often think others are judging us, but it's our fast brain (System 1) talking.")

            st.subheader("2. Better Thinking")
            st.write("Ask yourself: What is the evidence? Is there any other explanation? What would you tell a friend in same situation?")

            st.subheader("3. Better English Version")
            st.info(f"Improved: '{user_thought.capitalize()}. I might be overthinking this.'")
    else:
        st.warning("Pehle kuch likho!")

st.sidebar.write("Made for GitHub Portfolio")