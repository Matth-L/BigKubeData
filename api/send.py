import mysql.connector
from mysql.connector import Error
import os
import subprocess
from time import sleep
import socket 

mysql_host = "mysql.default.svc.cluster.local"

try:
    print(f"Resolving {mysql_host}...")
    ip = socket.gethostbyname(mysql_host)
    print(f"DNS resolution successful: {mysql_host} → {ip}")
except socket.gaierror as e:
    print(f"DNS resolution failed: {e}")


try:
    # Connexion à la base de données MySQL
    mydb = mysql.connector.connect(
        host=mysql_host,
        user="root",
        password="password",
        database="data",
        port=3306
    )
    
    if mydb.is_connected():
        print("Successfully connected to the database.")

    cursor = mydb.cursor()

    while True:
        sleep(1) 
        print("Waiting...")  

        # Exécution de la requête SELECT *
        cursor.execute("SELECT * FROM student")  
        
        # Récupération des résultats
        results = cursor.fetchall()
        
        print("Query executed successfully.")
        
        # Affichage des résultats
        for row in results:
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection closed.")
