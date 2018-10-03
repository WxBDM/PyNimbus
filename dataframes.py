import csv
import requests
import pandas as pd

class StormReports:
    
    def __init__(self, url):
        try:
            # try pandas. Sometimes SSL sslv3 alert handshake failure will pop up.
            # if using url
            df = pd.read_csv(url)
            self.all = df
            self.tornado = self._make_dataframes_from_pandas(df, 'tor')
            self.wind = self._make_dataframes_from_pandas(df, 'win')
            self.hail = self._make_dataframes_from_pandas(df, 'hail') 
        except:
            # if it for some reason throws an error, use requests.
            with requests.Session() as s:
                download = s.get(url)
                try:
                    decoded_content = download.content.decode('utf-8')
                except:
                    decoded_content = download.content.decode("latin-1")
                cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                reports_in_list = list(cr)
            
            # the loop to spit back the indexes where the first element is 'time',
            # thus making a new dataframe.
            index = [i for i in range(len(reports_in_list)) if reports_in_list[i][0] == 'Time']
            index.append(len(reports_in_list))
            
            self.all = self._make_dataframes_from_requests(reports_in_list, 
                index[0], index[3])
            self.tornado = self._make_dataframes_from_requests(reports_in_list, 
                        index[0], index[1])
            self.wind = self._make_dataframes_from_requests(reports_in_list,
                        index[1], index[2])
            self.hail = self._make_dataframes_from_requests(reports_in_list,
                        index[2], index[3])

    def _make_dataframes_from_pandas(self, df, start_index, end_index, type_df):
        '''makes the dataframes from pandas reading in csv file (or url)'''
        # grabs the index where the next report begins
        findIndex = df['Time'].tolist()
        index = [i for i in range(len(findIndex)) if findIndex[i] == 'Time']
        index.append(len(findIndex))
        
        # split the reports based upon hazard.
        if type_df == 'tor':
            df2 = df.drop(index = range(index[0], index[2]))
            return df2
        elif type_df == 'win':
            df2 = df.drop(index = range(0, index[0]))
            df2 = df2.drop(index = range(index[1], index[2]))
            newCols = df2.iloc[0].tolist()
            df2 = self._rename_columns(df2, newCols, index[0])
            return df2
        elif type_df == 'hail':
            df2 = df.drop(index = range(0, index[2]))
            newCols = df2.iloc[0].tolist()
            df2 = self._rename_columns(df2, newCols, index[0])
            return df2
        
    def _rename_columns(self, df, rename, index_of_first_row):
        ''' renames the columns in the pandas dataframe'''
        newCols = df.iloc[0].tolist()
        df.drop(index = index_of_first_row)
        
        # dictionary to rename
        d = {}
        for i, oldName in enumerate(list(df)):
            d[oldName] = newCols[i]
        
        df.rename(columns = d)
        return df
        

    def _make_dataframes_from_requests(self, data, start_index, end_index):
        '''If using requests, 
            df: PANDAS DATAFRAME -> dataframe of the information.'''
        
        # if there's more than 8 columns, delete the ones that have no data.
        for i in range(len(data)):
            if len(data[i]) > 8:
                data[i][7:] = [''.join(data[i][7:])]
        
        # construct pandas dataframes and return them.
        if end_index == start_index + 1:
            df = pd.DataFrame([0] * len(data[start_index]), data[start_index]).T
            return df
        else:
            lists = [data[i] for i in range(start_index + 1, end_index)]
            df = pd.DataFrame(lists, columns = data[start_index])
            return df
