#!/bin/bash

# source: https://denibertovic.com/posts/handling-permissions-with-docker-volumes/

# Add local user
# Either use the LOCAL_USER_ID if passed in at runtime or
# fallback

USER_ID=${LOCAL_USER_ID:-9001}
USER_NAME=student

echo "Starting with UID : $USER_ID"
useradd --shell /bin/bash -u $USER_ID -o -c "" -m ${USER_NAME}
export HOME=/home/${USER_NAME}

cd ${HOME}
exec /usr/sbin/gosu ${USER_NAME} "$@"
