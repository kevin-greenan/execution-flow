init:
	pip install --upgrade pip
	pip install -r requirements.txt

build:
	docker build --platform linux/amd64 -t sample:latest .

run:
	docker run --platform linux/amd64 sample:latest
