# -*- encoding: utf-8 -*-
"""
@File           :   main.py
@Time           :   2023-03-09, 周四, 18:18
@Author         :   焦棚子
@Email          :   jiaopengzi@qq.com
@Blog           :   https://jiaopengzi.com/
@Version        :   1.0.0
@Description    :   获取 dax & m 官方文档信息 入口文件
"""

import time

from dax import DAX
from m import M

# DAX
start_time_dax = time.time()
# dax = DAX()
# download_dax = dax.get_dax()
# print(f"DAX 下载完毕！文件存放位置：{download_dax}")
# end_time_dax = time.time()
# print(f"耗时 {(end_time_dax - start_time_dax):.2f} 秒！")  # 耗时 276.18 秒！,注意英文版需要 科 + 学 + 上 + 网

# Power Query
start_time_m = time.time()
m = M()
download_m = m.get_m()
print(f"Power Query 下载完毕！文件存放位置：{download_m}")
end_time_m = time.time()
print(f"耗时 {(end_time_m - start_time_m):.2f} 秒！")  # 耗时 386.98 秒！