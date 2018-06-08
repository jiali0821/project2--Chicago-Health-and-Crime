# Dependencies
import pandas as pd
# Python SQL toolkit and Object Relational Mapper
# import sqlalchemy
# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Numeric, Text, Float 

from flask import (
    Flask,
    render_template,
    jsonify)

# importing cleaned measurments data 
data_file = "combo_data.csv"
# Read CSV file into a pandas DataFrame
crime_health_df= pd.read_csv(data_file, dtype=object)

#crime_health_df.head()

# # Create an engine to a SQLite database file called `hawaii.sqlite`
# engine = create_engine("sqlite:///crime_health.sqlite")

# # Create a connection to the engine called `conn`
# conn = engine.connect()

# #creating the measurments and stations tables
# Base = declarative_base()

# #creating the sql table
# crime_health_df.to_sql("crime_ph",conn, if_exists='fail', index=False) 

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def index():
    """Render Home Page."""
    return render_template('index2.html')

@app.route('/tb')
def tb2():
    # tb_different = crime_health_df.copy()
    # tb_different['Crime_Count'] = tb_different['Tuberculosis']

    # tb_grouped = tb_different.groupby(["Community_Area_Name","Tuberculosis"],as_index=False)["Crime_Count"].count()

    # tb_json=tb_grouped.to_json(orient="records")
    # return tb_json

    #grouping TB by community area
    tb_different = crime_health_df.copy()
    tb_different['Crime_Count'] = tb_different['Tuberculosis']

    tb_grouped = tb_different.groupby(["Community_Area_Name","Tuberculosis"],as_index=False)["Crime_Count"].count()

    #grouping stroke by community area
    stroke_different = crime_health_df.copy()
    stroke_different['Crime_Count'] = tb_different['Stroke']

    stroke_grouped = stroke_different.groupby(["Community_Area_Name","Stroke"],as_index=False)["Crime_Count"].count()

    #creating series with only stroke rates for each community area
    stroke=stroke_grouped["Stroke"]

    #grouping preterm births by community area
    Preterm_Births_different = crime_health_df.copy()
    Preterm_Births_different['Crime_Count'] = tb_different['Preterm_Births']

    Preterm_Births_grouped = stroke_different.groupby(["Community_Area_Name","Preterm_Births"],as_index=False)["Crime_Count"].count()

    #creating series with only preterm birth rates for each community area
    Preterm_Births=Preterm_Births_grouped["Preterm_Births"]

    #grouping stroke by percent below poverty level
    Below_Poverty_Level_different = crime_health_df.copy()
    Below_Poverty_Level_different['Crime_Count'] = tb_different['Below_Poverty_Level']

    Below_Poverty_Level_grouped = stroke_different.groupby(["Community_Area_Name","Below_Poverty_Level"],as_index=False)["Crime_Count"].count()

    #creating series with only percent of people below poverty level for each community area
    pl=Below_Poverty_Level_grouped["Below_Poverty_Level"]

    #adding all the series together into one dataframe
    tb_grouped["Stroke"] =stroke
    tb_grouped["Preterm_Births"] =Preterm_Births
    tb_grouped["Below_Poverty"] = pl

    tb_json=tb_grouped.to_json(orient="records")

    return tb_json

# # by Jiali 
@app.route("/crime_area")
def total_crimes():
   # total_crime_df = crime_health_df.groupby([“Community Area Name”])[“ID”].count()
   # JSON_data = total_crime_df.to_json(orient = ‘records’)
   # return JSON_data

   tb_different = crime_health_df.copy()
   tb_different["Crime_Count"] = tb_different["ID"]

   tb_grouped = tb_different.groupby(["Community_Area_Name"],as_index=False)["Crime_Count"].count()

   tb_json=tb_grouped.to_json(orient="records")
   return tb_json

# # by another Jiali 
@app.route("/crime_pie")
def pie_crimes():

   tb_different = crime_health_df.copy()
   tb_grouped = tb_different.groupby(["Community_Area_Name", "Primary_Type"],as_index=False)["ID"].count()
   tb_json=tb_grouped.to_json(orient="records")
   return tb_json

@app.route("/treemap.html")
def treemap():
   """Render Home Page."""
   return render_template('treemap.html')


if __name__ == "__main__":
    app.run(debug=True)
