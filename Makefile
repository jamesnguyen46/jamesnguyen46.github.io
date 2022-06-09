ifneq (,$(wildcard dev.env))
include dev.env
export
endif

SHELL := /bin/bash

all: run

# Activate virtual environment. Create new virtual environment in case it is not existed.
active_env:
	. .venv/bin/activate && echo "Has activated the virtual environment!" || (\
		rm -rf .venv; \
		poetry config virtualenvs.in-project true; \
		poetry install --no-root; \
		. .venv/bin/activate; \
	)

# Run local server
run: active_env
	python manage.py migrate
	python manage.py runserver

# Generate static site
gen: active_env clean
	python manage.py migrate
	python manage.py collectstatic --noinput
	python manage.py distill-local --force

# Remove generated folders
clean:
	rm -rf static docs
