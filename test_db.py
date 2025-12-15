import sys
import os

# Add the absolute path of the 'models' folder to sys.path
sys.path.append(r"C:\Users\JANKIRAM\Desktop\MyStreamlitProject\models")

sys
import sqlite3
from config import DB_PATH

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from project.models.user import init_db, register_user, authenticate_user
# Add the root directory to sys.path



# Initialize the database and create the users table
init_db()

# Register a new user
username = "test_user"
password = "securepassword"
register_user(username, password)

# Authenticate the user
auth_result = authenticate_user(username, password)

# Check if authentication was successful
if auth_result:
    print(f"User {username} authenticated successfully!")
else:
    print(f"Authentication failed for {username}.")
