import pandas as pd
import csv

DATA_BRIXO = pd.ExcelFile("for_xlsx.xlsx")


def articles():
    brixo = pd.read_excel(DATA_BRIXO)
    nibk = pd.read_csv("articles.csv",  sep=";")
    brixo.rename(columns={'OEM номер': 'oem_num', 'Номер ': 'number'}, inplace=True)
    res_df = brixo.merge(nibk, left_on=["oem_num"], right_on=["ART_NUM"])
    res_df["ART_ID"] = "1111#" + res_df["number"]
    res_df = res_df[["ART_ID", "number", "GEN_ART_NO", "SUP_NAME", "Assembly_Group", "Generic_Article", "ATTRIBUTES"]]
    res_df.rename(columns={'number': 'ART_NUM'}, inplace=True)
    res_df = pd.concat([nibk, res_df])
    res_df.to_csv("test.csv", sep=";", index=False, encoding='utf-8', quoting=csv.QUOTE_NONE)


def exp_articles_oem():
    brixo = pd.read_excel(DATA_BRIXO)
    nibk = pd.read_csv("articles_oem.csv", sep=";")
    brixo.rename(columns={'OEM номер': 'oem_num', 'Номер ': 'number'}, inplace=True)
    nibk['ART_ID'] = nibk['ART_ID'].str[5:]
    res_df = brixo.merge(nibk, left_on=["oem_num"], right_on=["ART_ID"])
    res_df["ART_ID"] = "1111#" + res_df["number"]
    res_df = res_df[["ART_ID", "OEM_BRAND", "OEM_COMPETITOR", "OEM_NUM", "REPLACE"]]
    res_df = pd.concat([nibk, res_df])
    res_df.to_csv("articles_oem.csv", sep=";", index=False, encoding='utf-8', quoting=csv.QUOTE_NONE)


def article_vehicle_links():
    brixo = pd.read_excel(DATA_BRIXO)
    nibk = pd.read_csv("article_vehicle_links.csv", sep=";")
    brixo.rename(columns={'OEM номер': 'oem_num', 'Номер ': 'number'}, inplace=True)
    res_df = brixo.merge(nibk, left_on=["oem_num"], right_on=["ART_NUM"])
    res_df["ART_ID"] = "1111#" + res_df["number"]
    res_df = res_df[["ART_ID", "VEH_TYPE_NO", "number", "CRITERIAS"]]
    res_df.rename(columns={'number': 'ART_NUM'}, inplace=True)
    res_df = pd.concat([nibk, res_df])
    res_df.to_csv("article_vehicle_links.csv", sep=";", index=False, encoding='utf-8', quoting=csv.QUOTE_NONE)


articles()
exp_articles_oem()
article_vehicle_links()