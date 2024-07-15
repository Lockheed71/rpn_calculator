# Lancer le projet

## Avec docker compose
- Lancer la commande "docker-compose up --build -d", attention a ce que le port 8000 ne soit pas utilisé
	- Le swagger sera accessible a l'adresse http://127.0.0.1:8000/docs ou http://localhost:8000/docs

## Sans docker
- Executer le fichier setup.sh afin d'installer les dependances nécéssaire
- Lancer la commande "python server.py --host=127.0.0.1 --port=8000"
	- Le swagger sera accessible a l'adresse http://[host]:[port]/docs