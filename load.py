from sqlalchemy import create_engine
import os
import pandas as pd

def main():
    path = "data"
    print(os.listdir(path))
    engine = create_engine("postgresql://postgres:password@localhost:5432/postgres")
    
    for file in os.listdir(path):
        full_path =  f"{path}/{file}" # path + "/" + file
        
        df = pd.read_csv(full_path)
        table_name = file.split(".")[0]
        table_name = table_name.replace("-","_")
    
        df.to_sql(table_name, engine, if_exists="replace")




if __name__ == "__main__":
    main()