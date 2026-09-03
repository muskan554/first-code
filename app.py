import streamlit as st
from groq import Groq
st.set_page_config(page_title="MindMate", page_icon="🧠")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title(🧠 MindMate - AI Psychology Assistant")
st.write("Your thought ko better thinking me badlo")

user_thought = st.text_area("Apna thought / problem yaha likho (English me):", 
                            placeholder="Ex: I feel everyone is judging me...")

if st.button("Analyze"):
    if user_thought:
        with st.spinner("Thinking..."):
          prompt = f"""
          user thought:{user_thought}
          Give 3 things:
          1. Psychology Analysis (possible bias)
          2. Better Thinking (CBT based reframe)
          3. Better English Version of their thought keep it simple and supportive."""
          response = client.chat.completion.creat(
              model="11ama3-8b-8192",
              Message=[{"role": "user", "content": prompt}]
          ) 
          st.write(response.choice[0].message.content) 
        else:
             st.warning("Pehle kuch likho!")
        st.sidebar.write("Made for GitHub Portfolio") 