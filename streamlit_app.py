# Imports required ---
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data
from PIL import Image


def main():
    
    st.title('Alltech Inc.🎈') 
    

    with st.expander("About this App"):
        st.write("""
            This web application leverages the datasets to unpack key insights and trends to be used by buyers (e.g. retailers) and sellers (farmers) to set and negotiate their price on a given day. 😉
        """)


    #################################################################################################
    # Sidebar section ---
    with st.sidebar:
        logo = Image.open("pics/Alltech_logo.PNG")
        st.image(logo, width=200)
        st.header("Price Insight App✨")
        select = st.selectbox("Explore Categories 👀", ["Home", "Livestock","Horticulture", "Grain","About Us", "Ratings 📷"])
        
         
    
        st.write('Bringing you the best of insights')

    

    ################################################################################################
    # Data and Charts elements section --->
    if select == 'Livestock':
        st.header('Insights from Livestock Dataset')
        st.write('Insights from Livestock Dataset')
        # generates random numeric values!
        df = pd.DataFrame(
            np.random.randn(50, 20),
            columns=('col %d' % i for i in range(20))
        ) 
        st.dataframe(df) 
        
        

        st.header('Displaying Some Charts 📊')
        
                

    ################################################################################################
    # Text display section --->
    elif select == 'Horticulture':
        st.header('Insight from Horticulture Dataset')
        choice = st.selectbox("Select any type of Text 👇", ["Simple", "Markdown", "Subheader", "Code", "LaTex", "Caption"])
        
        if choice == 'Simple':
            st.write('This is an example of simple text')
        elif choice == 'Markdown':
            st.markdown("st.markdown --> *example* of **markdown text**")
        elif choice == 'Subheader':
            st.subheader('st.subheader --> for writing subheadings!')
        elif choice == 'Code':
            st.write('st.code example 👇')
            st.code("console.log('Hello World');")
        elif choice == 'LaTex':
            st.write('st.latex --> You can also write Math equations here! 🤓')
            st.latex("(a + b)^2 = a^2 + 2ab + b^2")
        elif choice == 'Caption':
            st.write('st.caption -->')
            st.caption('This is a caption!')
        else:
            st.write('')
            
        select_1 = st.selectbox("Explore Categories 👀", ["Home", "Livestock","Horticulture","About Us", "Ratings 📷"])

        select_1 = st.selectbox("Explore Categories 👀", ["Home", "Livestock","Horticulture","About Us", "Ratings 📷"])


    ################################################################################################
    # Input data display section --->
    elif select == 'Grains':
        st.header('Insight From Grain Dataset')

        # Part of Streamlit's "Layouts and Containers" Section
        col1, col2, col3 = st.columns([5, 5, 5], gap="medium") 
        with col1:
            st.write('📌This section covers **button** & **radio buttons** widgets')
            st.subheader('st.button')
            if st.button('Click me!✨'):
                st.balloons()
            else:
                st.write('')
        
        with col2:
            st.write('📌This section covers **selectbox** & **checkbox widgets**')
            st.subheader('st.selectbox')
            fruit = st.selectbox(
                'Which fruit do you like the most?',
                ('Apple 🍎', 'Peach 🍑', 'Banana 🍌', 'Watermelon 🍉', 'Grapes 🍇'))
            st.write('Your favorite fruit is', fruit)
            

        with col3:
            st.write('📌This section covers **slider** & **text input** widgets')
            st.subheader('st.slider')
            age = st.slider('Check your age 👇', 1900, 2022)
            calc = 2022 - age
            st.write('You are', calc, 'years old!')


        col4, col5, col6 = st.columns([5, 5, 5])
        with col4:
            st.subheader('st.radio')
            food = st.radio(
                "What's your favorite cuisine?",
                ('Indian', 'Chinese', 'Italian'))
            if food == 'Indian':
                st.write('You like to taste dishes made with different spices! 🌶')
            else:
                st.write('Your most common picks are either noodles 🍜/ 🍕')
            

        with col5:
            st.subheader('st.checkbox')
            st.write('Streamlit is easy to learn and apply!😎')
            agree = st.checkbox('I agree')
            disagree = st.checkbox("I don't think so! 😅")
            if agree:
                st.write('Great!')
            
            if disagree:
                st.write('No problem! Just start with some basics and then decide! 😏')
            
            
        with col6:
            st.subheader('st.text_input')
            greet = st.text_input('Your name here')
            st.write('👋 Hey!', greet, 'Glad to see you here.')
            
        
        
        st.subheader('st.file_uploader')
        st.write('⬆️ Upload Anything like images, CSVs, videos, audio, et.')
        uploaded = st.file_uploader("🖼️ Upload any Image")
        if uploaded is not None:
            display_image = Image.open(uploaded)
            st.image(display_image)
            
            
        st.markdown('🌟 You can try out with more widgets [here](https://docs.streamlit.io/library/api-reference/widgets)')

    ################################################################################################
    # Text display section --->
    elif select == 'About Us':
        st.header('About Us')
        st.write("Alltech Inc. is an International company with headquarters in Nigeria and branches in South Africa,Kenya and Uk.")
        st.write("Our team is made of Data Scientist, Data Engineers and UI team.")
        st.write("Our Services includes but not limited to Data extraction, Data Cleaning, Data Processing and Model Building in solving real world problems.")
        st.header('Meet Our Team')
        c1, c2, c3 = st.columns(3)
        with c1:
            logo = Image.open("pics/Bukola.PNG")
            st.image(logo, width=150)
            st.write("Bukola Badeji")
            st.write("Data Engineer")
            logo = Image.open("pics/Praise.PNG")
            st.image(logo, width=150)
            st.write("Praise Taiwo")
            st.write("Data Engineer")
        with c2:     
            logo = Image.open("pics/Chisom.PNG")
            st.image(logo, width=150)
            st.write("Chisom Nwankwo")
            st.write("Data Scientist")
            logo = Image.open("pics/Michael.PNG")
            st.image(logo, width=150)
            st.write("Michael Benjamin")
            st.write("Data Scientist")
        with c3:     
            logo = Image.open("pics/Simon.PNG")
            st.image(logo, width=150)
            st.write("Simon Nong")
            st.write("Data Scientist")
            logo = Image.open("pics/Mbusela.PNG")
            st.image(logo, width=150)
            st.write("Mbuyiselo Mkwanazi")
            st.write("Data Scientist")
            
        ##  st.image('https://www.scoopbyte.com/wp-content/uploads/2019/12/tom-and-jerry.jpg', width=300)
        ##with c2:
        #    st.image('https://github.com/Explore-AI/internship-project-2207-09/tree/main/streaamlit/pics/Chisom.PNG', width=200)
        #   st.image('https://im.indiatimes.in/media/content/itimes/blog/2014/Jul/9/1404917161_mickey+mouse.jpg', width=200)
        #   st.image('https://images6.fanpop.com/image/polls/1578000/1578435_1470083461280_full.jpg' ,width=250)
    ##st.caption('You can add images filepath using both online links (like above 👆) & from your hard disk!')    
    ################################################################################################
    # Media display section --->
    elif select == 'Ratings 📷':
        st.header('You can embed Images, Videos & Audio files all at one place! 😉')
        st.subheader('st.image')

        c1, c2 = st.columns(2)
        with c1:
            st.image('https://blog.streamlit.io/content/images/size/w2000/2022/03/snowflake_streamlit-1.gif', width=300)
            st.image('https://www.scoopbyte.com/wp-content/uploads/2019/12/tom-and-jerry.jpg', width=300)
        with c2:
            st.image('https://im.indiatimes.in/media/content/itimes/blog/2014/Jul/9/1404917161_mickey+mouse.jpg', width=200)
            st.image('https://images6.fanpop.com/image/polls/1578000/1578435_1470083461280_full.jpg' ,width=250)
        st.caption('You can add images filepath using both online links (like above 👆) & from your hard disk!')

        st.subheader('st.video')
        st.video('https://www.youtube.com/watch?v=fVsONlc3OUY')

        st.subheader('st.audio')
        audio_file = open('demo.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        st.write("""Audio Info :
                \n- *Genre* -- Holidays & Christmas, Worship
                \n- *Mood* -- Relaxed, Patient, Respectful, Subdued.
                \n- *Instruments* -- Acoustic Guitar, Flute
                \n- *Downloaded from* -- https://www.videvo.net/royalty-free-music/sort/popular/instrument/flute/""")
# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()

  