FROM mysql:5.7

# datasource
ENV MYSQL_DATABASE top250_db

# ajouter les scripts SQL de creation et de peuplement
ADD database/ /docker-entrypoint-initdb.d/