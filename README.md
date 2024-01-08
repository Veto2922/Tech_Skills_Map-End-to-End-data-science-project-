# SkillsMap-End-to-End

This project aimed at providing a data-driven solution to enable students to gain insights into the relationships between different functions and their associated technologies.

**Problem Description:**

In the fast-evolving landscape of IT jobs and technologies, students often find themselves bewildered by the multitude of skills associated with different roles. Questions like "Do I need to learn C++ to be a Data Scientist?" or "Can I use JavaScript in Data Analytics?" reflect the confusion that aspiring professionals face.

Our client is an IT educational institute that asked us to create a project aimed at providing a data-driven solution to enable students to gain insights into the relationships between different functions and their associated technologies.

**Business Case:**

To secure investment for this project, we must demonstrate its positive financial impact. The following key performance indicators (KPIs) will serve as metrics for success:

1. **Higher Enrollment Rate:** The project aims to increase the enrollment rate by providing students with a clearer understanding of the skills required for different jobs. A higher certainty in career paths is likely to attract more students to IT programs.

2. **Decrease in Drop-out Rate:** By addressing the students' uncertainties and guiding them toward the most relevant skills for their desired roles, we anticipate a decrease in the dropout rate. A clearer career trajectory will contribute to higher student retention.

3. **Time Saved for Academic Advisors:** The SkillMap project aims to streamline the academic advisory process by providing a comprehensive and easily accessible resource for students. Academic advisors can utilize this tool to efficiently guide students, saving time and resources.

**Data Source:**

The project will leverage the Stack Overflow Developer Survey 2023 dataset, as it provides a rich source of information regarding the skills and technologies associated with various IT jobs. This dataset will serve as the foundation for the data-driven analysis and recommendations provided by SkillMap.
Data link: https://www.kaggle.com/datasets/stackoverflow/stack-overflow-2023-developers-survey?select=survey_results_public.csv

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
