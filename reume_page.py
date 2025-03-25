import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

# Variables for dynamic content
RESUME_FILE_PATH = "data/pdfs/Abhishek_Vyas_Resume.pdf"
DOWNLOAD_BUTTON_LABEL = "Download Resume"
DOWNLOAD_BUTTON_HELP = "Click to download."
DOWNLOAD_BUTTON_STYLE = """
    <style>
    .stDownloadButton button {
        background-color: #1E9E35 !important;
        color: white !important;
    }
    </style>
"""
CONTAINER_STYLE = """
    <style>
    .stContainer > div {
        width: 55%;
        margin: auto;
    }
    </style>
"""

def resume():
    with open(RESUME_FILE_PATH, "rb") as pdf_file:
        document = pdf_file.read()

    # Apply download button styling
    st.markdown(DOWNLOAD_BUTTON_STYLE, unsafe_allow_html=True)

    # Display download button
    st.download_button(
        label=DOWNLOAD_BUTTON_LABEL,
        key="download_button",
        file_name=RESUME_FILE_PATH.split("/")[-1],
        data=document,
        help=DOWNLOAD_BUTTON_HELP,
    )

    # Apply container styling
    with st.container():
        st.markdown(CONTAINER_STYLE, unsafe_allow_html=True)

        # Display PDF viewer
        pdf_viewer(RESUME_FILE_PATH)
