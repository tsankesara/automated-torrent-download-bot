from selenium import webdriver
from qbittorrent import Client
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
def Fmodule(n, lst, quality):
    qb = Client("http://127.0.0.1:8080/")
    qb.login("admin", "adminadmin")
    i = 0
    j = 0
    tor_not_found = []

    while n > i:
     torr_name = str(lst[j] + " " + str(quality))
     print("Downloading: " + torr_name)

     browser = webdriver.Chrome(ChromeDriverManager().install())
     browser.get('https://1337x.to/')
     print("Browser Stated")
     torr_input = browser.find_element_by_xpath('//*[@id="autocomplete"]')
     torr_input.send_keys(torr_name)
     print("Torrent Name Entred")

     try:
         click_search = browser.find_element_by_xpath('//*[@id="search-form"]/button')
     except NoSuchElementException:
     	 click_search = browser.find_element_by_xpath('//*[@id="search-index-form"]/button')
     	 
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
    return tor_not_found 
    
