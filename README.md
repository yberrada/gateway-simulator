# gateway-simulator

 Details

**Project** : _Fleet Management_  
**Team Number** : _Group_5_  
**Team Name** : _The Grove_  
**Demonstration Video** : _***_  

# Overview

_Insert Executive Overview of your application/demonstration_
"""
We are trying to solve a problem of capturing real-time data, processing it for analytics purpose for business insights.
We are trying to capture data points from IOT sensors from each of the vehicles transporting variety of goods like FMCG or Retail & fashion accesories. Using the data points we are trying to optimize the travel routes, travelling less distance still delivering in an optimal fashion benfiting the business as well earning more dimes...
"""

# Justification

_Please explain why you decided to build the application/demonstration for this project. What inspired you? What problems does it solve or how will it make Presales activities easier?_
_What MongoDB competitive differentiators (developer productivity, resiliency, scalability, etc.) does this demonstration showcase?_

"""
We wanted to solve a problem where we trying to demonstrate capabilties of mongo to be part of Real-time event driven architecture covering a problem faced by host of different industry verticles with same Proof of Value like Manfacturing, Retail, FMCG, transaportation , Home-borne automated system generating IOT data
Key Differentiators would be Lean code, resulting into developer productivity, High Availability of data, Scalable system, integeration with streaming platform like kafka, ease of usage for BI tools and in house data visualization capability, compression of data stream 4:1
"""

# Detailed Application Overview

_Describe the architecture of your application and include a diagram._
_List all the MongoDB components/products used in your demonstration._
_Describe what you application does and how it works_
"""
Architecture Diagram
! /gateway-simulator/Architecture.png

Mongo Components used in demonstration
-> Realm Application
-> GraphQL
-> Charts embedded on Application using SDK
-> Online Archive on the data platform
-> MongoDB kafka connector as sink 
-> Timeseries Collection

Application ingests the streaming data from IOT sensors in a fleet of vehicles used for transaportation of goods. From IOT sensors data is streamed using kafka pipeline to MongoDB. A Realm application uses this data to see meterics and visualizations of data points presenting various business KPIs and helps business in decision making. These meterics are designed on MongoDB Charts which refesh in near real time as more data is ingested and processed by the aggregation framework. Further, for analytics purpose 1 year of data would suffice as Hot data. We have configured Online Archive rule for tiering data older than 1 year into Cold data. 

Further in a future state, this project can have Data Science component feeding data points to an ML algo predicting optimized route for the fleet. Trying to minimize distance travelled and achive more.

In a real world scenario an IOT hub will be receiving the data first, however for simplicity we have omitted that step and created simulators which are generating this data continously to mimic a real-time pipeline.
"""

# Roles and Responsibilities

_List all the team members and summarize the contributions each member made to this project_
"""
Younes Berrada: Realm App, GraphQL , Kafka connection to MongoDB, Data Simulation script
Claudio Rubello: Capturing RCs, Usage of Online Archives
Tomislav Bartolin: Charts, Timeseries Collection
Divya Bhanot: Data Model, Schema & Presentation
Aiccha Sarr: Field Gap for "Multi-Region: Business Continuity under a cloud region outage"
"""
# Demonstration Script

_Demonstration script (or link to script) goes here_

_The demonstration script should provide all the information required for another MongoDB SA to deliver your demonstration to a prospect. This should include:_

* _setup/installation steps_
* _step by step instructions on how to give the demonstration_
* _key points to emphasize at each point in the demonstration_
* _any tear down steps required to reset the demonstration so it is ready for the next time_
