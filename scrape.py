import selenium
import time
from selenium import webdriver

browser = webdriver.PhantomJS(r"C:\Users\puneet\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe")
chrome_options = webdriver.ChromeOptions()
input=["enter the page name"]

chrome_options.add_argument('window-size=1920x1080')
browser = webdriver.Chrome(executable_path=r"C:\Users\puneet\Downloads\chromedriver.exe",options=chrome_options)
browser.get("https://twitter.com/"+input)
print( browser.title)
lastHeight = browser.execute_script("return document.body.scrollHeight")
print (lastHeight)
i = 0
while True:
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	newHeight = browser.execute_script("return document.body.scrollHeight")
	print (newHeight)
	if newHeight ==255025:
		break
	lastHeight = newHeight
	i += 1

html=browser.page_source
soup=BeautifulSoup(html,'lxml')
tag=soup.find_all("ol",id="stream-items-id")
tags=tag.find_all("li")
tags
lis=[]
names=[]
for i in tags:
    a=i.find_all("div",class_="stream-item-header")
    for j in a:
        link=j.find_all("strong",class_="fullname show-popup-with-id u-textTruncate ")
        try:
            link=link[0]
            p=(link.text)
            names.append(p)
        except:
            continue
date=[]
for i in tags:
    a=i.find_all("div",class_="stream-item-header")
    for j in a:
        link=j.find_all("small",class_="time")
        try:
            link=link[0]
            link=link.text
            date.append(link.strip())
        except:
            continue
paragraphs=[]
for i in tags:
    a=i.find_all("div",class_="content")
    for j in a:
        link=j.find_all("div",class_="js-tweet-text-container")
        try:
            link=link[0]
            v=link.find_all("p")
            paragraphs.append(v[0].text)
        except:
            continue
comments=[]
for i in tags:
    a=i.find_all("div",class_="content")
    for j in a:
        link=j.find_all("button",class_="ProfileTweet-actionButton js-actionButton js-actionReply")
        link=link[0]
        for k in link:
            try:
                v=k.find_all("span",class_="ProfileTweet-actionCountForPresentation")
                if v !=None:
                    v=v[0]
                    comments.append(v.text)
            except:
                continue
test_df=pd.DataFrame({'date':date,'names':names,'paragraph':paragraphs,'no. of comments':comments})
test_df.to_csv('data.csv')
