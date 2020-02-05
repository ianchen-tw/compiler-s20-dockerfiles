FROM ubuntu:18.04

# TODO: add pip into dependency

# Combine all three RUNs into 1 in deloyment
RUN apt-get update
RUN apt-get --no-install-recommends install -y \
    gosu \
    python3 python3-pip python3-setuptools python3-wheel\
    gcc flex bison
    # && rm -rf /var/lib/apt/lists/*
# RUN rm -rf /var/lib/apt/lists/*


# will be installed at /usr/local/lib/python3.6/dist-packages
RUN pip3 install colorama

# optional packages

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

CMD ["/bin/bash"]
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
