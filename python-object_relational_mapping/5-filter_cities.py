#!/usr/bin/env python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    # Get user input from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    # Execute the query
    cursor.execute(query, (state_name,))

    # Fetch and display the results
    results = cursor.fetchall()
    cities = [row[0] for row in results]
    print(", ".join(cities))

    # Close cursor and database connection
    cursor.close()
    db.close()
