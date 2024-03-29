import json
import requests
import pandas as pd


def lambda_handler(event,context):
    print(f"event data-->{event}")
    response = requests.get("https://www.google.com/")
    print(response.text)

    d =  {'col1':[1,2,0] ,'col2':[3,4,5]}
    df = pd.DataFrame(d)
    print(df)
    print("Done.....")
