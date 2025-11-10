import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CampusHub", layout="wide")

menu = st.sidebar.radio("Go to", ["Home", "Courses", "Faculty", "Student Dashboard", "Feedback"])

if menu == "Home":
    st.title("🎓 CampusHub — Student Information & Learning Portal")
    st.image("https://example.com/college.jpg", use_container_width=True)
    st.write("Welcome to CampusHub! Explore courses, meet faculty, and view student dashboards.")
    st.write("Use the sidebar to navigate through the pages.")
    st.caption("Developed by Preethi • © 2025")

# ---------------- COURSES ----------------
elif menu == "Courses":
    st.title("📘 Courses Offered")
    data = {
        "Course": ["Data Science", "Web Development", "Machine Learning"],
        "Instructor": ["Dr. Smith", "Prof. Lee", "Dr. Patel"],
        "Duration": ["12 Weeks", "10 Weeks", "14 Weeks"]
    }
    df = pd.DataFrame(data)
    st.table(df)

    st.write()

    st.button("Enroll now")

# ---------------- FACULTY ----------------
elif menu == "Faculty":
    st.title("👩‍🏫 Faculty Members")
    faculty = pd.DataFrame({
        "Name": ["Dr. Smith", "Prof. Lee", "Dr. Patel"],
        "Department": ["Data Science", "Web Development", "AI/ML"]
    })
    st.table(faculty)

# ---------------- STUDENT DASHBOARD ----------------
elif menu == "Student Dashboard":
    st.title("📊 Student Dashboard")
    students = pd.DataFrame({
        "Name": ["Yasotha", "Shobi", "Vidhya"],
        "Department": ["AI/ML", "Data Science", "Web Dev"],
        "Attendance": [92, 85, 88],
        "Grade": [88, 75, 82]
    })
    st.dataframe(students)
    st.metric("Total Students", len(students))
    st.metric("Average Attendance", f"{students['Attendance'].mean():.1f}%")

    chart = px.bar(students, x="Name", y="Attendance", color="Department", title="Attendance by Student")
    st.plotly_chart(chart)

# ---------------- FEEDBACK ----------------
elif menu == "Feedback":
    st.title("📝 Feedback Form")
    name = st.text_input("Your Name")
    score = st.slider("Rate CampusHub", 1, 10)
    comment = st.text_area("Comments")
    if st.button("Submit"):
        st.success(f"Thank you {name}! Feedback recorded ✅")
