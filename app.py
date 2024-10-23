import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyBP3r5VSrL7MCciA1k7Gl4sEXhFTL2_z_8"

def configure_genai(api_key: str) -> genai.GenerativeModel:
    """Configure the Generative AI model with the provided API key."""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-pro")

def generate_sql_query(model: genai.GenerativeModel, description: str) -> str:
    """Generate a SQL query based on the provided description."""
    prompt = f"""
Create a SQL query snippet using the below text:

```
{description}
```
I just want a SQL query.
"""
    response = model.generate_content(prompt)
    sql_query = response.text.strip().strip("```sql").strip("```")
    return sql_query

def generate_expected_output(model: genai.GenerativeModel, sql_query: str) -> str:
    """Generate the expected output for the given SQL query."""
    prompt = f"""
What would be the expected response of this SQL query snippet?

```
{sql_query}
```
Provide sample response in tabular format with no explanation.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_explanation(model: genai.GenerativeModel, sql_query: str) -> str:
    """Generate a clear and concise explanation of the SQL query."""
    prompt = f"""
Please provide a clear and concise explanation of the following SQL query snippet:

```
{sql_query}
```
The explanation should be detailed, easy to understand, and cover the purpose and functionality of each part of the query.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def main():
    model = configure_genai(GOOGLE_API_KEY)
    
    st.set_page_config(page_title="SQL Query Generator", page_icon=":robot:")
    st.markdown(
        """
            <div style="text-align: center;">
                <h1>SQL Query Generator 👨‍💻📟</h1>
                <h3>Hello! I can generate SQL queries for you.</h3>
                <h4>With Explanation as well!</h4>
                <p>Just describe the query you want to generate, and I'll handle the rest.</p>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    description = st.text_area("Enter the query description in plain English:")
    
    if st.button("Generate SQL Query"):
        if not description.strip():
            st.warning("Please enter a description for the SQL query.")
            return
        
        with st.spinner("Generating SQL Query..."):
            try:
                sql_query = generate_sql_query(model, description)
                expected_output = generate_expected_output(model, sql_query)
                explanation = generate_explanation(model, sql_query)
                
                st.success("✅ SQL Query Generated Successfully!")
                st.code(sql_query, language="sql")
                
                st.success("📊 Expected Output with Sample Data:")
                st.markdown(expected_output)
                
                st.success("📝 Explanation of the SQL Query:")
                st.markdown(explanation)
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
