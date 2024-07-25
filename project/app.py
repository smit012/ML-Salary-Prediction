import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = "Predict"  # Default page

# Define custom CSS for sidebar button styling with glow effect
st.markdown("""
    <style>
    .sidebar-button {
        width: 250px;
        text-align: center;
        display: block;
        padding: 10px;
        margin: 10px auto;
        background-color: black;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        text-decoration: none; /* Remove underline */
        box-shadow: 0 0 0 rgba(255, 255, 255, 0);
        transition: box-shadow 0.3s ease-in-out;
    }
    .sidebar-button:hover {
        background-color: black;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.8); /* Glowing effect */
        text-decoration: none; /* Ensure no underline on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar with custom HTML buttons
# st.sidebar.header("Navigation")

# HTML for buttons
buttons_html = """
<div style="display: flex; flex-direction: column; align-items: center;">
    <a href="?page=Predict" class="sidebar-button">Predict</a>
    <a href="?page=Explore" class="sidebar-button">Explore</a>
</div>
"""

st.sidebar.markdown(buttons_html, unsafe_allow_html=True)

# Handle query parameters for page navigation
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["Predict"])[0]

# Display the appropriate page based on the selected button
if page == "Predict":
    st.session_state.page = "Predict"
    show_predict_page()
else:
    st.session_state.page = "Explore"
    show_explore_page()
