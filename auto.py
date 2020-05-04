from selenium import webdriver
from qbittorrent import Client
from selenium.common.exceptions import NoSuchElementException


qb = Client("http://127.0.0.1:8080/")
qb.login("admin", "adminadmin")

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

tor_not_found = []

i = 0
j = 0

Wish_quality = str(input("Do you wish to set quality? Type 'Yes' or 'No': "))

if Wish_quality == "Yes":
	quality = int(input("Enter your required quality in terms of 480, 720 and 1080 DO NOT Write 'p' next to it: "))
if Wish_quality == "No":
	quality = str("")
while n > i:
  torr_name = str(lst[j] + " " + str(quality))
  print("Downloading: " + torr_name)

  browser = webdriver.Chrome(ChromeDriverManager().install())
  browser.get('https://1337x.to/')
  print("Browser Stated")
  torr_input = browser.find_element_by_xpath('//*[@id="autocomplete"]')
  torr_input.send_keys(torr_name)
  print("Torrent Name Entred")

  click_search = browser.find_element_by_xpath('//*[@id="search-form"]/button')

  click_search.click()
  print("Element Searched")
  try:
      first_sel = browser.find_element_by_xpath('/html/body/main/div/div/div/div[3]/div[1]/table/tbody/tr[1]/td[1]/a[2]')
      first_sel.click()
      print("Torrent Found")
  except NoSuchElementException:
      print(torr_name + " Not found")
      tor_not_found.append(torr_name)
      j = j+1
      browser.close()
      continue

  Murl = browser.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[1]/ul[1]/li[1]/a')
  magnet_link = Murl.get_attribute("href")
  print("Magnet link copied")
  browser.close()
  qb.download_from_link(magnet_link)
  print("\n Downloading: " + torr_name )
  i = i+1
  j = j+1

print("Torrent Not found are: \n" + (list(tor_not_found)))
