include .env

run:
	docker run --env-file ./.env -it app bash