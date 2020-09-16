# Use the official image as a parent image.
FROM python:latest

# Run the command inside your image filesystem.
RUN apt update && apt upgrade && apt install -yqq curl jq sudo

# Installs some python packages we use
RUN pip3 install selenium==4.0.0a6.post2 requests pyyaml

# The following commands will install jekyll and its dependencies.
RUN sudo apt-get install -yqq ruby-full build-essential zlib1g-dev

RUN gem install jekyll bundler jekyll-less therubyracer
