from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Charger le modèle entraîné
model = joblib.load('movie_review_classifier.joblib')


@app.route('/predict', methods=['POST'])
def predict():
    # Obtenir la critique de film du corps de la requête
    review = request.json['review']

    # Vectoriser la critique de film
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform([review])

    # Prédire si la critique est positive ou négative
    prediction = model.predict(X)

    # Retourner la prédiction sous forme de JSON
    return jsonify({'prediction': 'positive' if prediction[0] == 1 else 'negative'})


if __name__ == '__main__':
    app.run(debug=True)
