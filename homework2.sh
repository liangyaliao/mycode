#!/bin/bash
# to create user, group; assign the user to the group; exit

echo "Welcome to lillian's application. You can create a new user,assign it to a group(create a group if it doesn't exit). Type exit to exit the application. Please enter the new user's name: "
read NEWUSER
if [ "$USER" == "exit" ]
then
    exit
else
    sudo useradd $NEWUSER
fi


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

