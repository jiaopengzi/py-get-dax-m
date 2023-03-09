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
import sys
import json


def base_dir() -> str:
    """获取当前文件夹路径

    Returns:
            返回主文件文件夹绝对路径
    """
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


def read_file_to_str(path: str) -> str:
    """读取文本文件

    Args:
        path (str):文本文件的路径

    Returns:读取的文件的文本内容

    """
    with open(path, "r", encoding="utf8") as f:
        return f.read()


def read_json(path: str) -> dict:
    """读取 json 文件

    Args:
        path (str):json文件的路径

    Returns:json 转成的字典

    """
    with open(path, "r", encoding="utf8") as f:
        return json.load(f, strict=False)


def write_str_in_file(path: str, text_str: str, encoding="utf8") -> None:
    """覆盖写入文本字符串写入文件

    Args:
        path (str):
        text_str (str): 需要写入文本
        encoding (str): 编码方式、默认为 encoding="utf8"

    Returns:None

    """
    with open(path, "w", encoding=encoding) as f:
        f.write(text_str)


if __name__ == "__main__":
    path_dax = os.path.join(base_dir(), "dax.json")
    dax_dic = read_json(path_dax)
    print(dax_dic)