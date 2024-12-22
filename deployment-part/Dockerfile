#Ce fichier définit l'environnement d'exécution de notre application Python dans un conteneur Docker.

# Utilisation de l'image officielle Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installer les dépendances Python (décrites dans requirements.txt)
RUN pip install -r requirements.txt

# Copier tous les fichiers du projet dans le conteneur
COPY . /app/

# Commande pour exécuter le script Python au démarrage du conteneur
CMD ["python", "script.py"]
