import pandas as pd
import os

def convert_to_bits(row):
    if 'K' in row:
        return float(row[:row.find('K')]) * 1024 * 8
    elif 'M' in row:
        return float(row[:row.find('M')]) * 1024**2 * 8
def create_dataframe(file):
    rows=[]
    with open(file) as f:
        for line in f:
            rows.append(line.split(']'))
    rows = rows[1:299]

    data = []
    datarate = []

    for i in range(len(rows)):
        data.append(rows[i][1].split('s')[1][2:])
        datarate.append(rows[i][1].split('s')[2])
    df = pd.DataFrame({'data':data, 'datarate':datarate})
    for col in df.columns:
        df[col] = df[col].apply(convert_to_bits)

    return df


def find_all_files(directory, ending):
    files_listed = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(f'.{ending}'):
                
                files_listed.append( os.path.join(root, file))
    return files_listed

if __name__ == '__main__':

    path = os.getcwd()

    for file in find_all_files(path, 'txt'):
        create_dataframe(file).to_csv(file[:-4] + '.csv')