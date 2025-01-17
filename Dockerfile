FROM python:3.9

# Copie tout le contenu du dépôt de l'action dans le conteneur Docker
COPY . /app

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances, si nécessaire
RUN pip install -r requirements.txt

# Commande par défaut (peut être modifiée par l'utilisateur)
CMD ["python", "main.py"]
