SHELL := /bin/bash #define que se trbajara con bash/linux

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
	python3 -m venv .venv #entorno virtual

run: #activa el entorno virtual
	source .venv/bin/activate && echo "Entorno activado (temporalmente en subshell)"

install: #instala paquetes/dependencas
	.venv/bin/pip install -r requirements.txt

typecheck: #ejecuta main y processing
	mypy main.py
	mypy processing/

test: #ejecuta pruebas unitarias
	python -m unittest discover -s tests

build: banner create run install
