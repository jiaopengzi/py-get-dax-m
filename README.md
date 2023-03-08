# py-get-dax-m

**博客：[www.jiaopengzi.com](www.jiaopengzi.com)**

Python 获取 DAX 和 powerquery-m 官方文档信息, 用于代码分析和快速查阅等。
## 1、python 环境

```shell
# 版本：Python 3.9.13
```

## 2、安装依赖

```shell
pip install -r requirements.txt
```

## 3、执行 python 文件

```shell
# dax 文件, 大约耗时 21.20 秒！
python dax.py

# m 文件, m函数较多大约 耗时 192.54 秒！
python m.py
```

## 4、json说明

### Ⅰ、`dax.py` 会在项目目录下生成 `dax.json` 文件。

键名如下：

- `url-en-us` : 函数英文版链接
- `description-en-us` :函数英文版简短说明
- `category-en-us` :函数英文版分类
- `url-zh-cn` :函数中文版链接
- `description-zh-cn` :函数中文版简短说明
- `category-zh-cn` :函数中文版分类
- `url-dax-guide` :函数英文版 SQLBI 链接

```json
    {
  "CALCULATE": {
    "url-en-us": "https://learn.microsoft.com/en-us/dax/calculate-function-dax",
    "description-en-us": "Evaluates an expression in a modified filter context.",
    "category-en-us": "Filter functions",
    "url-zh-cn": "https://learn.microsoft.com/zh-cn/dax/calculate-function-dax",
    "description-zh-cn": "在已修改的筛选器上下文中计算表达式。",
    "category-zh-cn": "筛选器函数",
    "url-dax-guide": "https://dax.guide/calculate/"
  }
}
```

### Ⅱ、`m.py` 会在项目目录下生成 `m.json` 文件。

键名如下：

- `url-en-us` : 函数英文版链接
- `description-en-us` :函数英文版简短说明
- `category-en-us` :函数英文版分类
- `url-zh-cn` :函数中文版链接
- `description-zh-cn` :函数中文版简短说明
- `category-zh-cn` :函数中文版分类

```json
    {
  "Excel.Workbook": {
    "url-en-us": "https://learn.microsoft.com/en-us/powerquery-m/excel-workbook",
    "description-en-us": "Returns a table representing sheets in the given excel workbook.",
    "category-en-us": "Accessing data functions",
    "url-zh-cn": "https://learn.microsoft.com/zh-cn/powerquery-m/excel-workbook",
    "description-zh-cn": "返回表示给定 excel 工作簿中工作表的表。",
    "category-zh-cn": "数据访问函数"
  }
}
```