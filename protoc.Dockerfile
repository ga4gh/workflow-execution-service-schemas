FROM debian:8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get clean && \
    apt-get update && \
    apt-get -yq --no-install-recommends -o Acquire::Retries=6 install \
    curl unzip ca-certificates git && \
    apt-get clean

ENV PROTOC_VER=3.2.0rc2

RUN cd /usr/local && \
    curl -OL https://github.com/google/protobuf/releases/download/v${PROTOC_VER}/protoc-${PROTOC_VER}-linux-x86_64.zip && \
    unzip protoc-${PROTOC_VER}-linux-x86_64.zip && \
    chmod o+r -R include/google && \
    chmod o+x $(find include/google -type d) && \
    rm protoc-${PROTOC_VER}-linux-x86_64.zip

ENV GOVERSION=1.7.5

# Install golang binary
RUN cd /usr/local && \
    curl -O http://storage.googleapis.com/golang/go${GOVERSION}.linux-amd64.tar.gz && \
    tar -xzf go${GOVERSION}.linux-amd64.tar.gz && \
    rm go${GOVERSION}.linux-amd64.tar.gz

ENV PATH ${PATH}:/usr/local/go/bin
ENV GOPATH=/usr/local

RUN go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
RUN go get -u github.com/golang/protobuf/protoc-gen-go
