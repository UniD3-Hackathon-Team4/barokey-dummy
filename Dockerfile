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
RUN apt-get install -y wget curl

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt -y install ./google-chrome-stable_current_amd64.deb
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN mkdir chrome
RUN apt-get install -y unzip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/src/chrome

COPY requirements.txt /etc/requirements.txt
COPY scripts/run.sh /etc/run.sh

RUN pip3 install -r /etc/requirements.txt

CMD /etc/run.sh