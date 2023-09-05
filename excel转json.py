import pandas as pd
import json

def excel_to_json(excel_file, output_file):
    # 读取 Excel 文件
    df = pd.read_excel(excel_file)

    # 将 DataFrame 转换为字典列表
    data = df.to_dict('records')

    # 将字典列表转换为 JSON 字符串
    data_json = json.dumps(data, ensure_ascii=False, indent=4)

    # 保存 JSON 字符串到文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(data_json)
    print(data_json)
# 调用函数，将 'data.xlsx' 转换为一个 JSON 文件 'output.json'
excel_to_json('D:\edr_kb\excel1.xlsx', 'D:\edr_kb\output.json')
