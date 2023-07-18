import streamlit as st
from PIL import Image

# specify the file path for the images
image1_path= "C:/Users/Home-User/Pictures/company.jpeg"
image2_path= "C:/Users/Home-User/Pictures/Company-Analysis 2.jpg"

# Header
st.header("ABOUT US.")

# Introduction
st.markdown("We are a company that is dedicated to providing advanced analytics solutions. We aim not only to leverage advanced analytics, artificial intelligence, and machine learning, Our target is to also transform industries, drive innovation, and shape a data-driven future")
st.markdown("We are committed to staying at the forefront advancements in data science as we work closely with our clients, to understand their unique challenges and goals.")
            
st.write("")
st.write("")
st.write("")
# Open the image file
image2 = Image.open(image2_path)
st.image(image2, use_column_width=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

# ADDING COLUMNS 
col1, col2,= st.columns([1,2])
col1.markdown("---") 

# Column 1: Company motto
with col1:
    # Using st.empty() to create empty lines
    for _ in range(15):
        st.empty()
    quote = "Good business leaders create a vision, articulate the vision, passionately own the vision, and relentlessly drive it to completion."
    author = "Jack Welch"

    st.markdown(f"> {quote}\n\n— {author}")

# Column 2: Company Photo
with col2:
    st.write("")
    # Open the image file
    image1 = Image.open(image1_path)
    st.image(image1, use_column_width=True)
    
st.write("")
st.write("")
st.write("")
st.write("")

st.header("Our Team")
st.markdown("We are a proud exceptional team that works together towards the company's shared goals. Our collective skills, commitment, and collaborative spirit is what drive us forward,as we ensure that we consistently deliver outstanding results to our valued clients.")

st.write("")
st.write("")
st.write("")
# Define the team members
team_members = [
    {
        "image_path": "C:\\Users\\Home-User\\Pictures\\images\\Nare.jpg",
        "name": "Nare Moloto",
        "role": "CEO",
        "bio": "A visionary leader with extensive experience in the industry. She is passionate about driving the company's growth and ensuring its success. After the work dust has settled, she is a gymnastic coach.",
        "twitter": "https://twitter.com/@MOLOTO NARE",
        "facebook": "https://facebook.com/Moloto Nare",
        "linkedin": "https://linkedin.com/in/Moloto Nare"
        
    },
    {
        "image_path": "C:\\Users\\Home-User\\Pictures\\images\\Tshepo.jpg",
        "name": "Tshepo Serumula",
        "role": "Data Scientist",
        "bio": "A tech-savvy professional with a strong background in software development. He leads our technical team and ensures innovative solutions are delivered to our clients. He is a skilled beatboxer, creating impressive beats using only his voice.",
        "twitter": "https://twitter.com/@Tshepo",
        "facebook": "https://facebook.com/Tshepo_Serumule",
        "linkedin": "https://linkedin.com/in/Serumule T"
    },
    {
        "image_path": "C:\\Users\\Home-User\\Pictures\\images\\Mkhanyisi.jpg",
        "name": "Mkhanyisi Mlombile",
        "role": "Data Scientist",
        "bio": "Mkhanyisi's passion for data science goes beyond his professional work. In his free time, he enjoys participating in Kaggle competitions, where he applies his skills to real-world datasets and collaborates with other data scientists worldwide. He is also an avid reader of data science literature and actively contributes to the data science community by sharing his knowledge. The same dedication he puts in when preparing his mouth watering dishes. A professional chef too.",
        "twitter": "https://twitter.com/@Mkhanyisi27",
        "facebook": "https://facebook.com/Mkhanyisi_Mlombile",
        "linkedin": "https://linkedin.com/in/Mlombile Mkhanyisi"

    },
    {
        "image_path": "C:\\Users\\Home-User\\Pictures\\images\\Ghaalib.jpg",
        "name": "Ghaalib Van Der Ross",
        "role": "Data Scientist",
        "bio": " an accomplished data scientist with a passion for extracting insights from complex datasets. With a strong background in statistics, mathematics, and programming, he leverages his expertise to tackle challenging analytical problems. Our award winnng author who has won  over 20 writing competitions around the world.",
        "twitter": "https://twitter.com/@Ghalibe__",
        "facebook": "https://facebook.com/Ghaalib_Van Der Ross",
        "linkedin": "https://linkedin.com/in/Ghaalib_Van Der Ross"
        
    },
    {
        "image_path": "C:\\Users\\Home-User\\Pictures\\images\\Katlego.jpg",
        "name": "Katlego Mthunzi",
        "role": "Business Analyst",
        "bio": "A results-oriented marketing specialist with a strong background in digital marketing strategies. He excels in crafting effective marketing campaigns, leveraging her analytical skills to drive customer engagement and increase brand activity. A former professional athlete, whom is coach during weekends.",
        "twitter": "https://twitter.com/@Katlego_Mthunzi",
        "facebook": "https://facebook.com/Katlego_Mthunzi",
        "linkedin": "https://linkedin.com/in/Katlego_Mthunzi"
        
    },
    {
        "image_path": "C:\\Users\\Home-User\\Pictures\\images\\Edna.jpg",
        "name": "Edna Kobo",
        "role": "Coordinator",
        "bio": "A talented and innovative designer who brings a creative flair to our team. With a keen eye for aesthetics and a deep understanding of user-centered design principles, she consistently delivers visually appealing and user-friendly designs. In her spare time she performs her magic through kids as a yoga instructor.",
        "twitter": "https://twitter.com/@Edna_Kobo_",
        "facebook": "https://facebook.com/Edna_Kobo",
        "linkedin": "https://linkedin.com/in/EdnaKobo"
        
    },
    {
        "image_path": "C:\\Users\\Home-User\\Pictures\\images\\Koketso.jpg",
        "name": "Koketso Makofane",
        "role": "Feature Engineer",
        "bio": "With a solid foundation in statistics, mathematics, and programming, koketso utilizes her expertise to analyze data and develop innovative feature engineering strategies.",
        "twitter": "https://twitter.com/@Koketso_makofane",
        "facebook": "https://facebook.com/koketso_makofane",
        "linkedin": "https://linkedin.com/in/koketso_makofane"
    },
]
social_icons = {
    "twitter": "fab fa-twitter",
    "facebook": "fab fa-facebook",
    "linkedin": "fab fa-linkedin"
}
col1, col2 = st.columns(2)

# Render team members in the left column
with col1:
    for member in team_members[:len(team_members)//2]:
        with st.container():
            st.image(member['image_path'],use_column_width=True)
            st.markdown(f"# {member['name']}")
            st.write(f"**Role:** {member['role']}")
            st.write(f"**Bio:** {member['bio']}")
            with st.container():
                for social in ["twitter", "facebook", "linkedin"]:
                    icon = social_icons.get(social, "fas fa-link")
                    st.markdown(
                        f'<a href="{member[social]}" target="_blank"><i class="{icon}"></i></a>',
                        unsafe_allow_html=True
                    )        
        st.write("---")  # Add a separator between team members
        
with col2:
    for member in team_members[len(team_members)//2:]:
        with st.container():
            st.image(member['image_path'], use_column_width=True)
            st.markdown(f"# {member['name']}")
            st.write(f"**Role:** {member['role']}")
            st.write(f"**Bio:** {member['bio']}")
            with st.container():
                for social in ["twitter", "facebook", "linkedin"]:
                    icon = social_icons.get(social, "fas fa-link")
                    st.markdown(
                        f'<a href="{member[social]}" target="_blank"><i class="{icon}"></i></a>',
                        unsafe_allow_html=True
                    )        
        st.write("---")  # Add a separator between team members
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)        

    
    
    