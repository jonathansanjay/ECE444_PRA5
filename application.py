from flask import Flask, request, jsonify
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

application = Flask(__name__)

# Load the model and vectorizer
def load_model():
    with open('basic_classifier.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('count_vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

# Load model and vectorizer once when the application starts
model, vectorizer = load_model()

# Route to check if the service is working
@application.route('/')
def home():
    return "Fake News Detection API is running!"

# Route for Fake News Detection
@application.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON data from request
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    # Vectorize the input text
    text_vector = vectorizer.transform([text])
    
    # Predict using the loaded model
    prediction = model.predict(text_vector)[0]
    
    # Return 1 for fake news and 0 for real snews
    result = {'prediction': 'FAKE' if prediction == 1 else 'REAL'}
    return jsonify(result)

if __name__ == '__main__':
    application.run(debug=True)