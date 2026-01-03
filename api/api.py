from flask import Flask, request, jsonify
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

encoder=joblib.load('api\encoder')
encoder2=joblib.load('api\encoder2')
knn=joblib.load('api\knn')
mlb=joblib.load('api\mlb')


def add_Memper_to_csv( Member_ID,Age,Skills,Availability,Task_Preference,Family_ID):
    file_path = "api\member.csv"  
    df = pd.read_csv(file_path)
    # Member_ID,Age,Skills,Availability,Task_Preference,Family_ID
    new_row1 = {'Member_ID': Member_ID, 
               'Age': Age, 
               'Skills': Skills,
               "Availability":Availability,
               "Task_Preference":Task_Preference,
               "Family_ID":Family_ID
               }  
    new_row = pd.DataFrame([new_row1])
    df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(file_path, index=False)


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
    member_info = members[members['Member_ID']==best_match][['Family_ID','Member_ID','Age','Skills','Availability']].iloc[0].to_dict()

    return {"Task Name": task_name, "Assigned To": member_info}


@app.route('/assign_task', methods=['POST'])
def assign_task():
    data=request.form
    fid=data.get('Family_ID')
    task_name=data.get('task_name')
    task_skills=data.get('task_skills')
    task_availability=data.get('task_availability')
    task_preference=data.get('task_preference')
    
    res=assign_task_knn( fid, task_name,task_skills,task_availability,task_preference,pd.read_csv('api\member.csv'))
    
    return jsonify({
        "outcome": res,
    })
    
@app.route('/add_member', methods=['POST'])
def add_mem():
    try:
        data=request.form
        Member_ID=data.get("Member_ID")
        Age=data.get("Age")
        Skills=data.get("Skills")
        Availability=data.get("Availability")
        Task_Preference=data.get("Task_Preference")
        Family_ID=data.get("Family_ID")
        add_Memper_to_csv( Member_ID,Age,Skills,Availability,Task_Preference,Family_ID)
          
        return jsonify({
            "outcome": 'Done',
        })
    except Exception as e:
         
        return jsonify({
            "outcome": e,
        })
        
        
        
if __name__ == '__main__':
    app.run(debug=True)