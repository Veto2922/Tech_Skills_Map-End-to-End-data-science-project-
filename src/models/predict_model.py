import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

import joblib


preperocessor_path = r'models\preperocessor.pkl'
final_model_path = r'models\final_model.pkl'

DATA_COL = r'models\data_col.pkl'
Classes_NAME = r'models\classes_names.pkl'

LANGUAGES_PATH = r'models\data details\languages.pkl'
DATABASES_PATH = r'models\data details\DATABASES.pkl'
PLATFROMS_PATH = r'models\data details\PLATFROMS.pkl'
WEB_FRAMES_PATH = r'models\data details\WEB_FRAMES.pkl'
VARIED_TACH_PATH = r'models\data details\VARIED_TACH.pkl'
TOOLS_PATH = r'models\data details\TOOLS.pkl'
COLLABTOOLS_PATH = r'models\data details\COLLABTOOLS.pkl'

skills_clusters_path = r'models\data details\skills_clusters.pkl'

#############################################################################################

class PredictPipeline:
    """
    A class for making predictions using a pre-trained machine learning model.

    Attributes:
    - model (object): The pre-trained machine learning model.
    - preprocessor (object): The preprocessor used for feature scaling.
    - col_list (list): List of column names used in the model.
    - class_names (list): List of class names for prediction.

    Methods:
    - prediction(skills_list): Make a prediction based on a list of skills.
    - prediction_prob(skills_list): Get class probabilities based on a list of skills.
    """

    def __init__(self , skill_list: list):
        """
        Initializes the PredictPipeline instance.

        Parameters:
        - final_model_path (str): Path to the pre-trained machine learning model.
        - preprocessor_path (str): Path to the preprocessor used for feature scaling.
        - DATA_COL (str): Path to the list of column names.
        - Classes_NAME (str): Path to the list of class names.
        """
        self.model = joblib.load(final_model_path)
        self.preprocessor = joblib.load(preperocessor_path)
        self.col_list = joblib.load(DATA_COL)
        self.class_names = joblib.load(Classes_NAME)
        self.skills_dict = joblib.load(skills_clusters_path)
        self.skills_list = skill_list

    def prediction(self):
        """
        Make a prediction based on a list of skills.

        Parameters:
        - skills_list (list): List of skills for prediction.

        Returns:
        - str: Predicted class.
        """
        try:
            skills_list = self.skills_list
            col_list = self.col_list
            model = self.model

            pred_df = pd.DataFrame(col_list.isin(skills_list)).T
            pred_df = pred_df.astype(int)
            pred_df.columns = col_list
            pred_df['experanse_years'] = 1

            pred_df_scl = StandardScaler().fit_transform(pred_df.T)
            result = model.predict(pred_df_scl.T)

            return result[0]
        
        except: 
            print('The skills list in not valid' )

    def prediction_prob(self):
        """
        Get class probabilities based on a list of skills.

        Parameters:
        - skills_list (list): List of skills for prediction.

        Returns:
        - pandas.DataFrame: DataFrame with class names and corresponding probabilities.
        """
        try:
            skills_list = self.skills_list
            col_list = self.col_list
            class_names = self.class_names
            model = self.model

            pred_df = pd.DataFrame(col_list.isin(skills_list)).T
            pred_df = pred_df.astype(int)
            pred_df.columns = col_list
            pred_df['experanse_years'] = 0

            pred_df_scl = StandardScaler().fit_transform(pred_df.T)
            probabilities = model.predict_proba(pred_df_scl.T)

            class_prob_dict = dict(zip(class_names, probabilities.flatten()))
            df = pd.DataFrame(list(class_prob_dict.items()), columns=['Class', 'Probability'])
            df_sorted = df.sort_values(by='Probability', ascending=False)

            return df_sorted
        except:
            print('The skills list in not valid')
    
    def find_matching_skill_groups(self ):
        """
        Find matching skill groups based on a list of skills.

        Parameters:
        - skill_list (list): List of skills for comparison.
        - skill_dict (dict): Dictionary of skill groups.

        Returns:
        - list: List of matching skill groups and non-common skills.
        """
        
        skills_list = self.skills_list
        matching_skill_groups = []
        skills_dict = self.skills_dict.to_dict()

        for group_name, group_skills in skills_dict.items():
            common_skills = set(skills_list) & set(group_skills)
            if len(common_skills) >= 3:
                non_common_skills = list(set(group_skills) - set(common_skills))
                matching_skill_groups.append((group_name, non_common_skills))

        
        # Display matching skill groups and list without common skills
        if matching_skill_groups:
            print("Matching skill groups:")
            for group_name, non_common_skills in matching_skill_groups:
                print(f"Group: {group_name}")
                print(f"Original Skills: {skills_dict[group_name]}")
                print(f"Non-Common Skills: {non_common_skills}")
                print("---")
                return non_common_skills
            else:
                print("No matching skill groups found.")

        
        
        

#############################################################################################################

class DataDetails():
    '''
     Description:
    This module defines the DataDetails class, which is responsible for loading and providing access to various lists of data details stored in pickled files.

    Usage:
    1. Instantiate the DataDetails class.
    2. Access different lists using the provided methods.

    Example:
    ```python
    # Instantiate DataDetails
    data_details = DataDetails()

    # Access classes names list
    classes_names = data_details.get_classes_names()

    # Access languages list
    languages_list = data_details.get_languages_list()

    # Access databases list
    databases_list = data_details.get_databases_list()

    # Access platforms list
    platforms_list = data_details.get_platforms_list()

    # Access web frames list
    web_frames_list = data_details.get_web_fromes_list()

    # Access varied tech list
    varied_tach_list = data_details.get_varied_tach_list()

    # Access tools list
    tools_list = data_details.get_Tools_list()

    # Access collaboration tools list
    collab_tools_list = data_details.get_collab_tools()
    '''
    
    def __init__(self):  
        self.class_names = joblib.load(Classes_NAME)

        self.language = joblib.load(LANGUAGES_PATH)
        self.data_bases = joblib.load(DATABASES_PATH)
        self.platforms = joblib.load(PLATFROMS_PATH)
        self.web_frames = joblib.load(WEB_FRAMES_PATH)
        self.varied_tach = joblib.load(VARIED_TACH_PATH)
        self.Tools = joblib.load(TOOLS_PATH)
        self.collab_tools = joblib.load(COLLABTOOLS_PATH)


    def get_classes_names(self):
        return self.class_names
    
    def get_languages_list(self):
        return self.language
    
    def get_databases_list(self):
        return self.data_bases
    
    def get_platforms_list(self):
        return self.platforms
    
    def get_web_fromes_list(self):
        return self.web_frames
    
    def get_varied_tach_list(self):
        return self.varied_tach
    
    def get_Tools_list(self):
        return self.Tools
    
    def get_collab_tools(self):
        return self.collab_tools