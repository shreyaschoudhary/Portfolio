import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="Shreyas Choudhary", page_icon="📊", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Projects", "📞 Contact"])

# --- HOME PAGE ---
if page == "🏠 Home":
    st.title("Welcome to Shreyas's Portfolio 🎯")
    st.write("### Hi, I'm **Shreyas**, a Data Professional and Machine Learning Enthusiast.")
    st.image("https://via.placeholder.com/800x300?text=Welcome+to+My+Portfolio", caption="Showcasing Data Insights")

    st.write(
        """
        **I specialize in**:
        - 📊 **Data Analysis & Visualization**: Power BI, Tableau, Python  
        - 🧠 **Machine Learning**: Building and deploying models  
        - 🛠️ **Technical Skills**: Python, SQL, Excel 
        
        Explore my projects below and feel free to reach out for collaborations!
        """
    )
    st.markdown("---")

    # Skills Section
    st.subheader("Skills")
    skills = {
        "Data Visualization": "⭐⭐⭐⭐⭐",
        "Python Programming": "⭐⭐⭐⭐⭐",
        "Machine Learning": "⭐⭐⭐⭐",
        "SQL & Databases": "⭐⭐⭐⭐",
        "Power BI / Tableau": "⭐⭐⭐⭐",
    }
    for skill, rating in skills.items():
        st.write(f"- {skill}: {rating}")

# --- PROJECTS PAGE ---
elif page == "📊 Projects":
    st.title("My Projects 🚀")

    # --- PROJECT 1: Power BI Dashboard ---
    st.subheader("1. Interactive Power BI Dashboard")
    st.write(
        "Designed a dynamic **claims reporting dashboard** to analyze customer insights and reduce reporting time by 40%."
    )
    st.write("[🔗 View Power BI Dashboard](#)")  # Replace '#' with the actual link

    # --- PROJECT 2: Machine Learning Model ---
    st.subheader("2. Fraud Detection ML Model")
    st.write(
        "Developed a Python-based **fraud detection model** using Random Forest Classifier, achieving 90% accuracy."
    )
    st.code(
        """
        from sklearn.ensemble import RandomForestClassifier

        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
        """
    )
    st.write("[🔗 View GitHub Code](#)")  # Replace '#' with your GitHub link

    # --- PROJECT 3: SQL Data Analysis ---
    st.subheader("3. SQL Churn Analysis")
    st.write("Performed customer churn analysis using SQL queries to uncover key retention strategies.")
    st.code(
        """
        SELECT customer_id, COUNT(*) AS churned_customers
        FROM customer_data
        WHERE status = 'churned'
        GROUP BY customer_id;
        """
    )
    st.write("[🔗 View Queries](#)")

    st.markdown("---")
    st.write("More projects coming soon...")

# --- CONTACT PAGE ---
elif page == "📞 Contact":
    st.title("Contact Me 💼")
    st.write(
        "Feel free to reach out to me for collaboration or job opportunities:"
    )
    st.write("- 📧 **Email**: shreyas.uoft@gmail.com")
    st.write("- 🔗 [**LinkedIn**](www.linkedin.com/in/shreyas-choudhary-4786bb106)")  # Replace '#' with your LinkedIn link
    st.write("- 🐙 [**GitHub**](https://github.com/shreyaschoudhary)")  # Replace '#' with your GitHub link

    # Contact Form
    st.subheader("Send a Message")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            st.success("Thank you for reaching out! I will get back to you soon.")
