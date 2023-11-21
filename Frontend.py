import streamlit as st
import mysql.connector
import time
import pandas as pd

# Establish a connection to MySQL database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ajey@123",
        database="timetablemanager"
    )
except:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="adi1416",
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
    selected_option = st.radio("Select an option:", [
                               "Edit Student", "Edit Teacher", "Edit Subject", "Edit Room", "Edit Timeslot", "Edit Batch", "Generate timetable"])

    if selected_option == "Edit Student":
        edit_students()

    elif selected_option == "Edit Teacher":
        edit_teachers()

    elif selected_option == "Edit Subject":
        edit_subjects()


    elif selected_option == "Generate timetable":
        generate_timetable()

    if st.button("Logout", key="logout", on_click=lambda: st.rerun()):
        st.session_state.logged_in = False
        st.session_state.page = "admin_login"
        st.rerun()


def generate_timetable():
    pass


def edit_students():

    st.subheader("Edit Students")

    # Functionality Toggle Buttons
    selected_option = st.radio("Select Action", [
                               "Add Student", "Remove Student", "Update Student", "View student details"])

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
            df = pd.DataFrame([result], columns=['studentid',
                              'studentname', 'semester', 'section', 'batchid'])
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

    operation = st.radio("Select Action", [
                         "Add Teacher", "Remove Teacher", "Update Teacher", "View teacher details","leave"])

    if operation == "Add Teacher":
        add_teacher()
    elif operation == "Remove Teacher":
        remove_teacher()
    elif operation == "Update Teacher":
        update_teacher()
    elif operation == "View teacher details":
        view_teacher()
    elif operation == "leave":
        leave()


def leave():
    st.title("Leave")
    teacher_id = st.text_input("Teacher ID")
    days = [
        "Monday", 
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]
    wday = st.selectbox("which day you are taking leave?", days)



    # Query to get the classes taught by the teacher
    classes_query = f"""
    SELECT DISTINCT t.batchid
    FROM Teaches t
    WHERE t.teacherid = '{teacher_id}';
    """



    cursor.execute(classes_query)
    teacher_classes = cursor.fetchall()

    if not teacher_classes:
        st.warning("No classes found for the given teacher.")
        return
    
    for selected_class in [cls[0] for cls in teacher_classes]:
        # Query to get the time slots for the selected class on the specified day
        timeslots_query = f"""
        SELECT slot_id, room_id, batch_id, subjectcode, day, starttime, endtime
        FROM Timeslot
        WHERE batch_id = '{selected_class}';
        """
        cursor.execute(timeslots_query)
        class_timeslots = cursor.fetchall()

        if not class_timeslots:
            st.warning(f"No time slots found for {selected_class} on {day}.")
            continue

        # Add the selected time slots to the 'UpdatedTables' table

        for slot_id, room_id, batch_id, subjectcode, day, starttime, endtime in class_timeslots:
            insert_query = f"""
            INSERT INTO UpdatedTables (slot_id, room_id, batch_id, subjectcode, day, starttime, endtime)
            VALUES ({slot_id}, '{room_id}', '{batch_id}', '{subjectcode}', '{day}', '{starttime}', '{endtime}');
            """
            cursor.execute(insert_query)

        
        for selected_class in [cls[0] for cls in teacher_classes]:
            # Query to get the time slots for the selected class on the specified day
            timeslots_query = f"""
            SELECT slot_id, room_id, batch_id, subjectcode, day, starttime, endtime
            FROM UpdatedTables
            WHERE batch_id = '{selected_class}' AND day = '{wday}' AND subjectcode IN (
                SELECT subjectcode
                FROM Teaches
                WHERE teacherid = '{teacher_id}'
            );
            """
            cursor.execute(timeslots_query)
            class_timeslots = cursor.fetchall()

            if not class_timeslots:
                st.warning(f"No time slots found for {selected_class} on {day}.")
                continue

            # Delete the selected time slots from the 'UpdatedTables' table
            for slot_id, room_id, batch_id, subjectcode, day, starttime, endtime in class_timeslots:
                delete_query = f"""
                DELETE FROM UpdatedTables
                WHERE slot_id = {slot_id} AND batch_id = '{batch_id}' AND day = '{wday}' AND subjectcode = '{subjectcode}';
                """
                cursor.execute(delete_query)
    conn.commit()

    
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
            df = pd.DataFrame([result], columns=[
                              'teacherid', 'name', 'dept', 'email'])
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
    uid = st.text_input("Enter Student ID or BatchID")
    if uid:
        st.session_state.timetable_id = uid
    if st.session_state.timetable_id:
        st.write("Timetable for ", st.session_state.timetable_id)

    # Original Timetable Query
    if len(st.session_state.timetable_id) > 12:
        original_query = f"""
            SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname, t.batch_id
            FROM timeslot t
            JOIN subject s ON t.subjectcode = s.subjectcode
            WHERE t.batch_id IN
            (SELECT batchid FROM Student WHERE studentid = '{st.session_state.timetable_id}')
        """
    elif len(st.session_state.timetable_id) > 10:
        original_query = f"""
            SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname, t.batch_id
            FROM (SELECT * FROM timeslot
            NATURAL JOIN teaches
            WHERE timeslot.subjectcode = teaches.subjectcode
            AND batchid = batch_id AND teacherid='{st.session_state.timetable_id}') AS t
            NATURAL JOIN subject s
            WHERE t.subjectcode = s.subjectcode
        """
    else:
        original_query = f"""
            SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname, t.batch_id
            FROM timeslot t
            JOIN subject s ON t.subjectcode = s.subjectcode
            WHERE t.batch_id = '{st.session_state.timetable_id}'
        """

    cursor.execute(original_query)
    original_result = cursor.fetchall()
    updated_result = 0
    # Updated Timetable Query
    if len(st.session_state.timetable_id) <5:
        updated_query = f"""
            SELECT day, starttime, endtime, subjectcode, room_id, subjectcode, batch_id
            FROM UpdatedTables
            WHERE batch_id = '{st.session_state.timetable_id}'
        """
        cursor.execute(updated_query)
        updated_result = cursor.fetchall()


    if original_result or updated_result:
        st.write("Original Timetable:")
        display_timetable(original_result)

        if updated_result:
            st.write("\nUpdated Timetable:")
            display_timetable(updated_result)

    else:
        st.error("No entry found.")
        
def display_timetable(result):
    # Convert the result to a Pandas DataFrame
    df = pd.DataFrame(result, columns=[
                      'day', 'starttime', 'endtime', 'subjectcode', 'room_id', 'subjectname', 'batch_id'])

    # Display the DataFrame
    df['starttime'] = df['starttime'].astype(str)
    df['endtime'] = df['endtime'].astype(str)
    df['Timing'] = df['starttime'].str[-8:-3] + '-' + df['endtime'].str[-8:-3]

    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    df['day'] = pd.Categorical(
        df['day'], categories=day_order, ordered=True)

    if len(st.session_state.timetable_id) == 11:
        df['alloted'] = df['subjectname'] + \
            " [" + df['room_id'] + ']' + '(' + df['batch_id'] + ')'
    else:
        df['alloted'] = df['subjectname'] + " [" + df['room_id'] + ']'

    timetable = df.pivot(index='day', columns='Timing', values='alloted')
    timetable = timetable.reset_index()

    # Increase row height using custom CSS
    if not st.session_state.logged_in:
        st.dataframe(timetable, hide_index=True)
    else:
        updated_vals = st.data_editor(timetable, hide_index=True)


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
