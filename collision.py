import pandas as pd
from collections import Counter

data=pd.read_csv("/Users/patel/OneDrive/Desktop/Project/Toronto Fatal-Collision Analysis/Fatal_Collisions.csv")

data.head(5)
data.info()
data.dtypes
data.columns # write down just the column names of dataset

data.YEAR=data.YEAR.astype(str) # changineg Column Data types
data.TIME=data.TIME.astype(str) # changineg Column Data types
data.dtypes

#Data Cleaning
#Removing property Damage
print("Number of rows: ", len(data))    
data = data[data['ACCLASS'] != 'Property Damage Only']
print("Number of rows after cleaning: ", len(data))  # There is no Non-Fatal Data, for ex:Property Damanage

data.isnull().sum() # No of Nan values 
data_clean=data.drop(columns=['TRSN_CITY_VEH','Ward_ID','Ward_Name','Hood_Name']) # Dropping Columns with Null Values
data_clean.isnull().sum()

description_district=data_clean.iloc[:,12] # Fetching column : with description
description_district.head()
len(description_district.unique().tolist() # No of categories , unique values in violation desctiption

# most_common() produces k frequently encountered 
from collections import Counter
Counter = Counter(description_district) 
n=10
most_occur_district = Counter.most_common(6) #[:-n-1:-1] uncomment this if you want to get least common items
print(most_occur_district) 

description_impacttype=data_clean.iloc[:,22]
description_impacttype.head()
len(description_impacttype.unique().tolist())

from collections import Counter
Counter = Counter(description_impacttype)
n=15
most_occur_impact=Counter.most_common(15)
print(most_occur_impact)

# Step 3: As we have latitude's and longitude we can plot on a toronto map to analyze the common areas where violations were found.
# You will need to get mapbox api token no and use that api. 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data=pd.read_csv("/Users/patel/OneDrive/Desktop/Project/Toronto Fatal-Collision Analysis/Fatal_Collisions.csv")

mapbox_access_token = "pk.eyJ1IjoicGF0ZWwtbmlzYXJnIiwiYSI6ImNrMWt2N3ZmZjAwNWozbHBiMzAwMXhzZ2EifQ.dsTHS-J086ftWR4BBhbsUQ"

fig = go.Figure(go.Scattermapbox(

        lat=data.iloc[:,13].values.tolist(),
        lon=data.iloc[:,14].values.tolist(),
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=10
        ),
        text="Street: "+data.iloc[:,8]+ '<br>' +"District: "+data.iloc[:,12]+ '<br>' +"Light: "+data.iloc[:,19]+ '<br>' +"Impact Type: "+data.iloc[:,22]+ '<br>' +"Injury: "+data.iloc[:,25]+ '<br>' +"Date: "+data.iloc[:,5]

    ))

fig.update_layout(
    #autosize=True,

    hovermode='closest',
    mapbox=go.layout.Mapbox(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=43.6532, # Toronto Coordinates
            lon=-79.3832
        ),
        pitch=0,
        zoom=11
    )
)

fig.show() 
# This will open a browser and display a map !