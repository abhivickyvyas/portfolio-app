import streamlit as st
from streamlit_lottie import st_lottie
import json

def experience():
    col1,col2 =st.columns(2)

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
                <h2>Experience</h2>
            </div>
        """, unsafe_allow_html=True)
    path = "data/animations/Animation_exp.json"
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
        col1,col2 = st.columns([3,2])
        col1.markdown(""" 
            ### Software Engineer –– [Nextuple](https://www.linkedin.com/company/nextuple/) (PRESENT)
            - Conducted A/B testing experiments to assess the effectiveness of various
            promotion strategies, resulting in a remarkable 24% increase in revenue.
            - Developed and implemented a machine learning model to predict customer
            churn, reducing churn rate by 20%.
            - Created a recommendation system using collaborative filtering, boosting
            customer engagement by 30%.
            - Designed and developed a dashboard to monitor key metrics and KPIs, enabling
            data-driven decision-making.
                            """)
        col2.markdown("""
            **Tools:**

            - Programming Languages: Python, SQL
            - Machine Learning: Scikit-Learn, TensorFlow, Keras
            - Data Visualization: Matplotlib, Seaborn, Plotly, Retool, Tableau
            - Cloud: Redshift, Sagemaker, S3 Bucket
            - ETL Processes: Custom SQL, Python scripts
            - A/B Testing: Custom Python scripts
            - Other Tools: Git, Colab Notebooks, Retool
            """)
    with st.container():
        col1, col2 = st.columns([3, 2])
        col1.markdown("""
           ### Software Programmer ––  [10Times](https://www.linkedin.com/company/10times-events/) (August 2021-October 2021 )
    
           - **Top Rated freelancer**, representing the top 10% of Upwork talent.
           - Collaborated with 7 clients to understand their company needs and devise data-driven solutions.
           - Successfully completed 6 jobs, each with a 5-star rating and positive feedback.
           - Facilitated end-to-end development, testing, and monitoring of analytical models for 5 clients.
           - Designed and developed a News search tool leveraging LLM and Langchain technologies, enhancing the efficiency of information retrieval and analysis.
           - Efficiently managed Azure Databricks, executed ETL, and developed ML models for small and large datasets (125GB, 1B rows), automated scheduling, tracked experiments, implemented Auto ML, and maintained resource efficiency.
           """)
        col2.markdown(""" 
        **Tools:**
        
        - Programming Languages: Python, R, SQL
        - Machine Learning: Scikit-Learn, TensorFlow, PyTorch, Auto ML
        - Data Visualization: Matplotlib, Seaborn, Plotly
        - Big Data Technologies: Azure Databricks, Spark
        - ETL Processes: Azure Data Factory
        - Generative AI: LLM, Langchain
        - Other Tools: Git, Jupyter Notebooks, streamlit  """)
    
    # st.markdown()