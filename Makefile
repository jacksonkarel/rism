check:
	black selfmodifai --line-length 120
	pytype . --keep-going

rerun:
	docker compose build --no-cache
	docker compose up

