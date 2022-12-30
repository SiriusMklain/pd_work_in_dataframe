import pandas as pd
import csv
import os
import pathlib
import configparser

THIS_PATH = pathlib.Path(__file__).parent


CSV_FOLDER_PATH = os.path.join(THIS_PATH, "csv")
DIR_SRC = os.path.join(THIS_PATH, "sure_filter", "xlsx_pics")

DATA_BRIXO = pd.ExcelFile(os.path.join(THIS_PATH, "sure_filter", "for_xlsx.xlsx"))


def articles():
    brixo = pd.read_excel(DATA_BRIXO)
    nibk = pd.read_csv(os.path.join(THIS_PATH, "csv", "articles.csv"), sep=";")
    brixo.rename(columns={'OEM номер': 'oem_num', 'Номер ': 'number'}, inplace=True)
    res_df = brixo.merge(nibk, left_on=["oem_num"], right_on=["ART_NUM"])
    res_df["ART_ID"] = "1111#" + res_df["number"]
    res_df["SUP_NAME"] = "BRIXO"
    res_df = res_df[["ART_ID", "number", "GEN_ART_NO", "SUP_NAME", "Assembly_Group", "Generic_Article", "ATTRIBUTES"]]
    res_df.rename(columns={'number': 'ART_NUM'}, inplace=True)
    res_df = pd.concat([nibk, res_df])
    res_df.to_csv(os.path.join(THIS_PATH, "csv", "test_articles.csv"), sep=";", index=False, encoding='utf-8',
                  quoting=csv.QUOTE_NONE)


def exp_articles_oem():
    brixo = pd.read_excel(DATA_BRIXO)
    nibk = pd.read_csv(os.path.join(THIS_PATH, "csv", "articles_oem.csv"), sep=";")
    nibk = nibk.astype({"REPLACE": "Int64"})
    brixo.rename(columns={'OEM номер': 'oem_num', 'Номер ': 'number', 'Производитель': 'oem'}, inplace=True)
    id_art = nibk['ART_ID'].str[5:]
    res_df = brixo.merge(nibk, left_on=["oem_num"], right_on=id_art)
    res_df["ART_ID"] = "1111#" + res_df["number"]
    res_df = res_df[["ART_ID", "OEM_BRAND", "OEM_COMPETITOR", "OEM_NUM", "REPLACE"]]
    oem_nibk = nibk.merge(brixo, left_on=id_art, right_on=["oem_num"])
    oem_nibk = oem_nibk[["ART_ID", "oem", "OEM_COMPETITOR", "number", "REPLACE"]].drop_duplicates(subset=['ART_ID', 'number'])
    oem_nibk.rename(columns={'oem': 'OEM_BRAND', 'number': 'OEM_NUM'}, inplace=True)
    oem_brixo = oem_nibk[["ART_ID", "OEM_BRAND", "OEM_COMPETITOR", "OEM_NUM", "REPLACE"]]
    oem_brixo["ART_ID"] = '1111#' + oem_nibk['OEM_NUM']
    res_df = pd.concat([nibk, res_df, oem_nibk, oem_brixo])
    res_df.to_csv(os.path.join(THIS_PATH, "csv", "test_articles_oem.csv"), sep=";", index=False, encoding='utf-8',
                  quoting=csv.QUOTE_NONE)


def article_vehicle_links():
    brixo = pd.read_excel(DATA_BRIXO)
    nibk = pd.read_csv(os.path.join(THIS_PATH, "csv", "article_vehicle_links.csv"), sep=";")
    brixo.rename(columns={'OEM номер': 'oem_num', 'Номер ': 'number'}, inplace=True)
    res_df = brixo.merge(nibk, left_on=["oem_num"], right_on=["ART_NUM"])
    res_df["ART_ID"] = "1111#" + res_df["number"]
    res_df = res_df[["ART_ID", "VEH_TYPE_NO", "number", "CRITERIAS"]]
    res_df.rename(columns={'number': 'ART_NUM'}, inplace=True)
    res_df = pd.concat([nibk, res_df])
    res_df.to_csv(os.path.join(THIS_PATH, "csv", "test_article_vehicle_links.csv"), sep=";", index=False, encoding='utf-8',
                  quoting=csv.QUOTE_NONE)


def files_art():
    brixo = pd.read_excel(DATA_BRIXO)
    nibk = pd.read_csv(os.path.join(THIS_PATH, "csv", "article_files.csv"), sep=";")
    brixo.rename(columns={'OEM номер': 'oem_num', 'Номер ': 'number'}, inplace=True)
    res_df = brixo
    res_df["ART_ID"] = "1111#" + res_df["number"]
    res_df["FILE_NAME"] = "brixo.png"
    res_df["FILE_ORDER"] = "1"
    res_df = res_df[["ART_ID", "FILE_NAME", "FILE_ORDER"]]
    res_df = pd.concat([nibk, res_df])
    res_df.to_csv(os.path.join(THIS_PATH, "csv", "test_article_files.csv"), sep=";", index=False, encoding='utf-8',
                  quoting=csv.QUOTE_NONE)


# articles()
exp_articles_oem()
# article_vehicle_links()
# files_art()
