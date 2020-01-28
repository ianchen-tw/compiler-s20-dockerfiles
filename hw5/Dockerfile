FROM ubuntu:18.04
MAINTAINER SSLAB

RUN apt-get update && apt-get install -y \
    git autoconf automake autotools-dev curl \
    libmpc-dev libmpfr-dev libgmp-dev libusb-1.0-0-dev gawk \
    build-essential bison flex device-tree-compiler \
    texinfo gperf libtool patchutils bc zlib1g-dev \
    device-tree-compiler pkg-config libexpat-dev
ENV RISCV /risc-v
RUN mkdir -p $RISCV && cd ~ && \
    git clone -b rvv-0.7.x --recursive https://github.com/riscv/riscv-gnu-toolchain && \
    cd riscv-gnu-toolchain && ./configure --prefix=$RISCV && \
    make -j8 && make clean
ENV PATH="/risc-v/bin:${PATH}"
RUN cd ~ && git clone https://github.com/riscv/riscv-pk.git && \
    cd riscv-pk && mkdir build && cd build && \
    ../configure --prefix=$RISCV --host=riscv64-unknown-elf && \
    make -j8 && make install -j8 && make clean
RUN cd ~ && git clone https://github.com/riscv/riscv-isa-sim.git && \
    cd riscv-isa-sim && mkdir build && cd build && \
    ../configure --prefix=$RISCV && make -j8 && make install -j8 && make clean
RUN cd ~ && rm -rf riscv-gnu-toolchain/ && rm -rf riscv-isa-sim/ && rm -rf riscv-pk/
