#!/usr/bin/python
# -*- coding: utf8 -*-

"""
     author : menqi
     desp: 爬取图片,仅供学习O(∩_∩)O
"""


import os
import requests
from bs4 import BeautifulSoup
from lxml import etree
from multiprocessing import Process
import codecs


url = "https://www.869ee.com"

# 对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，
# 有的服务器不会响应，所以我们还可以在headers中加入referer
# "referer": "xxxxxx"
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "__cfduid=d003f333c8fa21bdb61c4acbb10f0e82b1524496879",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}
OUTPUT = 'f:/output'

def get(url):
    """
        伪装报头http访问
    """
    r = requests.get(url, headers=headers)
    return r

def head(url):
    r = requests.head(url, headers=headers, allow_redirects=True)
    return r

def get_head():
    """
    	获取真实地址
    """
    r = head(url)
    return r.url

def get_home_url():
    """
        获取主页
        没有实现动态获取
        根据实际情况需要修改
    """
    return get_head() + '/index/home.html'

def write_page(mm_type, img_srcs, page_name):
    """保存整页图片内容"""
    path = os.path.join(OUTPUT, mm_type, page_name)
    if os.path.exists(path):
        return
    os.makedirs(path)
    print("正在下载..." + path)
    for src in img_srcs:
        if not src:
            continue
        image = get(src).content
        with open(os.path.join(path, os.path.split(src)[-1]), "wb") as f:
            f.write(image)

def load_image(mm_type, images_urls):
    """加载图片 """
    for url in images_urls:
        content = etree.HTML(get(url).text)
        img_srcs = content.xpath('//div[@class="content"]/img/@data-original')
        if not img_srcs:
            continue
        write_page(mm_type, img_srcs, os.path.split(url)[-1].split('.')[0])

def get_next_page(head_url, soup):
    """ 获取下一页地址"""
    next_page_soup = soup.select('div.pagination a')[-2]
    url = codecs.escape_decode(next_page_soup['href'].encode('unicode-escape'))[0].decode('utf8')
    if not url:
        return
    if '.html' not in url:
        return
    return head_url + url

def get_page(head_url, url):
    """ 循环获取页面"""
    # 图片类型定义
    mm_type = url.split('/')[-1].split('.')[0].split('-')[1]
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    alist = soup.select('ul.img-list-data li a')
    links = [(head_url + codecs.escape_decode(item['href'].encode('unicode-escape'))[0].decode('utf8')) for item in
             alist]
    if links:
        load_image(mm_type, links)

    # 获取下一页
    next_page = get_next_page(head_url, soup)
    if not next_page:
        return
    get_page(head_url, next_page)

def parser(head_url):
    """ 抓取主页地址内容并解析"""
    r = get(head_url + '/index/home.html')
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    alist = soup.select('#section-menu div .row-item.odd')[1].select('ul li a')
    links = [(head_url + codecs.escape_decode(item['href'].encode('unicode-escape'))[0].decode('utf8')) for item in alist]
    # 取其中部分链接
    links = [links[1], links[2], links[5]]
    print(links)
    for link in links:
        p = Process(target=get_page, args=(head_url, link))
        p.start()

if __name__ == "__main__":
    head_url = get_head()
    parser(head_url)
