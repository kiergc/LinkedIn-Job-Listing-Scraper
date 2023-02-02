from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd


k_job_lst = ["data specialist", "data analyst", "data scientist", "machine learning engineer", "artificial intelligence"]
k_loc_lst = ["san francisco bay area", "san francisco", "san jose", "marin", "oakland", "palo alto", "mountain view"]
k_url_lst = []

i_job_lst = ["fullstack", "full stack", "frontend", "software engineer"]
i_loc_lst = ["palo alto", "san jose"]
i_url_lst = []

#function that takes in job list and place list
    #for item in each list
        ##regex to put into right format
    #zip lists together
    #for each item in zipped list, make a url
    #return list of urls

##########
# DRIVER #
##########

# Creating a webdriver instance
#TODO: replace ChromeDriver path
driver = webdriver.Chrome("Users/kier/Downloads/chromedriver_mac64/chromedriver")

# Opening the url we have just defined in our browser
#for url in k_url_lst:
 #   driver.get(url)
#for url in i_url_lst:
 #   driver.get(url)

test_url = "https://www.linkedin.com/jobs/search?8keywords=data%20scientist&location=San%20Francisco%20Bay%20Area"
driver.get(test_url)


