# Storm-Solr

## Objective 
Apache storm POC to read data from multiple source and store on solr index

## Apache Solr
Apache Solr is a high-performance, full featured text search engine library written in Java.

## Apache Storm
Storm is a distributed realtime computation system. Similar to how Hadoop provides a set of general primitives for doing batch processing, Storm provides a set of general primitives for doing realtime computation.

## Prerequisites
JRE <br />
lein  (A Clojure build tool)<br />
Apache Storm<br />
Apache Solr<br />
python<br />
streamparse  (python wrapper for storm)<br />
sqlalchemy  (python library for DB connection )<br />
Faker (python library for fake data generation )<br />
Flask (python library to create REST API ) <br />
and<br />
Basic understanding of Apache Storm and Solr Architecture <br />

## Installing 
Solr - [Installation Steps](https://github.com/technodivesh/storm-solr/blob/master/solr_installation_steps.txt)

Storm - [Installation Steps](https://github.com/technodivesh/storm-solr/blob/master/storm_and_streamparse_installation_steps.txt)


## Getting Started 
### Step 1: Run Solr
```bash
cd solr-7.3.1/
bin/solr start
bin/solr create -c products
```
To check - open http://localhost:8983/solr 

### Step 2: Run Flask API
```bash
cd flask_api/
python flask_api.py
```
To Check - open http://localhost:5000/api/v1/profiles </br>
list of profiles will be displayed 

### Step 3: Create DB
Create a database named 'storm' and restore the db_dump/products.sql
```bash
mysql -u<user> -p<passwd> storm < db_dump/products.sql
```

### step 4: Run Storm
```bash
cd products/
sparse run
```
This will start storm </br>

Data from 2 source ie. DB and REST API will be started indexing in Solr DB




