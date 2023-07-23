# Start from the Python 3.11 image
FROM python:3.11

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN google-chrome --version