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
    res_df = res_df[["ART_ID", "number", "GEN_ART_NO", "SUP_NAME", "Assembly_Group", "Generic_Article", "ATTRIBUTES"]]
    res_df.rename(columns={'number': 'ART_NUM'}, inplace=True)
    res_df = pd.concat([nibk, res_df])
    res_df.to_csv(os.path.join(THIS_PATH, "csv", "articles.csv"), sep=";", index=False, encoding='utf-8',
                  quoting=csv.QUOTE_NONE)


def exp_articles_oem():
    brixo = pd.read_excel(DATA_BRIXO)
    nibk = pd.read_csv(os.path.join(THIS_PATH, "csv", "articles_oem.csv"), sep=";")
    brixo.rename(columns={'OEM номер': 'oem_num', 'Номер ': 'number'}, inplace=True)
    id_art = nibk['ART_ID']
    id_art = nibk['ART_ID'].str[5:]
    res_df = brixo.merge(nibk, left_on=["oem_num"], right_on=id_art)
    res_df["ART_ID"] = "1111#" + res_df["number"]
    res_df = res_df[["ART_ID", "OEM_BRAND", "OEM_COMPETITOR", "OEM_NUM", "REPLACE"]]
    res_df = pd.concat([nibk, res_df])
    res_df.to_csv(os.path.join(THIS_PATH, "csv", "articles_oem.csv"), sep=";", index=False, encoding='utf-8',
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
    res_df.to_csv(os.path.join(THIS_PATH, "csv", "article_vehicle_links.csv"), sep=";", index=False, encoding='utf-8',
                  quoting=csv.QUOTE_NONE)


def files_art():
    brixo = pd.read_excel(DATA_BRIXO)
    brixo.rename(columns={'OEM номер': 'oem_num', 'Номер ': 'number'}, inplace=True)
    res_df = brixo
    res_df["ART_ID"] = "1111#" + res_df["number"]
    res_df["image"] = "brixo.png"
    res_df["i"] = "1"
    res_df = res_df[["ART_ID", "image", "i"]]
    res_df.to_csv(os.path.join(THIS_PATH, "csv", "article_files.csv"), sep=";", index=False, encoding='utf-8',
                  quoting=csv.QUOTE_NONE, header=None)


articles()
exp_articles_oem()
article_vehicle_links()
files_art()
