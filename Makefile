check:
	black selfmodifai --line-length 120
	pytype setup.py selfmodifai/preprocessing selfmodifai/agents/fine_tunable_agents --keep-going

rerun:
	docker compose build --no-cache
	docker compose up

