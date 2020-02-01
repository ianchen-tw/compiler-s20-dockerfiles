all: build
.PHONY: build run

IMG_NAME = compiler-hw0-env

build: Dockerfile
	docker build -t $(IMG_NAME) .

run:
	docker run --rm -it --hostname compiler-f19  -e LOCAL_USER_ID=`id -u ${USER}` $(IMG_NAME)