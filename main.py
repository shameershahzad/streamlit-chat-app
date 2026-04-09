import streamlit as st
from model import get_response
from langchain_core.messages import HumanMessage, AIMessage

st.title("Streamlit Chat App")

if "memory" not in st.session_state:
   st.session_state.memory = []

for msg in st.session_state.memory:
   if isinstance(msg,HumanMessage):
      with st.chat_message("user"):
         st.write(msg.content)
   
   elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

userInput = st.chat_input("Ask something!")

if userInput:
   with st.chat_message("user"):
      st.write(userInput)

   with st.spinner("Thinking..."):
      ai_response,update_memory = get_response(userInput,st.session_state.memory)
      st.session_state.memory = update_memory
      st.write(ai_response)


if st.button("Clear memory"):
   st.session_state.memory = []
   st.rerun() # st.rerun() forces full refresh immediately
   