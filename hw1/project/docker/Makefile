all: build
.PHONY: build fake

CONTAINER_USERNAME ?= dummy
CONTAINER_GROUPNAME ?=dummyg
CONTAINER_HOMEDIR ?= /home/dummyg
IMAGE_NAME ?= dummy-image

build: Dockerfile
	docker build \
		--build-arg CONTAINER_USERNAME=${CONTAINER_USERNAME} \
		--build-arg CONTAINER_GROUPNAME=${CONTAINER_GROUPNAME} \
		--build-arg CONTAINER_HOMEDIR=${CONTAINER_HOMEDIR} \
		-t $(IMAGE_NAME) .
fake:
	echo "IMG NAME: ${IMAGE_NAME}"