# PROJET 3 : Mysql Python

# Contexte

L’objectif de ce projet est de choisir, mettre en place, et peupler une base de données à partir d’un jeu de données de l’open data, et d’implémenter une API permettant de requêter cette base de données.

# Installation et lancement

liste d'instructions à exécuter pour lancer l'api :
cd backend
docker image build . -t mmaoual/top250_api:latest -f ./Dockerfile
docker push mmaoual/top250_api:latest
cd ../mysql
docker image build . -t mmaoual/top250_db:latest -f ./Dockerfile
docker push mmaoual/top250_db:latest
cd ..
docker-compose up

liste d'instructions à exécuter pour arrêter l'api :
docker-compose down
docker volume prune -f
docker image rm -f mmaoual/top250_api:latest
docker image rm -f mmaoual/top250_db:latest

Pour tester l'api : http://localhost:8000/docs