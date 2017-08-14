.SILENT:

up:
	docker-compose stop
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up

up-develop:
	docker-compose stop
	docker-compose up

build:
	docker-compose stop
	docker-compose build

upgrade:
	# Similar to manage.py migrate of django
	docker-compose stop
	docker-compose run --rm backend python3 manage.py db upgrade

install:
	# Provisiona toda máquina necessárias.
	docker-compose stop
	docker-compose build
	docker-compose stop
	docker-compose run --rm backend python3 manage.py db upgrade
	docker-compose stop
	docker-compose run --rm frontend npm run build

migrate:
	# Similar to manage.py makemigrations of django
	docker-compose stop
	docker-compose run --rm backend python3 manage.py db migrate

migration-help:
	docker-compose stop
	docker-compose run --rm backend python3 manage.py db --help

olx-backend:
	docker exec -it olx-sac-backend sh

olx-frontend:
	docker exec -it olx-sac-frontend sh

backend-test:
	docker-compose stop
	docker-compose run --rm backend pytest tests/ -s -r a --color=yes -vvv

backend-test-cov:
	docker-compose stop
	docker-compose run --rm backend pytest tests/ --cov=app -s

front-end-test:
	docker-compose stop
	docker-compose run --rm frontend npm test

front-end-build:
	docker-compose stop
	docker-compose run --rm frontend npm run build

shell:
	docker-compose stop
	docker-compose run --rm backend python3 manage.py shell
