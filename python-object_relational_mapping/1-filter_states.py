#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper or lower N)
from the database test_1.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor
    cursor = db.cursor()

    # Execute the query to retrieve states starting with 'N' (upper or lower N)
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' OR name LIKE BINARY 'n%' ORDER BY id ASC")

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
