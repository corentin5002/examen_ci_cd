# Importation des bibliothèques nécessaires
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Chargement du dataset
reviews_dataset = pd.read_csv('reviews_unique.csv')

# Préparation des données
# Supposons que 'text' est la colonne contenant les critiques et 'label' la colonne contenant les labels
reviews_dataset = reviews_dataset.drop_duplicates(subset='critiques')

text = reviews_dataset['critiques']
label = reviews_dataset['labels']

print(f"Nombre de critiques: {len(text)}")

# Encodage des label
le = LabelEncoder()
y = le.fit_transform(label)

# Vectorisation du texte
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialisation du modèle de régression logistique
model = LogisticRegression()

# Entraînement du modèle
model.fit(X_train, y_train)

# Prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluation de la performance du modèle
print(classification_report(y_test, y_pred))
print("AUC-ROC:", roc_auc_score(y_test, y_pred))

# Sauvegarde du modèle entraîné
filename = './movie_review_classifier.joblib'
joblib.dump(model, filename)