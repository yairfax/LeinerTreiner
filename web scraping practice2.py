from selenium import webdriver
from bs4 import BeautifulSoup
from bs4 import NavigableString
import pandas as pd
from time import time

sounds1=['w','a','y','ə','d','b','ē','r','‘','ă','l','ê','ḵ','e','m','i','t','ô','h','ā','š','q','b','î','ō','û','t','n','z','p','k','ṣ','ĕ','’']
sounds2=['V','AA','Y','IH','D','B','AY','R','','AA','L','EY','/H','EH','M','IY','T','OH','/H','AA','SH','K','V','IY','OH','UX','T','N','Z','F','K','TZ','EH','']
sefer=input('Which sefer would you like to see? ')
perek=input('Which perek would you like to see? ')       

options=webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome("/usr/local/bin/chromedriver",options=options)
words=[]
wordsheb=[]
notes=[]
#driver.get("https://www.tanakhml.org/d11.php2xml?sfr="+sefer+"&prq="+perek+"&psq=1&lvl=99&pnt=tru&acc=tru&dia=tru&enc=mcw&xml=tru")
driver.get("https://www.tanakhml.org/d11.php2xml?sfr="+sefer+"&prq="+perek+"&pnt=tru&acc=fls&dia=tru&enc=mcw&xml=tru")
content=driver.page_source
soup=BeautifulSoup(content,features="html.parser")
for a in soup.findAll('body',href=False, attrs={'id':'body_box_1'}):
    for b in a.findAll('div',attrs={'class':'xml'}):
        for c in b.findAll('span',attrs={'class':'trl_inline'}):
            if len(notes)==0 or notes[len(notes)-1]=='SLQ0':
                d=c.previous_element.previous_element.previous_element
                while True:
                    if not isinstance(d,str):
                        d=d.previous_element
                    elif len(d)>0 and d[0]!='<':
                        d=d.previous_element
                    else:
                        break
                d=d.split('.')
                words.append(int(d[2]))
                notes.append(int(d[2]))
            words.append(c.text)
            notes.append(c.next_element.next_element[7:11])
        for e in b.findAll('span',attrs={'class':'bhs_inline'}):
            if isinstance(notes[len(wordsheb)],int):
                wordsheb.append(notes[len(wordsheb)])
            wordsheb.append(e.text)
driver.quit()

pasuk=int(input('Which pasuk would you like to see? '))

printer=False
found=False
pasukout=[]
pasukoutheb=[]
tropout=[]
for i in words:
    if isinstance(i,int) and i!=pasuk:
        printer=False
    if printer==True:
        pasukout.append(i)
    if isinstance(i,int) and i==pasuk and found==False:
        printer=True
        found=True
printer=False
found=False
for i in wordsheb:
    if isinstance(i,int) and i!=pasuk:
        printer=False
    if printer==True:
        pasukoutheb.append(i)
    if isinstance(i,int) and i==pasuk and found==False:
        printer=True
        found=True
printer=False
found=False
for i in notes:
    if isinstance(i,int) and i!=pasuk:
        printer=False
    if printer==True:
        tropout.append(i)
    if isinstance(i,int) and i==pasuk and found==False:
        printer=True
        found=True
pasukout=" ".join(pasukout)
pasukoutheb=" ".join(pasukoutheb)
tropout=" ".join(tropout)
print(pasukoutheb)
print(pasukout)
print(tropout)
