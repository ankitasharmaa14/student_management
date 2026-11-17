import streamlit as st
import sqlite3

# Database connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
""")
conn.commit()

st.title("Student Record Management System")
st.write("Manage Student Records Using CRUD Operations")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Add Student", "View Students", "Update Student", "Delete Student"]
)

# CREATE
if menu == "Add Student":
    st.subheader("Add New Student")

    name = st.text_input("Student Name")
    email = st.text_input("Email")
    course = st.text_input("Course")

    if st.button("Add Student"):
        cursor.execute(
            "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
            (name, email, course)
        )
        conn.commit()
        st.success("Student Added Successfully!")

# READ
elif menu == "View Students":
    st.subheader("All Student Records")

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    st.table(data)

# UPDATE
elif menu == "Update Student":
    st.subheader("Update Student Details")

    student_id = st.number_input("Enter Student ID", min_value=1)

    name = st.text_input("New Name")
    email = st.text_input("New Email")
    course = st.text_input("New Course")

    if st.button("Update Student"):
        cursor.execute(
            "UPDATE students SET name=?, email=?, course=? WHERE id=?",
            (name, email, course, student_id)
        )
        conn.commit()

        if cursor.rowcount > 0:
            st.success("Student Updated Successfully!")
        else:
            st.error("Student ID Not Found!")

# DELETE
elif menu == "Delete Student":
    st.subheader("Delete Student Record")

    student_id = st.number_input("Enter Student ID", min_value=1)

    if st.button("Delete Student"):
        cursor.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )
        conn.commit()

        if cursor.rowcount > 0:
            st.success("Student Deleted Successfully!")
        else:
            st.error("Student ID Not Found!")

conn.close()