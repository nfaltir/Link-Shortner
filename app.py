import streamlit as st
import pyshorteners as pyshort

#streamlit config
st.set_page_config(page_title="Short Url", page_icon="✂")
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
         
            footer {visibility: hidden;}
           
            </style>
            """

urlshortner = pyshort.Shortener()

st.markdown("<h1 style='text-align:center;'>Short Url</h1", unsafe_allow_html=True)

#form object
form = st.form("name")
url = form.text_input("Paste URL:")
app_btn = form.form_submit_button("Generate")

#check if btn was clicked
if app_btn:
    short_url = urlshortner.tinyurl.short(url)
    st.markdown("<h3 style='text-align:center;'>Copy Url</h3", unsafe_allow_html=True)
    st.code(short_url)
  
