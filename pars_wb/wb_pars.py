import pandas as pd
import csv
import os
import pathlib
import configparser
import pymysql.cursors

THIS_PATH = pathlib.Path(__file__).parent

DATA_WB = pd.ExcelFile(os.path.join(THIS_PATH, "wb_url.xlsx"))


def articles():

    df_data = pd.read_excel(DATA_WB)
    df_url = df_data["url"]\
        .str.replace("https://www.wildberries.ru/catalog/", "")\
        .str.replace("/detail.aspx", "")\
        .str.replace("?", "")\
        .str.replace("targetUrl=GP", "")
    res_df = pd.merge(df_data, df_url, left_index=True, right_index=True)
    res_df = res_df.drop(columns=['url_x'])
    res_df = res_df.reset_index(drop=True)
    res_df.rename(columns={'url_y': 'id_wb'}, inplace=True)
    out_wb = pd.ExcelWriter('result_wb.xlsx')
    res_df.to_excel(out_wb)
    out_wb.save()


def search_id_art():

    # Подключиться к базе данных.
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='brixo',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connect successful!!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT Dept_No, Dept_Name FROM Department "
            # Выполнить команду запроса (Execute Query).
            cursor.execute(sql)
            print("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                print(row)
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

articles()

