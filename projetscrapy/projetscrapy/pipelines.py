# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from itemadapter import ItemAdapter


class MysqlPipeline:
    def open_spider(self, spider):
        """
        Méthode exécutée lorsque le spider démarre.
        Initialise la connexion à la base de données.
        """
        self.connection = mysql.connector.connect(
            host="localhost",  
            user="root",
            password="root",
            database="phonedb",
            port=3306
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        """
        Méthode exécutée lorsque le spider se termine.
        Ferme la connexion à la base de données.
        """
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        """
        Insère chaque item dans la base de données.
        """
        # Prépare et exécute la requête SQL
        self.cursor.execute("""
            INSERT INTO phones_ldlc (nom, prix, lien)
            VALUES (%s, %s, %s)
        """, (
            item.get('nom'),  # Champ Nom récupéré par le spider
            item.get('prix'),  # Champ Prix récupéré par le spider
            item.get('lien')  # Champ Lien récupéré par le spider
        ))

        # Sauvegarde les modifications dans la base
        self.connection.commit()

        # Retourne l'item pour continuer le pipeline
        return item


        
    



    