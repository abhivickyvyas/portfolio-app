import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import requests
import json
from reume_page import resume
from experience_page import experience
from project_page import projects
from contact_form import contact
from about import aboutMe
from utils import get_base64_image  # Import from utils

# Page setup
PAGE_TITLE = "Abhishek Vyas"
PAGE_ICON = "📋"
LAYOUT = "wide"

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
)

# Variables for dynamic content
FULL_NAME = "Abhishek Vyas"
PROFILE_IMAGE = "abhishek_vyas_pic.jpeg"

# Navigation tabs configuration
NAV_TABS = [
    {"label": "About me", "icon": "person-fill", "function": lambda: aboutMe()},
    {"label": "Resume", "icon": "file-text", "function": lambda: resume()},
    {"label": "Experience", "icon": "briefcase", "function": lambda: experience()},
    {"label": "Projects", "icon": "folder", "function": lambda: projects()},
    {"label": "Contact", "icon": "envelope", "function": lambda: contact()},
]

SIDEBAR_TITLE = "Abhishek Vyas"

LOGO_HTML_TEMPLATE = """
    <style>
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }}
    .logo {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
"""

# Get the base64 string of the image
logo_base64 = get_base64_image(PROFILE_IMAGE)

# Logo styling
logo_html = LOGO_HTML_TEMPLATE.format(logo_base64=logo_base64)

# Display logo in the sidebar
st.sidebar.markdown(logo_html, unsafe_allow_html=True)
with st.sidebar:
    nav_tab_op = option_menu(
        menu_title=SIDEBAR_TITLE,
        options=[tab["label"] for tab in NAV_TABS],
        icons=[tab["icon"] for tab in NAV_TABS],
        menu_icon="cast",
        default_index=0,
    )

# Main content of the app
for tab in NAV_TABS:
    if nav_tab_op == tab["label"]:
        tab["function"]()
        break


