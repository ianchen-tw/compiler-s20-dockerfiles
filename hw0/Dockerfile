from ubuntu:18.04


# Combine all three RUNs into 1 in deloyment
RUN apt-get update

RUN apt-get --no-install-recommends install -y \
    python3 gosu

# RUN rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

CMD ["/bin/bash"]
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
