from pytube import YouTube
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
from moviepy.editor import *

def plist(pl_name, pl_url):
    urls = []
    path = 'F:\\binod\\' + pl_name

    driver = webdriver.Chrome("F:\\down\\driver_may\\chromedriver.exe")
    driver.get(pl_url)
    time.sleep(5)
    p = driver.page_source
    soup = bs(p,'lxml')

    titles = soup.find_all('a', {'id':"video-title"})
    for title in titles:
        n = title.text.strip()
        l = title['href']
        urls.append(l)

    time.sleep(10)
    driver.close()
    print('Items to be downloaded',len(urls))
    i=0
    for k in range(0,len(urls)):
        try:
            yt = YouTube(urls[k],use_oauth=True, allow_oauth_cache=True)
            yt = yt.streams.get_highest_resolution()
            v_name = yt.default_filename
            p = path + '\\' + v_name
            print('File number:',i,'   ','File size:',yt.filesize_mb,'MB')

            yt.download(path)
            print('downloaded file',k)
            
            video = VideoFileClip(p)
            video.audio.write_audiofile(p.replace('.mp4', '.mp3'))
        except Exception as e:
            print(e)
            print('one video omitted')
            pass

    print('Successfully downloaded playlist',pl_name)

#plist('kumar_sanu', 'https://www.youtube.com/playlist?list=PLJtG4Hz7NMYUJ_8akQaoTAVcetqKIGxcE')

df = pd.read_excel("F:\\binod\\songs.xlsx")
rows = df.shape[0]

for p in range(0,rows):
    plist(df.iat[p,0],df.iat[p,1])