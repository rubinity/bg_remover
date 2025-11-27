IMAGE_NAME = bg_remover

WORK_DIR = $(CURDIR)

all: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p 8080:8080 -it --name $(IMAGE_NAME)_cont $(IMAGE_NAME)

run_dev:
	docker run -p 8080:8080 -v $(WORK_DIR):/usr/src -it $(IMAGE_NAME)

clean:
	docker rm -f $(IMAGE_NAME)_cont

empty:
	rm $(CURDIR)/app/output/*.jpg

fclean: clean
	docker image rm $(IMAGE_NAME)

.PHONY: build run run_dev