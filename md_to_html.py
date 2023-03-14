# -*- encoding: utf-8 -*-
"""
@File           :   md_to_html.py
@Time           :   2023-03-14, 周二, 15:37
@Author         :   焦棚子
@Email          :   jiaopengzi@qq.com
@Blog           :   https://jiaopengzi.com/
@Version        :   1.0.0
@Description    :   markdown 转换为 html 修改样式 和 第一个表格
"""
import os.path

from utils import Utils


def md_to_html(c_or_s: str, path_html_old: str, path_html_new: str) -> None:
    """markdown 转换为 html 修改样式 和 第一个表格

    :param c_or_s: 是 sort 或者 category
    :param path_html_old: 导出的 html 路径
    :param path_html_new: 修改后的 html 路径
    :return: None
    """
    u = Utils()
    # 读取 html
    html = u.read_file_to_str(path_html_old)

    # 判断使用哪个 css 文件
    if c_or_s == "category":
        path_css_category = "css-category.css"
        css = u.read_file_to_str(path_css_category)
    else:
        path_css_sort = "css-sort.css"
        css = u.read_file_to_str(path_css_sort)

    # 找到 css 的最后结点增加 css
    h_list = html.split("</style>")
    h_list.insert(1, f"{css}</style>")
    html = "".join(h_list)

    # 如果是分类的形式需要对对一个表使用单独的样式
    if c_or_s == "category":
        index = html.find("<table>")
        html = f'{html[:index + 6]} id="table-content"{html[index + 6:]}'

    # 写出新的文件
    u.write_str_in_file(path_html_new, html)


def init_md_to_html(folder_old: str, folder_new: str) -> None:
    """批量初始化文件

    :param folder_old: 老文件夹
    :param folder_new: 新文件夹
    :return:
    """
    # 初始化文件夹
    u = Utils()
    u.init_folder(folder_new)
    file_list = ["dax-category.html", "dax-sort.html", "m-category.html", "m-sort.html"]
    for file in file_list:
        if file.__contains__("category"):
            md_to_html("category", os.path.join(folder_old, file), os.path.join(folder_new, file))
        else:
            md_to_html("sort", os.path.join(folder_old, file), os.path.join(folder_new, file))


if __name__ == "__main__":
    folder_old = "C:/desktop/"
    folder_new = "C:/desktop/new/"
    init_md_to_html(folder_old, folder_new)
    print("完成")