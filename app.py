# Dependencies
import pandas as pd
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float 

# importing cleaned measurments data 
data_file = "combo_data.csv"
# Read CSV file into a pandas DataFrame
crime_health_df= pd.read_csv(data_file, dtype=object)

#crime_health_df.head()

# Create an engine to a SQLite database file called `hawaii.sqlite`
engine = create_engine("sqlite:///crime_health.sqlite")

# Create a connection to the engine called `conn`
conn = engine.connect()

#creating the measurments and stations tables
Base = declarative_base()

#creating the sql table
crime_health_df.to_sql("crime_ph",conn, if_exists='fail', index=False) 

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def index():
    """Render Home Page."""
    return render_template('index.html')