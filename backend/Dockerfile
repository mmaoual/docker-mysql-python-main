FROM python:3.9

# Definir un workdir
WORKDIR /code

# deplacer les requirements vers le workdir
ADD requirements.txt /code/requirements.txt

# Instaler les dependances
RUN pip install --trusted-host pypi.python.org -r /code/requirements.txt

# Copier le rep app du projet dans le workdir
ADD app /code/app

# commande pour executer l api
EXPOSE 8000
CMD uvicorn app.main:app --host 0.0.0.0