import json
from pprint import pprint
from openpyxl import Workbook, load_workbook

with open('./datas/warriors.json') as data_file:
    datas = json.load(data_file)
    data_title = datas.get('name')
    data_value = datas.get('value')

    wb = load_workbook('NBA.xlsx')
    sheet = wb.get_active_sheet


    for data in data_value:
        print(data)


    print(data_title)

