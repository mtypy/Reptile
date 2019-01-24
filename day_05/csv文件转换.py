# json 与 csv文件转换
"""
逗号分隔符可以称为字符分隔符，文件是以文本形式存储表格结构
"""
# 1. 导入csv模板
import csv

# 2. 创建文件写入对象
with open("../statics/01-data.csv", "w", encoding="utf-8") as f:
    # 3. 创建csv写入对象
    csv_writer = csv.writer(f)

    # 4. 写入json数据的key作为标题
    csv_writer.writerow(["姓名", "年龄", "性别"])
    csv_writer.writerow(["cao", 18, "男"])
    csv_writer.writerow(["zhuwei", 33, "女"])



