# SMART ASK AI

SMART ASK AI is a Streamlit-based AI web application that provides user authentication and AI-powered features such as code generation and document question answering. The application includes login, registration, password validation, and page-based navigation using Streamlit sidebar controls.

## Features

- User registration and login
- Password validation with security rules
- Session-based authentication
- Sidebar navigation
- Welcome page after login
- Code generation module
- Document Q&A module
- SQLite database support
- Environment variable configuration using `.env`

## Tech Stack

- Python
- Streamlit
- SQLite
- Cohere API
- PyPDF2
- python-dotenv

## Project Structure

```text
Smark-Ask-Ai-main/
│
├── app.py                 # Main Streamlit application
├── config.py              # Database configuration
├── requirements.txt       # Python dependencies
├── test_db.py             # Database testing script
├── users.db               # SQLite database file
├── .env                   # Environment variables
└── .github/workflows/     # GitHub workflow configuration
```

> Note: The current uploaded ZIP imports `models.user` and `backend` modules, but those folders are not included in the ZIP. Make sure the following folders/files exist before running the project:

```text
models/
└── user.py

backend/
├── welcome.py
├── code.py
└── docqanda.py
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Smark-Ask-Ai-main
```

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root and add the database path:

```env
DB_PATH=./database/app.sqlite
```

If you are using Cohere API for AI features, also add:

```env
COHERE_API_KEY=your_cohere_api_key_here
```

## How to Run

Start the Streamlit application using:

```bash
streamlit run app.py
```

After running the command, open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Application Flow

1. User opens the Streamlit application.
2. The database is initialized when the application starts.
3. New users can register with a valid password.
4. Existing users can log in using their username and password.
5. After login, users can access:
   - Welcome page
   - Code Generation page
   - Document Q&A page
6. Users can log out from the sidebar.

## Password Rules

The password must follow these rules:

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character
- Should not start with a special character

## Database

The application uses SQLite for storing user details. The database path is loaded from the `.env` file using the `DB_PATH` variable.

Example:

```env
DB_PATH=./database/app.sqlite
```

## Testing the Database

To test database registration and authentication logic, run:

```bash
python test_db.py
```

## Important Notes

- Do not upload `.env` files to GitHub because they may contain secret API keys.
- Avoid hardcoding local system paths in `config.py`.
- Use relative paths for better portability.
- Make sure all required folders such as `models` and `backend` are included in the project.

## Future Improvements

- Add forgot password functionality properly
- Add password hashing for better security
- Improve UI design
- Add document upload support
- Add support for multiple LLM providers
- Add error handling and logging
- Add deployment configuration

## Author

Developed as part of the SMART ASK AI project.
