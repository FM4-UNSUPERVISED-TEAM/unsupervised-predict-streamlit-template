"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
#------------------------------------------Loading Libraries---------------------------------------------------------------------------------------------------

# Streamlit dependencies
import streamlit as st
import joblib,os
from PIL import Image
from streamlit_lottie import st_lottie		#pip install streamlit-lottie
import requests	#pip install requests
from streamlit_option_menu import option_menu  #pip install streamlit-option-menu 
import json
import hydralit_components as hc
import datetime
import time

# Data handling dependencies
import pandas as pd
import numpy as np
import seaborn as sns
from sympy import im
import re
import csv
from nlppreprocess import NLP
import matplotlib.pyplot as plt
nlp = NLP()
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from scipy import sparse
from streamlit_player import st_player

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

#---------------------------------------Loading Data---------------------------------------------------------------------------------------------------------------
# Data Loading
title_list = load_movie_titles('https://raw.githubusercontent.com/FM4-UNSUPERVISED-TEAM/Data/main/movies.csv')

st.set_page_config(page_icon='resources/imgs/MovieWhiz.png', page_title= 'MovieWhiz', layout='wide',initial_sidebar_state='auto')

over_theme = {'txc_inactive': '#FFFFFF'}

# menu_data = [
#         {'icon':'Recommender System','label':"Recommender System"},
# 		{'id':'Solution Overview', 'icon': "far fa-clone", 'label':"Solution Overview"},
#         {'id':'Trailers','icon':'fas fa-film','label':'Trailers'},
#         {'id':'Insights', 'icon': "far fa-chart-bar", 'label':"Insights"},#no tooltip message
# 		{'id': 'About Us' , 'icon': "far fa-copy", 'label':"About Us"},
# 		{'id': 'Contact Us',  'icon': "far fa-address-book ", 'label':"Contact Us"},
# ]

# menu_id = hc.nav_bar(menu_definition=menu_data,home_name='Home',override_theme=over_theme,
#                       hide_streamlit_markers=False,sticky_nav=True, sticky_mode='pinned')

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
Performance = load_lottieurl("https://lottie.host/a3be8d01-63d0-4b44-b0fa-820597e7287b/E2WCCMuj8o.json")

local_css("resources/style/style.css")


#----------------------------------------------------------App Function--------------------------------------------------------------------------------------------
# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Insights", "Solution Overview","Trailers", "About Us", "Contact Us",]
    # page_selection = f'{menu_id}'

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        # st.write('### EXPLORE Data Science Academy Unsupervised Predict')
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
                    # with hc.HyLoader('Recommending movies you will like...\n',hc.Loaders.standard_loaders,index=[5,0,3]):
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
                    # with hc.HyLoader('Recommending movies you will like...\n',hc.Loaders.standard_loaders,index=[5,0,3]):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION --------------------------------------------------------------------------------------------------------------------------------------------------------
    # Solution Overview
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describing our winning approach on this page")

        st.markdown("""A Recommender System (RecSys) have become a key component in many online services, such as e-commerce, social media, news service, 
        or online video streaming. However with their growth in importance,  the growth in scale of industry datasets, and more sophisticated models, the bar
        has been raised for computational resources required for recommendation systems. This is no doubt one of the most obvious ways in which companies are enhancing the user experience
        in the platform that they provide their customers services. Companies Like Facebook, Netflix, Amazon, and Youtube are using RecSys to do so.
        RecSys are trained to understand the preferences, previous decisions, and characteristics of people and products, using data gathered about their interactions, which include
        impressions, clicks, likes, and purchases. Recommender systems help solve information overload by helping users find relevant products from a wide range of selections by 
        providing personalized content.  Because of their capability to predict consumer interests and desires on a highly personalized level, recommender systems are a favorite
        with content and product providers because they drive consumers to just about any product or service that interests them, from books to videos to health classes to clothing.
        More likely, these companies and other companies that are implementing the RecSys are doing so in introducing machine learning into these
        companies. It is therefore important for aspiring Data Scientists to develop skills in such areas. At Explore Data Science Academy (EDSA),
        our team was given a task to build a RecSys. There are three available approaches to building a recommender system. As part of this project our
        team explored two of these which were the Content Based Filtering and Collaborative Based Filtering algorithm.

            """)
        RecSys=Image.open("resources/imgs/RecSys.png")
        st.image(RecSys, use_column_width=False)

        # Collaborative Based Filtering
        st.subheader("**Collaborative Filtering**")
        st.markdown("""Collaborative filtering algorithms recommend items (this is the filtering part) based on preference information from many users (this is the collaborative part).
        This approach uses similarity of user preference behavior,  given previous interactions between users and items, recommender algorithms learn to predict future interaction. 
        These recommender systems build a model from a user’s past behavior, such as items purchased previously or ratings given to those items and similar decisions by other users.
        The idea is that if some people have made similar decisions and purchases in the past, like a movie choice, then there is a high probability they will agree on additional future selections.
        For example, if a collaborative filtering recommender knows you and another user share similar tastes in movies, it might recommend a movie to you that it knows this other user already likes. """)

        ColFil=Image.open("resources/imgs/ColFil2.png")
        st.image(ColFil, use_column_width=False)
        
        # Content Based Filtering
        st.subheader("**Content Based Filtering**")
        st.markdown("""Content filtering, by contrast, uses the attributes or features of an item  (this is the content part) to recommend other items similar to the user’s preferences. This approach is 
        based on similarity of items and user features,  given information about a user and items they have interacted with, (e.g. a user’s demographics, like age or gender, the category of a restaurant’s 
        cuisine, the average review for a movie), model the likelihood of a new interaction.  For example, if a content filtering recommender sees you liked the movies “You’ve Got Mail” and “Sleepless in 
        Seattle,” it might recommend another movie to you with the same genres and/or cast, such as “Joe Versus the Volcano.”""")

        ConFil=Image.open("resources/imgs/ConFil2.png")
        st.image(ConFil, use_column_width=False)

        st.subheader("**Building the Recommender Sytem**")
        st.markdown("""The recommender system application was built mainly for consumers to have a personalized experience of watching movies that they are
        likely to enjoy based on the three movies they have selected. The figure below shows the recommender app that uses both content based filtering and also collaborative based filtering. 
        Our app is similar to it in a sence that it uses the same algorithms to make predictions but it was built very different from it. From the 'recommender system' page, three movies are required as input in order to make recommendations based on which movie you have inputed in the seelction box.""")


        image=Image.open("resources/imgs/PickAMovie.png")
        st.image(image, use_column_width=False)

        st.markdown("""In building this web application, a couple of steps were followed starting with forking the repository from Github given by EDSA,
         using the dataset provided and obtained from the repository to build the recommender system. Following that was working with the script of the
         collaborative filtering algorithm by editing the code to obtain a movie prediction when using the main script run with streamlit. The about
         us has a link to the Github repo for if the intention is to attain better grasp on how the code works using python code.
            """)

        st.markdown("""This recommender engine is considered to be user friendly and one can easily use it to get movies that others have enjoyed and are
         related to the movies that they enjoy. This is done by only selecting three movies and press 'Recommend' and 10 movies will be suggested. """ )
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

# ----------------------------------------------HOME PAGE---------------------------------------------------------------------------------------------------
    # if page_selection == 'Home':
    #     # Header contents
    #     st.write('# Welcome to MovieWhiz')
    #     st.image('resources/imgs/1MovieWhiz.png')

# ----------------------------------------------EDA SECTION---------------------------------------------------------------------------------------------------
   	# Building out the Visualizations page
    if page_selection == "Insights":
        st.title("Exploratory Data Analysis")
        
        visual_options = ["Insights", "Raw Data", "Movies Genres", "Movies Ratings", "Top Users", "Movies Releases Per Year", "Contents of Movies Data", "Duration Of Movies", "Movies Budget", "Model Performance"]
        visual_options_selection = st.selectbox("Which visual category would you like to choose?",
		visual_options)
        
        if visual_options_selection == "Insights":
            st_lottie(
				EDA,
				speed=1,
				reverse=False,
				loop=True,
				quality="low",
				#renderer="svg",
				height=500,
				width=700,
				key=None,
			)
#------------------------------------------------------------------------------------------------------------------------------------------------
        if visual_options_selection == "Model Performance":
            
            if visual_options_selection == "Model Performance":
                st.header("Model Performance Evaluation")
                st_lottie(
                    Performance,
				    speed=1,
				    reverse=False,
				    loop=True,
				    quality="low",
				    #renderer="svg",
				    height=400,
				    width=600,
				    key=None,
			    )
            
            per_listed = ['Model Performance']
            per_list = st.selectbox('I would like to view the...', per_listed)
            
            if per_list == 'Model Performance':
                st.subheader('RMSE Scores Of The Various Models Used')
                st.image('https://i.imgur.com/8cHPlxM.png', width=730)
                st.write("We implemented a few models for Both the collaborative and content-based filtering to find a model that gives us the best rmse score which is a representation of our model performance. The model with the best rmse score was the singular value decomposition (SVD). The SVD is very good at noise detection and does this by reducing the dimensions of a matrix in order to make certain subsequent matrix calculations simpler, which is why it gave better RSME score. By the Implementation of Singular Value Decomposition, which returned a very good score of 0.779  we can conclude that the algorithm implemented for our app is very good at movie recommendations.We implemented a few models for Both the collaborative and content-based filtering to find a model that gives us the best rmse score which is a representation of our model performance. The model with the best rmse score was the singular value decomposition (SVD). The SVD is very good at noise detection and does this by reducing the dimensions of a matrix in order to make certain subsequent matrix calculations simpler, which is why it gave better RSME score. By the Implementation of Singular Value Decomposition, which returned a very good score of 0.779  we can conclude that the algorithm implemented for our app is very good at movie recommendations.")

#------------------------------------------------------------------------------------------------------------------------------------------------
# The 'Movies Genres' Page   
        if visual_options_selection == "Movies Genres":
            
            if visual_options_selection == "Movies Genres":
                st.image('https://i.imgur.com/JXcldP7.jpg', width=600)
            
            bar_nav_list = ['Most Common Genres', 
			'Top 10 Genres', 
			]
            bar_nav = st.selectbox('I would like to view the...', bar_nav_list)
            
            if bar_nav == 'Most Common Genres':
                st.subheader('The Most Popular And The Least Popular Genres')
                st.image('https://i.imgur.com/TCmHONY.png', width=700)
                #st.write("This is how the Word Visual Above Was Generated.")
                #st.write("1) The 'stopword' variable is a list of words that will be excluded from the word cloud. In this case, the stopwords are set to ['no genres', 'no', 'genres', 'genre', 'listed'].")
                #st.write("WordCloud visualization showed the most prevalent genres (comedy and drama) and the effect. This provides a better idea of potential biases in the training set so we can eliminate them during our model constructing stage.")
                st.write("From the bar graph depicted above, there is a clear indication that Drama is the most common genre preferred by the users from this movies dataset with comedy coming in the second place. The least preferred genres are Musical, Film-Noir and IMAX. From this data, this insinuates that users prefer movies that can make them laugh and have drama in them to movies which songs by the characters are interwoven into the narrative, sometimes accompanied by dancing (Musical Genre).")
                st.write("Observations:")
                st.write("Drama, Comedy, Action, Thriller and adventure are the top 5 genre in the dataset.")
                st.write("Recommendations:")
                st.write("Netflix should endeavor to match the order of genre of movies available in terms of quantity to the popularity of the genre so as to maximise the views, this in turn will maximise the revenue in films.")
                
                
            if bar_nav == 'Top 10 Genres':
                
                raw_common_words_list = ['Top 10 Most Common Genres', 'Popular Genres',]
                
                raw_common_words = st.radio('Most Common and Least Common Genres', raw_common_words_list)
                
                if raw_common_words == 'Top 10 Most Common Genres':
                    st.subheader('Top 10 Genres by Volume')
                    st.image('https://i.imgur.com/5oZp0Wc.png', width=700)
                    #st.image("https://i.imgur.com/dTw9zLo.png", width=700)
                    
                    #left_column, right_column = st.columns(2)
                    #with left_column:
                        #st.write("Top 10")
                        #st.image('https://i.imgur.com/db3JHGR.png', width=300)
                        #with right_column:
                            #st.write("Bottom 10")
                            #st.image("https://i.imgur.com/rP6MptS.png", width=400)
                    
                    st.write('Interestingly, we observe that the top genres by volume only have one or two genre types, whereas the bottom genres consist of multiple genres. This is probably because these movies are a lot uncommon, resulting in a lower volume in the dataset.')
                
                if raw_common_words == 'Popular Genres':
                    st.subheader('Popular Genres From Common To Least Common')
                    st.image('https://i.imgur.com/TCmHONY.png', width=700)
                    st.write("From the plot above, it is clearly visible that Drama is the most common genre preferred by the users from this movie.csv dataset with comedy coming in the second place. The least preferred genres are Musical, Film-Noir and also IMAX. From this data, this insinuates that users prefer movies that can make them laugh and have drama in them to movies which songs by the characters are interwoven into the narrative, sometimes accompanied by dancing (Musical Genre).")
                    st.write("The dominance of drama as a genre is perhaps not surprising when we consider the following:")
                    st.write("1) Drama is the cheapest genre to produce as movies don’t necessarily require special sets, costumes, locations, props, special/visual effects, etc.")
                    st.write("2) Drama has the broadest definition of all genres – everything that happens anywhere ever is a drama. Conversely, other genres have a higher bar for classification, such as the need for high-octane events for a movie to be classed as Action, scary events to be Horror, funny elements to be a Comedy, etc.")
                    st.write("Film marketers often complain that “Drama is not a genre”, insofar as it doesn’t give the potential audience member any clues as to what to expect.  Conversely, simply stating that a movie is a Western conveys a great deal of aboutUsrmation about what may be on offer, including time period, location, tone, plot elements, character tropes and more.")

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
			'Top Rated Movies',
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
                st.write("To get a sense of the distribution of movie ratings a bar chart was made to reveal that the ratings are skewed to left and have a mode of 4. From the figure above we observe that 4.0 is the most commonly score (rated), with 26.5% of the movies in the dataframe assigned that score. This could be explained by the fact that users tend to only rate movies they enjoyed and avoid rating movies which they failed to enjoy. If a user does not enjoy a movie, it is unlikely that they will watch it up until the end and provide a rating. This is why 18% of all the rated movies have a score of less than 3. To support this idea, the most rated stars range from 3 to 5 while the less rated columns are from 0.5 to 2.5. This might also mean that people tend to rate a movie they have watched to the end and actually enjoyed it, rather than a movie which they didn't finish or enjoy.")
                st.write("We also observe that half scores (0.5, 1.5, 2.5, 3.5 and 4.5) are less commonly used than integer score values. We do not know if this is because users prefer to rate movies with integer values or if it's because half scores were introduced after the original scoring system was already in use, leading to a decreased volume in a dataset with ratings from 1995.")
                st.write("Observations:")
                st.write("We can observe that a high percentage of our movies were rated above average i.e above 3. A low percentage were below 3")
                st.write("Recommendations:")
                st.write("Hence More movies are high quality perhaps people are watching movies that are recommended to them, either by their social groups or the recommender system itself.")
                
            if bar_nav == 'Top Rated Movies':
                st.subheader('Top Rated Movies')
                st.write("We investigate how ratings, which range from 0 to 5, incremented by 0.5, are distributed in the movies data. So we will analyze the movie ratings based on how users rate different movies from 0 to 5.")
                st.image('https://i.imgur.com/DkCDJSr.png', width=700)
                st.write("Insights From The Figure.")
                st.write("From the above plot we observe that the most poular movie of all time is Shawshank Redemption that was released in 1994 and that has an average rating of approximately 4.42.")
             
            if bar_nav == 'Number Of Ratings Per Movie':
                st.subheader('Distribution Of Number Ratings Per Movie')
                st.write("The figure above shows the distribution of the number of ratings per movie from a DataFrame df_train. The clip function is used to limit the maximum count to 50, ensuring that the histogram does not have overly long bars due to outliers or high counts.")
                st.write("We explore how many movies receive a number of ratings and visualize this in a plot. We group the 'rating' column in a DataFrame called 'df_train' by the 'movieId' column and counts the number of ratings for each movie. The count is then clipped at a maximum value of 50.")
                st.image('https://i.imgur.com/YbXyZ1p.png', width=700)
                st.write("Most movies have a relatively low number of ratings: The majority of movies fall within the lower count range, which indicates that most movies receive a limited number of ratings.")
                st.write("Long-tail distribution: The plot shows a long-tail distribution, where there are a few movies with a significantly higher number of ratings compared to the rest. These are likely popular or blockbuster movies that have received more attention and reviews from users.")
                st.write("Outliers: There might be a few outliers on the higher end of the count, representing movies with an unusually large number of ratings. These outliers could be influential or polarizing movies that garnered extensive attention from viewers.")
                st.write(" User engagement: The plot can provide insights into user engagement with movies. Movies with higher ratings counts are likely to be more well-known and have received feedback from a broader user base.")
                st.write("Data quality: The plot can also be used to identify potential data quality issues. For example, movies with very high or very low ratings counts could be outliers or misreported data points.")
                
            if bar_nav == 'Ratings Per Day Of The Week':
                st.subheader('Ratings Per Day Of The Week')
                st.write("The number of ratings for the movies recieved per day of the week. We first convert a timestamp column to datetime format, extract the days of the week from the timestamp, and create a bar plot of the total number of ratings for each day of the week")
                st.image('https://i.imgur.com/GFf2hnM.png', width=700)
                st.write("Observations:")
                st.write("Weekend Peaks: There is a higher number of ratings during weekends (Saturday and Sunday). This could indicate that users are more likely to watch and rate movies during their leisure time, especially on weekends when they have more free time. ")
                st.write("Movie Releases and Marketing: Spikes in ratings on specific days could be linked to movie releases and marketing strategies. For instance, if many movies are released on Fridays, there might be a higher number of ratings on Fridays and Saturdays.")
                st.write("User Engagement on Specific Days: The ratings per day of the week can help identify which days users are most engaged with the platform. This insight can be useful for scheduling content updates, promotions, or site maintenance.")
                
            if bar_nav == 'Ratings Per Movie Genres':
                st.subheader('Ratings Per Movie Genres')
                #st.write("Here we wanted to check the ratings recieved by each movie genres in the dataset.")
                st.write("Here we wanted to check the ratings recieved by each movie genres in the dataset by volume. We first merge the 'df_train' and 'df_movies' DataFrames based on the 'movieId' column and perform a group-by operation to calculate the average rating for each movie genre. We then create a bar plot of the top 15 movie genres based on the average rating.")
                st.write("The average ratings for movie genres can provide useful insights into the popularity of the different genres. Those genres with high average ratings indicate a higher level of audience satisfaction and appreciation for movies in those particular genres and vice versa. This insight will help us understand the genres that resonate most positively with users.")
                #st.image('https://i.imgur.com/4uLTKdA.png', width=700)
                
                bar_nav_list = ['Top 15 Most Popular Movie Genres by Rating', 
			    'Top 15 Least Popular Movie Genres by Rating', 
			    ]
                bar_nav = st.radio('I would like to view the...', bar_nav_list)
            
                if bar_nav == 'Top 15 Most Popular Movie Genres by Rating':
                    st.subheader('Top 15 Most Popular Movie Genres by Rating')
                    st.image('https://i.imgur.com/4uLTKdA.png', width=700)
                    st.write("Observations:")
                    st.write("Most Explored Themes: The most popular genres could represent movie themes and concepts that are more explored in mainstream cinema. This include genres Animation|Crime|Fantasy|Mystery|Sci-Fi.")
                    st.write("More Exposure: These genres might have extended exposure or distribution, leading to more ratings compared to less widely available genres.")
                    
                if bar_nav == 'Top 15 Least Popular Movie Genres by Rating':
                    st.subheader('Top 15 Most Popular Movie Genres by Rating')
                    st.image('https://i.imgur.com/IByrt4V.png', width=700)
                    st.write("Observations:")
                    st.write("Less Explored Themes: The least popular genres could represent movie themes and concepts that are less explored in mainstream cinema. This include genres like Drama|Horror|Western.")
                    st.write("Limited Exposure: These genres might have limited exposure or distribution, leading to fewer ratings compared to more widely available genres.")
                    
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
                st.write("Observations:")
                st.write("User Engagement: The chart shows which users are the most active and engaged on the platform, providing the highest number of ratings. These users could be key influencers or frequent users who contribute significantly to the platform's activity.")
                
        
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
                    st.write("Observations:")
                    st.write("We observed a decrease in the movies published per year from 2000")
                    st.write("Recommendations:")
                    st.write("It is not clear what accounts for the decrease in movies published but possible reasons for this change include finacial crisis in 2000 and in 2009.")

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
                st.write("Observations:")
                st.write("Popularity and Demand: By identifying the top actors by volume, base on the data provided, is an indication of the actors popularity and demand within the film industry. Those actors cast in a large number of movies are likely to have a significant fan base and appeal to audiences and filmmakers.")
                st.write("Experience and Versatility: Actors cast in large number of movies demonstrate their experience and versatility in portraying different roles and genres. These actors clearly possess the necessary skills and range to adapt to various characters and storytelling styles.")
                st.write("Movie Success: The presence of top actors may have an impact on the success of those films. Their established fan base and reputation can attract viewers and contribute to the box office performance or viewership of the movies regardless on whether the movies is highly rated or not.")
                
            if bar_nav == 'Top 10 Most Popular Movie Directors':
                st.subheader('Top 10 Most Popular Movie Directors')
                st.write("Here we looked at the top directors based on the number of movies they have directed.")
                st.image('https://i.imgur.com/LA7pP7y.png', width=700)
                st.write("By identifying the most commonly used directors is a clear indication of their popularity, skill and talent within the film industry. Much like the top actors, the presence of top directors will also have an impact on the success of the film. With an established reputation they can attract viewers and contribute to the box office performance or viewership of the movies.")
                
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
                st.write("Observations:")
                st.write("Epic Productions: The presence of extremely long movies among the top 10 suggests that epic and ambitious productions have been popular or significant in the dataset with Taken(2002) toping the chart as the longest movie from the dataset.")
                st.write("Filmmaking Styles: Long movies often indicate that filmmakers are exploring complex narratives, in-depth character development, or immersive storytelling techniques.")
                
                
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

            bar_nav_list = ['Sum Of Total Movie Budget Per Year', 'Top 20 Movies By Budget', "Average Budget Per Genre"]
            bar_nav = st.radio('I would like to view the...', bar_nav_list)
            
            if bar_nav == 'Sum Of Total Movie Budget Per Year':
                st.subheader('Sum Of Total Movie Budget Per Year')
                st.image('https://i.imgur.com/InPkVi0.png', width=700)
                st.write("It is clear that the data in terms of the budget of the movies is missing a lot of entries from the year 2013 to 2019. However, it is clear that there is an increase in the budget used to produce movies over the years.")
                
            if bar_nav == 'Top 20 Movies By Budget':
                st.subheader('Top 20 Movies By Budget')
                st.write("Despite the significant number of missing data from the budget column of the merged_df dataset, we are still provided with a view of high budgets provided for certain movies. If we were to have additional information which provides the revenue for each movie there is scope for extremely valuable insights such as:")
                st.image('https://i.imgur.com/lAKh39D.png', width=700)
                st.write("Profitability: If we compare the revenue-to-budget ratio across different movies we can identify those movies that have been particularly profitable and those who have failed to generate any profit at all. Movies with a high ratio indicate that they have exceeded revenue expectations, therefore, providing profits to the studios and production companies involved.")
                
            if bar_nav == "Average Budget per Genre":
                st.header("Average Budget per Genre")
                st.image('https://i.imgur.com/oXiA633.png', width=700)
                st.write("The visual above shows the average budget per movie genre. This provides valuable insights into how budgets are distributed across different genres.")
                st.write("Observations:")
                st.write("Genre Budget Comparison: The bar chart allows the compare of the average budgets of different genres directly. We can identify genres with higher budgets and those with lower budgets, giving us an idea of which genres tend to require more significant investments, which in this case is th IMAX followed by Adventure.")
                st.write("Popular vs. Expensive Genres: By comparing the average budgets with genre popularity, we might identify whether there is a correlation between a genre's popularity and its budget. Some genres may have high budgets due to their appeal to a broader audience, while others might have relatively high budgets despite being less popular. From the 'Most Popular Genre' figure at the top, we showed that Drama is the most popular genre. The insights drawn was that Dramatic movies are cheaper to produce. This is supported by this 'Average Budget per Genre' figure where Drama is shown to have a very low budget.")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------Raw Data-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if visual_options_selection == "Raw Data":
            st.title("Raw Data")
            st.write("This page was designed to help data analysts to get a better understanding of the data. It focuses specifically on the movies and ratings datasets.")
            st.header("The Movies dataset")
            df = pd.read_csv('resources/data/movies.csv')
            st.write("Displaying the first few entries in the movie dataset")
            st.write(df)
        
            st.write("Displaying basic statistics about the movieId column.")
            st.write(df.describe())

            # show shape
            if st.checkbox("Check to display the shape of the Movies Dataset"):
                data_dim = st.radio("Show Dimensions By ", ("Rows", "Columns"))
                if data_dim == 'Row':
                    st.text("Number of Rows")
                    st.write(df.shape[0])
                elif data_dim == 'Columns':
                    st.text("Number of Columns")
                    st.write(df.shape[1])
                else:
                    st.write(df.shape[0])

            if st.checkbox("Check to see specific columns"):
                all_columns = df.columns.tolist()
                selected_columns = st.multiselect("Select", all_columns)
                new_df = df[selected_columns]
                st.dataframe(new_df)

            # Show values
            if st.button("Display the amount of movies for each genre"):
                st.text("The amount of movies by genre.")
                st.write(df.iloc[:,-1].value_counts())

        

            df1 = pd.read_csv("resources/data/ratings.csv")
            st.header("The Ratings (Train) dataset")
            st.write("Displaying the first few entries in the ratings dataset")
            st.write(df1)


            if st.checkbox("Check to display the shape of the Ratings Dataset"):
                data_dim1 = st.radio("Show Dimensions by ", ("Rows", "Columns"))
                if data_dim1 == 'Rows':
                    st.text("Number of Rows")
                    st.write(df1.shape[0])
                elif data_dim1 == 'Columns':
                    st.text("Number of Columns")
                    st.write(df1.shape[1])
                else:
                    st.write(df1.shape[0])

            if st.checkbox("Check to see specific columns "):
                all_columns = df1.columns.tolist()
                selected_columns = st.multiselect("Select one or more columns to display", all_columns)
                new_df = df1[selected_columns]
                st.dataframe(new_df)

            st.write("Displaying basic statistics of the Ratings dataset")
            st.write(df1.describe())


            st.write("Displaying the ratings distribution accross all users")
            fig, ax = plt.subplots()
            df1.hist(
            bins=8,
            column="rating",
            grid=False,
            figsize=(8, 8),
            color="#86bf91",
            zorder=2,
            rwidth=0.9,
            ax=ax,  
            )
            st.write(fig)

# ----------------------------------------------trailers---------------------------------------------------------------------------------------------------
    
    # embed a youtube video
    if page_selection == "Trailers":

        st.header("Top 10 movies")
        year = st.slider('Select Release Year Period', 2023, 2018, 2023)
        st.write('You selected movies released between', str(2018), 'and', str(year))
        if year == 2023:
            with st.expander('Top 10 Best Movies 2023'):
                st_player('https://www.youtube.com/watch?v=YQZJinEtFlM')
                st.write('**Which movies did you like?**')
        
        if year >= 2022:
            with st.expander('Top 10 Best Movies 2022'):
                st_player('https://www.youtube.com/watch?v=emrUk0cW3O4')
                st.write('**Which movies did you like?**')
                
        if year >= 2021:
            with st.expander('Top 10 Best Movies 2021'):
                st_player('https://www.youtube.com/watch?v=_wRoljeeF5k')
                st.write('**Which movies did you like?**')
                
        if year >= 2020:
            with st.expander('Top 10 Best Movies 2020'):
                st_player('https://www.youtube.com/watch?v=K7AHRF9X1i8')
                st.write('**Which movies did you like?**')
                
        if year >= 2019:
            with st.expander('Top 10 Best Movies 2019'):
                st_player('https://youtu.be/48NL3N6KMFo?t=9')
                st.write('**Which movies did you like?**')
                
        if year >= 2018:
            with st.expander('Top 10 Best Movies 2018'):
                st_player('https://youtu.be/FkUtWUy77fQ?t=9')
                st.write('**Which movies did you like?**')
                

    #-----------------------------------------------CONTACT US----------------------------------------------------------------------------
    if page_selection == 'Contact Us':
        st.header("Get In Touch With Us!")
        
        col1, col2, col3 = st.columns(3)
        col1.header('Location')
        col1.write('523 De Kock ST, Pretoria, 0002')
        col2.header('Telephone')
        col2.write('(+27) 727910473')
        col3.header('Email')
        col3.write('simon.blanco@synergysolution.com')
        
        
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
        #Loading the google maps
        def main():
            st.title("Directions To The Main Office")
            google_maps_embed_code = """<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3593.4376091292775!2d28.212081211194214!3d-25.756105445780477!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1e95618dd4b32c81%3A0x86adf140930befdb!2s523%20De%20Kock%20St%2C%20Sunnyside%2C%20Pretoria%2C%200002!5e0!3m2!1sen!2sza!4v1689921462377!5m2!1sen!2sza" width="800" height="600" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>"""
            st.components.v1.html(google_maps_embed_code, width=1400, height=400)
        #call the function
        map = main()
        #st.write(map)

        
#-----------------------------------------About Us Page---------------------------------------------------------------------------------------------------

    if page_selection == "About Us":
        
        st.title("About Us")
        
        st.markdown("We are a company that is dedicated to providing advanced analytics solutions. We aim not only to leverage advanced analytics, artificial intelligence, and machine learning, Our target is to also transform industries, drive innovation, and shape a data-driven future")
        st.markdown("We are committed to staying at the forefront advancements in data science as we work closely with our clients, to understand their unique challenges and goals.")

        
        st.title("Meet The Synergy Solution Team")
        # st.aboutUs("The Team Behind This Robust Work")
        st.markdown("We are a proud exceptional team that works together towards the company's shared goals. Our collective skills, commitment, and collaborative spirit is what drive us forward,as we ensure that we consistently deliver outstanding results to our valued clients.")

        
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
                st.subheader("Chief Executive Officer: Nare Moloto")
                st.write("A visionary leader with extensive experience in the industry. She is passionate about driving the company's growth and ensuring its success. Nare is a machine learning whiz who can build powerful models with ease. Apart from her coding prowess, she has a deep passion for films and after the work dust has settled, she is a gymnastic coach.")
                
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Mkhanyisi = Image.open("resources/imgs/MK.jpg")
                st.image(Mkhanyisi)
            with text_column:
                st.subheader("Data Scientist: Mkhanyisi Mlombile")
                st.write("Mkhanyisi's passion for data science goes beyond his professional work. In his free time, he enjoys participating in Kaggle competitions, where he applies his skills to real-world datasets and collaborates with other data scientists worldwide. He is also an avid reader of data science literature and actively contributes to the data science community by sharing his knowledge. The same dedication he puts in when preparing his mouth watering dishes. A professional chef too.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Ghaalib = Image.open("resources/imgs/Ghaalib.jpg")
                st.image(Ghaalib)
            with text_column:
                    st.subheader("Data Scientist: Ghaalib Van Der Ross")
                    st.write(" an accomplished data scientist with a passion for extracting insights from complex datasets. With a strong background in statistics, mathematics, and programming, he leverages his expertise to tackle challenging analytical problems. Our award winnng author who has won  over 20 writing competitions around the world.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Edna = Image.open("resources/imgs/Edna.jpg")
                st.image(Edna)
            with text_column:
                st.subheader("Coordinator: Edna Kobo")
                st.write("A talented and innovative designer who brings a creative flair to our team. With a keen eye for aesthetics and a deep understanding of user-centered design principles, she consistently delivers visually appealing and user-friendly designs. In her spare time she performs her magic through kids as a yoga instructor.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Tshepo = Image.open("resources/imgs/Tshepo.jpg")
                st.image(Tshepo)
                with text_column:
                    st.subheader("Data Scientist: Tshepo Serumula")
                    st.write("Specializes in integrating diverse data sources into a unified and usable format for analysis and decision-making purposes and responsible for designing and implementing data integration Solution Overviews. A tech-savvy professional with a strong background in software development. He leads our technical team and ensures innovative solutions are delivered to our clients. He is a skilled beatboxer, creating impressive beats using only his voice.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Koketso = Image.open("resources/imgs/Koketso.jpg")
                st.image(Koketso)
                with text_column:
                    st.subheader("Feature Engineer: Koketso Makofane")
                    st.write("With a solid foundation in statistics, mathematics, and programming, koketso utilizes her expertise to analyze data and develop innovative feature engineering strategies. Off the clock, she immerses herself in the world of books. Koketso is an avid reader who devours literature from various genres.")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                Katlego = Image.open("resources/imgs/Katlego.jpg")
                st.image(Katlego)
            with text_column:
                st.subheader("Business Analyst: Katlego Mthunzi")
                st.write("A results-oriented marketing specialist with a strong background in digital marketing strategies. He excels in crafting effective marketing campaigns, leveraging her analytical skills to drive customer engagement and increase brand activity. A former professional athlete, whom is coach during weekends.")

#---------------------------------------TSHEPO'S END OF EDA Section----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
