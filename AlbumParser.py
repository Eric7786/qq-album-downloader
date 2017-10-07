# !/usr/bin/env python2
# -*- coding:utf-8 -*-


#########
# 解析（单个）相册所有图片地址
#########

import requests
import json
import codecs
from time import time,sleep

header={
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.8",
        "authority": "h5.qzone.qq.com",
        "referer": "https://qzs.qq.com/qzone/photo/v7/page/photo.html?init=photo.v7/module/albumList/index&navBar=1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36"
    }

# 可修改参数，相册名称、id、开始和结尾的index
alubmName = u'裸照'
topicId = 'V10OuqVo0Gm1sY'
pageStart = '1001'
pageNumer = '1085'
cookie={
        "RK": "rHmXL4f+ZH",
        "__Q_w_s__QZN_TodoMsgCnt": "1",
        "o_cookie": "394321749",
        "p_skey": "TgQ8fUCTCF*qfvMQvP0VuHhzouyesu10pqf7MkiZm-g_",
        "p_uin": "o2437979300",
        "pgv_info": "ssid=s9482845211",
        "pgv_pvi": "4779133952",
        "pgv_pvid": "1823440060",
        "pgv_si": "s6132285440",
        "pt2gguin": "o2437979300",
        "pt4_token": "cXN*YwLB2aNdrcC1qFxWfJYNP*54jYLmv*bqeWjb358_",
        "ptcz": "56d8dae9d308f7721534d13d1220061631f0727f94aa626b6b464992b7b48100",
        "ptisp": "cm",
        "ptui_loginuin": "931978415",
        "skey": "@R67NUEDe2",
        "tvfe_boss_uuid": "96e0189fb9f47dc0",
        "uin": "o2437979300",
        "verifysession": "h017d8b9b9bc79d6c9d656120071785a35ae8d37e28f55fa3245c4ad306443014daffc47e4c76deba8a",
        "zzpanelkey": "",
        "zzpaneluin": ""
    }
param = (
    ('g_tk', '1559184744'),#
    ('callback', 'shine0_Callback'),
    ('t', '444496822'),#
    ('mode', '0'),
    ('idcNum', '4'),
    ('hostUin', '3076137119'),
    ('topicId', topicId),
    ('noTopic', '0'),
    ('uin', '2437979300'),
    ('pageStart', pageStart),
    ('pageNum', pageNumer),
    ('skipCmtCount', '0'),
    ('singleurl', '1'),
    ('batchId', ''),
    ('notice', '0'),
    ('appid', '4'),
    ('inCharset', 'utf-8'),
    ('outCharset', 'utf-8'),
    ('source', 'qzone'),
    ('plat', 'qzone'),
    ('outstyle', 'json'),
    ('format', 'jsonp'),
    ('json_esc', '1'),
    ('question', ''),
    ('answer', ''),
    ('callbackFun', 'shine0'),
    ('_', '1507221921290'),#
)
req = requests.get(
    url="https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/cgi_list_photo",
    headers=header,
    params=param,
    cookies=cookie,
    verify = False,
    timeout=15
    )
# print req.headers
res = req.text
# print res

photoList = {}
pohotListText = res.split('_Callback(')[1].split(');')[0]
photoList = json.loads(pohotListText)

#返回的异常文本
# shine0_Callback({
# 	"code":-3000,
# 	"subcode":-4001,
# 	"message":"对不起，您尚未登录或者登录超时。",
# 	"notice":0,
# 	"time":1507044419,
# 	"tips":"E50B-0",
# 	"data":{
#    "t" : "495572535"
# }
# }
# 正常
# {
#     "code":0,
#     "subcode":0,
#     "message":"",
#     "default":0,
#     "data":

try:
    if "" != photoList['message'] and 0 != photoList["code"]:
        print photoList['message']
    fp = codecs.open('../textFile/' + alubmName ,'a+', 'utf-8')

    count = int(pageStart)
    for k,v in photoList.iteritems():
        if 'data'==k and 0 == photoList["code"]:
            for photo in photoList['data']['photoList']:

                url = photo['url']
                pName = photo['name']

                line = url + u' | ' + alubmName + u' | '+ pName + '-' + str(count)+'\n'
                # print line
                fp.writelines(line)
                count += 1
except:
    print '---异常---'
finally:
    fp.close()

