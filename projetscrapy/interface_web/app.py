import os
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="mysql", 
        user=os.environ.get("DB_USER", "myuser"),
        password=os.environ.get("DB_PASSWORD", "password"),
        database=os.environ.get("DB_NAME", "phonedb")
    )

@app.route('/')
def comparateur():
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT nom, prix, lien, categorie, stockage FROM phones_ldlc WHERE categorie != 'Autre'")
    produits_site_1 = cursor.fetchall()
    
    cursor.execute("SELECT nom, prix, lien, categorie, stockage FROM phones_mobileshop")
    produits_site_2 = cursor.fetchall()
    
    conn.close()

    
    produits_par_categorie = {}
    
  
    for produit in produits_site_1:
        key = (produit['categorie'], produit['stockage'])
        if key not in produits_par_categorie:
            produits_par_categorie[key] = []
        produit['site'] = 'LDLC' 
        produits_par_categorie[key].append(produit)
    
    for produit in produits_site_2:
        key = (produit['categorie'], produit['stockage'])
        if key not in produits_par_categorie:
            produits_par_categorie[key] = []
        produit['site'] = 'Mobile Shop' 
        produits_par_categorie[key].append(produit)
    
    
    for key, produits in produits_par_categorie.items():
        # Trier produits par prix 
        produits.sort(key=lambda x: x['prix'])
        
        # prix min
        min_price = produits[0]['prix']  

        # Marquer les produits avec le prix minimum
        for produit in produits:
            produit['moins_cher'] = produit['prix'] == min_price

    return render_template('index.html', produits_par_categorie=produits_par_categorie)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
