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
    # Additional 5 agents
    {"name": "Dashboard Creator 📊", "description": "Create insightful financial dashboards with ease", "link": "https://dashboardcreator.streamlit.app/"},
    {"name": "Finance Data Visualizer 🎨", "description": "Transform raw data into beautiful financial insights", "link": "https://finance-data-is-beautiful.streamlit.app/"},
    {"name": "Data Visualizer for Finance 🖼️", "description": "Explore financial data through interactive visualizations", "link": "https://data-visualizer-finance.streamlit.app/"},
    {"name": "Sankey Diagrams for Finance 🔗", "description": "Visualize financial flows with Sankey diagrams", "link": "https://sankey-diagrams-for-finance.streamlit.app/"},
    {"name": "Python Finance Learning Path 📘", "description": "Learn Python for finance with step-by-step guidance", "link": "https://pythonfinancelearningpath.streamlit.app/"},
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
            st.write(f"Redirecting to {app['link']}... (Click the link below)")
            st.markdown(f"[Open {app['name']}]({app['link']})", unsafe_allow_html=True)

# Custom App Request Section
st.markdown("---")
st.subheader("Need a Custom AI Finance App?")
st.write("Don't see what you're looking for? Let us build a custom AI-powered financial application tailored to your specific needs.")

# Redirect to Google Form link
form_url = "https://forms.gle/bkheBL4PDceiJpn19"
st.markdown(f"[Request Custom App]({form_url})", unsafe_allow_html=True)
