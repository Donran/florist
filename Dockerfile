# Use the official image as a parent image.
FROM python:latest

# Run the command inside your image filesystem.
RUN apt update && apt upgrade && apt install -yqq curl jq

# Installs nodejs and npm
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt install -yqq nodejs

# Install less globally with npm
RUN npm install -g less

# Installs selenium and requests python packages
RUN pip3 install selenium==4.0.0a6.post2 requests
