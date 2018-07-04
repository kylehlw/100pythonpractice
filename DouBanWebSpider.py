#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys

import xlwt as xlwt

reload(sys)
import urllib2

sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup


def main():
    baseurl = 'https://movie.douban.com/top250?start='
    # askURL(baseurl)
    datalist = getDate(baseurl)
    savapath='doubanTop250.csv'
    saveData(datalist,savapath)


# get web all
def askURL(url):
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)  # get the response
        html = response.read()
        # print html
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getDate(baseurl):
    findLink = re.compile(r'<a href="(.*?)">')  # 找到影片详情链接
    findImgSrc = re.compile(r'<img.*src="(.*jpg)"', re.S)  # 找到影片图片
    findTitle = re.compile(r'<span class="title">(.*)</span>')  # 找到片名
    # 找到评分
    findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
    # 找到评价人数
    findJudge = re.compile(r'<span>(\d*)人评价</span>')
    # 找到概况
    findInq = re.compile(r'<span class="inq">(.*)</span>')
    # 找到影片相关内容：导演，主演，年份，地区，类别
    findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
    # findBd = re.compile(r'<p class="">(.*?)<br >', re.S)

    # 去掉无关内容
    remove = re.compile(r'|\n|<br/>|\.*')
    datalist = []

    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        soup = BeautifulSoup(html)
        # print soup
        for item in soup.find_all('div', class_='item'):  # 找到每一个影片项
            data = []
            item = str(item)
            # print(item)
            # print(type(item))
            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            # 片名可能只有一个中文名，没有外国名
            if(len(titles) == 2):
                ctitle = titles[0] # 中文片名
                data.append(ctitle)
                otitle = titles[1].replace("/","").lstrip() # revmoe无关符号
                data.append(otitle) # 外文片名
            else:
                data.append(titles[0])
                data.append(' ')
            rating =re.findall(findRating,item)[0] #评分
            data.append(rating)
            judgeNum = re.findall(findJudge,item) #添加评论人数
            data.append(judgeNum)
            inq = re.findall(findInq,item) #可能没有概况
            if len(inq) != 0:
                inq = inq[0].replace("。","") #remove 句号
                data.append(inq)
            else:
                data.append(' ')
            # todo need 这里的处理 要写更多的 方法来处理 防止栏位不对
            bd = re.findall(findBd, item)[0].strip()
            # bd = re.sub('...', "",bd)
            bd = re.sub(remove, "", bd)
            bd = re.sub('<br/>', " ", bd)  # 去掉<br>
            bd = re.sub('/', "|", bd)  # 替换/
            bd = re.sub(r"\.*", "", bd)
            bd = re.sub(r"\n", "", bd)
            bd = re.sub(r'导演:|主演:',"|",bd)
            # data.append(bd)
            # print bd
            words = bd.split("|")
            for s in words:
                if len(s) != 0 and s != ' ':  # 去掉空白内容
                    s = re.sub(remove,'',s)
                    data.append(s.strip())
            # 主演有可能因为导演内容太长而没有
            if (len(data) != 12):
                data.insert(8, ' ')  # 留空
            datalist.append(data)
    return datalist
            
#将相关数据写入excel中
def saveData(datalist,savepath):
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet=book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    col=('电影详情链接','图片链接','影片中文名','影片外国名',
                '评分','评价数','概况','导演','主演','年份','地区','类别')
    for i in range(0,12):
        sheet.write(0,i,col[i])#列名
    for i in range(0,250):
        # print i, datalist[i]
        data=datalist[i]

        for j in range(0,len(data)):
            sheet.write(i+1,j,data[j])#数据
    book.save(savepath)#保存

main()
