
````markdown
# 🏠 House Price Prediction – Flask Web App

A **Machine Learning** web application that predicts house prices using **Linear Regression**.  
Users can enter property details like square footage, number of bedrooms/bathrooms, and get **instant predictions**.  

---

## 📊 Project Overview

```mermaid
flowchart LR
A[User Inputs Data in Form] --> B[Flask Backend Receives Data]
B --> C[Model Loads with Joblib]
C --> D[Model Predicts Price]
D --> E[Prediction Sent Back to Frontend]
E --> F[Result Displayed Instantly]
````

---

## 🎯 Features

✅ Predict house prices based on multiple features
✅ Real-time predictions with JavaScript (no page reload)
✅ Clean HTML/CSS interface for easy input
✅ Fully deployable on free platforms like Render/Railway
✅ Simple, lightweight, and beginner-friendly

---

## 🛠 Tech Stack

| **Component**     | **Technology**        |
| ----------------- | --------------------- |
| ML Framework      | Scikit-learn          |
| Backend           | Flask                 |
| Frontend          | HTML, CSS, JavaScript |
| Model Persistence | Joblib                |
| Numerical Ops     | NumPy                 |

---

## 📂 Project Structure

```
📦 house-price-prediction
 ┣ 📂 templates
 ┃ ┗ 📜 form.html      # Frontend form
 ┣ 📜 app.py           # Flask application
 ┣ 📜 model.pkl        # Saved Linear Regression model
 ┣ 📜 requirements.txt # Dependencies
 ┣ 📜 Procfile         # Deployment config
 ┗ 📜 README.md        # Project documentation
```

---


## ⚙️ How It Works

1. User fills out the **HTML form** with property details.
2. JavaScript collects the data and sends it to Flask via **AJAX POST** request.
3. Flask loads the **trained Linear Regression model** from `model.pkl`.
4. Model predicts the price based on the given inputs.
5. Prediction is sent back to the browser and shown instantly.

---

## 📖 What I Learned

* Training and saving ML models using Scikit-learn.
* Serving ML predictions through Flask APIs.
* Building interactive web forms with HTML & JavaScript.
* Using AJAX for real-time communication between frontend & backend.
* Deploying an ML app on free cloud platforms.

