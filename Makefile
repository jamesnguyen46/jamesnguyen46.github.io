all: clean build

build:
	mkdir -p static
	mkdir -p docs
	python manage.py collectstatic --noinput
	python manage.py distill-local --force

clean:
	rm -rf docs
	rm -rf static