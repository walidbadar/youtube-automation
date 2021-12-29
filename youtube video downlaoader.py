#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pytube import YouTube
from datetime import datetime
import os, re, time, requests, json

def youtube_video_downlaoader(topic,linkorder):
    global driver

    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.get('https://youtube.com/')

    # Search Topic
    xpath_searchBar = '//input[@id="search"]'
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_searchBar)))
    uid_input = driver.find_element_by_xpath(xpath_searchBar)
    uid_input.send_keys(topic)  # Bitcoin416
    time.sleep(1)
    uid_input.send_keys(Keys.ENTER)

    # Click on Filter Button
    xpath_searchButton = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/tp-yt-paper-button/yt-icon'
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_searchButton)))
    driver.find_element_by_xpath(xpath_searchButton).click()
    driver.implicitly_wait(1)

    # Use Creative Common Filter
    xpath_filterButton = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[4]/ytd-search-filter-renderer[5]/a/div/yt-formatted-string'
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_filterButton)))
    driver.find_element_by_xpath(xpath_filterButton).click()

    # Search Video Links
    driver.get(driver.current_url)
    searchedlinks = driver.page_source
    #print(searchedlinks)
    linklist = re.findall("href\=\"\/watch\?v=(.*?)\"", searchedlinks, re.M)  # dollar price
    linklist = list(dict.fromkeys(linklist))
    #print(linklist)
    driver.quit()

    # Download Video from Links
    yt = YouTube("https://www.youtube.com/watch?v="+linklist[linkorder]+"\"")
    d_video = yt.streams.get_by_itag(22)
    # d_video.download(filename=str(linkorder)+".mp4")
    d_video.download('video')
    #print('Video Dowloaded!')

while 1:
    try:
        youtube_video_downlaoader("physcology",0)
        time.sleep(1800)

    except:
        print("Some Error")
        time.sleep(300)