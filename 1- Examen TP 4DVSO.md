### Examen Technique de MLOps sur les Critiques de Films - 4DVSO - Integration Continue - M1

#### Objectif de l'Examen
Cet examen vise à évaluer vos compétences en MLOps en vous faisant travailler sur un projet de classification des critiques de films. Vous utiliserez GitLab pour l'automatisation CI/CD et Docker pour la conteneurisation.

#### Contexte
Vous êtes un Data Scientist dans une entreprise de streaming vidéo en ligne. On vous demande de mettre en place un système pour classer automatiquement les critiques de films en deux catégories : positives (1) et négatives (0), en utilisant les pratiques MLOps.

#### Instructions
Vous disposerez de 2 heures pour compléter cet examen qui se divise en cinq parties principales.

#### Partie 1 : Préparation du Dataset
1. Téléchargez le fichier `reviews_unique.csv` contenant les critiques de films et leurs labels associés.
2. Explorez rapidement le dataset pour comprendre sa structure et effectuez un prétraitement simple si nécessaire (par exemple, suppression des doublons).

#### Partie 2 : Entraînement d'un Modèle de Machine Learning
1. Utilisez Python pour développer un script (`train_model.py`) qui entraîne un modèle de classification (par exemple, Logistic Regression) sur le dataset.
2. Votre script doit inclure une phase de validation pour évaluer la performance du modèle (par exemple, précision, rappel).
3. Sauvegardez le modèle entraîné pour une utilisation ultérieure.

#### Partie 3 : Conteneurisation avec Docker
1. Créez une API Flask simple avec un endpoint `/predict` qui prend une critique de film en entrée et retourne la prédiction du modèle (positif/négatif).
2. Conteneurisez votre application Flask et le modèle entraîné en utilisant Docker. Fournissez le `Dockerfile` correspondant.

#### Partie 4 : Automatisation CI/CD avec GitLab
1. Configurez un pipeline CI/CD dans GitLab à l'aide d'un fichier `.gitlab-ci.yml`. Le pipeline doit effectuer les tâches suivantes :
   - Construction de l'image Docker de votre application Flask.
   - Exécution de tests unitaires simples pour vérifier la fonctionnalité de l'API.
   - (Optionnel) Déploiement de l'image Docker sur un registre d'images Docker.

#### Partie 5 : Gestion des Données avec DVC
1. **Initialisation de DVC :**
   - Dans votre projet, initialisez DVC pour commencer à suivre les versions de vos données.
   - Installez DVC sur votre système si ce n'est pas déjà fait, en utilisant pip ou un autre packages manager.

2. **Configuration du Stockage Distant :**
   - Configurez un stockage distant avec DVC. Vous pouvez utiliser un service cloud comme Azure Storage Account, AWS S3, Google Cloud Storage...
   - Assurez-vous que les identifiants d'accès et les permissions nécessaires sont correctement configurés pour permettre à DVC de pousser et de tirer les données.

3. **Versionnement du Dataset :**
   - Utilisez DVC pour ajouter le fichier `reviews_unique.csv` au suivi. Cela permettra de versionner le dataset et de faciliter son partage et sa récupération.
   - Exécutez les commandes DVC nécessaires pour pousser les données vers le stockage distant configuré.

4. **Intégration de DVC dans le Pipeline CI/CD :**
   - Modifiez votre fichier `.gitlab-ci.yml` pour inclure des étapes qui utilisent DVC pour récupérer la version la plus récente du dataset avant l'entraînement du modèle.
   - Assurez-vous que les variables d'environnement nécessaires pour l'accès au stockage distant sont correctement configurées dans les paramètres CI/CD de GitLab.

#### Critères d'Évaluation
- Documentation, qualité et clarté du code Python pour l'entraînement du modèle.
- Efficacité et précision du modèle de classification.
- Complétude et fonctionnalité du `Dockerfile`.
- Configuration correcte et fonctionnement du pipeline CI/CD dans `.gitlab-ci.yml`.
- Documentation du code yaml pour construire la CI.

#### Livrables
- Votre repos git avec l'ensemble de vos fichiers de code source.




Bonne chance !
