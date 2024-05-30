# QueryGen

QueryGen is a Streamlit application that allows you to generate SQL queries based on natural language prompts and CSV file inputs. It uses LangChain's SQL query generation capabilities and the ChatGroq language model to interpret user prompts and generate optimized SQL queries tailored to the uploaded CSV data.

## Features

- Upload multiple CSV files
- Enter natural language prompts to generate SQL queries
- Automatically create a SQLite database from the uploaded CSV files
- Display the generated SQL query and its result
- Error handling for invalid prompts or database issues

## Installation

1. Clone the repository:

```
https://github.com/Pragateeshwaran/QueryGen.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Obtain an API key from [ChatGroq](https://www.chatgroq.com/) and replace the placeholders in `GenAi.py` with your actual API key.

## Usage

1. Navigate to the project directory:

```
cd QueryGen
```

2. Run the Streamlit application:

```
streamlit run app.py
```

3. The application will open in your default web browser.

4. Upload one or more CSV files using the file uploader in the sidebar.

5. Enter your natural language query in the text input field.

6. The generated SQL query and its result will be displayed on the page.

## File Structure

- `app.py`: The main Streamlit application file that handles the user interface and file uploads.
- `csv_db.py`: A utility module that creates a SQLite database from the uploaded CSV files.
- `GenAi.py`: This module contains functions for generating SQL queries from natural language prompts using LangChain and ChatGroq.

