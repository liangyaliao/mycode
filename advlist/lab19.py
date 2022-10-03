#!/usr/bin/env python3

def main():
    import random
    wordbank= ["indentation", "spaces"] 
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", 
            "Cedric", "Chris", "Cory", "Ebrima", 
            "Franco", "Greg", "Hoon", "Joey", "Jordan", 
            "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]
    wordbank.append(4)

#PART4
    num=int(input(f"please enter a student number, from 0 to {len(tlgstudents)}: "))-1
#from rando
#PART5
    student_name= tlgstudents[num]

#PART6
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    name=random.choice(tlgstudents)
    print(f"{name}")

main()
