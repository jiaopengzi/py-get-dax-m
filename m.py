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

from utils import Utils


class M(object):
    """ Power Query 官方文档获取为 json 文案 用于分析使用
    """

    @staticmethod
    def get_m() -> str:
        """获取 Power Query 函数信息

        :param category_m: 函数分类英文名称
        :param language: 对应函数版本 中文版:zh-en 和 英文版:en-us
        :param dic_func: 函数字典
        :param dic_category: 函数类别的字典，有就使用，没有不添加
        :return:返回函数参数字典
        """

        url_base_en = "https://learn.microsoft.com/en-us/powerquery-m/"
        url_base_cn = "https://learn.microsoft.com/zh-cn/powerquery-m/"
        url_en = "https://learn.microsoft.com/en-us/powerquery-m/toc.json"
        url_cn = "https://learn.microsoft.com/zh-cn/powerquery-m/toc.json"

        dic_en = Utils.response_json_to_dict(url_en)
        dic_cn = Utils.response_json_to_dict(url_cn)

        func_dict = {}

        items_en = dic_en.get("items")[0].get("children")[10].get("children")
        items_cn = dic_cn.get("items")[0].get("children")[10].get("children")
        # print(items_cn)
        # i = 0
        for item_en, item_cn in zip(items_en[2:], items_cn[2:]):

            category_en = item_en.get("toc_title")
            category_cn = item_cn.get("toc_title")
            group_en = item_en.get("children")

            for fx in group_en[1:]:
                fx_url_en = url_base_en + fx.get("href")
                fx_url_cn = url_base_cn + fx.get("href")
                # i += 1
                # print(i)
                # print(fx_url_en)
                func_dict[fx.get("toc_title")] = {"url-en-us"         : fx_url_en,
                                                  "url-zh-cn"         : fx_url_cn,
                                                  "description-en-us" : Utils.get_func_description(fx_url_en),
                                                  "category-en-us"    : category_en,
                                                  "url-category-en-us": url_base_en + group_en[0].get("href"),
                                                  "category-zh-cn"    : category_cn,
                                                  "url-category-zh-cn": url_base_en + group_en[0].get("href"),
                                                  "description-zh-cn" : Utils.get_func_description(fx_url_cn)
                                                  }

        # 函数信息使用 json 存放在当前文件夹下
        json_path = os.path.join(Utils.base_dir(), "m.json")
        Utils.write_json_in_file(json_path, func_dict)
        return json_path


if __name__ == "__main__":
    import time

    start_time = time.time()
    m = M()
    download = m.get_m()
    print(f"Power Query 下载完毕！文件存放位置：{download}")
    end_time = time.time()
    print(f"耗时 {(end_time - start_time):.2f} 秒！")  # 耗时 386.98 秒！