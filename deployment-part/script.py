import mysql.connector
import pandas as pd

# Chargement du fichier CSV
df = pd.read_csv('temperature.csv')

# Connexion à la base de données MySQL
connection = mysql.connector.connect(
     host='mysql',
    port=3306,
    user='user',
    password='password',
    database='dataops'
)
cursor = connection.cursor()

# Création de la table (si elle n'existe pas)
cursor.execute('''
CREATE TABLE IF NOT EXISTS temperature (
    time DATE,
    temperature_2m_max FLOAT
)
''')

# Insertion des données
for _, row in df.iterrows():
    cursor.execute('''
    INSERT INTO temperature (time, temperature_2m_max)
    VALUES (%s, %s)
    ''', (row['time'], row['temperature_2m_max']))

# Sauvegarde et fermeture
connection.commit()
cursor.close()
connection.close()

print("Données chargées avec succès dans MySQL.")
