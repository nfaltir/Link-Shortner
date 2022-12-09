import streamlit as st
import pyshorteners as pyshort
import pyperclip as clip


urlshortner = pyshort.Shortener()

#create copy btn function using pyperclip
def copyurl():
    clip.copy(short_url)

st.markdown("<h1 style='text-align:center;'>Link Shortner</h1", unsafe_allow_html=True)

#form object
form = st.form("name")
url = form.text_input("Paste URL:")
app_btn = form.form_submit_button("Generate")

#check if btn was clicked
if app_btn:
    short_url = urlshortner.tinyurl.short(url)
    st.markdown("<h2 style='text-align:center;'>Copy Url</h2", unsafe_allow_html=True)
    st.code(short_url)
    st.button('Copy', on_click=copyurl)
