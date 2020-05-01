# coding=utf-8
import csv


f = open("xieru.csv", 'wb')
writer = csv.writer(f)

# 需要写入的信息
data = ["日期", "内容", "时长", "效果"]
writer.writerow(data)
f.close()
