import streamlit as st
import altair as alt
import pandas as pd

from src.models.predict_model import PredictPipeline, DataDetails

# Sample skills list
model_data = DataDetails()
languages_list = model_data.get_languages_list()
Data_base_list = model_data.get_databases_list()
varied_tech_list = model_data.get_varied_tach_list()
tools_list = model_data.get_Tools_list()
platforms_list = model_data.get_platforms_list()
web_frames_list = model_data.get_web_fromes_list()
collab_tools = model_data.get_collab_tools()


def main():
    # Centered and styled title with emoji
    st.markdown(
        """
        <h1 style='text-align: center; color: blue;'>🚀 Tach Skills MAP App</h1>
        """,
        unsafe_allow_html=True
    )
    st.info('This application helps you find the most suitable job based on your technological skills. Additionally, it suggests skills to develop further in your chosen field.')

    st.sidebar.title('🛠️ Please choose your skills:')
    # Create multiselect boxes for skills
    langouge = st.sidebar.multiselect('Select Languages:', languages_list)
    database = st.sidebar.multiselect('Select Databases:', Data_base_list)
    varied_tech = st.sidebar.multiselect('Select Varied Tech:', varied_tech_list)
    tools = st.sidebar.multiselect('Select Tools:', tools_list)
    platforms = st.sidebar.multiselect('Select Platforms:', platforms_list)
    web_frames_work = st.sidebar.multiselect('Select Web Frameworks Work:', web_frames_list)
    collaboration_tools = st.sidebar.multiselect('Select Collaboration Tools:', collab_tools)

    # Combine selected skills
    selected_skills = langouge + database + varied_tech + tools + platforms + web_frames_work + collaboration_tools
    #################################################################################################################
    # Predict and find matching skills
    model = PredictPipeline(selected_skills)
    pred = model.prediction()
    pred_prob = model.prediction_prob()
    matching_skills = model.find_matching_skill_groups()
    #########################################################################################################
    # Display the selected and matching skills
    st.subheader('Your Skills:')
    st.markdown(' '.join(f'`{item}` ' for item in selected_skills))
    ######################################################################################################################
    # Display prediction information
    st.subheader('🎯 The job proposed for you:')
    st.subheader(f':red[{pred}]')

    ##############################################################
    st.subheader('Probability of all jobs based on your skills ')

    # Create an Altair chart with horizontal bars and gradient color
    chart = alt.Chart(pred_prob).mark_bar().encode(
        y=alt.Y('Class:N', sort='-x'),  # Sort 'Class' by Probability in descending order
        x='Probability:Q',
        color=alt.Color('Probability:Q', scale=alt.Scale(scheme='viridis')),  # Gradient color scale
        tooltip=['Class:N', 'Probability:Q']
    ).properties(
        height=alt.Step(30)   # Adjust the height of the bars as needed
    ).interactive()

    # Display the Altair chart using st.altair_chart
    st.subheader('📊 Probability of Different Jobs:')
    st.altair_chart(chart, use_container_width=True)

    ##############################################################
    st.subheader('🚀 Other skills you might be interested in learning:')
    try:
        st.markdown(' '.join(f' - `{item}` ' for item in matching_skills))
    except:
        st.write('No skills matching ')
    ##############################################################
    st.subheader('🚀 You can discover the skills clusters through the following graph:')
    
    # Load and display the saved HTML file in Streamlit
    html_code = open(r"reports/figures/scatter_plot.html", 'r', encoding='utf-8').read()
    st.components.v1.html(html_code, width=2000, height=1000 , scrolling = True)

    ##############################################################
    # Footer with LinkedIn, GitHub, and Medium links
    st.markdown('---')
    st.subheader('🚀 For more info about this project:')
    st.markdown('[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abdelrahman_Mohamed-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/abdelrahman-mohamed-28649120b/) [![GitHub](https://img.shields.io/badge/GitHub-Veto2922-darkgreen?style=flat&logo=github)](https://github.com/Veto2922/SkillMap-End-to-End-data-science-project) [![Medium](https://img.shields.io/badge/Medium-Abdelrahman_M-ff69b4?style=flat&logo=medium)](https://medium.com/@abdelrahman.m2922/skillsmap-end-to-end-data-science-project)')

    if st.button('🚀 Show Support'):
        st.balloons()

    if st.button('🚀 Star on GitHub'):
        st.write('⭐️ Thank you for your support!')



if __name__ == '__main__':
    main()
