# Overview

For my third sprint, I decided to work on SQL Relational Database. Databases are really important in the programming world as it is a way to store and access important information. Whether it be passwords, usernames, notes, etc. databases are useful in storing data. One of the benefits to using a relational database is due to its simplicity. Not only is it easy to connect each databases and tables together but it can store a bunch of information and run efficiently.

This SQL Relational Database, when ran, will display out a menu in which the user can choose an option below. My SQL database stores cars and displays specific specifications of those models and makes of those vehicles. You can insert new cars and display the brands, makes and specifications of a specific make.

The software that I used to program and create a database was through MySQL Workshop. This program allows me to create tables and forward engineer the tables so that I can have access to SELECT and INSERT data into my tables. The other program that I used is VSCode. It is a common software for programmers to program in multiples languages

[Software Demo Video](https://clipchamp.com/watch/GyTMfpnJl99)

# Relational Database

The relational database that I used is a MySQL database. It is an open source database that is used by a lot of big companies. It is also one of the most used databases in the programming world. 

In the video, you can see three tables. You have the Model table, the specifications table, and the make table. The model and the specifications table has a one-to-one relationship. The reason why it has a one-to-one relationship is because each make of the car has a unique type of specification. The model table has a one-to-many relationship. Each model has a bunch of makes. No brand just makes one specific type of make. That is why it has a one-to-many relationship. 

# Development Environment

One of the tools that I used in MySQL Workbench is the forward engineer function. When I created the three tables, the workbench had a option to forward engineer the database into something where I can have access to it. It is really useful when creating a database with several tables.

In the Python program, I imported mysql.connector. This allows the programmer to access the database using the mysql.connector, hence its name.

# Useful Websites


- [W3Schools SQL](https://www.w3schools.com/sql/default.asp)
- [W3Schools Python-MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- One of the things that I want to try to implement in my program is to allow other people to have access to my database. I've been trying to figure out how to do it instead of my having access to it on my localhost.