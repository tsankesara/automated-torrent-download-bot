from selenium import webdriver
from qbittorrent import Client
from selenium.common.exceptions import NoSuchElementException
import OneThreeThreeSevenX as OTTSx

# creating an empty list 
lst = [] 
  
print("For manuly typing list: Enter 1")
print("For useing download.txt: Enter 2")
print("For useing list from listGen: Enter 3")

enter = int(input())
if enter == 1:
   n = int(input("Enter number of elements : ")) 
   for i in range(0, n): 
     ele = str(input("Torrent Name: "))
     lst.append(ele) # adding the element

if enter == 2:
   f = open('download.txt', "r") 
   #name = f.readline().split()
   lst = list(f)
   print("File Read Complete")
if enter == 3:
   f_name = str(input("Your txt file name(add .txt extention): "))
   f = open(f_name, "r")
   lst = list(f)

n = len(lst)

Wish_quality = str(input("Do you wish to set quality? Type 'Yes' or 'No': "))

if Wish_quality == "Yes":
	quality = int(input("Enter your required quality in terms of 480, 720 and 1080 DO NOT Write 'p' next to it: "))
if Wish_quality == "No":
	quality = str("")

OTTSx.Fmodule(n, lst, quality) #FirstModule is 1337x.to
	

print("Torrent Not found are: \n" + (list(tor_not_found)))
