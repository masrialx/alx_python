#!/usr/bin/env python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Get user input from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    cursor = db.cursor()

    # Create the SQL query
    query = "SELECT cities.id, cities.name, states.name FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "ORDER BY cities.id ASC"

    # Execute the query
    cursor.execute(query)

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
