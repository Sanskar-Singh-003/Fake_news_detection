# Fake_news_detection
Sure! Here's the copy-paste-friendly version of your `README.md`:

---

```markdown
# 📰 Fake News Detection Web App

This is a Flask-based web application that predicts whether a given news article is **Fake** or **Real** using a pre-trained machine learning model (`XGBoost`) and a TF-IDF vectorizer.

## 🚀 Features

- Input news text and receive instant prediction: **FAKE** or **REAL**
- Pre-trained TF-IDF vectorizer and XGBoost model
- Simple and intuitive web interface using Flask

## 📂 Project Structure

```

├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── tfidf\_vectorizer.pkl      # TF-IDF vectorizer used for text processing
├── xgb\_fake\_news\_model.pkl   # Trained XGBoost model for classification
├── templates/
│   └── index.html            # HTML template for UI (not included here)

````

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd <your-project-folder>
````

2. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
python app.py
```

Then open your browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 📦 Model Info

* `tfidf_vectorizer.pkl`: Used to convert text into numeric features.
* `xgb_fake_news_model.pkl`: Trained XGBoost classifier model.
* Output classes:

  * `0` → FAKE
  * `1` → REAL

## 🧪 Example

Input:

```
The Prime Minister announces a new economic reform.
```

Output:

```
This news is: REAL
```

## 📋 Requirements

All dependencies are listed in `requirements.txt`:

* Flask
* scikit-learn
* xgboost
* joblib
* nltk

Install them with:

```bash
pip install -r requirements.txt
```

## 📝 License

This project is intended for educational and demonstration purposes.

## 🙋 Support

Feel free to open an issue if you have any questions or suggestions!
