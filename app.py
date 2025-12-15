import streamlit as st
import sys
import os
import re
from dotenv import load_dotenv
import os

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "./database/app.sqlite")

def init_db(): 
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from models.user import register_user, authenticate_user, init_db
from backend.welcome import show_welcome_page
from backend.code import show_code_generation_page
from backend.docqanda import show_docqanda_page
from models.user import update_password  


def is_valid_password(password):
    """
    Validate password based on these rules:
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character (@#$%^&+=!)
    - Cannot start with a special character
    - Minimum length: 8 characters
    """
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return "Password must contain at least one number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    if re.match(r"^[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password cannot start with a special character."

    return None  # Password is valid


def main():
    # Initialize the database when the app starts
    init_db()

    # Display the app title
    st.title("SMART ASK")

    # Handle session state for login
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        # Get username from session state
        username = st.session_state["username"]

        # Sidebar navigation (same options across pages)
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Select a Page", ["Welcome", "Code Generation", "Doc Q&A"])

        # Show the selected page based on user navigation
        if page == "Welcome":
            show_welcome_page(username)

        elif page == "Code Generation":
            show_code_generation_page()

        elif page == "Doc Q&A":
            show_docqanda_page()

        # Log out functionality
        if st.sidebar.button("Logout"):
            st.session_state.clear()  # Clear session state to log out
            st.rerun()  # Rerun the app to reset the interface

    else:
        # Handle Login/Register if not logged in
        menu = ["Login", "Register"]
        choice = st.sidebar.selectbox("Choose an action", menu)

        if choice == "Register":
            st.subheader("Create a New Account")
            username = st.text_input("Username")
            password = st.text_input("Password", type='password')
            confirm_password = st.text_input("Confirm Password", type='password')

            if st.button("Register"):
                error_msg = is_valid_password(password)
                if error_msg:
                    st.error(error_msg)  # Show password validation error
                elif password != confirm_password:
                    st.error("Passwords do not match.")
                else:
                    register_user(username, password)  # Call function to register the user
                    st.success("Registration successful! You can now log in.")
                # if password == confirm_password:
                #     register_user(username, password)  # Call the function to register the user
                # else:
                #     st.error("Passwords do not match.")

        # elif choice == "Login":
        #     st.subheader("Login to Your Account")
        #     username = st.text_input("Username")
        #     password = st.text_input("Password", type='password')

        #     if st.button("Login"):
        #         if authenticate_user(username, password):  # Call the function to authenticate the user
        #             # Set session state on successful login
        #             st.session_state["logged_in"] = True
        #             st.session_state["username"] = username
        #             st.rerun()  # Rerun the app to redirect to the other pages

        elif choice == "Login":
            st.subheader("Login to Your Account")
            username = st.text_input("Username")
            password = st.text_input("Password", type='password')

            col1, col2 = st.columns([1, 1])  # Create two columns for layout
            
            st.markdown(
                """
                <style>
                .center-button {
                    display: flex;
                    justify-content: center;
                }
                .center-button button {
                    background-color: #4CAF50;
                    color: white;
                    font-size: 16px;
                    border-radius: 10px;
                    border: none;
                    padding: 10px 20px;
                    cursor: pointer;
                    transition: 0.3s;
                }
                .center-button button:hover {
                    background-color: #45a049;
                }
                </style>
                """,
                unsafe_allow_html=True
            )         
            with col1:
                if st.button("Login"):
                    if authenticate_user(username, password):  # Call the function to authenticate
                        st.session_state["logged_in"] = True
                        st.session_state["username"] = username
                        st.rerun()
                    else:
                        st.error("Invalid username or password.")

            st.markdown(
                '<p style="text-align: right; margin-top: 10px;">'
                '<a href="#" style="color: #007BFF; text-decoration: none;">Forgot Password?</a>'
                '</p>',
                unsafe_allow_html=True
            )
            # with col2:
            #     if st.button("Forgot Password"):
            #         st.session_state["forgot_password"] = True  # Switch to forgot password section
            #         st.rerun()

        if "forgot_password" in st.session_state:
            st.subheader("Reset Your Password")
            username = st.text_input("Enter your username")
            new_password = st.text_input("Enter new password", type='password')
            confirm_new_password = st.text_input("Confirm new password", type='password')

            if st.button("Reset Password"):
                if not username:
                    st.error("Username is required.")
                else:
                    error_msg = is_valid_password(new_password)
                    if error_msg:
                        st.error(error_msg)
                    elif new_password != confirm_new_password:
                        st.error("Passwords do not match.")
                    else:
                        if update_password(username, new_password):
                            st.success("Password updated successfully! You can now log in.")
                            del st.session_state["forgot_password"]  # Remove session state after reset
                        else:
                            st.error("Username not found. Please register first.")

        # elif choice == "Forgot Password":
        #     st.subheader("Reset Your Password")
        #     username = st.text_input("Enter your username")
        #     new_password = st.text_input("Enter new password", type='password')
        #     confirm_new_password = st.text_input("Confirm new password", type='password')

        #     if st.button("Reset Password"):
        #         if not username:
        #             st.error("Username is required.")
        #         else:
        #             error_msg = is_valid_password(new_password)
        #             if error_msg:
        #                 st.error(error_msg)  # Show password validation error
        #             elif new_password != confirm_new_password:
        #                 st.error("Passwords do not match.")
        #             else:
        #                 if update_password(username, new_password):  # Update password in DB
        #                     st.success("Password updated successfully! You can now log in.")
        #                 else:
        #                     st.error("Username not found. Please register first.")

        
if __name__ == '__main__':
    main()
