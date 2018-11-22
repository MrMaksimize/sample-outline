## Beginner Data Engineering / ETL Basics

* Things that should be covered
* Extract from multiple sources
* Reshaping data (creating fact tables)
* Large vs tall data
* Merging multiple data sources
* Working with messy data
* Writing multiple outputs (multiple reports)
* Loading data to S3

* Creating cron jobs?
* Introduction to AF?

The story:

Sam works for the City of San Diego.  
Every day, she needs to report to each of the 9 council districts how many get it done requests are open by type, and how long they have been open for.  

* Pull csv in
* Clean it up
* Geocode it
* spatial join it
* Aggregate by day
* Output
* Upload
* Email
* Schedule

At the end, the student will be able to create a data pipeline that loads a dataset, cleans it, adds an additional data source, and outputs reports and star-schema ready tables.  

The Set UP (Assumptions)

* GID data is stored in a SQL database, as a prod type schema.
* The data comes out raw on query, but it's not normalized in the db.  SO what can happen is you have manual entry fields for things that should be categorical (eg - case type)
* There are lookup tables for case type, etc - they're in separate csv files.
* Data output needs to be tested / validated. 
* Error reports sent to GiD team. 
* Data needs to be loaded in as star schemas to the database.  
* Council district agg reports need to be sent to the districts



## Chapter 1 - Setting Up PythonFire
  * Lesson 1.1 - Introduction to Python Fire
    * A learning objective: Create a basic PythonFire script that we can run from the command line.
  * Lesson 1.2 - 
    * A learning objective:  Tweak the PythonFire script to add interactivity and visibility.
  * Lesson 1.3 - 
    * A learning objective:  Create a shell for your data pipeline, make sure it runs, and accepts and uses the right variables and parameters.  Make sure the documentation works too.

----- IDEA - load data from db, load csv, + geocode over ws
----- IDEA -- reshape data somewhere here?

## Chapter 2 - 
  * Lesson 2.1 - 
    * A learning objective:  Load and clean the GetItDone dataset using the variables provided in the script.  Pull it from SQL, with a SQL template (facts).
  * Lesson 2.2 - 
    * Objectives: Load and clean referential data. Join it with GID 
  * Lesson 2.3 -
    * A learning objective:  Use a webservice to enrich your data (geocoding)
  * Lesson 2.4 - 
    * A learning objective:  Use the new geocoded data to join an additional reference file - council district
  

----- IDEA -- reshape data somewhere here?

## Chapter 3 -

  * Lesson 3.1 
    * Objectives: Validate your dataset; Get failure output for GID team.  
  * Lesson 2.4 - 
    * A learning objective:  Upload new facts table to db (and explain why we dont load ref tables here).  Upload failures to another facts table.  Write CSVs.
  * Lesson 3.3 - 
    * A learning objective:  Query the star schema (OR csv - tbd);  Generate reports.
  * Lesson 3.4 - 
    * A learning objective:  Query the CSV output directly (if you had no db to write to);  Generate reports;

## Chapter 4 - 
  * Lesson 4.1
    * A learning objective:  Learn how to send emails and alerts with reports, or when conditions are met.
  * Lesson 4.2 
    * A learning objective:  Schedule and run your pipeline!
  * Lesson 4.5 
    * A learning objective:  Build your own pipeline to geocode GID Requests for a police district, and email them to the captain!



## Chapter 1 - Setting Up Interactive Web Maps
   * Lesson 1.1 - Introduction to leaflet
     * A learning objective: Create a basic interactive web map in R using the `leaflet` and `htmlwidgets` packages.
   * Lesson 1.2 - Working with Map tiles
     * A learning objective: Tweak the base map in `leaflet` using provider tiles, such as those on [OpenStreetMap](https://www.openstreetmap.org/)
   * Lesson 1.3 - Setting the Default Map View
     * A learning objective: Create a default map by centering on a certain location, setting a default zoom level, and adding markers or pins to your map.
## Chapter 2 - Plotting Points
   * Lesson 2.1 - Introduction to IPEDS Data
     * A learning objective: Create a map step-by-step to gain a better understanding of how your data will dictate the map you create.
   * Lesson 2.2 - Mapping California Colleges
     * A learning objective: Pan and plot a point on a map using the IPEDS case study.
   * Lesson 2.3 - Labels and Pop-ups
     * A learning objective: Center, zoom in, and plot points on the IPEDS map.
   * Lesson 2.4 - Color Coding Colleges
     * A learning objective: Enhance the appearance of the IPEDS map by changing the color palette of the markers and adding a map legend.
## Chapter 3 - Groups, Layers, and Extras
   * Lesson 3.1 - The Leaflet Extras Package
     * A learning objective: Add search capabilities to your map! Find a location by typing it in a search bar, plus find the name of a location by clicking on a point in your map.
   * Lesson 3.2 - Overlay Groups
     * A learning objective: Clarify how your data is distributed by adding toggles to group data on your map.
   * Lesson 3.3 - Base Groups
     * A learning objective: Give your user control over their view by adding toggles between base maps.
   * Lesson 3.4 - Pieces of Flair
     * A learning objective: Create an advanced and searchable map using special features like clustering.
## Chapter 4 - Plotting Polygons
   * Lesson 4.1 - Spatial Data
     * A learning objective: Define your map boundaries by performing a spatial join.
   * Lesson 4.2 - Mapping Polygons
     * A learning objective: Perform exploratory data analysis using polygons to examine data missingness.
   * Lesson 4.3 - Putting it All Together
     * A learning objective: Use interactive web maps to explore and understand the properties of data.

