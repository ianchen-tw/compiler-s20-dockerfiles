all: docker-build
.PHONY: docker-build activate

# Docker args
IMAGE_NAME = compiler-s20-env
CONTAINER_USERNAME = asdf
CONTAINER_GROUPNAME = ee
HOST_NAME=testhost
HOMEDIR = /home/$(CONTAINER_USERNAME)



docker-build:
	${MAKE} \
		IMAGE_NAME=${IMAGE_NAME} \
		CONTAINER_USERNAME=${CONTAINER_USERNAME}\
		CONTAINER_GROUPNAME=${CONTAINER_GROUPNAME}\
		CONTAINER_HOMEDIR=${HOMEDIR}\
		HOMEDIR=${HOMEDIR} \
		-C docker

activate:
	python3 ./activate_docker.py \
		--username ${CONTAINER_USERNAME} \
		--homedir ${HOMEDIR} \
		--imagename ${IMAGE_NAME} \
		--hostname ${HOST_NAME}

