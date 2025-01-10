import streamlit as st

# App title
st.set_page_config(page_title="AI Agents for Finance", page_icon="🤖")
st.title("AI Agents for Finance")
st.subheader("Essential applications for Finance, Planning & Analysis")

# Stay Updated Section
st.text_input("Stay Updated", "Enter your email")

# Define apps
apps = [
    {"name": "File Converter", "description": "Convert financial data between CSV and XLSX formats seamlessly", "launch_text": "Launch application →"},
    {"name": "Finance Data Cleaner", "description": "Clean and standardize your financial datasets efficiently", "launch_text": "Launch application →"},
    {"name": "Stock Market Analysis", "description": "Analyze market trends and financial KPIs", "launch_text": "Launch application →"},
    {"name": "Excel File Merger", "description": "Combine multiple Excel files into a single consolidated dataset", "launch_text": "Launch application →"},
    {"name": "Monte Carlo Simulator", "description": "Run sophisticated Monte Carlo simulations for financial modeling", "launch_text": "Launch application →"},
    {"name": "Prophet Forecaster", "description": "Advanced time series forecasting for financial data analysis", "launch_text": "Launch application →"},
]

# Display apps in grid
col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

for i, app in enumerate(apps):
    with columns[i % 3]:
        st.subheader(app["name"])
        st.text(app["description"])
        st.button(app["launch_text"])

# Custom App Request Section
st.markdown("---")
st.subheader("Need a Custom AI Finance App?")
st.write("Don't see what you're looking for? Let us build a custom AI-powered financial application tailored to your specific needs.")
if st.button("Request Custom App"):
    st.write("Redirecting to custom app request...")

