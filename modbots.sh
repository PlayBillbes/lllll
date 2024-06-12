#!/bin/bash


echo "ttyd serving at port 80 with username:pass as kali:kali"

nohup python bot.py & ls
chmod +x /usr/local/bin/ttyd_linux
/usr/local/bin/ttyd_linux -p 8080 -c modsbots:modsbots bash 
