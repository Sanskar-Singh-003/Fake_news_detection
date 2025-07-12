from flask import Flask, render_template, request
import joblib  # Use joblib for loading

app = Flask(__name__)

# Load the TF-IDF vectorizer saved by joblib
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Load the model saved by joblib
model = joblib.load('xgb_fake_news_model.pkl')

# Map numeric model output to readable labels
label_map = {0: 'Fake', 1: 'Real'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    news_text = request.form['news']

    # Vectorize the input text
    vect_text = vectorizer.transform([news_text])

    # Predict the label
    prediction = model.predict(vect_text)[0]

    # Convert prediction to label
    label = label_map.get(int(prediction), "Unknown")

    return render_template('index.html', prediction=f'This news is: {label.upper()}')

if __name__ == '__main__':
    app.run(debug=True)
