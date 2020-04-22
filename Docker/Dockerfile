# Télécharger l'image initial (ubuntu 18.04)
FROM ubuntu:18.04

MAINTAINER Asic ALI  <ali.asic.mougamadou@gmail.com>
 
# Update du répertoire Ubuntu
RUN sudo apt-get update
RUN sudo apt-get -y upgrade
# creat workspace 
RUN mkdir -p /workspace
WORDIR /workspace
COPY . .
# Install Python 3
RUN sudo apt-get install python3
# Install pip3 for python
RUN sudo apt-get -y install python3-pip
# Install vim
RUN sudo apt install vim git
# requirements.txt file installation
RUN sudo pip install -r requirements.txt

RUN pip3 install -r requirement.txt && pip3 install jupyter

# Expose port 8000 
EXPOSE 8000

CMD workspace --port 8000
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
