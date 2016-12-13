#!/usr/bin/python
#-*- coding : UTF-8 -*-
#New Game Just For Fun

print "Don't always sit down every day. just walk and look, which record your every day step life.\n"

step_count = input("Please input your step_count: ")

if 0 < step_count <= 1000:
    print "Dear.Your walk is weak, pls strengthen your table_support and push_up after you get home."
    print "1. You are so lazy."
    print "2. Just so so."
    print "3. You are a great man.\n"

    tablet_support = int(raw_input("Please input your tablet_support: "))
    push_up =int(raw_input("Please input your push_up: "))

    if  0 < tablet_support <= 10 and 0 < push_up <= 10:
        print "Training is not enough, you will gain weight."
    elif 10 < tablet_support <="20" and "10" <  push_up <= "20":
        print "Just so so, pls come on."
    else:
        print "You are great today."
        print "1. Reward an apple to you."
        print "2. Your body is not too strong, pls be care for Nutrition.\n"

        weight = input("Please input your weight: ")

        if 60 <= weight <= 65:
            print "You can have an apple tonight."
        else:
            print "You are fatter or thinner, pls balanced diet."

elif 1000 < step_count <= 10000:
    print "Walk is normal, you'd better have dinner."
    print "1. Tall or Digest is good."
    print "2. Do not eat too much.\n"

    height = int(raw_input("Please input your height: "))
    Digest = raw_input("Please input your Digest: ")

    if  170 <= height < 175  and Digest == "good":
        print "You can have a bowl of rice or increase half a bowl of rice."
    elif  height >= 175 or Digest == "good":
        print "You can have two bowl of rice."
    else:
        print "Pay attention dietary, a bowl of rice is enough."

        gender = raw_input("Please input your gender: ")

        if gender == "male":
            print "Control yourself, insist on is vactory."
        else:
            print "Do not forget have dinner."

else:
    print "Well done, you can see a movie or talk with your family."


