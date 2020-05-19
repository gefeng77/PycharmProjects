# coding=utf-8

import xlrd
"""
读取excel文件
"""


class ReadExcelData(object):

    def open_excel(self, file):
        """读取excel文件"""
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception as e:
            print("Fail to open excel: %s" % file)

    def excel_table(self, file, sheet_name):
        data = self.open_excel(file)
        table = data.sheet_by_name(data)
        # 获取行数
        Trows = table.nrows
        # 获取第一行数据，即表头信息
        Tcolnames = table.row_values(0)
        lister = []

        # 从第二行开始读取数据，第一行是表头信息
        for rownumber in range(1, Trows):
            row = table.row_values(rownumber)
            if row:
                app = {}
                # 总列数，即一行有几个值
                for i in range(len(Tcolnames)):
                    app[Tcolnames[i]] = row[i]
                    lister.append(app)











