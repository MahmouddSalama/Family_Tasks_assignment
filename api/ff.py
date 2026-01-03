from flask import Flask, request, jsonify
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder
import numpy as np
import pandas as pd
import joblib


encoder=joblib.load('api\encoder')
encoder2=joblib.load('api\encoder2')
knn=joblib.load('api\knn')
mlb=joblib.load('api\mlb')

def assign_task_knn(fid,task_name, task_skills, task_availability, task_preference,members):
    members = members[members['Family_ID'] == fid]

    mlb = MultiLabelBinarizer()
    skills_encoded = mlb.fit_transform(members["Skills"])

    encoder = OneHotEncoder(sparse=False)
    encoder2 = OneHotEncoder(sparse=False)
    availability_encoded = encoder.fit_transform(members[["Availability"]])
    preference_encoded = encoder2.fit_transform(members[["Task_Preference"]])

    X = np.hstack([skills_encoded, availability_encoded, preference_encoded])

    knn = NearestNeighbors(n_neighbors=1, metric="euclidean")
    knn.fit(X)
    
    task_skills_encoded = mlb.transform([task_skills])[0]
    task_availability_encoded = encoder.transform([[task_availability]])[0]
    task_preference_encoded = encoder2.transform([[task_preference]])[0]
    
    task_vector = np.hstack([task_skills_encoded, task_availability_encoded, task_preference_encoded])
    
    distance, index = knn.kneighbors([task_vector])
    best_match = members.iloc[index[0][0]]["Member_ID"]
    member_info = members[members['Member_ID']==best_match][['Member_ID','Age','Skills','Availability']].iloc[0].to_dict()

    return {"Task Name": task_name, "Assigned To": member_info}


print(assign_task_knn("F1",'Wash the dishes',["Cleaning"],'Evenings','Indoor',pd.read_csv('api\member.csv')))