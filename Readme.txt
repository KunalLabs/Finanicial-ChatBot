Chatbot Overview:
The chatbot is designed to interact with financial data stored in an HTML file. It reads the data from the HTML file, converts it into a Pandas Data Frame, and allows the user to ask questions about financial metrics like Net Income and Revenue for specific companies and years. The chatbot responds to queries by extracting the company and year from the user's question and searching the loaded dataset for relevant information

Reading the Data:

The chatbot reads financial data from an HTML file using the read_html_to_dataframe() function.
It looks for tables within the HTML file and converts them into a DataFrame for querying.

Handling User Queries:
The chatbot continuously asks the user questions about financial data, such as "Net Income for Apple in 2022" or "Revenue Growth for Tesla in 2021."
It uses the handle_query() function to determine the type of query (Revenue or Net Income) and then processes the query using the corresponding function.

Extracting the Company and Year:
The chatbot uses regular expressions to extract the company name and year from the user’s query.
It normalizes company names to ensure case-insensitive matching between user queries and the dataset.

Responding to Queries:
The chatbot searches the DataFrame for matching entries based on the query type.
If a valid match is found, it returns the relevant financial metric (e.g., Net Income or Total Revenue).
If no data is found, it returns a message indicating the lack of data for the specified company and year.


Limitations:
Data Availability: If the specified company or year is not in the dataset, the chatbot will return an error message indicating no available data.
Company and Year Formatting: The chatbot expects company names and years to be correctly spelled and formatted. Misspelled company names or missing years may lead to errors or incomplete responses.
Static Data: The chatbot relies on the financial data provided in the HTML file and does not fetch real-time data.
Limited Query Types: Currently, the chatbot only supports queries related to Net Income and Revenue. Additional metrics can be added with modifications to the script.
