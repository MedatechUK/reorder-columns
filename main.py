import os, shutil
import pandas as pd

def handle_files():
    input_dir = os.fsencode('Input')

    for file in os.listdir(input_dir):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            reorder_columns(os.path.join('Input', filename))
            path_to_current_file = os.path.join('Input', filename)
            path_to_new_file = os.path.join('Output', filename)
            shutil.move(path_to_current_file, path_to_new_file)

def reorder_columns(path):
    df = pd.read_csv(path, delimiter=';')
    df["e"] = ''
    df['Seller Brand Name'] = df['Seller Brand Name'].str.upper()
    df_reorder = df[['Seller MFPN','PDI  Item Product Description','e','e','e','e','e','e','e','e','e','e','e','Seller Brand Name','e','e','e','e','PDI UNSPSC Code','PDI OT Classification Code','Seller Item EAN']] # rearrange column here
    df_reorder.to_csv(path, header=None, index=False, sep="\t")
    
handle_files()

