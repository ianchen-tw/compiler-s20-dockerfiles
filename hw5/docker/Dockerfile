FROM ubuntu:18.04 AS riscv-builder

ENV RISCV /risc-v

RUN apt-get update

RUN apt-get install -y \
    git autoconf automake autotools-dev curl \
    libmpc-dev libmpfr-dev libgmp-dev libusb-1.0-0-dev gawk \
    build-essential  device-tree-compiler bison flex \
    texinfo gperf libtool patchutils bc zlib1g-dev \
    device-tree-compiler pkg-config libexpat-dev

RUN mkdir -p $RISCV && cd ~ && \
    git clone -b rvv-0.7.x --recursive https://github.com/riscv/riscv-gnu-toolchain && \
    cd riscv-gnu-toolchain && ./configure --prefix=$RISCV && \
    make -j "$(nproc)" && make clean

ENV PATH="/risc-v/bin:${PATH}"

RUN cd ~ && git clone https://github.com/riscv/riscv-pk.git && \
    cd riscv-pk && mkdir build && cd build && \
    ../configure --prefix=$RISCV --host=riscv64-unknown-elf && \
    make -j "$(nproc)" && make install -j "$(nproc)" && make clean

RUN cd ~ && git clone https://github.com/riscv/riscv-isa-sim.git && \
    cd riscv-isa-sim && mkdir build && cd build && \
    ../configure --prefix=$RISCV && make -j "$(nproc)" && make install -j "$(nproc)" && make clean

# RUN cd ~ && rm -rf riscv-gnu-toolchain/ && rm -rf riscv-isa-sim/ && rm -rf riscv-pk/

# final image
FROM ubuntu:18.04

ENV RISCV_BIN /risc-v/bin/
COPY --from=riscv-builder $RISCV_BIN/riscv64-unknown-elf-gcc $RISCV_BIN/spike $RISCV_BIN


ENV PATH="/risc-v/bin:${PATH}"

RUN apt-get update && apt-get install -y \
    gosu \
    bison flex

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

CMD ["/bin/bash"]
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
