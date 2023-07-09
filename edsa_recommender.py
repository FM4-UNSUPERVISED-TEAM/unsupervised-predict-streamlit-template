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
Ratings = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_qq6gioyz.json")
Users = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_bo8vqwyw.json")
Movies = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_khzniaya.json")
Calender = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_mqzp4dzs.json")
Actors = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_51ja6AIG9j.json")
Timer = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ya9vcglm.json")
Budget = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_l5o1uey5.json")


local_css("resources/style/style.css")
#-------------------------------------------------------END OF TSHEPO ADDITION------------------------------------------------------------

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", 
                    "Solution Overview",
                    "EDA",
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


    # -------------------------------------------------------------------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    
# --------------------------------------TSHEPO'S START OF EDITION--------------------------------------------------------------------
#-----------------------------------------------CONTACT US----------------------------------------------------------------------------
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
                Nare = Image.open("resources/imgs/Nare.jpg")
                st.image(Nare)
            with text_column:
                st.subheader("Team leader and Project Manager: Nare Moloto")
                st.write("Oversees the project, coordinates team members, and ensures project goals are achieved.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Mkhanyisi = Image.open("resources/imgs/MK.jpg")
                st.image(Mkhanyisi)
            with text_column:
                st.subheader("Vice team leader and Data Analyst: Mkhanyisi Mlombile")
                st.write("Assists the team leader, contributes to data analysis, and provides insights and recommendations.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Ghaalib = Image.open("resources/imgs/Ghaalib.jpg")
                st.image(Ghaalib)
            with text_column:
                    st.subheader("Data Scientist: Ghaalib Van Der Ross")
                    st.write("Applies advanced analytics, develops and trains machine learning models, and extracts insights for predictions.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Edna = Image.open("resources/imgs/Edna.jpg")
                st.image(Edna)
            with text_column:
                st.subheader("Deadline Coordinator: Edna Kobo")
                st.write("A professional responsible for managing and overseeing project deadlines to ensure timely completion of tasks and deliverables.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Tshepo = Image.open("resources/imgs/Tshepo.jpg")
                st.image(Tshepo)
                with text_column:
                    st.subheader("Data Integration Engineer: Tshepo Serumula")
                    st.write("Specializes in integrating diverse data sources into a unified and usable format for analysis and decision-making purposes and responsible for designing and implementing data integration solutions.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Koketso = Image.open("resources/imgs/Koketso.jpg")
                st.image(Koketso)
                with text_column:
                    st.subheader("Feature Engineer: Koketso Makofane")
                    st.write("Responsible for identifying, designing, and extracting relevant features from raw data to improve model performance and predictive accuracy.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Katlego = Image.open("resources/imgs/Katlego.jpg")
                st.image(Katlego)
            with text_column:
                st.subheader("Business Analyst: Katlego Mthunzi")
                st.write("Responsible for bridging the gap between data analysis and business needs within an organization.")
                
# ----------------------------------------------EDA SECTION---------------------------------------------------------------------------------------------------
   	# Building out the Visualizations page
    if page_selection == "EDA":
        st.title("Exploratory Data Analysis")
        
        visual_options = ["EDA", "Movies Genres", "Movies Ratings", "Top Users", "Movies Releases Per Year", "Contents of Movies Data", "Duration Of Movies", "Movies Budget"]
        visual_options_selection = st.selectbox("Which visual category would you like to choose?",
		visual_options)
        
        if visual_options_selection == "EDA":
            st_lottie(
				EDA,
				speed=1,
				reverse=False,
				loop=True,
				quality="low",
				#renderer="svg",
				height=None,
				width=None,
				key=None,
			)
#------------------------------------------------------------------------------------------------------------------------------------------------
        if visual_options_selection == "F1_measure":
            per_listed = ['F1_measure']
            per_list = st.selectbox('I would like to view the...', per_listed)
            
            if per_list == 'F1_measure':
                st.subheader('F1 scores of the various models used')
                st.image('https://imgur.com/o1zYqC8.png', width=730)

#------------------------------------------------------------------------------------------------------------------------------------------------
# The 'Movies Genres' Page   
        if visual_options_selection == "Movies Genres":
            
            if visual_options_selection == "Movies Genres":
                st.image('https://i.imgur.com/JXcldP7.jpg', width=600)
            
            bar_nav_list = ['Most Common Genres (WordCloud)', 
			'Top 10 Genres', 
			]
            bar_nav = st.selectbox('I would like to view the...', bar_nav_list)
            
            if bar_nav == 'Most Common Genres (WordCloud)':
                st.subheader('The Most Popular And The Least Popular Genres')
                st.image('https://i.imgur.com/fPJwftY.png', width=700)
                st.write("This is how the Word Cloud Visual Above Was Generated.")
                st.write("1) The 'stopword' variable is a list of words that will be excluded from the word cloud. In this case, the stopwords are set to ['no genres', 'no', 'genres', 'genre', 'listed'].")
                
                
                
            if bar_nav == 'Top 10 Genres':
                
                raw_common_words_list = ['Top 10 Most Common Genres', 'Popular Genres',]
                
                raw_common_words = st.radio('Most Common and Least Common Genres', raw_common_words_list)
                
                if raw_common_words == 'Top 10 Most Common Genres':
                    st.subheader('Top 10 Genres by Volume')
                    st.image('https://i.imgur.com/4CrcSii.png', width=700)
                    #st.image("https://i.imgur.com/dTw9zLo.png", width=700)
                    
                    left_column, right_column = st.columns(2)
                    with left_column:
                        st.write("Top 10")
                        st.image('https://i.imgur.com/db3JHGR.png', width=300)
                        with right_column:
                            st.write("Bottom 10")
                            st.image("https://i.imgur.com/rP6MptS.png", width=400)
                    
                    st.write('Interestingly, we observe that the top genres by volume only have one or two genre types, whereas the bottom genres consist of multiple genres. This is probably because these movies are a lot uncommon, resulting in a lower volume in the dataset.')
                
                if raw_common_words == 'Popular Genres':
                    st.subheader('Popular Genres From Common To Least Common')
                    st.image('https://i.imgur.com/TCmHONY.png', width=700)
                    st.write("From the plot above, it is clearly visible that Drama is the most common genre preferred by the users from this movie.csv dataset with comedy coming in the second place. The least preferred genres are Musical, Film-Noir and also IMAX. From this data, this insinuates that users prefer movies that can make them laugh and have drama in them to movies which songs by the characters are interwoven into the narrative, sometimes accompanied by dancing (Musical Genre).")
                    st.write("The dominance of drama as a genre is perhaps not surprising when we consider the following:")
                    st.write("1) Drama is the cheapest genre to produce as movies don’t necessarily require special sets, costumes, locations, props, special/visual effects, etc.")
                    st.write("2) Drama has the broadest definition of all genres – everything that happens anywhere ever is a drama. Conversely, other genres have a higher bar for classification, such as the need for high-octane events for a movie to be classed as Action, scary events to be Horror, funny elements to be a Comedy, etc.")
                    st.write("Film marketers often complain that “Drama is not a genre”, insofar as it doesn’t give the potential audience member any clues as to what to expect.  Conversely, simply stating that a movie is a Western conveys a great deal of information about what may be on offer, including time period, location, tone, plot elements, character tropes and more.")

# Movies Ratings Page                    
            
        if visual_options_selection == 'Movies Ratings':
            st_lottie(
                Ratings,
			    speed=1,
				reverse=False,
				loop=True,
				quality="low",
				#renderer="svg",
				height=400,
				width=None,
				key=None,
			    )
            
            bar_nav_list = ['The Distribution Of The Movies Ratings', 
			'Tob Rated Movies',
            'Number Of Ratings Per Movie',
            'Ratings Per Day Of The Week',
            'Ratings Per Movie Genres', 
			]
            bar_nav = st.selectbox('I would like to view the...', bar_nav_list)
            
            if bar_nav == 'The Distribution Of The Movies Ratings':
                st.subheader('The Distribution Of The Movies Ratings')
                st.write("We Investigate The Top Rated Movies From The Dataset")
                st.image('https://i.imgur.com/woNxKn2.png', width=700)
                st.write("Insights From The Figure.")
                st.write("From the above plot we observe that the most poular movie of all time is Shawshank Redemption that was released in 1994 and that has an average rating of approximately 4.42.")

            if bar_nav == 'Tob Rated Movies':
                st.subheader('Tob Rated Movies')
                st.write("We investigate how ratings, which range from 0 to 5, incremented by 0.5, are distributed in the movies data. So we will analyze the movie ratings based on how users rate different movies from 0 to 5.")
                st.image('https://i.imgur.com/DkCDJSr.png', width=700)
                st.write("Insights From The Figure.")
                st.write("From the figure above we observe that 4.0 is")
             
            if bar_nav == 'Number Of Ratings Per Movie':
                st.subheader('Ratings Per Movie')
                st.write("We explore how many movies receive a number of ratings and visualize this in a plot. We group the 'rating' column in a DataFrame called 'df_train' by the 'movieId' column and counts the number of ratings for each movie. The count is then clipped at a maximum value of 50.")
                st.image('https://i.imgur.com/YbXyZ1p.png', width=700)
                
            if bar_nav == 'Ratings Per Day Of The Week':
                st.subheader('Ratings Per Day Of The Week')
                st.write("The number of ratings for the movies recieved per day of the week. We first convert a timestamp column to datetime format, extract the days of the week from the timestamp, and create a bar plot of the total number of ratings for each day of the week")
                st.image('https://i.imgur.com/GFf2hnM.png', width=700)
                
            if bar_nav == 'Ratings Per Movie Genres':
                st.subheader('Ratings Per Movie Genres')
                st.write("Here we wanted to check the ratings recieved by each movie genres in the dataset.")
                #st.image('https://i.imgur.com/4uLTKdA.png', width=700)
                
                bar_nav_list = ['Top 15 Most Popular Movie Genres by Rating', 
			    'Top 15 Least Popular Movie Genres by Rating', 
			    ]
                bar_nav = st.radio('I would like to view the...', bar_nav_list)
            
                if bar_nav == 'Top 15 Most Popular Movie Genres by Rating':
                    st.subheader('Top 15 Most Popular Movie Genres by Rating')
                    st.image('https://i.imgur.com/4uLTKdA.png', width=700)
                    
                if bar_nav == 'Top 15 Least Popular Movie Genres by Rating':
                    st.subheader('Top 15 Most Popular Movie Genres by Rating')
                    st.image('https://i.imgur.com/IByrt4V.png', width=700)
                    
        if visual_options_selection == 'Top Users':
            st_lottie(
                Users,
			    speed=1,
				reverse=False,
				loop=True,
				quality="low",
				#renderer="svg",
				height=400,
				width=None,
				key=None,
			    )
            bar_nav_list = ['Top Users By Number Of Ratings']
            bar_nav = st.radio('I would like to view the...', bar_nav_list)
            
            if bar_nav == 'Top Users By Number Of Ratings':
                st.subheader('Top Users By Number Of Ratings')
                st.write("Examining the top users using the number of ratings dataset. We create a bar plot of the top 20 users by the number of ratings they have given.")
                st.image('https://i.imgur.com/Nlnp8VL.png', width=700)
                
        
        if visual_options_selection == 'Movies Releases Per Year':
            left_column, right_column = st.columns(2)
            with left_column:
                st_lottie(
                    Movies,
				    speed=1,
				    reverse=False,
				    loop=True,
				    quality="low",
				    #renderer="svg",
				    height=300,
				    width=300,
				    key=None,
			        )
                with right_column:
                    st_lottie(
                        Calender,
				        speed=1,
				        reverse=False,
				        loop=True,
				        quality="low",
				        #renderer="svg",
				        height=400,
				        width=400,
				        key=None,
			            )
                bar_nav_list = ['Movies Releases Per Year']
                bar_nav = st.radio('I would like to view the...', bar_nav_list)
                if bar_nav == 'Movies Releases Per Year':
                    st.subheader('Movies Releases Per Year')
                    st.write("Examining the top users using the number of ratings dataset. We create a bar plot of the top 20 users by the number of ratings they have given.")
                    st.image('https://i.imgur.com/b9vljhW.png', width=700)
                    st.write("Generally, we observe that as the years progress, the amount of movies being released have significantly increased with the most movies released in 2015 and 2016. The number of movies being released per year have definitely shot up since the year 2000. We also observe that heading to the year of 2020, the number of movies released decreased significantly. This was during the year of COVID-19 which led to the total shutdown of the whole planet to quarantine. This proves significantly why there was a decrease in the number of movies released from the year 2018, 2019 and eventually going into the year of 2020.")


        if visual_options_selection == 'Contents of Movies Data':
            st_lottie(
                Actors,
				speed=1,
				reverse=False,
				loop=True,
			    quality="low",
				#renderer="svg",
				height=300,
			    width=300,
				key=None,
			    )

            bar_nav_list = ['Top 10 Popular Actors', 'Top 10 Most Popular Movie Directors', 'Most Common Words In The IMBD Dataset']
            bar_nav = st.radio('I would like to view the...', bar_nav_list)
            
            if bar_nav == 'Top 10 Popular Actors':
                st.subheader('Top 10 Popular Actors')
                st.write("Here we looked at the top actors based on the number of movies they have acted on.")
                st.image('https://i.imgur.com/lH56j9N.png', width=700)
                
            if bar_nav == 'Top 10 Most Popular Movie Directors':
                st.subheader('Top 10 Most Popular Movie Directors')
                st.write("Here we looked at the top directors based on the number of movies they have directed.")
                st.image('https://i.imgur.com/LA7pP7y.png', width=700)
                
            if bar_nav == 'Most Common Words In The IMBD Dataset':
                st.subheader('Most Common Words In The IMBD Dataset')
                st.write(" A Word cloud of the plot keywords from the 'plot_keywords' column in a IMBD DataFrame")
                st.image('https://i.imgur.com/xj4i6cG.png', width=700)
        
        if visual_options_selection == 'Duration Of Movies':
            st_lottie(
                Timer,
				speed=1,
				reverse=False,
			    loop=True,
			    quality="low",
				#renderer="svg",
				height=400,
				width=400,
				key=None,
			    )
            bar_nav_list = ['Top 10 Longest Movies From The Dataset']
            bar_nav = st.radio('I would like to view the...', bar_nav_list)
            if bar_nav == 'Top 10 Longest Movies From The Dataset':
                st.subheader('Top 10 Longest Movies From The Dataset')
                st.image('https://i.imgur.com/akScXGh.png', width=700)
                
        if visual_options_selection == 'Movies Budget':
            st_lottie(
            Budget,
			speed=1,
			reverse=False,
			loop=True,
		    quality="low",
		    #renderer="svg",
			height=None,
			width=None,
			key=None,
			)

            bar_nav_list = ['Sum of Total Movie budget per year', 'Top 20 Movies by Budget']
            bar_nav = st.radio('I would like to view the...', bar_nav_list)
            
            if bar_nav == 'Sum of Total Movie budget per year':
                st.subheader('Sum of Total Movie budget per year')
                st.image('https://i.imgur.com/InPkVi0.png', width=700)
                
            if bar_nav == 'Top 20 Movies by Budget':
                st.subheader('Top 20 Movies by Budget')
                st.image('https://i.imgur.com/lAKh39D.png', width=700)


#---------------------------------------TSHEPO'S END OF EDITION---------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
