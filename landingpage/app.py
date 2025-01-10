import streamlit as st

# App title
st.set_page_config(page_title="AI Agents for Finance", page_icon="🤖")
st.title("AI Agents for Finance")
st.subheader("Essential applications for Finance, Planning & Analysis")

# Stay Updated Section
st.text_input("Stay Updated", "Enter your email")

# Define apps with emojis and links
apps = [
    {"name": "File Converter 📂", "description": "Convert financial data between CSV and XLSX formats seamlessly", "link": "#"},
    {"name": "Finance Data Cleaner 🧹", "description": "Clean and standardize your financial datasets efficiently", "link": "#"},
    {"name": "Stock Market Analysis 📈", "description": "Analyze market trends and financial KPIs", "link": "#"},
    {"name": "Excel File Merger 📑", "description": "Combine multiple Excel files into a single consolidated dataset", "link": "#"},
    {"name": "Monte Carlo Simulator 🎲", "description": "Run sophisticated Monte Carlo simulations for financial modeling", "link": "#"},
    {"name": "Prophet Forecaster 📊", "description": "Advanced time series forecasting for financial data analysis", "link": "#"},
]

# Display apps in grid
col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

for i, app in enumerate(apps):
    with columns[i % 3]:
        st.subheader(app["name"])
        st.text(app["description"])
        # Button with link
        if st.button(f"Go to {app['name'].split(' ')[0]}", key=f"button_{i}"):
            st.write(f"Redirecting to {app['link']}... (Add real links here)")
            # Add real redirect logic here, if needed.

# Custom App Request Section
st.markdown("---")
st.subheader("Need a Custom AI Finance App?")
st.write("Don't see what you're looking for? Let us build a custom AI-powered financial application tailored to your specific needs.")

# Redirect to Google Form link
form_url = "https://forms.gle/bkheBL4PDceiJpn19"
st.markdown(f"[Request Custom App]({form_url})", unsafe_allow_html=True)
