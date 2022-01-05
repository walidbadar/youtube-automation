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

path = "D:/Softwares/Waleed Docs/Projects/Selenium/Youtube Automation/Videos/"

def youtube_video_downloader(topic,linkorder):
    global driver

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.get('https://youtube.com/')

    # Search Topic
    xpath_searchBar = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_searchBar)))
    uid_input = driver.find_element_by_xpath(xpath_searchBar)
    uid_input.send_keys(topic)

    xpath_searchButton = '//*[@id="search-icon-legacy"]'
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_searchButton)))
    searchButton = driver.find_element_by_xpath(xpath_searchButton)
    searchButton.click()

    # Click on Filter Button
    xpath_filterButton = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/tp-yt-paper-button/yt-icon'
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_filterButton)))
    driver.find_element_by_xpath(xpath_filterButton).click()

    # Use Creative Common Filter
    xpath_creativeCommon = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[4]/ytd-search-filter-renderer[5]/a/div/yt-formatted-string'
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_creativeCommon)))
    driver.find_element_by_xpath(xpath_creativeCommon).click()

    # Click on Filter Button
    driver.get(driver.current_url)
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_filterButton)))
    driver.find_element_by_xpath(xpath_filterButton).click()

    # Sort Videos by Upload Date
    xpath_sortButton = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[2]/a/div/yt-formatted-string'
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_sortButton)))
    driver.find_element_by_xpath(xpath_sortButton).click()

    # Search Video Links
    driver.get(driver.current_url)
    searchedlinks = driver.page_source
    # print(searchedlinks)
    linklist = re.findall("href\=\"\/watch\?v=(.*?)\"", searchedlinks, re.M)  # dollar price
    linklist = list(dict.fromkeys(linklist))
    # print(linklist)
    driver.quit()

    # Download Video from Links
    yt = YouTube("https://www.youtube.com/watch?v="+linklist[linkorder]+"\"")
    d_video = yt.streams.get_by_itag(22)
    # d_video.download(filename=str(linkorder)+".mp4")
    d_video.download(path)
    print('Video Dowloaded!')

while 1:
    try:
        for i in range(20):
            youtube_video_downloader("psychology",i)
            time.sleep(1800)

    except:
        print("Some Error")
        time.sleep(300)
