import streamlit as st
import json
from streamlit_lottie import st_lottie

# Variables for dynamic content
ABOUT_ME_TEXT = """
I am a dedicated Data Scientist with over 4.5 years of professional experience in the dynamic fields of 
machine learning and artificial intelligence. I have a proven track record in developing innovative ML models, 
conducting in-depth data analysis, and implementing data-driven solutions that significantly impact business outcomes.

I have successfully led projects across various stages of the data lifecycle, from data collection and cleaning to 
feature engineering, modeling, and validation. I hold a Master's in Electronics (Signal Processing) and a 
Bachelor's in Electronics and Communication Engineering. I am passionate about continuous learning and advancing in the AI field.

Experienced software developer with a passion for Omni-channel fulfillment solutions and Order Management Systems (OMS). 
Skilled in crafting robust REST APIs using Spring Boot and Flask, with a solid foundation in Python for data analysis and insights generation. 
Proficient in creating dynamic dashboards with the ELK stack to visualize and analyze product outcomes. 
A Post-graduate from IIIT Delhi, with hands-on experience in NLP and advanced data analysis projects.
"""
ANIMATION_PATH = "data/animations/Animation_blue_robo.json"

HEADER_TEXT = "<h2 style='text-align: center;'>Hello! I'm Abhishek Vyas 👋</h2>"
GITHUB_MARKDOWN = "**[GitHub](https://github.com/abhivickyvyas)**"
LINKEDIN_MARKDOWN = "**[LinkedIn](https://www.linkedin.com/in/abhishek-vyas-306009128)**"

def aboutMe():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(HEADER_TEXT, unsafe_allow_html=True)
        st.markdown(f"<div class='justify-text'>{ABOUT_ME_TEXT}</div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        c1.markdown(GITHUB_MARKDOWN)
        c2.markdown(LINKEDIN_MARKDOWN)

    with open(ANIMATION_PATH, "r") as file:
        animation_data = json.load(file)
    with col2:
        st_lottie(animation_data,
                  reverse=True,
                  height=400,
                  width=400,
                  speed=1,
                  loop=True,
                  quality='high',
                  )
