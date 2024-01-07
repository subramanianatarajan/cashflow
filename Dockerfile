FROM ubuntu:latest
LABEL authors="nsubramanian-mac"

ENTRYPOINT ["top", "-b"]