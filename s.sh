#!/bin/sh
#I wrote this little bash script for people.
#It's just for people that don't know how to make an auto login script for SSH.
clear
echo "Welcome, $USER !"
echo "Connecting to SSH server..."
if $(sshpass -p "passwordhere" ssh -o StrictHostKeyChecking=no user@host); then echo "Success!"; else echo "Connection failed. Check your password and login, and/or whether the server is online."; fi
