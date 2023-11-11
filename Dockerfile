FROM ubuntu:20.04

# ENV Settings - for Container
ENV DEBIAN_FRONTEND=noninteractive

# For the situation when the "archieve.ubuntu.com" server downed or too slow to apt-get commands
RUN sed -i 's@archive.ubuntu.com@mirror.kakao.com@g' /etc/apt/sources.list

# DEPRECATED !!
# Only for when the archieve ubuntu is dead
RUN sed -i 's@security.ubuntu.com@mirror.kakao.com@g' /etc/apt/sources.list

# Installing ProgramDeps
RUN apt-get -y update
RUN apt-get install -y python-dev python python3 python3-pip python-pkg-resources python3-pkg-resources libtool software-properties-common nginx

RUN pip3 install uvicorn fastapi gunicorn
