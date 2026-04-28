from openai import OpenAI
import streamlit as st

import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)
st.set_page_config(page_title="Ai Blog", page_icon="🤷‍♂️")

st.title("AI Blog Generator")
st.write("Generate structured blogs using AI with customizable style and length.")
user_input=st.text_input("enter your topic!")
word=st.slider("word Count",100,500,150)
style = st.selectbox("Blog Style", ["General", "Technical", "SEO", "Creative"])



def blog(user_input,word,style):
    system_prompt=f"You are a professional blog writer. write a blog  on {user_input} of at least {word} words with a proper introduction, and have a {style} side blog reference, and conclusion. Keep the language simple and engaging."
    message=[
        {
            "role":"system",
            "content":system_prompt
        },{
            "role":"user",
            "content":user_input
        }
    ]
    response=client.chat.completions.create(
        model="nvidia/nemotron-3-nano-30b-a3b:free",
        messages=message
    )
    return response.choices[0].message.content



output=""
if st.button("Generate Blog"):
    if user_input:
      with st.spinner("Generating blog..."):
        result = blog(user_input,word,style)
        st.success("Blog generated successfully!")
        output=result
        st.write(result)
    else:
        st.warning("Please enter a topic first")

if st.button("Reset"):
    st.write("")

st.download_button("download_blog",output,file_name="blog.txt")