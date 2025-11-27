IMAGE_NAME = bg_remover

WORK_DIR = $(CURDIR)

all: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p 8080:8080 -it --name $(IMAGE_NAME)_cont $(IMAGE_NAME)

run_dev:
	docker run --entrypoint bash -v $(WORK_DIR):/usr/src -it $(IMAGE_NAME)

test:
	docker run --entrypoint bash -it --name $(IMAGE_NAME)_cont $(IMAGE_NAME)

check:
	docker exec -it $(IMAGE_NAME)_cont sh


clean:
	docker rm -f $(IMAGE_NAME)_cont

empty:
	rm $(CURDIR)/app/output/*.jpg

fclean: clean
	docker image rm -f $(IMAGE_NAME)

.PHONY: build run run_dev