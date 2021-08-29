# PROJECT TITLE
Fb-Data analysis based on likes and age groups using hive, hdfs and mapreduce.

# Project Description
Used Hive QL to query on the data set and got some solution to basic questions.
Stored the result data set into new hive tables.
Finally moved those tables into HDFS (using overwrite directory).
"fb_details.txt" file is the output file of the python program using pandas, containing few columns of the input fb data.

# Technologies Used
1. HIVE - version 1.2
2. HADOOP - version 2.7

# Input Data
Input data obtained from Kaggle as a .CSV file.

# Features
1. Imported data from hdfs into hive table with the same schema (no.of columns and its data types).
2. Performed SQL like queries with hive on the data.
3. The results are transfered into separate hive tables.
4. Finally stored those output hive tables into directories of hdfs.

To-do list:
1. Performing bucketing and partitioning of the result data set and store that into hdfs.
2. And also doing advanced queries on the data set like sub-queries and regexp (string searching).
