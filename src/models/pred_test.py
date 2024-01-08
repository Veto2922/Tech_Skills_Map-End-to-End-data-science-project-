from predict_model import PredictPipeline , DataDetails
    

# skills = ['Python' , 'Scikit-Learn' , 'TensorFlow' , 'NumPy' , 'Pandas' , 'Opencv']
# skills = ['R' , 'SQL' , 'RStudio']
skills = ['Python' , 'Pandas' ]



x = PredictPipeline(skills)
# print(x.prediction())
print(x.prediction_prob())
print(x.find_matching_skill_groups())
    

# data = DataDetails()
# print(data.get_classes_names())

# data = DataDetails()
# print(data.get_languages_list())

# data = DataDetails()
# print(data.get_databases_list())

# data = DataDetails()
# print(data.get_platforms_list())

# data = DataDetails()
# print(data.get_web_fromes_list())

# data = DataDetails()
# print(data.get_varied_tach_list())

# data = DataDetails()
# print(data.get_Tools_list())
                                               
# data = DataDetails()
# print(data.get_collab_tools())

   
    