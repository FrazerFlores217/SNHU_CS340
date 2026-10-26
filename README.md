# SNHU_CS340
This repository is for my CS340 reflection Journal:

**How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?**

When writing programs, I ensure my code is structured in a way other developers can easily follow along with clear naming conventions. The cookie cutter CRUD Python module at the start of this course helped me organize my workflow for both Projects.

**How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?** 

When working with any assignment there is always a sense of anxiety I face knowing there is an unsolved problem that is needing a time-sensitive solution (by the end of each Module). The best thing to do is spending time researching for possible solutions from resources such as useful links for MongoDB and Python giving examples of code structures I can implement into my current assignments.

**What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?** 

I would say our job as computer scientists is to solve a problem(s) and/or improve a task using available resources such as IDE's. The work I completed for Grazioso Salvare's dashboard helps filter and visual animal shelter records without the need to spend wasted time searching through large databases.

This course showed me my strengths and weaknesses as a developer and how important it is to manage your time consuming new ways to improve your coding skills. 

**About the Project/Grazioso Salvare Rescue Dashboard**
The Grazioso Salvare Rescue Dashboard is a Python based web application developed to help identify dogs which may be good candidates for search and rescue training. This application uses animal shelter records from Austin Animal Center stored in a MongoDB database (for this README this will be abbreviated as aac and/or AAC). 
For this project, there are two components: 1) The project uses a Python CRUD module designed to interact with the Austin Animal Center (aac) animal database in MongoDB. It provides reusable functionality for creating/reading/updating/deleting animal records stored in the animal’s collection of the aac database. This was developed using object-oriented programming (OOP) so it can later be imported/used by other Python applications. Also, 2) this project offers an interactive web dashboard to retrieve and display information through an interactive data table, pie chart, and geolocation map.
Users can filter animal records based on rescue categories: Water Rescue, Mountain or Wilderness Rescue, and Disaster or Individual Tracking. A reset option is available for users to return to unfiltered settings.
**The dashboard was developed using the following resources:**
•	Python
•	MongoDB
•	PyMongo
•	Dash
•	Plotly
•	Dash Leaflet

**Motivation**
The purpose of this project is to provide Grazioso Salvare an efficient way to access and analyze animal shelter records to identify dogs suitable for search and rescue training. 
The Python CRUD module provides a reusable way for the Python application to communicate with MongoDB instead of having users interact directly with Mongo shell. The interactive dashboard allows users to view and filter animal records based on rescue categories: Water Rescue, Mountain or Wilderness Rescue, and Disaster or Individual Tracking.
The dashboard includes an interactive data table, pie chart displaying animal breeds, and a geolocation map showing animal locations. Using these features helps to understand available data and pinpoint rescue candidates.
**Getting Started**
Before attempting to run the Grazioso Salvare Rescue Dashboard, the AAC database must be imported into MongoDB using the aac database and animals’ collection. A MongoDB user named “aacuser” must be created with the “readWrite” role for the aac database. Then, the username and password are used by the Python CRUD module to authenticate with MongoDB.
“CRUD_Python_Module.py” file contains “AnimalShelter” class which provides CRUD operations (Create, Read, Update, Delete) to interact with the database. “ProjectTwoDashboard.ipynb” file contains Python code for the interactive dashboard. It imports the “AnimalShelter” class to retrieve animal records from MongoDB and uses the Dash framework to display data.

**Run the dashboard:**
1)	Open the Codio environment and navigate to the code_files directory.
2)	Verify MongoDB is running and the aac database contains the animal shelter records.
3)	Open ProjectTwoDashboard.ipynb in JupyterLab.
4)	Verify MongoDB username and password are configured correctly.
5)	Execute the notebook code to initialize the dashboard.
6)	Open the generated Dash application URL to access the dashboard.
Once the dashboard loads, users can view the animal dataset, apply rescue filters, examine breed distribution pie chart, and select animal records to view their locations.
The reset option will return the dashboard back to its original state.

**Installation**
Ensure the following are installed/available:
Codio – operates JupyterlLab/terminal.
JupyterLab – used to view/edit/run scripts/files.
Python – used to develop CRUD module and dashboard.
MongoDB – stores/manages aac animal records.
**PYTHON LIBRARIES:**
PyMongo – provides connection between Python/MongoDB.
BSON Object library – work with MongoDB object identifiers.
Dash - Framework for developing interactive web dashboard.
JupyterDash – Allows Dash application to run within Jupyter Notebook.
Dash Leaflet – Provides geolocation map used to display animal locations.
Plotly Express – Used to create pie chart displaying animal breeds.
Pandas – Organizes MongoDB records into DataFrames.
NumPy – Provides support for numerical operations.
Matplotlib – Support for plotting library into the dashboard.

**Usage** 
The Grazioso Salvare Rescue Dashboard uses the Python CRUD module to retrieve animal shelter records from MongoDB and display through an interactive web application.
The AnimalShelter class is imported from CRUD_Python_Module.py and instantiated using the MongoDB username and password.

Once connected, the read() method retrieves animal records from the database. The returned records are converted into Pandas DataFrame to use in the dashboard.
The empty dictionary {} retrieves all available records without a filter.

**The dashboard provides four filter options:**
1)	Water Rescue: Displays dogs breed, age, and sex requirements for water rescue training.
2)	Moutain or Wilderness Rescue: Displays dogs matching requirements for mountain or wilderness training.
3)	Disaster or Individual Tracking: Displays dogs matching requirements for Disaster Response or Individual Tracking.
4)	Reset: Removes filters and returns the dashboard to view all the animal dataset.

The dashboard includes three main components for user interactions.

Interactive Data Table: Displays animal records retrieved from MongoDB

Pie Chart: Displays the distribution of the most common animal breeds in the area. 

Geolocation Map: Displays geographic location of selected animal using latitude/longitude coordinates.

**Code Example**
A doc can be inserted into the animals collection using the create() method:

The read() method can locate the record using the animal ID:

The update() method modifies an existing record:

The delete() method can remove a record:

Dashboard Filtering 

**Tests**
Testing was used to verify the Python CRUD Module and Grazioso Salvare Rescue Dashboard functioned as intended. 

**CRUD testing**
The CRUD_Python_Module.py file was tested using Jupyter Notebook to verify Create, Read, Update, and Delete operations worked. The Create test returned TRUE, showing French Bulldog was successfully inserted into MongoDB. The Read test queried for animal ID “A123456” which confirmed the module can successfully retrieve new records. The update test changed the outcome_type from “Adoption” to “Transfer”. The delete test removed the test record and returned a deleted count of 1. 

**Dashboard testing**
The ProjectTwoDashboard.ipynb notebook was tested to verify the interactive dashboard displayed animal records and was responsive to user commands.
1)	Water Rescue
2)	Mountain or Wilderness Rescue
3)	Disaster or Individual Tracking
4)	Reset
5)	Interactive Data Table
6)	Pie Chart
7)	Geolocation Map

While in development, an issue occurred in MongoDB filtering queries where $in operator was incorrectly entered as “Sin” which caused for certain data to not populate. This is one of many examples of why testing is important to ensure an application runs successfully. 
