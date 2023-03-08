# -*- encoding: utf-8 -*-
"""
@File           :   main.py
@Time           :   2023-03-08, 周三, 16:18
@Author         :   焦棚子
@Email          :   jiaopengzi@qq.com
@Blog           :   https://jiaopengzi.com/
@Version        :   1.0.0
@Description    :   python 获取 Power Query 官方文档信息
"""
import os
import sys
import json
import copy
from bs4 import element
from bs4 import BeautifulSoup
import requests
import lxml


class M(object):
    """ Power Query 官方文档获取为 json 文案 用于分析使用
    """

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
    def get_m_category(language: str, dic: dict = None) -> dict:
        """获取 Power Query 函数信息类别

        :param language: 对应函数版本 中文版:zh-cn 和 英文版:en-us
        :param dic: 函数类别字典
        :return: 返回函数类别字典
        """

        if dic is None:
            dic = {}
        url = f'https://learn.microsoft.com/{language}/powerquery-m/power-query-m-function-reference'

        try:
            response = requests.get(url)
            response.encoding = 'utf-8'
        except:
            raise Exception("请求失败")

        html_content = response.text
        bs = BeautifulSoup(html_content, "lxml")

        class_div = {"class": "content"}
        content = bs.find("div", class_div)
        ul = content.find_all("ul")[1]

        for li in ul:
            # print(repr(li))
            if li != '\n' and type(li) == element.Tag:
                herf = li.a["href"]
                if herf not in dic:
                    dic[herf] = {}
                dic[herf][f"category-{language}"] = li.a.text

        return dic

    @staticmethod
    def get_m(category_m: str, language: str, dic_func: dict = None, dic_category: dict = None) -> dict:
        """获取 Power Query 函数信息

        :param category_m: 函数分类英文名称
        :param language: 对应函数版本 中文版:zh-en 和 英文版:en-us
        :param dic_func: 函数字典
        :param dic_category: 函数类别的字典，有就使用，没有不添加
        :return:返回函数参数字典
        """

        global name
        if dic_func is None:
            dic_func = {}
        url_base = f'https://learn.microsoft.com/{language}/powerquery-m/'
        url = url_base + category_m

        try:
            response = requests.get(url)
            response.encoding = 'utf-8'
        except:
            raise Exception("请求失败")

        html_content = response.text
        bs = BeautifulSoup(html_content, "lxml")

        table = bs.find("table")

        rows = table.find_all("tr")

        for row in rows[1:]:
            cols = row.find_all("td")
            for col in cols:
                if col.a is not None:
                    name = col.text

                    if name not in dic_func:
                        dic_func[name] = {}
                    dic_func[name][f"url-{language}"] = url_base + col.a["href"]
                dic_func[name][f"description-{language}"] = col.text
                if dic_category:
                    dic_func[name][f"category-{language}"] = dic_category[category_m][f"category-{language}"]

        return dic_func

    def get_all_functions(self) -> str:
        """获取所有 Power Query 函数信息

        :return: 文件下载路径
        """
        # 中文分类
        category_cn = self.get_m_category("zh-cn")

        # 英文分类，二参字典延续使用 category_cn
        category_en = self.get_m_category("en-us", category_cn)

        # 区域第一个和最后一个不需要的类别
        category = category_en

        all_func_dict = {}

        # 通过类别循环获取函数信息
        for c in category:
            func_en = self.get_m(category_m=c, language="en-us", dic_category=category)
            func_cn = self.get_m(category_m=c, language="zh-cn", dic_func=func_en, dic_category=category)
            all_func_dict |= func_cn

        # 函数信息使用 json 存放在当前文件夹下
        json_path = os.path.join(self.base_dir(), "m.json")
        self.write_json_in_file(json_path, all_func_dict)
        return json_path


if __name__ == "__main__":
    import time

    start_time = time.time()
    m = M()
    download = m.get_all_functions()
    print(f"Power Query 下载完毕！文件存放位置：{download}")
    end_time = time.time()
    print(f"耗时 {(end_time - start_time):.2f} 秒！")
    # m函数较多大约 耗时 192.54 秒！