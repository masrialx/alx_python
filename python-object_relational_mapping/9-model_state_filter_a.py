#!/usr/bin/python3
"""Lists all State objects containing the letter a from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Get user input from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server using SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(mysql_username, mysql_password, database_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve State objects containing the letter 'a' and display the results
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
