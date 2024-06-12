FROM kalilinux/kali-rolling

#ENV TTY_VER 1.6.1
#ENV USER kali
#ENV PASSWORD kali

RUN apt-get -y update && \
    apt-get install -y curl && \
    apt install -y python3-pip && \
    curl -sLk https://github.com/tsl0922/ttyd/releases/download/1.6.1/ttyd_linux.x86_64 -o ttyd_linux && \
    chmod +x ttyd_linux && \
    cp ttyd_linux /usr/local/bin/

RUN echo 'Installing additional packages...' && \
	export DEBIAN_FRONTEND=noninteractive && \
	apt-get update && \
	apt-get install \
	sudo \
	wget \
  	unzip \
	screen \
	-y --show-progress 
COPY . users
COPY . plugins
COPY requirements.txt /requirements.txt
RUN chmod 744 /requirements.txt
COPY usercount.json /usercount.json
RUN chmod 744 /usercount.json
COPY bot.py /bot.py
RUN chmod 744 /bot.py

RUN pip3 install -r requirements.txt

COPY modsbots.sh /modsbots.sh
RUN chmod 744 /modsbots.sh

CMD ["/bin/bash","/modsbots.sh"]

