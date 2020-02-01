#! /usr/bin/env python3

import sys
import subprocess
import pathlib
import os

assert sys.version_info >= (3, 4)
dirpath = os.path.dirname(os.path.abspath(__file__))


DOCKER_USER_NAME = 'student'
DOCKER_HOST_NAME = 'compiler-f19'
DOCKER_IMG_NAME = 'compiler-hw1-env'

dk_home = f'home/{DOCKER_USER_NAME}'


# TODO: add option:
#   --test-src-folder

def main():
    # print(f'dirpath :{dirpath}')
    cwd = os.getcwd()

    docker_options = [
        'docker', 'run',
        '--rm', '-it',
        '--hostname', DOCKER_HOST_NAME,
        '-e', f'LOCAL_USER_ID={os.getuid()}',
        '-v', f'{os.getcwd()}:/home/{DOCKER_USER_NAME}',

        # history file
        '-v', f'{dirpath}/history/docker_bash_history:/{dk_home}/.bash_history',
        DOCKER_IMG_NAME,
    ]
    # print(f'cmd: #{" ".join(docker_options)}#')
    os.system(' '.join(docker_options))


if __name__ == "__main__":
    main()
