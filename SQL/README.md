Program 1
Database Setup and Data Exploration
Introduction
Before any organization can analyze its business data, the information must first be collected, organized, and stored in a database. This preparation stage is one of the most important parts of every data analytics project. Even the most advanced SQL queries cannot produce meaningful results if the underlying data has not been properly organized.
Imagine joining a company as a Data Analyst on your very first day. Your manager does not immediately ask you to create reports or dashboards. Instead, the first task is to understand the company's database.
Questions such as the following naturally arise:
What data is available?
How many tables are present?
What does each table represent?
Which tables are related to each other?
What information does every column contain?
Are there missing values?
What type of business can be understood from this data?
Professional data analysts always begin by exploring the data before performing any analysis. This process is known as Data Exploration or Exploratory Data Analysis (EDA).
Although EDA often includes visualization and statistical techniques, the first step in SQL-based projects is understanding the database structure.
Why Import Existing Datasets?
Earlier in this book, we created small tables manually using the CREATE TABLE and INSERT INTO statements. That approach was useful for learning SQL syntax, but real organizations rarely enter thousands of records manually.
Instead, businesses collect data automatically through websites, mobile applications, billing software, payment gateways, inventory systems, and customer management software. These systems usually export their information into formats such as CSV (Comma-Separated Values).
Rather than recreating these records ourselves, we will import an existing dataset into MySQL. This allows us to work with realistic business data and experience a workflow similar to that followed by professional data analysts.
Using a real dataset also introduces you to practical challenges such as understanding unfamiliar tables, interpreting column names, and discovering relationships between different entities.
About the Dataset

For this project, we will work with a real-world e-commerce dataset instead of creating small sample tables manually. Using an actual business dataset allows us to experience the same workflow followed by professional data analysts in the industry.
The dataset chosen for this project is the Brazilian E-Commerce Public Dataset by Olist, one of the most popular datasets used for learning SQL, data analysis, and business intelligence.
It contains real transactional data collected from an online marketplace, including information about customers, products, orders, sellers, payments, and reviews. The data is organized into multiple related CSV files, making it an excellent example of a relational database.
The complete dataset can be downloaded from Kaggle using the following link:
Dataset Name:
Brazilian E-Commerce Public Dataset by Olist
Author:
Olist
Download Link:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce⁠�
After opening the dataset page, click the Download button to download the ZIP file. Extract the ZIP archive to obtain all the CSV files.
Dataset Files Required for This Project
The original dataset contains several CSV files. However, for this mini project, we will focus on the following files:
CSV File
Purpose
olist_customers_dataset.csv
Stores customer information such as customer ID, city, and state.
olist_products_dataset.csv
Contains product details including product category, dimensions, and weight.
olist_orders_dataset.csv
Stores order information such as order status, purchase date, and delivery dates.
olist_order_items_dataset.csv
Contains information about the products included in each order.
olist_order_payments_dataset.csv
Stores payment details including payment type, installments, and payment value.
These five datasets provide everything required to perform customer analysis, product analysis, sales reporting, payment analysis, and advanced SQL queries using JOINs and Subqueries