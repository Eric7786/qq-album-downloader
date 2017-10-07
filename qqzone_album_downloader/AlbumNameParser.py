# !/usr/bin/env python2
# -*- coding:utf-8 -*-

#########
# 解析（某一用户）所有相册，并获取名称、id、图片数量
#########
import json

fp = open('../textFile/album_callback_text','r')
shine_Callback = fp.read()
fp.close()


# print 'text size: ' , len(shine_Callback)

albumListText = shine_Callback.split('_Callback(')[1].split(');')[0]

albumList = {}
albumList = json.loads(albumListText)
# print type(albumList)


for k,v in albumList.iteritems():
    if 'data'==k:
        for album in albumList['data']['albumListModeSort']:
            print album['id'], album['name'], album['total']#, album['createtime']


