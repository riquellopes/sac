.SILENT:

up:
	docker-compose stop
	docker-compose up

build:
	docker-compose stop
	docker-compose build

migrate:
	docker-compose stop
	docker-compose run -rm backend python3 manage.py db upgrade

makemigrations:
	docker-compose stop
	docker-compose run -rm backend python3 manage.py db migrate
