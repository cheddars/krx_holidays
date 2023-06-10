import os
import pandas as pd
from json import loads, dumps


files = os.listdir(".")

dfs = pd.DataFrame()
for file in files:
    if file.endswith(".xls"):
        df = pd.read_excel(file)
        dfs = pd.concat([dfs, df])

dfs.columns = ["date", "week_name", "desc"]
dfs["date"] = dfs["date"].str.strip()
dfs["week_name"] = dfs["week_name"].str.strip()
dfs["desc"] = dfs["desc"].str.strip()
dfs["is_holiday"] = True
dfs.sort_values(by=["date"], inplace=True)

result = dfs.to_json(orient="records")
parsed = loads(result)
codes = dumps(parsed, indent=None, ensure_ascii=False)
codes = codes.replace("},", "},\n        ").replace("true", "True")


with open("../krxholidays/data.py", "w") as f:
    f.write(f"holidays = {codes}")