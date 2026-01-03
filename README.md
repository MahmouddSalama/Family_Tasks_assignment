# 🏠 Family Tasks Assignment System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3.2-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent, machine learning-powered system designed to streamline household management by automatically assigning tasks to family members based on their age, unique skills, availability, and personal preferences.

---

## 📖 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
  - [API Endpoints](#api-endpoints)
  - [Machine Learning Models](#machine-learning-models)
- [Configuration](#-configuration)
- [Running Tests](#-running-tests)
- [Visual Documentation](#-visual-documentation)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## ✨ Features
- **🤖 Intelligent Matching**: Uses K-Nearest Neighbors (KNN) to find the most suitable family member for a specific task.
- **📁 Member Management**: Easily add and manage family members with detailed profiles (Age, Skills, Availability).
- **🚀 RESTful API**: Flask-based API for seamless integration with frontend or mobile applications.
- **📊 Data-Driven Insights**: Comprehensive Jupyter notebooks for data analysis, preprocessing, and model evaluation.
- **⚖️ Automated Load Balancing**: Considers member availability and preferences to ensure fair task distribution.

---

## 🛠 Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn (KNN, OneHotEncoder, MultiLabelBinarizer, TfidfVectorizer)
- **Data Processing**: Pandas, Numpy
- **Visualization**: Matplotlib, Seaborn
- **Serialization**: Joblib

---

## 📂 Project Structure
```text
.
├── api/                    # Flask API and pre-trained models
│   ├── api.py              # Main API entry point
│   ├── member.csv          # Family member storage
│   ├── Family_Tasks_Dataset.csv
│   └── (encoders/models)   # joblib saved files (knn, mlb, etc.)
├── data/                   # Raw and processed datasets
├── family tasks/           # Project documentation and screenshots
│   ├── api/                # API usage screenshots
│   └── model/              # Model training and logic screenshots
├── weights/                # Additional model weights and scalers
├── model1.ipynb            # Notebook: Data Preprocessing
├── model2.ipynb            # Notebook: Data Visualization
├── model3.ipynb            # Notebook: Model Training & Evaluation
└── requirements.txt        # Project dependencies
```

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Family_Tasks_assignment.git
   cd Family_Tasks_assignment
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### API Endpoints

Start the Flask server:
```bash
python api/api.py
```

#### 1. Add Member
- **Endpoint**: `POST /add_member`
- **Body**:
  ```json
  {
    "Member_ID": 101,
    "Age": 25,
    "Skills": ["Cooking", "Cleaning"],
    "Availability": "Weekend",
    "Task_Preference": "Indoors",
    "Family_ID": 1
  }
  ```

#### 2. Assign Task
- **Endpoint**: `POST /assign_task`
- **Body**:
  ```json
  {
    "fid": 1,
    "task_name": "Lunch Prep",
    "task_skills": "Cooking",
    "task_availability": "Weekend",
    "task_preference": "Indoors"
  }
  ```

### Machine Learning Models
Explore the Jupyter notebooks to understand the underlying logic:
- `model1.ipynb`: Focuses on data cleaning and feature engineering.
- `model2.ipynb`: Provides visualizations of task distribution and member skills.
- `model3.ipynb`: Details the training of the KNN model and performance metrics.

---

## ⚙️ Configuration
The system is designed to work out-of-the-box with local CSV files and pre-trained models. No environment variables are required for basic operation.
- **Port**: The API runs on `http://127.0.0.1:5000` by default.
- **Data Path**: Data is stored in `api/member.csv` and `data/Family_Tasks_Dataset.csv`.

---

## 🧪 Running Tests
Currently, the project supports manual verification via API clients like Postman or cURL.

1. **Start the API**:
   ```bash
   python api/api.py
   ```
2. **Verify Endpoints**:
   - Send a `POST` request to `http://127.0.0.1:5000/assign_task` with the sample payload in the [Usage](#-usage) section.
   - Check the JSON response for the assigned member details.

---

## 🖼 Visual Documentation

### API Workflow
![API Add Member](file:///media/mahmoud-gado/New%20Volume/mohamed%20AbdelKAreem/Family_Tasks_assignment/family%20tasks/api/add%20memper%20function.png)
*Figure 1: `add_member` function logic.*

![API Task Assignment](file:///media/mahmoud-gado/New%20Volume/mohamed%20AbdelKAreem/Family_Tasks_assignment/family%20tasks/api/assign%20task%20.png)
*Figure 2: Task assignment endpoint in action.*

### Model Pipeline
![Data Preprocessing](file:///media/mahmoud-gado/New%20Volume/mohamed%20AbdelKAreem/Family_Tasks_assignment/family%20tasks/model/data%20preprocessing.png)
*Figure 3: Data cleaning and feature encoding steps.*

---

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---

## 🌟 Acknowledgements
- Thanks to the Scikit-learn community for the robust ML tools.
- Inspiration from modern smart home automation systems.
