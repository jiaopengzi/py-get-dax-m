# -*- encoding: utf-8 -*-
"""
@File           :   json_to_md.py
@Time           :   2023-03-09, 周四, 9:33
@Author         :   焦棚子
@Email          :   jiaopengzi@qq.com
@Blog           :   https://jiaopengzi.com/
@Version        :   1.0.0
@Description    :   json 转换到 markdown 格式.
"""

import os

from utils import Utils


def json_to_m_md_category():
    """通过 json 拼接成 m 函数 markdown 文件 (分类版)

    :return: markdown 文件路径
    """
    path_m = os.path.join(Utils.base_dir(), "m.json")
    m_dic = Utils.read_json(path_m)

    category = {m_dic[item]["category-zh-cn"]: "category" for item in m_dic}

    h1 = '# Power Query M 函数文档(分类版)'
    line1 = '| 函数名称 | 描述 | 链接 |'
    line2 = '| :--: | :--: |:--: |'
    md_list = [h1]
    for index, c in enumerate(category):
        h2 = f"## {index + 1}、{c}"
        md_list.append(h2)
        md_list.append(line1)
        md_list.append(line2)
        for key in m_dic:
            if m_dic[key]["category-zh-cn"] == c:
                line_n = f'| {key} | {m_dic[key]["description-zh-cn"]} | [中文]({m_dic[key]["url-zh-cn"]}) [英文]({m_dic[key]["url-en-us"]}) |'
                md_list.append(line_n)

    path_md = os.path.join(Utils.base_dir(), "m_category.md")
    md_str = "\n".join(md_list)
    return Utils.write_str_in_file(path_md, md_str)


def json_to_m_md_sort():
    """通过 json 拼接成 m 函数 markdown 文件 (排序版)

    :return: markdown 文件路径
    """
    path_m = os.path.join(Utils.base_dir(), "m.json")
    m_dic = Utils.read_json(path_m)
    keys = sorted(m_dic.keys(), reverse=False)

    h1 = '# Power Query M 函数文档(排序版)'
    line0 = '| 函数名称 | 描述 | 链接 |'
    line1 = '| :--: | :--: |:--: |'
    md_list = [h1, line0, line1]
    for key in keys:
        line_n = f'| {key} | {m_dic[key]["description-zh-cn"]} | [中文]({m_dic[key]["url-zh-cn"]}) [英文]({m_dic[key]["url-en-us"]}) |'
        md_list.append(line_n)

    path_md = os.path.join(Utils.base_dir(), "m_sort.md")
    md_str = "\n".join(md_list)
    return Utils.write_str_in_file(path_md, md_str)


def json_to_dax_md_category():
    """通过 json 拼接成 dax 函数 markdown 文件 (分类版)

    :return: markdown 文件路径
    """
    path_dax = os.path.join(Utils.base_dir(), "dax.json")
    dax_dic = Utils.read_json(path_dax)

    category = {dax_dic[item]["category-zh-cn"]: "category" for item in dax_dic}

    h1 = '# DAX 函数文档(分类版)'
    line1 = '| 函数名称 | 描述 | 链接 |'
    line2 = '| :--: | :--: |:--: |'
    md_list = [h1]
    for index, c in enumerate(category):
        h2 = f"## {index + 1}、{c}"
        md_list.append(h2)
        md_list.append(line1)
        md_list.append(line2)
        for key in dax_dic:
            if dax_dic[key]["category-zh-cn"] == c:
                line_n = f'| {key} | {dax_dic[key]["description-zh-cn"]} | [中文]({dax_dic[key]["url-zh-cn"]}) [英文]({dax_dic[key]["url-en-us"]}) [SQLBI]({dax_dic[key]["url-dax-guide"]}) |'
                md_list.append(line_n)

    path_md = os.path.join(Utils.base_dir(), "dax_category.md")
    md_str = "\n".join(md_list)
    return Utils.write_str_in_file(path_md, md_str)


def json_to_dax_md_sort():
    """通过 json 拼接成 dax 函数 markdown 文件 (排序版)

    :return: markdown 文件路径
    """
    path_dax = os.path.join(Utils.base_dir(), "dax.json")
    dax_dic = Utils.read_json(path_dax)
    keys = sorted(dax_dic.keys(), reverse=False)

    h1 = '# DAX 函数文档(排序版)'
    line0 = '| 函数名称 | 描述 | 链接 |'
    line1 = '| :--: | :--: |:--: |'
    md_list = [h1, line0, line1]
    for key in keys:
        line_n = f'| {key} | {dax_dic[key]["description-zh-cn"]} | [中文]({dax_dic[key]["url-zh-cn"]}) [英文]({dax_dic[key]["url-en-us"]}) [SQLBI]({dax_dic[key]["url-dax-guide"]}) |'
        md_list.append(line_n)

    path_md = os.path.join(Utils.base_dir(), "dax_sort.md")
    md_str = "\n".join(md_list)
    return Utils.write_str_in_file(path_md, md_str)


if __name__ == "__main__":
    json_to_dax_md_category()
    json_to_dax_md_sort()
    json_to_m_md_category()
    json_to_m_md_sort()
    print("生成完毕！")