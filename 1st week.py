import requests
import bs4 

#open a file
f=open("1st week.txt",'w+')

#request to get the website
res=requests.get("https://www.betterteam.com/job-description")
bs=bs4.BeautifulSoup(res.text,"html.parser")

#create a list with class name 
baseclass=bs.select('.col-md-6.item')
i=0

#only for 10 jobs
while i!=10:
    
    #initialize each element of list to ul
    url=baseclass[i]
    
    #get only the link from each href
    link=url.select('a')[0]['href']
    print(link)
    
    #next linked page 
    req=requests.get(link)
    bsl=bs4.BeautifulSoup(req.text,"html.parser")

    #the 3rd ul in the page has the job requierments
    li=bsl.select('ul')[3]

    #get each requierments and store it in a file
    for item in li:
        f.write(item.text+"\n")
    f.write("\n")
    i+=1
f.close()
