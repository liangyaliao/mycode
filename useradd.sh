#!/bin/bash
# to create user, group; assign the user to the group; exit

CHOOSE="yes"

echo "Welcome!" | figlet

sleep 1

if [ "$CHOOSE" == "yes" ]
then

    read -p "Enter the new user name:" NEWUSER

    sudo useradd  $NEWUSER


    echo "Which group would you like to assign the new user to? "

    read GROUPNAME

    sudo groupadd -f $GROUPNAME 


    sudo usermod -aG $GROUPNAME $NEWUSER

    sleep 1


    echo "You just created a new user $NEWUSER and assigned it to the group $GROUPNAME!"

    sleep 1


    echo "Here is the ID for user $NEWUSER:"
    sleep 1
    id $NEWUSER


    echo "type yes to continue, press other key to exit:"
    read CHOOSE

else
    exit
fi
