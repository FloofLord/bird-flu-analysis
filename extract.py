import pandas as pd
import os

def main():
    links =  ["https://www.aphis.usda.gov/csv-data/hpai-wild-birds-ver2.csv",
              "https://www.aphis.usda.gov/csv-data/hpai-mammals.csv"]
    
    if "data" not in os.listdir():
        os.mkdir("data")


    for link in links:
        df = pd.read_csv(link)
        #print(df.head())
        filename = link.rsplit("/",1)[1].split(".")[0]

        df.to_csv(f"data/{filename}.csv", index=False)


if __name__ == "__main__":
    main()



