IMAGE_NAME = bg_remover
HOST_PORT = 8080
CONTAINER_PORT = 8000

all: build run

# Building the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Running the Docker container
run:
	@docker run \
		-p $(HOST_PORT):$(CONTAINER_PORT) \
		-it \
		--name $(IMAGE_NAME)_cont \
		$(IMAGE_NAME)
# Running the Docker container (if stopped)
start:
	docker start -i $(IMAGE_NAME)_cont

# Opening a shell in the container
shell:
	docker exec -it $(IMAGE_NAME)_cont sh

# Deleting the container
clean:
	docker rm -f $(IMAGE_NAME)_cont

# Deleting the container and the image
fclean: clean
	docker image rm -f $(IMAGE_NAME)

.PHONY: build run run_dev shell clean fclean