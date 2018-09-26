import requests,re
from bs4 import BeautifulSoup
from selenium import webdriver

def chart_parse():
    url = "http://www.mnet.com/chart/TOP100/"
    r = requests.get(url)
    html = r.text

    soup = BeautifulSoup(html,'html.parser')
    Music_item = soup.find("div",{"class" : "MMLTable jQMMLTable"})
    Music_title = Music_item.find_all("a",{"class":"MMLI_Song"})
    Music_artist = Music_item.find_all("div",{"class":"MMLITitle_Info"})

    title = []
    artist = []
    music = {}
    for t in Music_title:
        t = re.sub('<.+?>', '', str(t), 0, re.I|re.S)
        t = t.replace("&amp;","&")
        title.append(t)

    for art in Music_artist:
        a = ""
        art = art.find_all("a",{"class":"MMLIInfo_Artist"})
        for ar in art:
            ar = re.sub('<.+?>', '', str(ar), 0, re.I|re.S)
            ar = ar.replace("&amp;", "&")
            a += ar+", "
        artist.append(a[:-2])

    for i in range(50):
        music[str(title[i])] = artist[i]

    return music

def video_parse(search):
    driver = webdriver.Chrome("/Users/oonja/Downloads/Downloads/chromedriver_win32/chromedriver")

    url = "https://www.youtube.com/results?search_query="
    url += search

    driver.get(url)
    html = driver.page_source
    driver.close()

    soup = BeautifulSoup(html, 'html.parser')
    video_item = soup.find("div", {"id": "contents"}). \
        find_all("a", {"class": "yt-simple-endpoint style-scope ytd-video-renderer"})

    video_list = {}
    for video in video_item:
        video_url = video['href']
        video_title = video['title']
        video_list[str(video_title)] = video_url

    return video_list
