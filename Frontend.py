import streamlit as st
import mysql.connector
import time
import pandas as pd

# Establish a connection to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ajey@123",
    database="timetablemanager"
)
cursor = conn.cursor()


# check admin username and password:
def authenticate(username, password):
    query = f"SELECT * FROM admin WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result is not None


def admin_dashboard():
    st.title("Admin Dashboard")
    st.write("Welcome,", st.session_state.user[0])

    # Add buttons
    selected_option = st.radio("Select an option:", ["Edit Student", "Edit Teacher", "Edit Subject", "Edit Room", "Edit Timeslot", "Edit Batch","Generate timetable"])

    if selected_option == "Edit Student":
        edit_students()

    elif selected_option == "Edit Teacher":
        edit_teachers()

    elif selected_option == "Edit Subject":
        edit_subjects()

    elif selected_option == "Edit Room":
        edit_rooms()

    elif selected_option == "Edit Timeslot":
        edit_timeslots()

    elif selected_option == "Edit Batch":
        edit_batches()
    
    elif selected_option == "Generate timetable":
        generate_timetable()


    if st.button("Logout", key="logout", on_click=lambda: st.session_state.rerun()):
        st.session_state.logged_in = False
        st.session_state.page = "Home"


def generate_timetable():
    pass


def edit_students():

    st.subheader("Edit Students")

    # Functionality Toggle Buttons
    selected_option = st.radio("Select Action", ["Add Student", "Remove Student", "Update Student","View student details"])

    if selected_option == "Add Student":
        add_student()
    elif selected_option == "Remove Student":
        remove_student()
    elif selected_option == "Update Student":
        update_student()
    elif selected_option == "View student details":
        view_student()


def view_student():
    st.title("View Student Details")
    rollno = st.text_input("SRN")

    if st.button("View Student Details"):
        query = f"SELECT * FROM Student WHERE studentid = '{rollno}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            # Create DataFrame directly
            df = pd.DataFrame([result], columns=['studentid', 'studentname', 'semester', 'section', 'batchid'])
            st.dataframe(df, hide_index=True)

        else:
            st.error("No entry found.")

def add_student():
    st.title("Add Student")

    name = st.text_input("Name")
    id = st.text_input("SRN")
    semester = st.number_input("Semester", min_value=1, max_value=10, step=1)
    section = st.text_input("Section", max_chars=1)
    batchid = str(semester) + section

    if st.button("Add Student"):
        try:
            query = f"INSERT INTO Student VALUES ('{id}', '{name}', {semester}, '{section}', '{batchid}')"
            print("SQL Query:", query)

            cursor.execute(query)
            conn.commit()
            st.success("Student added successfully!")

            # Clear input values after successful addition
            name = ""
            id = ""
            semester = 1
            section = ""

        except Exception as e:
            st.error(f"An error occurred: {e}")

def remove_student():
    st.title("Remove Student")
    rollno = st.text_input("SRN")
    
    if st.button("Remove Student"):
        query = f"DELETE FROM Student WHERE studentid = '{rollno}'"
        cursor.execute(query)
        conn.commit()
        st.success("Student removed successfully!")

def update_student():
    st.title("Update Student")
    name = st.text_input("Name")
    rollno = st.text_input("Roll Number")
    batchid = st.text_input("Batch ID")

    if st.button("Update Student"):
        query = f"UPDATE Student SET studentname = '{name}', batchid = '{batchid}' WHERE studentid = '{rollno}'"
        cursor.execute(query)
        conn.commit()
        st.success("Student updated successfully!")

    # Add functionality to edit student information in the database
    # You can use st.text_input, st.button, and other Streamlit components to create the form

    

    


def edit_teachers():
    st.subheader("Edit Teachers")

    # Add functionality to edit teacher information in the database
    # You can use st.text_input, st.button, and other Streamlit components to create the form

    operation = st.radio("Select Action", ["Add Teacher", "Remove Teacher", "Update Teacher","View teacher details"])

    if operation == "Add Teacher":
        add_teacher()
    elif operation == "Remove Teacher":
        remove_teacher()
    elif operation == "Update Teacher":
        update_teacher()
    elif operation == "View teacher details":
        view_teacher()


def add_teacher():
    st.title("Add Teacher")
    
    name = st.text_input("Name")
    teacher_id = st.text_input("Teacher ID")
    department = st.text_input("Department")
    email = st.text_input("Email")

    if st.button("Add Teacher"):
        try:
            query = "INSERT INTO Teacher VALUES (?, ?, ?, ?)"
            cursor.execute(query, (teacher_id, name, department, email))
            conn.commit()
            st.success("Teacher added successfully!")

            # Clear input values after successful addition
            name = ""
            teacher_id = ""
            department = ""
            email = ""

        except Exception as e:
            st.error(f"An error occurred: {e}")

def remove_teacher():
    st.title("Remove Teacher")
    teacher_id = st.text_input("Teacher ID")

    if st.button("Remove Teacher"):
        try:
            query = "DELETE FROM Teacher WHERE teacherid = ?"
            cursor.execute(query, (teacher_id,))
            conn.commit()
            st.success("Teacher removed successfully!")

        except Exception as e:
            st.error(f"An error occurred: {e}")

def update_teacher():
    st.title("Update Teacher")

    teacher_id = st.text_input("Teacher ID")
    name = st.text_input("Name")
    department = st.text_input("Department")
    email = st.text_input("Email")

    if st.button("Update Teacher"):
        try:
            query = "UPDATE Teacher SET name = ?, dept = ?, email = ? WHERE teacherid = ?"
            cursor.execute(query, (name, department, email, teacher_id))
            conn.commit()
            st.success("Teacher updated successfully!")

        except Exception as e:
            st.error(f"An error occurred: {e}")

def view_teacher():
    st.title("View Teacher Details")
    teacher_id = st.text_input("Teacher ID")

    if st.button("View Teacher Details"):
        query = f"SELECT * FROM Teacher WHERE teacherid = '{teacher_id}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            # Create DataFrame directly
            df = pd.DataFrame([result], columns=['teacherid', 'name', 'dept', 'email'])
            st.dataframe(df, hide_index=True)

        else:
            st.error("No entry found.")


def edit_subjects():
    st.subheader("Edit Subjects")
    # Add functionality to edit subject information in the database
    # You can use st.text_input, st.button, and other Streamlit components to create the form


def edit_rooms():
    st.subheader("Edit Rooms")
    # Add functionality to edit room information in the database
    # You can use st.text_input, st.button, and other Streamlit components to create the form


def edit_timeslots():
    st.subheader("Edit Timeslots")
    # Add functionality to edit timeslot information in the database
    # You can use st.text_input, st.button, and other Streamlit components to create the form


def edit_batches():
    st.subheader("Edit Batches")
    # Add functionality to edit batch information in the database
    # You can use st.text_input, st.button, and other Streamlit components to create the form


def view_timetable():
    st.title("View TimeTable")

    user_type = st.radio("Select User Type", ["Student", "Teacher"])

    if user_type == "Teacher" :
        uid = st.text_input("Enter Teacher ID ")

    else:
        uid = st.text_input("Enter Student ID or Batch")
    
    
    if uid:
        st.session_state.timetable_id = uid

    if st.session_state.timetable_id:
        st.write("Timetable for ",st.session_state.timetable_id)

    # Modify the SQL query to include JOIN with the subjects table
    if len(st.session_state.timetable_id) > 11:
        query = f"""
            SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname
            FROM timeslot t
            JOIN subject s ON t.subjectcode = s.subjectcode
            WHERE t.batch_id in
            (SELECT batchid from Student where studentid = '{st.session_state.timetable_id}')
        """

    elif len(st.session_state.timetable_id) >9:

        query = f'''select t.day, t.starttime, t.endtime, t.subjectcode, t.room_id
                    teacherid , batchid,slot_id 
                    from Teaches s natural join Timeslot t where teacherid = '{uid}'
            '''
    else:
        query = f"""
            SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname
            FROM timeslot t
            JOIN subject s ON t.subjectcode = s.subjectcode
            WHERE t.batch_id = '{st.session_state.timetable_id}'
        """

    cursor.execute(query)
    result = cursor.fetchall()
    print (result)

    if result and len(uid) >11:
        # Convert the result to a Pandas DataFrame
        df = pd.DataFrame(result, columns=[
                          'day', 'starttime', 'endtime', 'subjectcode', 'room_id', 'subjectname'])

        # Display the DataFrame
        df['starttime'] = df['starttime'].astype(str)
        df['endtime'] = df['endtime'].astype(str)
        df['Timing'] = df['starttime'].str[-8:-3] + \
            '-' + df['endtime'].str[-8:-3]

        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        df['day'] = pd.Categorical(
            df['day'], categories=day_order, ordered=True)
        df['alloted'] = df['subjectname'] + " [" + df['room_id'] + ']'

        timetable = df.pivot(index='day', columns='Timing', values='alloted')
        timetable = timetable.reset_index()
        # Increase row height using custom CSS

        st.dataframe(timetable, hide_index=True)
        # st.data_editor(timetable, hide_index=True)
    
    elif result and len(uid)>9:
        columns = ["day", "starttime", "endtime", "subjectcode", "room_id", "batchid", "slot_id"]
        # Create a DataFrame
        df = pd.DataFrame(result, columns=columns)

        df['starttime'] = df['starttime'].astype(str)
        df['endtime'] = df['endtime'].astype(str)

        df['Timing'] = df['starttime'].str[-8:-3] + \
            '-' + df['endtime'].str[-8:-3]

        df.drop(columns=['starttime','endtime'], inplace=True)
        df.sort_values(by='slot_id', inplace=True)


        st.dataframe(df,hide_index=True)

    else:
        st.error("No entry found.")


def main():
    st.set_page_config(layout="wide")

    st.sidebar.title("Navigation")

    if 'user' not in st.session_state:
        st.session_state.user = []

    if 'timetable_id' not in st.session_state:
        st.session_state.timetable_id = ""

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    def set_page(page):
        st.session_state.page = page

    if st.session_state.page == 'admin_login':
        st.title("Admin Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        col1, col2 = st.columns([0.1, 0.6])

        with col2:
            if st.button("Login"):
                if authenticate(username, password):
                    st.session_state.logged_in = True
                    st.session_state.user.append(username)
                    st.session_state.page = "dashboard"
                    st.rerun()
                else:
                    st.error("Invalid credentials. Please try again.")

        with col1:
            st.button("Signup", on_click=set_page, args=['signup'])

    elif st.session_state.page == "signup":

        st.title("User Signup")
        username = st.text_input("New Username")
        password = st.text_input("New Password", type="password")
        secret_code = st.text_input("Secret Code", type="password")

        if st.button("Signup"):
            if secret_code == "secret":
                st.success("Signup successful! You can now login.")
                time.sleep(0.5)
                st.session_state.signup_page = False
                st.session_state.logged_in = False

    elif st.session_state.page == "dashboard":
        admin_dashboard()

    elif st.session_state.page == "timetable":
        view_timetable()

    elif st.session_state.page == "Home":
        st.title("Welcome to TimeTable manager!")

# Sidebars:
    if st.sidebar.button("Admin Dashboard"):
        if st.session_state.logged_in:
            st.session_state.page = "dashboard"
        else:
            st.session_state.page = "admin_login"
        st.rerun()

    st.sidebar.button("View TimeTable", on_click=set_page, args=['timetable'])



if __name__ == "__main__":
    main()

