import streamlit as st
import json
import base64
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.header("Get In Touch With Us") 

   
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

    
lottie_1 = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_kxkxycqz.json")
lottie_2 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_IBo4XKYgE3.json")
lottie_3 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_dd9wpbrh.json")


c1, c2, c3 = st.columns(3)
with c1:
    st_lottie(lottie_1,
             width=90)
    st.write("123 Lagos Nigeria")
    
with c2:
    st_lottie(lottie_2,
             width=90)
    st.write("012345678")
    
with c3:
    st_lottie(lottie_3,
             width=90)
    st.write("info@all-tech.org")
    
st.markdown("###") #adjusting for space between 
st.markdown("###")
st.markdown("###")

#insert message us section#


st.header(":mailbox: Write To Us!")

contact_form = """
<form action="https://formsubmit.co/mbuyiselom94@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
      <textarea name="message" placeholder="Your Message Here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

#use local css file
def local_css(File_name):
    with open(File_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(
    png_file,
    background_position="-10% -10%",
    margin_top="0%",
    image_width="40%",
    image_height="45%",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )


def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

add_logo("pics/logo.png")



   
    