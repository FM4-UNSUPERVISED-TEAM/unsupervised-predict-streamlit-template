"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ----------------------------------------------------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os
from PIL import Image
from streamlit_lottie import st_lottie		#pip install streamlit-lottie
import requests	#pip install requests
from streamlit_option_menu import option_menu  #pip install streamlit-option-menu 
import json

# Data handling dependencies
import pandas as pd
import numpy as np
import seaborn as sns
import re
from nlppreprocess import NLP
nlp = NLP()
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from scipy import sparse

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

#-------------------------------------------------------START OF TSHEPO's ADDITION-------------------------------------------------------------------
st.set_page_config(page_title="Synergy Solutions", page_icon="resources/imgs/EDSA_logo.png")

#theme.primaryColor
primary_clr = st.get_option("theme.primaryColor")
txt_clr = st.get_option("theme.textColor")
    # I want 3 colours to graph, so this is a red that matches the theme:
second_clr = "#d87c7c"

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

Contact_Us = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_ebqz3ltq.json")
Meet_Team = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tylfbkf3.json")
EDA = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_zcb74lq5.json")


local_css("resources/style/style.css")
#-------------------------------------------------------END OF TSHEPO ADDITION------------------------------------------------------------

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", 
                    "Solution Overview",
                    "About Us", 
                    "Contact Us"]
    
    
    # --------------------------------------TSHEPO'S START OF EDITION--------------------------------------------------------------------
    
    
    #---------------------------------------TSHEPO'S END OF EDITION-------------------------------------------------------------------------

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -----------------------------------------------------------------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    
# --------------------------------------TSHEPO'S START OF EDITION--------------------------------------------------------------------
    if page_selection == "Contact Us":
        st.header("Get In Touch With Us!")
        
        # ---- CONTACT ----
        with st.container():
            st.write("---")
            st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/tshepoelifa238@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(
				Contact_Us,
				speed=1,
				reverse=False,
				loop=True,
				quality="low",
				#renderer="svg",
				height=None,
				width=None,
				key=None,
			)

# ----------------------------------------------ABOUT US-------------------------------------------------------------------------------
    if page_selection == "About Us":
        st.title("Meet the Synergy Solutions Team")
        st.info("The Team Behind This Robust Work")
        
        st_lottie(
				Meet_Team,
				speed=1,
				reverse=False,
				loop=True,
				quality="low",
				#renderer="svg",
				height=400,
				width=400,
				key=None,
			)
        
        with st.container():
            st.write("---")
            st.write("##")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Nare = Image.open("resources/imgs/Tshepo.JPG")
                st.image(Nare)
            with text_column:
                st.subheader("Team leader and Project Manager: Nare Moloto")
                st.write("Oversees the project, coordinates team members, and ensures project goals are achieved.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Mkhanyisi = Image.open("resources/imgs/Tshepo.JPG")
                st.image(Mkhanyisi)
            with text_column:
                st.subheader("Vice team leader and Data Analyst: Mkhanyisi Mlombile")
                st.write("Assists the team leader, contributes to data analysis, and provides insights and recommendations.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Ghaalib = Image.open("resources/imgs/Tshepo.JPG")
                st.image(Ghaalib)
            with text_column:
                    st.subheader("Data Scientist: Ghaalib Van Der Ross")
                    st.write("Applies advanced analytics, develops and trains machine learning models, and extracts insights for predictions.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Edna = Image.open("resources/imgs/Tshepo.JPG")
                st.image(Edna)
            with text_column:
                st.subheader("Deadline Coordinator: Edna Kobo")
                st.write("A professional responsible for managing and overseeing project deadlines to ensure timely completion of tasks and deliverables.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Tshepo = Image.open("resources/imgs/Tshepo.JPG")
                st.image(Tshepo)
                with text_column:
                    st.subheader("Data Integration Engineer: Tshepo Serumula")
                    st.write("Specializes in integrating diverse data sources into a unified and usable format for analysis and decision-making purposes and responsible for designing and implementing data integration solutions.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Koketso = Image.open("resources/imgs/Tshepo.JPG")
                st.image(Koketso)
                with text_column:
                    st.subheader("Feature Engineer: Koketso Makofane")
                    st.write("Responsible for identifying, designing, and extracting relevant features from raw data to improve model performance and predictive accuracy.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Katlego = Image.open("resources/imgs/Tshepo.JPG")
                st.image(Katlego)
            with text_column:
                st.subheader("Business Analyst: Katlego Mthunzi")
                st.write("Responsible for bridging the gap between data analysis and business needs within an organization.")

#---------------------------------------TSHEPO'S END OF EDITION---------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
