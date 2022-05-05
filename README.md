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

Application front end:

![Screenshots of front end can be seen /gateway-simulator]

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
Prerequisites : Install Python on the local machine
1. Python script for data simulator which run on local

2. Follow the following link to MongoDB to connect to sink connector
https://www.mongodb.com/docs/kafka-connector/current/sink-connector/configuration-properties/
https://docs.confluent.io/platform/current/installation/configuration/connect/sink-connect-configs.html

3. Hosting the App with Realm

Upload Your Built Application to Realm
Single-page applications render in a single, specific HTML file, typically /index.html. The file should include the necessary JavaScript code to wire up and render your application, either inline in a <script> tag or imported from an external file. You'll also need to host any resources that you don't intend to access through a CDN.

When you are ready to host your SPA, run your application's build script and then upload the build folder to MongoDB Realm.

2 Configure Realm to Serve Your Application

Pull the Latest Version of Your App
To configure a single-page application with realm-cli, you need a local copy of your application's configuration files.

To pull a local copy of the latest version of your app, run the following:

realm-cli pull --remote="<Your App ID>"

TIP
You can also download a copy of your application's configuration files from the Deploy > Import/Export App screen in the Realm UI.

2
Add Your Built Application Code
Single-page applications render in a single, specific HTML file, typically /index.html. The file should include the necessary JavaScript code to wire up and render your application, either inline in a <script> tag or imported from an external file. You'll also need to host any resources that you don't intend to access through a CDN.

When you are ready to host your SPA, run your application's build script and then copy the output build folder into the /hosting/files directory of your application directory.

3 Configure Realm to Serve Your Application
In hosting/config.json, set default_response_code to 200 and set default_error_path to the resource path of your SPA's root HTML file. Make sure to save the file when you're done.

hosting/config.json
{
  "enabled": true,
  "default_response_code": 200,
  "default_error_path": "/index.html",
}

4
Deploy the Updated Hosting Configuration
Once you've updated and saved hosting/config.json you can push the updated config to your remote app. Realm CLI immediately supports your SPA on push.

realm-cli push --remote="<Your App ID>" --include-hosting


