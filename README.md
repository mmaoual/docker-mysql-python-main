# PROJET 3 : Mysql Python  
  
# Contexte  
  
L’objectif de ce projet est de choisir, mettre en place, et peupler une base de données à partir d’un jeu de données de l’open data, et d’implémenter une API permettant de requêter cette base de données.
  
  
# Choix et création de la base de donées  

On a choisi de gérer le fichier top 250 des transferts des joueurs de football "top250-00-19.csv" dans une base de données relationnelle MySql.  

Une seule table sera créée avec une clé primaire composée des champs "Name", "Team_from" et "Team_to".  

Le déploiement s'effectue via deux containers : un pour l'Api fastApi et l'autre pour la base mySql.  

Un docker-compose est implémenté pour le lancement global de l'API (base + fastApi)  
  
    
# Installation et lancement  
  
liste des instructions à exécuter pour lancer l'api :  
  
cd backend  
docker image build . -t mmaoual/top250_api:latest -f ./Dockerfile  
docker push mmaoual/top250_api:latest  
cd ../mysql  
docker image build . -t mmaoual/top250_db:latest -f ./Dockerfile  
docker push mmaoual/top250_db:latest  
cd ..  
docker-compose up  
  
    
liste des instructions à exécuter pour arrêter l'api :  
  
docker-compose down  
docker volume prune -f  
docker image rm -f mmaoual/top250_api:latest  
docker image rm -f mmaoual/top250_db:latest  
  
Pour tester l'api : http://localhost:8000/docs  