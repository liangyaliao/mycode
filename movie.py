#!/usr/bin/env python3

while True:
    Question01 = input("Guess what kind of movie I like most, Adventure, Action, Comedy, Drama, Crime, Fantasy, History, Horror, Musical, Mystery, Romance, Sci-Fi, War  or else?: ")
    answer = str(input())

    if answer == "Action":
        print("Congrats")
    elif answer == "Comedy":
        print("I like Comedy, but not most.")
    elif answer == "Drama":
        print("I don't like Drama")
    elif answer == "Crime":
        print("I do like Crime movies, but not most. Try again!")
    elif answer == "Fantasy":
         print("Maybe when i was little. Try again!")
    elif answer == "History":
         print("I am not sure if the history movies are the true history. Try again!")
    elif answer == "Horror":
         print("Not in my whole life.  Try again!")
    elif answer == "Musical":
         print("Not in my whole life.  Try again!")
    elif answer == "Mystery":
         print("Not in my whole life.  Try again!")
    elif answer == "Romance":
         print("Nope.  Try again!")
    elif answer == "Sci-Fi":
         print("Nope.  Try again!")
    elif answer == "War":
         print("Nope.  Try again!")
    
    else:
        print("Try again!")

    play = input("Play again? (y/n): ")
    if play != "y":
        break

