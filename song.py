# -*- coding:utf8 -*-

def list_songs(**songs):
    print(songs)
    print("Type is ", type(songs))

list_songs()

list_songs(adele_songs = ["Hello", "Someone like you"], backstreet_boys_songs = ["Larger than life", "I want it that way"])
