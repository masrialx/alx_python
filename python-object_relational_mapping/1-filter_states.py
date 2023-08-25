#!/usr/bin/env python3
"""
Script to filter states starting with 'N' from a database using MySQLdb.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    
    # Create a cursor
    cursor = db.cursor()
    
    # Execute the query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' OR name LIKE 'n%' ORDER BY id ASC")
    
    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)
    
    # Close the cursor and database connection
    cursor.close()
    db.close()
