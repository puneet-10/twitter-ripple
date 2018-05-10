import selenium
import time
from selenium import webdriver

browser = webdriver.PhantomJS(r"C:\Users\puneet\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe")
chrome_options = webdriver.ChromeOptions()
input=["enter the page name"]

chrome_options.add_argument('window-size=1920x1080')
browser = webdriver.Chrome(executable_path=r"C:\Users\puneet\Downloads\chromedriver.exe",options=chrome_options)
browser.get("https://twitter.com/"+input)

#setting selenium wbedriver for the given site
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
#getting to the last tweet
html=browser.page_source
soup=BeautifulSoup(html,'lxml')
tag=soup.find_all("ol",id="stream-items-id")
tags=tag.find_all("li")
tags
lis=[]
names=[]
for i in tags:
    names_div=i.find_all("div",class_="stream-item-header")
    for j in names_div:
        link=j.find_all("strong",class_="fullname show-popup-with-id u-textTruncate ")
        try:
            link=link[0]
            text=(link.text)
            names.append(text)
        except:
            continue
#getting the names of the people who tweeted	
date=[]
for i in tags:
    dates=i.find_all("div",class_="stream-item-header")
    for j in dates:
        link=j.find_all("small",class_="time")
        try:
            link=link[0]
            link=link.text
            date.append(link.strip())
        except:
            continue
#getting the dates of the tweets	
paragraphs=[]
for i in tags:
    para=i.find_all("div",class_="content")
    for j in para:
        link=j.find_all("div",class_="js-tweet-text-container")
        try:
            link=link[0]
            text=link.find_all("p")
            paragraphs.append(text[0].text)
        except:
            continue
#getting the text of the tweets	
comments=[]
for i in tags:
    comment=i.find_all("div",class_="content")
    for j in comment:
        link=j.find_all("button",class_="ProfileTweet-actionButton js-actionButton js-actionReply")
        link=link[0]
        for k in link:
            try:
                no_comments=k.find_all("span",class_="ProfileTweet-actionCountForPresentation")
                if no_comments !=None:
                    no_comments=no_comments[0]
                    comments.append(no_comments.text)
            except:
                continue
#getting no of comments 		
test_df=pd.DataFrame({'date':date,'names':names,'paragraph':paragraphs,'no. of comments':comments})
#storing the data in pandas
test_df.to_csv('data.csv')
#storing the data in csv file
