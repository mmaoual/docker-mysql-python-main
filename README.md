# PROJET 3 : Mysql Python

# Contexte

L’objectif de ce projet est de choisir, mettre en place, et peupler une base de données à partir d’un jeu de données de l’open data, et d’implémenter une API permettant de requêter cette base de données.

# Installation et lancement

cd backend

docker image build . -t mmaoual/top250_api:latest -f ./Dockerfile

docker push mmaoual/top250_api:latest

cd ../mysql

docker image build . -t mmaoual/top250_db:latest -f ./Dockerfile

docker push mmaoual/top250_db:latest

docker-compose up