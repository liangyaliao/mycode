#!/bin/bash
# to create user, group; assign the user to the group; exit



echo "Welcome! " | figlet

sleep 2

read -p "Enter the new user name:" NEWUSER

sudo useradd  $NEWUSER

echo "Which group would you like to assign the new user to? "
read GROUPNAME
sudo groupadd -f $GROUPNAME 

sudo usermod -aG $GROUPNAME $NEWUSER
sleep 2

echo "You just created a new user $NEWUSER and assigned it to the group $GROUPNAME!"
sleep 2

echo "Here is the ID for user $NEWUSER:"
sleep 2
id $NEWUSER


