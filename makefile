SHELL := cmd

banner:
	@echo "  ██████████   █████████  ███████████ ██████   ██████"
	@echo " ░░███░░░░░█  ███░░░░░███░░███░░░░░░█░░██████ ██████ "
	@echo "  ░███  █ ░  ███     ░░░  ░███   █ ░  ░███░█████░███ "
	@echo "  ░██████   ░███          ░███████    ░███░░███ ░███ "
	@echo "  ░███░░█   ░███          ░███░░░█    ░███ ░░░  ░███ "
	@echo "  ░███ ░   █░░███     ███ ░███  ░     ░███      ░███ "
	@echo " ██████████ ░░█████████  █████       █████     ██████"
	@echo "░░░░░░░░░░   ░░░░░░░░░  ░░░░░       ░░░░░     ░░░░░  "

create:
	python -m venv .venv

run:
	@call .venv\Scripts\activate && echo Entorno activado

install:
	.venv\Scripts\pip install -r requirements.txt

typecheck:
	.venv\Scripts\mypy main.py
	.venv\Scripts\mypy processing/

test:
	.venv\Scripts\python -m unittest discover -s tests

build: banner create install test typecheck run
