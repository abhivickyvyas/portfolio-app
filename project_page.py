import streamlit as st
import json
from streamlit_lottie import st_lottie

def projects():
    col1, col2 = st.columns(2)

    # col1.markdown("## Experience")
    with col1:
        st.markdown("""
                <style>
                .centered {
                    display: flex;
                    align-items: center;
                    height: 100%;
                    margin-top: 200px; /* Adjust this value as needed */
                }
                </style>
                <div class="centered">
                    <h2>Projects </h2>
                </div>
            """, unsafe_allow_html=True)
    path = "Animation_girl.json"
    with open(path, "r") as file:
        url = json.load(file)
    with col2:
        st_lottie(url,
                  reverse=True,
                  height=400,
                  width=400,
                  speed=1,
                  loop=True,
                  quality='high',
                  )

    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            with st.container(border=True):


                # Displaying the title of the project
                st.title("Insightful Data Explorer")

                # Displaying the description
                st.markdown("""
                **Description:**
                The Insightful Data Explorer is a Streamlit-based application designed for comprehensive data analysis and machine learning tasks. Key features include:
        
                - **Data Handling:** Upload, edit, and preprocess CSV or Excel files.
                - **Chat with Data:** Interactive data exploration using Google Gemini-1.5-Flash-Latest.
                - **Visualization:** Custom and automated chart generation.
                - **Feature Engineering:** Transform and create new features, handle missing values and outliers.
                - **AutoML:** Automated model selection, training, and optimization for various machine learning tasks with PyCaret.
                - **Data Profiling:** Detailed data profiling using YData Profiling.
                """)

                # Displaying the tools used
                st.markdown("""
                **Tools Used:**
                
                 **Python** ,
                 **Pandas**,
                **Streamlit** ,
                **Google Gemini**, 
                **PyCaret**, 
                **PygWalker**, 
                **AutoViz**, 
                **YData Profiling**, 
                """)
                st.markdown(""" """)


                c1,c2,c3,c4 = st.columns(4)
                c1.markdown("""**[Link to app](link here)**  """)
                c2.markdown("""**[GitHub]()**""")
                c3.markdown("""**[LinkedIn]()** """)
                c4.markdown("""**[X]()**""")
                rc1,rc2 = st.columns(2)
                rc1.markdown("""**[Streamlit community](https://buff.ly/3WqhYiB)**""")
                rc2.markdown("""**[YouTube]()**""")


        with col2:
                with st.container(border=True):
                    # Displaying the title of the project
                    st.title("Multimodal Biometric and Multi-Attack Protection Using Image Features")

                    st.markdown("""
                    **Description:** Multimodal biometrics is an integration of two or more biometric systems. It overcomes the limitations of other biometrics system like unimodal biometric system. Multimodal biometric for fake identity detection using image features uses three biometric patterns and they are iris, face, and fingerprint. In this system user chooses two biometric patterns as input, which will be fused. Gaussian filter is used to smooth this fused image. Smoothed version of input image and input image is compared using image quality assessment to extract image features. In this system different image quality measures are used for feature extraction. Extracted image features are used by artificial neural network to classify an image as real or fake. Depending on whether image is real or fake appropriate action is taken. Actions could be showing user identification on screen if image is classified as real or raising an alert if image is classified as fake. This system can be used in locker, ATM and other areas where personal identification is required.""")

                    # Displaying the published paper link
                    st.markdown("""
                    **Published Paper:** [Multimodal Biometric and Multi-Attack Protection Using Image Features]()
                    """)
    


        