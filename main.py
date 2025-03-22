

        tables = pd.read_html(html_io)
        return tables[0]
    except FileNotFoundError:
        print(f"File not found: {html_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


df = read_html_to_dataframe(r'D:\python\pythonProject\Financial_Data_Analysis .html')
print(df)

def read_html_to_dataframe(html_file_path):
    try:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        html_io = StringIO(html_content)
        tables = pd.read_html(html_io)
        if len(tables) > 0:
            return tables[0]
        else:
            print("No tables found in the HTML file.")
            return None
    except FileNotFoundError:
        print(f"File not found: {html_file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the HTML file: {e}")
        return None

def handle_query(df, query):
    if df is None:
        return "No data available. Please ensure the financial data is loaded correctly."

    query = query.lower()

    if "revenue" in query:
        return handle_revenue_query(df, query)
    elif "net income" in query:
        return handle_net_income_query(df, query)
    else:
        return "I'm sorry, I didn't understand that query."

def extract_company_and_year(query):
    company = None
    year = None

    if "for" in query:
        try:
            company = query.split("for")[1].split("in")[0].strip().title()
        except IndexError:
            return None, None

    year_match = re.search(r'\b(19|20)\d{2}\b', query)
    if year_match:
        year = int(year_match.group(0))
    else:
        year = None

    return company, year

def normalize_company_name(df, company_name):
    df['Company'] = df['Company'].str.lower()
    return df, company_name.lower()

def handle_revenue_query(df, query):
    company, year = extract_company_and_year(query)
    if not company:
        return "Please provide a valid company name."
    if not year:
        return "Please specify a valid year."
    df, company = normalize_company_name(df, company)
    result = df[(df['Company'] == company) & (df['Year'] == year)]
    if result.empty:
        return f"No data available for {company.title()} in {year}."
    else:
        return f"{company.title()}'s total revenue in {year} was {result['Total Revenue'].values[0]}."


def handle_net_income_query(df, query):
    company, year = extract_company_and_year(query)
    if not company:
        return "Please provide a valid company name."
    if not year:
        return "Please specify a valid year."
    df, company = normalize_company_name(df, company)
    result = df[(df['Company'] == company) & (df['Year'] == year)]
    if result.empty:
        return f"No data available for {company.title()} in {year}."
    else:
        return f"{company.title()}'s net income in {year} was {result['Net Income'].values[0]}."

def main():

    df = read_html_to_dataframe(r'D:\python\pythonProject\Financial_Data_Analysis .html')

    if df is None:
        print("Failed to load financial data.")
        return

    while True:
        user_query = input("Ask me about financial data: ")
        if user_query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = handle_query(df, user_query)
        print(response)


if __name__ == "__main__":
    main()
