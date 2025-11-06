An Object-Relational Mapper (ORM) is a tool that allows developers to interact with databases using object-oriented programming (OOP) concepts. It abstracts SQL commands, enabling you to work with database entities as if they were regular objects in your programming language. This simplifies database interaction by allowing developers to work with data in a familiar way, such as in Python, without writing raw SQL queries.
Why Use an ORM?
Ease of Use: Manipulate Python objects instead of writing SQL queries.
Portability: Write database-agnostic code, making it easier to switch between database systems (e.g., MySQL, PostgreSQL, SQLite).
Security: Built-in protections against SQL injection attacks.
Productivity: Spend less time writing boilerplate code for database interaction.
Basic Concepts of ORMs
Model: Represents a table in your database. Model attributes correspond to table columns.
Instance: An instance of a model represents a row/record in the table.
Query: Retrieve, filter, and manipulate data using the ORM's query builder.
SQLAlchemy 2.0: Python's Most Popular ORM
SQLAlchemy is a powerful and flexible ORM for database operations in Python. Version 2.0 introduces a more modern and expressive syntax, improved type hinting, and asynchronous support.
A virtual environment is like a separate folder for your project where all the tools and libraries it needs are kept in one place. Think of it as giving your project its own little toolbox that won’t get mixed up with tools from other projects.
PowerShell has an Execution Policy that controls whether scripts can run on your system. By default, it is set to Restricted, which prevents any scripts (even local ones) from running. 
To allow the script to run, we can update the execution policy to RemoteSigned, which allows locally created scripts (like activate.ps1) to run, but still requires scripts downloaded from the internet to be signed.

Run the following command in PowerShell 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
RemoteSigned: Allows local scripts but restricts unsigned remote scripts.
Scope CurrentUser: Ensures this change only affects your user account, not the entire system.
pip install sqlalchemy
To connect to our MySQL Database we'll also need the MySQL Connector package:
pip install mysql-connector-python
The first step in using SQLAlchemy is establishing a connection to your database. SQLAlchemy supports various database systems, including SQLite, PostgreSQL, MySQL, and more.

from sqlalchemy import create_engine

# Create an engine for SQLite
engine = create_engine('mysql+mysqlconnector://root:<YOUR_MYSQL_PASSWORD>@localhost/<DATABASE_NAME>')

The Base class serves as a foundation for all database models.
Every model (table) you define will inherit from this Base class.
It connects the models to SQLAlchemy’s ORM engine.
To insert data, you create an instance of a model and add it to a session. A session in SQLAlchemy manages the database transactions.

