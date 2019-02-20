#!/usr/bin/python
# -*- coding: utf8 -*-

"""
    获取美女图片
    https://www.mzitu.com/
"""

import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup as bs
import uuid
import os
from multiprocessing import Process

headers = {
    "Accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "Accept-Encoding": "gzip, deflate, sdch",
    "cookie": "__cfduid=d003f333c8fa21bdb61c4acbb10f0e82b1524496879",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}

request_retry = HTTPAdapter(max_retries=3)

def next_page_tag(tag):
    return tag.name == 'a' and '下一页»' in tag.text

def get(url, refer=None):
    """ 返回url的响应"""
    session = requests.session()
    session.headers = headers
    if refer:
        headers["referer"] = refer
    session.mount('https://', request_retry)
    session.mount('http://', request_retry)
    return session.get(url)

def download_pic(url, dir_name, refer):
    """ 下载图片"""
    response = get(url, refer)
    imgsoup = bs(response.content, "html.parser").select_one("div.main-image img")
    if not imgsoup:
        return
    href = imgsoup.attrs["src"]
    response = get(href)
    with open(dir_name + "/" + str(uuid.uuid1()) + ".jpg", 'wb') as fs:
        fs.write(response.content)

def get_pic(url, mm_type):
    """ 获取某图片集的所有页面图片
    每页面包含一张图片
    """
    refer = url
    li_soup = bs(get(url).content, "html.parser")
    next_page = li_soup.find(next_page_tag)
    if not next_page:
        return
    total_page = int(next_page.find_previous_sibling().text)
    title = li_soup.title.text.replace(' ', '-')
    dir_name = "img/" + mm_type + "/" + title
    if os.path.exists(dir_name):
        return
    os.makedirs(dir_name)
    print('下载...', title)
    for page in range(1, total_page + 1):
        download_pic(url + "/" + str(page), dir_name, refer)

def get_page_content(page, mm_type):
    """ 获取某页面的所有列表item对应链接的所有图片内容"""
    href = "http://www.mzitu.com/" + mm_type + "/page/" + str(page)
    soup = bs(get(href).content, "html.parser")
    li_list = soup.select("div.postlist ul#pins li")
    for li in li_list:
        # 每个li包含一个图片集
        get_pic(li.select_one("a").attrs["href"], mm_type)

def get_type_content(url, mm_type):
    """ 获取某类型的所有图片内容 """
    soup = bs(get(url).content, "html.parser")
    # 获取每一类型图片的总页面
    total_page = int(soup.select_one("a.next.page-numbers").find_previous_sibling().text)
    print("{0} 总页面: {1}".format(mm_type, total_page))
    for page in range(1, total_page + 1):
        get_page_content(page, mm_type)

if __name__ == "__main__":
    tasks = [Process(target=get_type_content, args=('http://www.mzitu.com/' + mm_type, mm_type)) for mm_type in ['xinggan', 'japan', 'mm']]
    for task in tasks:
        task.start()
