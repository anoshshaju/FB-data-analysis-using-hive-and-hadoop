# Fb-Data analysis based on likes and age groups using hive, hdfs and mapreduce.

## Project Description
Used Hive QL to query on the data set and got some solution to basic questions.
Stored the result data set into new hive tables.
Finally moved those tables into HDFS (using overwrite directory).
"fb_details.txt" file is the output file of the python program using pandas, containing few columns of the input fb data.

## Technologies Used
* HIVE - v1.2
* HADOOP - v2.7

## Input Data
Input data obtained from Kaggle as a .CSV file.

## Features
* Imported data from hdfs into hive table with the same schema (no.of columns and its data types).
* Performed SQL like queries with hive on the data.
* The results are transfered into separate hive tables.
* Finally stored those output hive tables into directories of hdfs.

To-do list:
* Performing bucketing and partitioning of the result data set and store that into hdfs.
* And also doing advanced queries on the data set like sub-queries and regexp (string searching).

## Getting Started

### STEP-1:

Hadoop command to create directory
```
 >>> hadoop fs -mkdir /anosh/fb/
```
Upload the input csv file into this directory using ambari

### STEP-2:

Created a table 'fb' in Hive with the required columns and corresponding data types and loading the csv file into it.
```
>>> CREATE TABLE fb(userid int,age int,dob_day int,dob_year int,dob_month int ,gender  string,tenure  int,friend_count  int,friendships_initiated  int,likes int,likes_received int,mobile_likes int , mobile_likes_received int ,computer_likes int ,computer_likes_received  int) row format delimited fields terminated by ',' stored as textfile location '/fb/';
```
### STEP-3:

Then perform various Hive queries on this table to get insights.
for example: Do young people use mobile or computer for fb browsing more frequently ?
```
hive> SELECT age,round(avg(mobile_likes),2) AS mobile_likes, round(avg(computer_likes),2) AS computer_likes FROM fb WHERE age<=25 AND age>=13 group by age;
```
### STEP-4:
Sending output data into separate Hive table
```
hive> insert overwrite table fb_young_age SELECT age,round(avg(mobile_likes),2) AS mobile_likes, round(avg(computer_likes),2) AS computer_likes FROM fb WHERE age<=25 AND age>=13 group by age;
```
Here the young age is considered to be between 13 and 25 (inclusive range)

### STEP-5:
Storing output Hive table into HDFS

```
hive> INSERT OVERWRITE DIRECTORY "/fb_young/" ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM fb_young_age;
```
### To display columns in new file using Python in Vscode:

```
import pandas as pd
data = pd.read_csv(r"C:\Users\Ajish Shaju\Downloads\input files\pseudo_facebook.csv")
n = len(data)
userid = list(data['userid'].unique())
old_userid = 0 
f = open("fb_details.txt",'a')
for i in data.index:
    if data['userid'][i] in userid:
        record = data['userid'][i],data['age'][i],data['gender'][i],data['friend_count'][i]
        f.write(str(record)+'\n')
        userid.remove(data['userid'][i])
f.close()
```
