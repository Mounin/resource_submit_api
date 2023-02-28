# -*- coding: utf-8 -*-
# @Time: 2023/2/28 16:16
# @Author: Honvin
# @File: baidu_api.py
# @Software: PyCharm

import requests

# 百度接口调用地址
url = "http://data.zz.baidu.com/urls?site=https://www.honvin.ink&token=nIG4SxngkVi1xPG2"

# 收录链接
site_urls = [
    "https://www.honvin.ink/",
    "https://www.honvin.ink/archives/fu-wu-qi-da-jian-halo-ge-ren-wang-zhan",
    "https://www.honvin.ink/archives/inheritanceandpolymorphism",
    "https://www.honvin.ink/archives/classandobject",
    "https://www.honvin.ink/archives/pycharm-lian-jie-fu-wu-qi-zhong-de-conda-huan-jing"
]

headers = {
    "User-Agent": "curl/7.12.1",
    "Host": "data.zz.baidu.com",
    "Content-Type": "text/plain",
    "Content-Length": "83"
}

for site_url in site_urls:
    response = requests.post(url, data=site_url, headers=headers)
    print(response.status_code)
    print(response.json())


