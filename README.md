# data_warehouse_dbt_airflow
![data_warehouse](https://miro.medium.com/max/1400/1*C30qzgp75f8ACyqvlxTbfA.png)

# About
Data warehouse is an electronic system that gathers data from a wide range of sources within a company and uses the data to support management decision-making.
A data warehouse system stores data from numerous sources, typically structured, Online Transaction Processing (OLTP) data such as invoices and financial transactions, Enterprise Resource Planning (ERP) data, and Customer Relationship Management (CRM) data. The data warehouse focuses on data relevant for business analysis, organizes and optimizes it to enable efficient analysis.
# Business Need
You and your colleagues have joined to create an AI startup that deploys sensors to businesses, collects data from all activities in a business - people’s interaction, traffic flows, smart appliances installed in a company. Your startup helps organisations obtain critical intelligence based on public and private data they collect and organise. 
A city traffic department wants to collect traffic data using swarm UAVs (drones) from a number of locations in the city and use the data collected for improving traffic flow in the city and for a number of other undisclosed projects. Your startup is responsible for creating a scalable data warehouse that will host the vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras. 
The data warehouse should take into account future needs, organise data such that a number of downstream projects query the data efficiently. You should use the Extract Load Transform (ELT) framework using DBT.  Unlike the Extract, Transform, Load (ETL), the ELT framework helps analytic engineers in the city traffic department setup transformation workflows on a need basis.

# Data
The data for the challenge https://open-traffic.epfl.ch/index.php/downloads/#1599047632450-ebe509c8-1330
The major Tools that we will use for this project are:-
Airflow
DBT
Postgres
redash
