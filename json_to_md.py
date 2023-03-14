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


class JTM(object):
    """ json to md 的简写
    """

    # 函数表头
    field_fun3 = '| 函数名称 | 描述 | 链接 |'
    # markdown 表格标识
    table_mark3 = '| :--: | :--: |:--: |'

    def contents_category(self, category: dict, md_list: list, cols: int = 3) -> list:
        """目录按照功能分类

        :param category: 分类的字典
        :param md_list: 生成 md 的 list 源
        :param cols: 需要生成几列，默认 3 列
        :return: 更新后的 md_list
        """
        line = ""
        md_list.append('<h2 id="home"><a href="https://jiaopengzi.com/doc" class="a-button">点击返回主页</a></h2><span id="jiaopengzi"><a href="https://jiaopengzi.com/">焦棚子</a>整理</span>')
        md_list.append('<h2 id="content">目录</h2>')
        for index, c in enumerate(category):
            # text = f"**[{index + 1}、{c}](#{index + 1}-{c})**"
            text = f'**<a href="#{index + 1}">{index + 1}、{c}({category[c]})</a>**'
            count = len(category)
            col = index % cols
            rows = len(category) // cols
            if col == 0:
                line = f'| {text} '
                if index // 3 == rows and index == count - 1:  # 处理最后一行
                    md_list.append(f'{line}|  |  |')
            elif col == 1:
                line = f'{line}| {text} '
                if index // cols == rows and index == count - 1:
                    md_list.append(f'{line}|  |')
            elif col == 2:
                line = f'{line}| {text} |'
                md_list.append(line)
        md_list.insert(4, self.table_mark3)
        return md_list

    @staticmethod
    def contents_capital(category: dict, md_list: list) -> list:
        """目录按照首字母分类

        :param category: 分类的字典
        :param md_list: 生成 md 的 list 源
        :return: 更新后的 md_list
        """
        line = ""
        # 设置目录标题
        md_list.append('<h2 id="home"><a href="https://jiaopengzi.com/doc" class="a-button">点击返回主页</a></h2><span id="jiaopengzi"><a href="https://jiaopengzi.com/">焦棚子</a>整理</span>')
        md_list.append('<h2 id="content">目录</h2>')
        for index, c in enumerate(category):
            line = f'{line}**<a href="#{index + 1}" >{c}({category[c]})</a>** '
        md_list.append(line)
        return md_list

    def json_to_m_md_category(self):
        """通过 json 拼接成 m 函数 markdown 文件 (功能分类版)

        :return: markdown 文件路径
        """
        path_m = os.path.join(Utils.base_dir(), "m.json")
        m_dic = Utils.read_json(path_m)

        # 字典去重获取分类
        category = {m_dic[item]["category-zh-cn"]: "category" for item in m_dic}
        for c in category:
            i = sum(c == m_dic[item]["category-zh-cn"] for item in m_dic)
            category[c] = i

        h1 = '# Power Query M 函数文档(功能分类版)'

        md_list = [h1]
        self.contents_category(category, md_list)

        for index, c in enumerate(category):
            # 换行显示目录返回锚点
            h2 = f"<h2 id='{index + 1}'>{index + 1}、{c}</h2>\n<a href='#content'>返回目录</a>"
            md_list.append(h2)  # 二级标题
            md_list.append(self.field_fun3)
            md_list.append(self.table_mark3)
            for key in m_dic:
                if m_dic[key]["category-zh-cn"] == c:
                    # 描述中只取第一句简单介绍。
                    des = m_dic[key]["description-zh-cn"].replace("\n", " ").strip()
                    des = f'{des.split("。")[0]}。'
                    line_n = f'| {key} | {des} | [中文]({m_dic[key]["url-zh-cn"]}) [英文]({m_dic[key]["url-en-us"]}) |'
                    # line_n = line_n.replace("\n", " ")
                    md_list.append(line_n)

        path_md = os.path.join(Utils.base_dir(), "m-category.md")
        md_str = "\n".join(md_list)
        return Utils.write_str_in_file(path_md, md_str)

    def json_to_m_md_sort(self):
        """通过 json 拼接成 m 函数 markdown 文件 (首字母排序版)

        :return: markdown 文件路径
        """
        path_m = os.path.join(Utils.base_dir(), "m.json")
        m_dic = Utils.read_json(path_m)
        keys = sorted(m_dic.keys(), reverse=False)

        h1 = '# Power Query M 函数文档(首字母排序版)'

        md_list = [h1]
        category = {key[0].upper(): "category" for key in keys}
        for c in category:
            i = sum(item[0].upper() == c for item in m_dic)
            category[c] = i

        md_list = self.contents_capital(category, md_list)
        for index, capital in enumerate(category):
            # 换行显示目录返回锚点
            h2 = f"<h2 id='{index + 1}'>{capital}</h2>\n<a href='#content'>返回目录</a>"
            md_list.append(h2)
            md_list.append(self.field_fun3)
            md_list.append(self.table_mark3)
            for key in keys:
                if key[0].upper() == capital:
                    # 描述中只取第一句简单介绍。
                    des = m_dic[key]["description-zh-cn"].replace("\n", " ").strip()
                    des = f'{des.split("。")[0]}。'
                    line_n = f'| {key} | {des} | [中文]({m_dic[key]["url-zh-cn"]}) [英文]({m_dic[key]["url-en-us"]}) |'
                    md_list.append(line_n)

        path_md = os.path.join(Utils.base_dir(), "m-sort.md")
        md_str = "\n".join(md_list)
        return Utils.write_str_in_file(path_md, md_str)

    def json_to_dax_md_category(self):
        """通过 json 拼接成 dax 函数 markdown 文件 (功能分类版)

        :return: markdown 文件路径
        """
        path_dax = os.path.join(Utils.base_dir(), "dax.json")
        dax_dic = Utils.read_json(path_dax)

        # 字典去重获取分类
        category = {dax_dic[item]["category-zh-cn"]: "category" for item in dax_dic}
        # category = {dax_dic[item]["category-zh-cn"]: "category" for item in dax_dic}
        for c in category:
            i = sum(c == dax_dic[item]["category-zh-cn"] for item in dax_dic)
            category[c] = i

        h1 = '# DAX 函数文档(功能分类版)'
        md_list = [h1]
        self.contents_category(category, md_list)

        for index, c in enumerate(category):
            # 换行显示目录返回锚点

            h2 = f"<h2 id='{index + 1}'>{index + 1}、{c}</h2>\n<a href='#content'>返回目录</a>"
            md_list.append(h2)
            md_list.append(self.field_fun3)
            md_list.append(self.table_mark3)
            for key in dax_dic:
                if dax_dic[key]["category-zh-cn"] == c:
                    # 描述中只取第一句简单介绍。
                    des = dax_dic[key]["description-zh-cn"].replace("\n", " ").strip()
                    des = f'{des.split("。")[0]}。'
                    line_n = f'| {key} | {des} | [中文]({dax_dic[key]["url-zh-cn"]}) [英文]({dax_dic[key]["url-en-us"]}) [SQLBI]({dax_dic[key]["url-dax-guide"]}) |'
                    md_list.append(line_n)

        path_md = os.path.join(Utils.base_dir(), "dax-category.md")
        md_str = "\n".join(md_list)
        return Utils.write_str_in_file(path_md, md_str)

    def json_to_dax_md_sort(self):
        """通过 json 拼接成 dax 函数 markdown 文件 (首字母排序版)

        :return: markdown 文件路径
        """
        path_dax = os.path.join(Utils.base_dir(), "dax.json")
        dax_dic = Utils.read_json(path_dax)
        keys = sorted(dax_dic.keys(), reverse=False)

        h1 = '# DAX 函数文档(首字母排序版)'
        md_list = [h1]

        # 字典去重获取分类
        category = {key[0].upper(): "category" for key in keys}
        for c in category:
            i = sum(item[0].upper() == c for item in dax_dic)
            category[c] = i

        md_list = self.contents_capital(category, md_list)

        for index, capital in enumerate(category):
            h2 = f"<h2 id='{index + 1}'>{capital}</h2>\n<a href='#content'>返回目录</a>"
            md_list.append(h2)
            md_list.append(self.field_fun3)
            md_list.append(self.table_mark3)
            for key in keys:
                if key[0].upper() == capital:
                    # 描述中只取第一句简单介绍。
                    des = dax_dic[key]["description-zh-cn"].replace("\n", " ").strip()
                    des = f'{des.split("。")[0]}。'
                    line_n = f'| {key} | {des} | [中文]({dax_dic[key]["url-zh-cn"]}) [英文]({dax_dic[key]["url-en-us"]}) [SQLBI]({dax_dic[key]["url-dax-guide"]}) |'
                    md_list.append(line_n)

        path_md = os.path.join(Utils.base_dir(), "dax-sort.md")
        md_str = "\n".join(md_list)
        return Utils.write_str_in_file(path_md, md_str)


if __name__ == "__main__":
    jtm = JTM()
    jtm.json_to_dax_md_category()
    jtm.json_to_dax_md_sort()
    jtm.json_to_m_md_category()
    jtm.json_to_m_md_sort()
    print("生成完毕！")