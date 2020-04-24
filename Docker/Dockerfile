# Télécharger l'image initial (ubuntu 18.04)
FROM ubuntu:18.04

MAINTAINER Asic ALI  <ali.asic.mougamadou@gmail.com>
 
# update and install depedencies
RUN apt-get update
RUN apt-get -y install curl
RUN apt-get install -qy python3
RUN apt-get install -qy python3-pip
RUN apt-get install -qy vim
RUN apt-get -y install git
RUN git clone https://github.com/Aliam95/JAVA-IOT_BigDataHadoop.git

WORKDIR /Docker
ADD . /workspace
WORKDIR /workspace

RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install jupyter

EXPOSE 8000

CMD workspace --port 8000
CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root"]

