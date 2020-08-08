from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source,'lxml')

article = soup.find('article')
headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)
summmary = article.find('div',class_='entry-content').p.text
print(summmary) #summary before the video

#to print out the video link
#'iframe' is used to insert a video file in the webpage
# youtube-player is used to view the video from the website directly

vid_src=article.find('iframe',class_='youtube-player')
#print(vid_src)

#to get only the value of the 'src' attribute, the value is taken in a dictionary

vid_src=article.find('iframe',class_='youtube-player')['src']
print("link is:" +vid_src)

vid_id=vid_src.split('/')[4]
vid_id=vid_id.split('?')[0]


print(vid_id)

yt_link= f'https://youtube.com/watch?v={vid_id}'
print(yt_link)