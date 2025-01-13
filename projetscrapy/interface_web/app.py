import os
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connexion à la base MySQL (les paramètres viennent de docker-compose)
def get_db_connection():
    return mysql.connector.connect(
        host="mysql",  # Nom du service MySQL dans docker-compose.yml
        user=os.environ.get("DB_USER", "myuser"),
        password=os.environ.get("DB_PASSWORD", "password"),
        database=os.environ.get("DB_NAME", "phonedb")
    )

@app.route('/')
def comparateur():
    # Connexion à la base
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Récupérer les produits des deux tables
    cursor.execute("SELECT nom, prix,lien, categorie, stockage FROM phones_ldlc WHERE categorie!= 'Autre' ")
    produits_site_1 = cursor.fetchall()
    
    cursor.execute("SELECT nom, prix,lien, categorie, stockage FROM phones_mobileshop")
    produits_site_2 = cursor.fetchall()
    
    conn.close()

    # Comparer les prix entre les deux tables
    comparaisons = {}
    for produit_1 in produits_site_1:
        for produit_2 in produits_site_2:
            if produit_1['categorie'] == produit_2['categorie'] and produit_1['stockage'] == produit_2['stockage']:
                key = (produit_1['categorie'], produit_1['stockage'])
                if key not in comparaisons:
                    comparaisons[key] = []
                comparaisons[key].append({
                    'produit_1_nom': produit_1['nom'],
                    'produit_1_prix': produit_1['prix'],
                    'produit_1_url': produit_1['lien'],
                    'produit_2_nom': produit_2['nom'],
                    'produit_2_prix': produit_2['prix'],
                    'produit_2_url': produit_2['lien'],
                    'moins_cher': 'site_1' if produit_1['prix'] < produit_2['prix'] else 'site_2'
                })

    # Passer les données au template
    return render_template('index.html', comparaisons=comparaisons)

if __name__ == '__main__':
    app.run(debug=True)

