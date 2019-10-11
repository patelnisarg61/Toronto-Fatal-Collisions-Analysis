# Toronto-Fatal-Collisions-Analysis
Pandas, Plotly, Scattermapbox

Open Source Data: http://data.torontopolice.on.ca/datasets/fatal-collisions

The Traffic Collision Fatalities dataset provides a summary of all traffic related collisions that resulted in a fatality in the last 10 Years.This project will analyze all indicated collisions where fatal injuries have been reported. This dataset only includes 'Closed' Cases indicating that the inspection process has ended.

## Column	Description: 

      Index(['X', 'Y', 'Index_', 'ACCNUM', 'YEAR', 'DATE', 'TIME', 'Hour', 'STREET1',
       'STREET2', 'OFFSET', 'ROAD_CLASS', 'District', 'LATITUDE', 'LONGITUDE',
       'LOCCOORD', 'ACCLOC', 'TRAFFCTL', 'VISIBILITY', 'LIGHT', 'RDSFCOND',
       'ACCLASS', 'IMPACTYPE', 'INVTYPE', 'INVAGE', 'INJURY', 'FATAL_NO',
       'INITDIR', 'VEHTYPE', 'MANOEUVER', 'DRIVACT', 'DRIVCOND', 'PEDTYPE',
       'PEDACT', 'PEDCOND', 'CYCLISTYPE', 'CYCACT', 'CYCCOND', 'PEDESTRIAN',
       'CYCLIST', 'AUTOMOBILE', 'MOTORCYCLE', 'TRUCK', 'TRSN_CITY_VEH',
       'EMERG_VEH', 'PASSENGER', 'SPEEDING', 'AG_DRIV', 'REDLIGHT', 'ALCOHOL',
       'DISABILITY', 'Division', 'Ward_Name', 'Ward_ID', 'Hood_ID',
       'Hood_Name', 'ObjectId'],
      dtype='object')
      
###Problem Case 1: Most Common Districts where Fatal Colission have occured

[('Toronto and East York', 182), ('Scarborough', 173), ('Etobicoke York', 130), ('North York', 123), (' ', 1), ('Toronto East York', 1)]

###Problem Case 2: Most occured Fatal Collisons Impact Type

[('Pedestrian Collisions', 355), ('SMV Other', 83), ('Turning Movement', 55), ('Cyclist Collisions', 30), ('Approaching', 30), ('Angle', 22), ('Rear End', 18), ('SMV Unattended Vehicle', 6), ('Other', 6), ('Sideswipe', 5)]

###Problem Case 3: Analysis of dataset using scattermapbox and pandas in python to get 
                1. Street
                2. District
                3. Impact Type
                4. Light
                5. Injury Type
                6. Fatal

<img src="https://github.com/patelnisarg61/Toronto-Fatal-Collision-Analysis/blob/master/Fatal-Collision-Plot.PNG" width="800" height="500" style="vertical-align:center;">
