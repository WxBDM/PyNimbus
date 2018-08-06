import csv
import requests
import pandas as pd

def make_dataframes(data, start_index, end_index):
    '''This makes the dataframe for each SPC report.
    First we have to figure out where each data[i] == 'Time'. This should
    be done beforehand. Once we do that, we can read in our start_index and
    end_index.
    
    Inputs:
        data: LIST -> listception... Should be achieved using csv.reader()
        start_index: INT -> where the loop should begin (+1 in the code
            because we don't want to have the column names in the dataset.
        end_index: INT -> The same as start_index but where the loop should end.
    
    Returns:
        df: PANDAS DATAFRAME -> dataframe of the information.'''
        
    if end_index == start_index + 1:
        df = pd.DataFrame([0] * len(data[start_index]), data[start_index]).T
        return df
    else:
        lists = [data[i] for i in range(start_index + 1, end_index)]
        df = pd.DataFrame(lists, columns = data[start_index])
        return df

# we need to download our data locally without downloading the file directly.
CSV_URL = 'http://www.spc.noaa.gov/climo/reports/today_filtered.csv'
with requests.Session() as s:
    download = s.get(CSV_URL)
    try:
        decoded_content = download.content.decode('utf-8')
    except:
        decoded_content = download.content.decode("latin-1")
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)

# the loop to spit back the indexes where the first element is 'time',
# thus making a new dataframe.
index = [i for i in range(len(my_list)) if my_list[i][0] == 'Time']
index.append(len(my_list))

#make the dataframes for each of the hazards in the csv file.
tor_df = make_dataframes(my_list, index[0], index[1])
win_df = make_dataframes(my_list, index[1], index[2])
hail_df = make_dataframes(my_list, index[2], index[3])
