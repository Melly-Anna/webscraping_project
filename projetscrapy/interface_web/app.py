from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connexion MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  
        user="root",
        password="root",
        database="phonedb",
        port=3306
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Requête SQL pour récupérer les produits avec leurs catégories et stockage
    cursor.execute("SELECT nom, prix,lien, categorie, stockage FROM phones_ldlc WHERE categorie != 'Autre' ")
    produits = cursor.fetchall()
    
    conn.close()
    
    # Passer les données récupérées au template
    return render_template('index.html', produits=produits)

if __name__ == '__main__':
    app.run(debug=True)
