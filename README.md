# Storm Prediction Center Storm Reports to Pandas Dataframe
This reads in the SPC storm reports .csv file (found here: https://www.spc.noaa.gov/climo/reports/today.html) and then seperates into 3 pandas dataframes based upon the hazard.

# Important Announcement  
8/24/19 - I will be making this into a package and publishing it to PyPi. This will enable you to easily install it on your machine using `pip`. In addition, there will be more functionality with this project, such as (but not limited to) returning SPC outlook and NHC outlook polygons.  
If you wish to contribute to this project, please get in contact with me via Twitter: @WxBDM (preliminary; until I figure out how to manage pull requests, etc). I will also be tweeting out updates on an as-needed basis.  
See change log at bottom of this README file. More information to follow at a later time.  

# Accessing the individual dataframes
```
a = StormReports("url_or_path.csv")
a.tornado # gives the tornado dataframe
a.hail # gives the hail dataframe
a.wind # gives the wind dataframe
```

# Outputs
If there are no reports for that day, the dataframe will look as such:
```   
   Time  F_Scale  Location  County  State  Lat  Lon  Comments
0     0        0         0       0      0    0    0         0
```

If there are reports for that day, a dataframe would look as such (in this example, hail):
```
    Time Size                 Location         County State    Lat      Lon  \
0   1850  100     1 W LIBRARY JUNCTION     WASHINGTON    PA  40.29   -80.07   
1   2120  100           3 SW BUTTERNUT          PRICE    WI  45.98   -90.54   
2   2146  125                1 N PEETZ          LOGAN    CO  40.98  -103.11   
3   2200  100                   NISULA       HOUGHTON    MI  46.76   -88.79   
4   2202  100                 CHASSELL       HOUGHTON    MI  47.03   -88.53   
5   2208  175  12 ESE CRESCENT LAKE NW         GARDEN    NE  41.65  -102.21   
6   2241  175               5 NW CROOK          LOGAN    CO  40.91  -102.87   
7   2305  100                   FARLEY        DUBUQUE    IA  42.44   -91.01   
8   2330  125            6 WSW LORENZO       CHEYENNE    NE     41  -103.15   
9   0101  100       1 SW GRUNDY CENTER         GRUNDY    IA  42.36   -92.78   
10  0205  100              4 SE OGLALA  OGLALA LAKOTA    SD  43.14  -102.68   
11  0210  100           6 N NORTH BEND          DODGE    NE  41.55   -96.76   
12  0238  275            2 SSW FLEMING          LOGAN    CO  40.65  -102.85   

                                             Comments  
0      QUARTER SIZE HAIL ON SPRINGBROOKE DRIVE. (PBZ)  
1   CORRECTS PREVIOUS HAIL REPORT FROM 3 SW BUTTER...  
2                                               (BOU)  
3                                               (MQT)  
4   PHOTO RECEIVED ON SOCIAL MEDIA. TIME ESTIMATED...  
5   HAIL RANGING IN SIZE FROM MARBLES TO GOLF BALL...  
6                                               (BOU)  
7                     REPORT RELAYED FROM KCRG. (DVN)  
8   A LOT OF HAIL FELL FAST... WITH THE LARGEST ST...  
9   MOSTLY PEA TO NICKEL SIZED BUT A FEW STONES AS...  
10                                              (UNR)  
11                                              (OAX)  
12                                              (BOU)
```


## Change Log
8/24 - See Important Announcement above  
8/28 - Renamed from SPC Storm Reports to PyNimbus to better reflect the purpose of the package  
