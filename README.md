# SQL Query Generator

Welcome to the SQL Query Generator! This application uses Google's Generative AI to help you generate SQL queries based on plain English descriptions. It also provides expected outputs and explanations for the generated queries.

## Features

- **Generate SQL Queries**: Describe the query you want, and the app will generate it for you.
- **Expected Output**: Get a sample response in tabular format.
- **Query Explanation**: Understand the purpose and functionality of each part of the query.

## Demo

Check out the live demo of the app [here](https://sql-query-generator-6gtx93matt2ksse8bczosz.streamlit.app/).

## Installation

To run this app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/satyansh-mittal/SQL-Query-Generator.git
   cd SQL-Query-Generator
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables. Create a `.env` file in the root directory and add your Google API key:

   ```env
   GOOGLE_API_KEY=your-api-key-here
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter a description of the SQL query you want to generate in plain English.
2. Click on "Generate SQL Query".
3. View the generated SQL query, expected output, and explanation.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
