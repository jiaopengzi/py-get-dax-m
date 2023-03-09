# -*- encoding: utf-8 -*-
"""
@File           :   main.py
@Time           :   2023-03-08, 周三, 16:18
@Author         :   焦棚子
@Email          :   jiaopengzi@qq.com
@Blog           :   https://jiaopengzi.com/
@Version        :   1.0.0
@Description    :   utils
"""
import json
import os
import sys

import requests
from bs4 import BeautifulSoup


class Utils(object):
    """ 工具
    """

    @staticmethod
    def response_json_to_dict(url: str) -> dict:
        """获取文档中函数的 json 数据

        # url = "https://learn.microsoft.com/en-us/powerquery-m/toc.json"
        # url = "https://learn.microsoft.com/zh-cn/dax/toc.json"

        :param url: 文档的 json 链接
        :return: json 转换后的字典
        """

        try:
            response = requests.get(url)
            response.encoding = 'utf-8'
            if response.status_code != 200:
                print(f"{url} 状态非 200,访问失败")
                return
            return response.json()
        except:
            raise Exception("请求失败")

    @staticmethod
    def write_json_in_file(path: str, json_dic: dict) -> None:
        """覆盖写入 json 文件

        Args:
            path (str):json文件的路径
            json_dic (dict):需要写入的字典内容

        Returns:None

        """
        with open(path, "w", encoding="utf8") as f:
            f.write(json.dumps(json_dic, indent=4, ensure_ascii=False))

    @staticmethod
    def base_dir() -> str:
        """获取当前文件夹路径

        Returns:
                返回主文件文件夹绝对路径
        """
        if getattr(sys, "frozen", False):
            return os.path.dirname(os.path.abspath(sys.executable))
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def get_func_description(url: str) -> str:
        """获取函数描述信息。

        :param url: 函数对应的链接
        :return: 该函数的描述信息
        """

        try:
            response = requests.get(url)
            response.encoding = 'utf-8'
            if response.status_code != 200:
                print(f"{url_dax} 不是200,访问失败")
                return
        except:
            raise Exception("请求失败")

        html_content = response.text
        bs = BeautifulSoup(html_content, "lxml")
        class_div = {"class": "content"}
        content = bs.find("div", class_div)
        p = content.find("p")
        return p.text