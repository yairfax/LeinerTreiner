from selenium import webdriver
from bs4 import BeautifulSoup
from bs4 import NavigableString
import pandas as pd
import requests


def getTrop(sefer, perek, pasuk):
    # options=webdriver.ChromeOptions()
    # options.add_argument('headless')
    # driver = webdriver.Chrome("/usr/local/bin/chromedriver",options=options)
    words=[]
    wordsheb=[]
    notes=[]
    #driver.get("https://www.tanakhml.org/d11.php2xml?sfr="+sefer+"&prq="+perek+"&psq=1&lvl=99&pnt=tru&acc=tru&dia=tru&enc=mcw&xml=tru")

    r = requests.get("https://www.tanakhml.org/d11.php2xml?sfr=%d&prq=%d&pnt=tru&acc=fls&dia=tru&enc=mcw&xml=tru" % (sefer, perek))
    # driver.get("https://www.tanakhml.org/d11.php2xml?sfr="+sefer+"&prq="+perek+"&pnt=tru&acc=fls&dia=tru&enc=mcw&xml=tru")
    # content=driver.page_source
    soup=BeautifulSoup(r.content,features="html.parser")
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
    # driver.quit()

    tropout=[]
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

    out=[]
    taamim={
        'ZAR2':'zarka',
        'SGL1':'segol',
        'RVI2':'rvii',
        'MHP4':'mapakh',
        'PSH2':'pashta',
        'MER4':'mercha',
        'TIP1':'tipcha',
        'ATN0':'etnachta',
        'PAZ3':'pazer',
        'TLQ4':'tlisha-ktana',
        'TLG3':'tlisha-gdola',
        'QAD4':'kadma',
        'DAR4':'darga',
        'TVR2':'tvir',
        'YTV2':'yetiv',
        'SHA1':'shalshelet',
        'SLQ0':'sof-pasuk',
        'GRM3':'gershaim',
        'ZQQ1':'zakef-katon',
        'ZQG1':'zakef-gadol',
        'LGM3':'munach-munach-rvii'
    }
    for i in range(len(tropout)):
        if tropout[i] in taamim:
            out.append(taamim[tropout[i]])
        elif tropout[i]=='GER3':
            if i==0:
                out.append('azla-geresh')
            else:
                j=i-1
                while j>0 and tropout[j]=='MUN4' or tropout[j]=='MQF5':
                    j-=1
                if tropout[j]=='QAD4':
                    out.append('vazla')
                else:
                    out.append('azla-geresh')

        elif tropout[i]=='MUN4':
            j=i
            while tropout[j+1]=='MQF5':
                j+=1
            if tropout[j+1]=='ZAR2':
                out.append('munach-zarka')
            elif tropout[j+1]=='SGL1':
                out.append('munach-segol')
            elif tropout[j+1]=='RVI2':
                out.append('munach-rvii')
            elif tropout[j+1]=='ATN0':
                out.append('munach-etnachta')
            else:
                out.append('munach')
    return out


# sefer=input('Which sefer would you like to see? ')
# perek=input('Which perek would you like to see? ')
# pasuk=int(input('Which pasuk would you like to see? '))

# out=getTrop(sefer,perek,pasuk)
# out=" ".join(out)
# print(out)
