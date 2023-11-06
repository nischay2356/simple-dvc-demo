#reading the data a from data src
#sve it in the /raw for further process
import os

from get_data import read_param,get_data
import argparse

def load_and_save(config_path):
    config = read_param(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ","_") for col in df.columns]
    raw_data_path = config['load_data']['raw_dataset_csv']
    df.to_csv(raw_data_path,sep=',',index = False,header = new_cols) #index = false means it does not create a new index columns in df
    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument('--config',default = 'params.yaml')
    parsed_args = args.parse_args()
    data = load_and_save(config_path=parsed_args.config)
