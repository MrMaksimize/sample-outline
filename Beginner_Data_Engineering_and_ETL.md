# Beginner Data Engineering / ETL Basics

#### What problems will students learn how to solve? (DC Question)

***Identify the specific real-world problems will students be able to solve by the end of this course.***


The student will learn how to create a data pipeline that pulls data from multiple sources, combines it, enriches it and pushes it into a database.  Then another pipeline for generating reports from this database.



***Identify at least 3 problems that students will learn to solve using materials they will learn across the 4-5 chapters of your course. You will be expected to expand on this at a later stage in the course development process.***

* Design and build a data pipeline
* Enrich data by combining multiple sources
* Create a repeatable, stable pipeline for moving data into a warehouse.
* Create a repeatable, stable pipeline for using the warehouse to generate and send a report to multiple stakeholders.
* Test data quality during ETL process.

#### What techniques or concepts will students learn? (DC Question)

Break down the specific concepts, methods, and techniques that students will learn in the chapters (and lessons) of your course. 

* Designing and building a data pipeline
  * Implementing Python Fire and using position arguments as parameters
  * Scheduling jobs
  * Job dependencies
  * Pulling data from multiple sources
  * Iterating over a dataframe and enriching from an API. 
  * Creating and testing dynamic ETLs.
  * Handling ETL errors
  * Working with real-world messy data.
* ETL best practices
  * Loading data incrementally
  * Thinking through job dependencies
  * Validating data quality
  * Ensuring idempotency
  * Parametrizing workflows
  * Shaping data for analytics



#### Things to Cover (MP Planning)
At the end, the student will be able to:
  * Pull data in from different sources
  * Reshape the data to fit a star schema model for database
  * Merge multiple data sources
  * Use a web service for data enrichment
  * Write a SQL template
  * Set up a cron job
  * KNow how to handle ETL errors
  * Send reports / alerts.
  * Validate messy data.
  * Clean messy data


#### Assumptions (MP Planning)
  * GID data is stored in a SQL database, as a prod type schema.
  * The data comes out raw on query, but it's not normalized in the db.  SO what can happen is you have manual entry fields for things that should be categorical (eg - case type)
  * There are lookup tables for case type, etc - they're in separate csv files.
  * Data output needs to be tested / validated. 
  * Error reports sent to GiD team. 
  * Data needs to be loaded in as star schemas to the database.  
  * Council district agg reports need to be sent to the districts
  * I have access to download static csv's, geojson (or shapefiles) with geopandas, a fake "prod" sql database, and a fake OLAP SQL database.

#### The Story (MP Planning)

The story:

Sam works for the City of San Diego.  
Every day, she needs to report to each of the 9 council districts how many GetItDone requests have been opened by type.

However, she doesn't want to do this as a one-off task.  She wants to leverage her work for future analysis - because she gets asked for these kinds of things a lot.  So, she's going to create a simple warehouse, and pump GetItDone data in there, letting her answer her questions.  

She also knows sometimes there is data corruption in the Get It Done data because people will sometimes freehand enter a field, and there's no validation on it.  She needs to generate a report on that day's data and send the discrepancies to the GiD team.  



Sam will:
  * Write a shell PythonFire script
  * Load GiD Dataset (fact table) from the database, using a SQL template that takes the date range as a parameter. 
  * Load and clean the dimensional data.  Join it with GID
  * Use a webservice to enrich GiD data (geocoding)
  * Use the geocodes to spatial join on council district

  * Validate the dataset and prepare a dataset of requests that don't conform to the case vocabulary.  
  * Upload facts table to DB;  Generate CSV of failures.
  * Create a new pipeline that will query the star schema to use SQL to pull data per council district.
  * Send an email with failure info; Dispatch emails for council districts

  * Create a pipeline for sending conditional alerts.
  * Schedule and run hjer pipelines;  Deal with errors and failures.
  * Build her own pipeline that tells council districts when businesses opened this quarter.  



#### Questions (MP Planning)
Ideally I'd like to do this in airflow, not Python fire.  But AFAIK DataCamp does not have those capabilities yet.  PythonFire is more approachable and people can start using this without setting up a whole AF framework.  

The only thing to think about is if I should use one of those lighter python frameworks in place of py fire? Bonobo?

Should I not have the learner write to a database first? Go directly to creating a report.  That way she can use variables from the get go.

Should I not go into alerting? Is it too much?

I think part of what will make people get excited about beginning data engineering is a quick way to automate some of the tedious work they have to do with running reports.  That's why I'm not sure about including the SQL writing stuff.


#### Outline (DC Question)

## Chapter 1 - Setting Up PythonFire
  * Lesson 1.1 - Introduction to Python Fire
    * Learning Objective:  Create a basic PythonFire script that takes some parameters through the command line.
  * Lesson 1.2 - Make the PythonFire script interactive.
    * Learning Objective:  Tweak the PythonFire script to add interactivity and logging. Make an API request and handle the response.
  * Lesson 1.3 - Create a shell pipeline
    * Learning Objective:   Create a shell for your data pipeline. Test that it runs, and accepts proper parameters as needed.  


## Chapter 2 - Loading, Transforming and Enriching.
  * Lesson 2.1 - Load and clean the GetItDone dataset.
    * Learning Objective:   Create a SQL template that takes date range as a parameter. Load and clean the GiD Dataset using this SQL template.
  * Lesson 2.2 - Get the reference data and join it!
    * Learning Objective:  Load and clean the reference data about case types for GetItDone. Join it to the get it done dataset.
  * Lesson 2.3 - Enrich your data using a webservice.
    * Learning Objective:   Use the census batch geocoder and an API request to geocode the addresses in GetItDone data.
  * Lesson 2.4 - Perform a spatial join.
    * Learning Objective:  Load a GeoJSON file of council districts. Perform a spatial join using the case's geocoded lat/lng and council districts polygon, using geopandas.
  

## Chapter 3 - Validating, Uploading and Reporting.

  * Lesson 3.1 - Validate the data before putting it into an OLAP database.
    * Learning Objective: Check the data for bad entries.  Make sure that every case has a council district, and data conforms to the case type vocabulary. 
  * Lesson 3.2 - Loading data.
    * Learning Objective:   Upload the new facts table for that day to the database.  Generate a list of requests with improper case; Touch on data partioning.
  * Lesson 3.3 - Write a query for our council district report.
    * Learning Objective:   Write a SQL query that takes a date parameter and pulls aggregates on case counts per council district.
  * Lesson 3.4 - Creating a report.
    * Learning Objective:  Add a task to our pipeline that executes this query and returns a set of CSV files.

## Chapter 4 - Alerting and Scheduling
  * Lesson 4.1 - Determining task flow and dependencies
    * Learning Objective:   Create a flow for your tasks and decide what happens when errors happen.  
  * Lesson 4.2 - Running your pipeline.
    * Learning Objective:   Use a cron scheduler to schedule your pipeline.
  * Lesson 4.3 - Make your own!
    * Learning Objective:   Build your own pipeline, this time taking active businesses, geocoding them, getting the council district, and reporting how many businesses opened in each council district every quarter.  Run it very quarter!


Capstone Exercise:






