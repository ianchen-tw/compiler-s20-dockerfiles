all: build
.PHONY: build run

DOCKER_USER_NAME = student
IMG_NAME = compiler-s20-env

build: Dockerfile
	docker build -t $(IMG_NAME) .

compact-build: compact.Dockerfile
	docker build -t $(IMG_NAME):compact -f compact.Dockerfile .

run:
	docker run --rm -it \
				--hostname compiler-f19 \
				-e LOCAL_USER_ID=`id -u ${USER}` \
				-v $(shell pwd)/project:/home/${DOCKER_USER_NAME} \
				$(IMG_NAME)