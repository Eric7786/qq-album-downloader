# !/usr/bin/env python2
# -*- coding:utf-8 -*-

import requests
import os
from time import strftime,localtime,time


def get_urls(alubmId, path='../textFile/'):
    urls = []
    fp = open(os.path.join(path,alubmId), 'r')
    for line in fp.readlines():
        u = {}
        l = line.strip().split(' | ')
        u['url'] = l[0]
        u['albumName'] = l[1]
        # http://b208.photo.store.qq.com/psb?/V10OuqVo1TvkDx/cX0Sk
        u['photoName'] = l[0][7:len('http://')+4] + '-' + l[2]
        urls.append(u)
    return urls

def get_local_time():
    return strftime('%Y%m%d%H%M%S',localtime(time()))


def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


def downloadJpg(u):
    url = u['url']
    name = u['photoName']
    path = u['albumName']
    check_path(path)

    real_path = os.path.join(path, name)
    print real_path

    header={"user-agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36"
            }

    ir = requests.get(url, headers=header, timeout=15)
    if ir.status_code == 200:
        open(real_path, 'wb').write(ir.content)


if __name__ == '__main__':
    t = get_local_time()
    print t
    for u in get_urls(u'裸照'):
        downloadJpg(u)


