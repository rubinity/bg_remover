IMAGE_NAME = bg_remover
IMAGE_GRAFANA = grafana
HOST_PORT = 8080
CONTAINER_PORT = 8080

all: build run

# Building the Docker compose
build:
	@docker compose -f docker-compose.yml -p bg_remover up --build
# 	docker run -d --name=grafana -p 3000:3000 grafana/grafana

# 	docker build -t $(IMAGE_NAME) .

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

stop: 
	docker compose down

# Opening a shell in the container
shell:
	docker exec -it $(IMAGE_NAME) sh
	

# Deleting the container
clean:
# 	docker rm -f $(IMAGE_NAME)_cont
	docker rm -f bg_remover grafana prometheus

# Deleting the container and the image
fclean: clean
	docker image rm -f $(IMAGE_NAME)

.PHONY: build run run_dev shell clean fclean