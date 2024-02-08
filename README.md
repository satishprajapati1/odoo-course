https://www.fullstackpython.com/

# What is ORM?
- An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.
- https://www.fullstackpython.com/object-relational-mappers-orms.html

# Why are ORMs useful?
- ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database. Developers can use the programming language they are comfortable with to work with a database instead of writing SQL statements or stored procedures.
- The ability to write Python code instead of SQL can speed up web application development, especially at the beginning of a project. The potential development speed boost comes from not having to switch from Python code into writing declarative paradigm SQL statements. While some software developers may not mind switching back and forth between languages, it's typically easier to knock out a prototype or start a web application using a single programming language.
- ORMs also make it theoretically possible to switch an application between various relational databases. For example, a developer could use SQLite for local development and MySQL in production. A production application could be switched from MySQL to PostgreSQL with minimal code modifications.

# What are the downsides of using an ORM?
1. Impedance mismatch - The phrase "impedance mismatch" is commonly used in conjunction with ORMs. Impedance mismatch is a catch-all term for the difficulties that occur when moving data between relational tables and application objects. The gist is that the way a developer uses objects is different from how data is stored and joined in relational tables.  https://agiledata.org/essays/impedanceMismatch.html
2. Potential for reduced performance
3. Shifting complexity from the database into the application code

2. Potential for reduced performance
  One of the concerns that's associated with any higher-level abstraction or framework is potential for reduced performance. With ORMs, the performance hit comes from the translation of application code into a corresponding SQL statement which may not be tuned properly.
  
  ORMs are also often easy to try but difficult to master. For example, a beginner using Django might not know about the select_related() function and how it can improve some queries' foreign key relationship performance. There are dozens of performance tips and tricks for every ORM. It's possible that investing time in learning those quirks may be better spent just learning SQL and how to write stored procedures.
  
  There's a lot of hand-waving "may or may not" and "potential for" in this section. In large projects ORMs are good enough for roughly 80-90% of use cases but in 10-20% of a project's database interactions there can be major performance improvements by having a knowledgeable database administrator write tuned SQL statements to replace the ORM's generated SQL code.

3. Shifting complexity from the database into the app code
  The code for working with an application's data has to live somewhere. Before ORMs were common, database stored procedures were used to encapsulate the database logic. With an ORM, the data manipulation code instead lives within the application's Python codebase. The addition of data handling logic in the codebase generally isn't an issue with a sound application design, but it does increase the total amount of Python code instead of splitting code between the application and the database stored procedures.

http://maetl.net/talks/rise-and-fall-of-orm

https://agiledata.org/essays/mappingObjects.html

# Common web framework functionality
- Frameworks provide functionality in their code or through extensions to perform common operations required to run web applications. These common operations include:
https://www.fullstackpython.com/web-frameworks.html
- URL routing
- Input form handling and validation
- HTML, XML, JSON, and other output formats with a templating engine
- Database connection configuration and persistent data manipulation through an object-relational mapper (ORM)
- Web security against Cross-site request forgery (CSRF), SQL Injection, Cross-site Scripting (XSS) and other common malicious attacks
- Session storage and retrieval


# Django
- Django is a widely-used Python web application framework with a "batteries-included" philosophy. The principle behind batteries-included is that the common functionality for building web applications should come with the framework instead of as separate libraries.

- For example, authentication, URL routing, a template engine, an object-relational mapper (ORM), and database schema migrations are all included with the Django framework. Compare that included functionality to the Flask framework which requires a separate library such as Flask-Login to perform user authentication.





