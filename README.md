# Spotify Songs Recmmender


#### This project was to put my skill of machine learning to create an end to end recommender model from the scratch to the deployment for user's engagement or usage.

## Table Of Content 
- [Tools Used](#tools-used-while-performing-the-analysis)
- [Data Cleaning](#data-cleaning-step-used-in-python-jupyter-notebook)
- [Features to Build Model](#features-in-jupyter-notebook)
- [Features to Build Website](#features-in-pycharm-ce)
- [Conclusion](#conclusion)

## Tools Used While performing the Analysis
- Excel - [Download Dataset Here](https://drive.google.com/file/d/1kXe41SVJ_6XPKp2KI_M_7Q_AfY_JV4aD/view?usp=sharing)
- Python
  - Jupyter notebook : Cleaning the dataset, preprocessing and making vectorization the features column to get the cosine_similarity to predict the recommended songs.
  - IDE : Like PyCharm CE for web devlopment.
  - Libraries : streamlit for making the website.
- Deployment    
  -  Render to create web services application. 

- Storage of dataset
  - AWS : Used it for creating https:// link as the dataset and model generated is large stored it in S3 bucket.


## Data Cleaning Step Used In Python Jupyter notebook
- imported the necessary libraries like numpy, pandas, scikit-learn, pickle, request.
- loaded the csv file from the system.
- performed the cleaning analysis:
  - Removing duplcates.
  - Replacing/Droping the Null/NA values.
  - adjusted the dtypes of date and time columns.
  - droped the unnecessary columns to remove confuctions.
    
## Features in Jupyter notebook
- **Vectorization** : Fit _Transfored the text column's or feature to array vector(0,1) if same feature it will give value 1 or 0 for disimilarity.
- **Checking Simlarity** : Used library scikit-learn to see the cosine_similarity of the vector to predict the model.
- **Pickled the Model** : Used pickle.dump to use the model for deploying the site.

## Features in PyCharm CE
- Created a new project (Spotify-Song-Recommend) and new environment in it to get started.
- Created files 
  - **app.py** the main file where your code of making for site is coded like streamlit for my web-site.
  - **Procfile** to run your code to website.
  - **requirements.txt** mention all the libraries used in the website building.
  - **.gitignore** it is optional if your file or model size is huge you can ignore the file upload in the site, but you can use server options by AWS S3 bucket.
- Git : Used it to synchronize the local files to remote repository Github.

## Conclusion
- This Spotify song recommendation app leverages machine learning to provide personalized music suggestions. By analyzing song features and user search preferences, the app delivers accurate and enjoyable recommendations, enhancing the music discovery experience for users.








  
