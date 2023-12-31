import streamlit as st
import random
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
                               "Edit Student", "Edit Teacher","upload timetable"])

    if selected_option == "Edit Student":
        edit_students()

    elif selected_option == "Edit Teacher":
        edit_teachers()

    elif selected_option == "upload timetable":
        upload_timetable()

    if st.button("Logout", key="logout", on_click=lambda: st.rerun()):
        st.session_state.logged_in = False
        st.session_state.page = "admin_login"
        st.rerun()


def upload_timetable():
    st.title("Upload Timetable")
    st.write("Welcome,", st.session_state.user[0])

    # Add buttons
    selected_option = st.radio("Select an option:", [
                               "Upload Student", "Upload Teacher", "Upload Subject", "Upload Room", "Upload Timeslot"])

    if selected_option == "Upload Student":
        upload_student()

    elif selected_option == "Upload Teacher":
        upload_teacher()

    elif selected_option == "Upload Subject":
        upload_subject()

    elif selected_option == "Upload Room":
        upload_room()

    elif selected_option == "Upload Timeslot":
        upload_timeslot()



def upload_student():
    # upload csv file which contains student details
    st.title("Upload Student")
    st.write("Welcome,", st.session_state.user[0])

    # display example format df as in csv
    df = pd.DataFrame(columns=['studentid', 'name', 'semester', 'section', 'batchid'])
    df.loc[0] = ['1BM18CS001', 'Aditya', 5, 'A', '5A']
    df.loc[1] = ['1BM18CS002', 'Ajey', 5, 'A', '5A']

    st.dataframe(df)
    # upload csv file
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # print(df)
        for index, row in df.iterrows():
            # print(row['studentid'], row['name'], row['semester'], row['section'], row['batchid'])
            query = f"INSERT INTO Student VALUES ('{row['studentid']}', '{row['name']}', {row['semester']}, '{row['section']}', '{row['batchid']}')"
            # print("SQL Query:", query)
            cursor.execute(query)
            conn.commit()
        st.success("Student added successfully!")

def upload_teacher():
    # upload csv file which contains teacher details
    st.title("Upload Teacher")
    st.write("Welcome,", st.session_state.user[0])

    # display example format df as in csv
    df = pd.DataFrame(columns=['teacherid', 'name', 'dept', 'email'])
    df.loc[0] = ['1BM18CS001', 'Aditya', 'CSE', 'abc@gmail.com']
    
    st.dataframe(df)
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # print(df)
        for index, row in df.iterrows():
            # print(row['teacherid'], row['name'], row['dept'], row['email'])
            query = f"INSERT INTO Teacher VALUES ('{row['teacherid']}', '{row['name']}', '{row['dept']}', '{row['email']}')"
            # print("SQL Query:", query)
            cursor.execute(query)
            conn.commit()
        st.success("Teacher added successfully!")

def upload_subject():
    # upload csv file which contains subject details
    st.title("Upload Subject")
    st.write("Welcome,", st.session_state.user[0])
    # display example format df as in csv
    df = pd.DataFrame(columns=['subjectcode', 'subjectname', 'semester'])
    df.loc[0] = ['CS101', 'Computer Science', 5]
    df.loc[1] = ['CS102', 'Computer Science', 5]

    st.dataframe(df)

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # print(df)
        # NSERT INTO Subject (subjectcode, subjectname, semester
        for index, row in df.iterrows():
            # print(row['subjectcode'], row['subjectname'], row['semester'])
            query = f"INSERT INTO Subject VALUES ('{row['subjectcode']}', '{row['subjectname']}', {row['semester']})"
            # print("SQL Query:", query)
            cursor.execute(query)
            conn.commit()

        st.success("Subject added successfully!")

def upload_room():
    # upload csv file which contains room details
    st.title("Upload Room")
    st.write("Welcome,", st.session_state.user[0])

    # display example format df as in csv
    df = pd.DataFrame(columns=['room_id', 'capacity'])
    df.loc[0] = ['CS101', 40]
    df.loc[1] = ['CS102', 40]

    st.dataframe(df)

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # print(df)
        # INSERT INTO Classroom (room_id, capacity) VALUES
        for index, row in df.iterrows():
            # print(row['room_id'], row['capacity'])
            query = f"INSERT INTO Classroom VALUES ('{row['room_id']}', {row['capacity']})"
            # print("SQL Query:", query)
            cursor.execute(query)
            conn.commit()

        st.success("Room added successfully!")


def upload_timeslot():
    # upload csv file which contains timeslot details
    st.title("Upload Timeslot")
    st.write("Welcome,", st.session_state.user[0])

    # display example format df as in csv
    df = pd.DataFrame(columns=['slot_id', 'room_id', 'batch_id', 'subjectcode', 'day', 'starttime', 'endtime'])
    df.loc[0] = [1, 'CS101', '5A', 'CS101', 'Monday', '09:00:00', '10:00:00']
    df.loc[1] = [2, 'CS102', '5A', 'CS102', 'Monday', '10:00:00', '11:00:00']

    # upload teaches csv of teaches
    # uploaded_teaches_file = st.file_uploader("upload teaches a file")
    # st.dataframe(df)
    uploaded_file = st.file_uploader("upload timeslot a file")


    if uploaded_file is not None:
        dft = pd.read_csv(uploaded_file)
        # INSERT INTO Timeslot (slot_id, room_id, batch_id, subjectcode, day, starttime, endtime) VALUES
        if st.button("upload") :
            for index, row in dft.iterrows():
                    query = f"INSERT INTO Timeslot VALUES ({row['slot_id']}, '{row['room_id']}', '{row['batch_id']}', '{row['subjectcode']}', '{row['day']}', '{row['starttime']}', '{row['endtime']}')"
                    # print("SQL Query:", query)
                    query1 = f"INSERT INTO updatedtables VALUES ({row['slot_id']}, '{row['room_id']}', '{row['batch_id']}', '{row['subjectcode']}', '{row['day']}', '{row['starttime']}', '{row['endtime']}')"

                    cursor.execute(query)
                    conn.commit()
                    cursor.execute(query1)
                    conn.commit()
            st.success("Timeslot added successfully!")      


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
    rollno = st.text_input("SRN")
    name = st.text_input("Name")
    batchid = st.text_input("Batch ID")
    try:
        if st.button("Update Student"):
            query = f"UPDATE Student SET name = '{name}',semester={int(batchid[0])},section='{batchid[1]}', batchid = '{batchid}' WHERE studentid = '{rollno}'"
            cursor.execute(query)
            conn.commit()
            st.success("Student updated successfully!")
    except Exception as error:
        st.error(error)
    # Add functionality to edit student information in the database
    # You can use st.text_input, st.button, and other Streamlit components to create the form


def edit_teachers():
    st.subheader("Edit Teachers")

    # Add functionality to edit teacher information in the database
    # You can use st.text_input, st.button, and other Streamlit components to create the form

    operation = st.radio("Select Action", [
                         "Add Teacher", "Remove Teacher", "Update Teacher", "View teacher details", "leave"])

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
    st.title("Leave Management")

    # Sidebar menu for selecting leave operation
    leave_operation = st.radio("Select Leave Operation", [
                               "Add Leave", "Delete Leave"])

    if leave_operation == "Add Leave":
        add_leave()
    elif leave_operation == "Delete Leave":
        delete_leave()


def add_leave():
    st.subheader("Add Leave")
    teacher_id = st.text_input("Teacher ID")

    # Menu dropdown for selecting the day on leave
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]
    wday = st.selectbox("Select the day on leave:", days)

    # Button to confirm leave
    if st.button("Confirm Leave"):
        process_leave(teacher_id, wday)


def display_teachers_on_leave():
    # Fetch data from LeaveTable to display teachers on leave
    query = "SELECT teacher_id, leave_day FROM LeaveTable"
    cursor.execute(query)
    leave_data = cursor.fetchall()

    if leave_data:
        st.subheader("Teachers on Leave:")
        leave_df = pd.DataFrame(leave_data, columns=[
                                "Teacher ID", "Leave Day"])
        st.table(leave_df, hide_index=True)
    else:
        st.subheader("No teachers currently on leave.")


def delete_leave():
    st.subheader("Delete Leave")
    display_teachers_on_leave()

    teacher_id = st.text_input("Teacher ID")

    # Menu dropdown for selecting the day to delete leave
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]
    wday = st.selectbox("Select the day to delete leave:", days)

    # Call the stored procedure

    # Button to confirm leave deletion
    if st.button("Confirm Leave Deletion"):
        cursor.callproc("AfterLeaveInsertProcedure", (teacher_id, wday, '5A'))
        conn.commit()

        process_leave_deletion(teacher_id, wday)


def process_leave(teacher_id, wday):
    # Insert the teacher into the 'LeaveTable'
    insert_leave_query = f"""
    INSERT INTO LeaveTable (teacher_id, leave_day)
    VALUES ('{teacher_id}', '{wday}');
    """
    cursor.execute(insert_leave_query)
    conn.commit()

    st.success(f"Leave for Teacher {teacher_id} on {wday} processed successfully.")


def process_leave_deletion(teacher_id, wday):
    # Delete the teacher's leave from the 'LeaveTable'
    delete_leave_query = f"""
    DELETE FROM LeaveTable
    WHERE teacher_id = '{teacher_id}' AND leave_day = '{wday}';
    """
    cursor.execute(delete_leave_query)
    conn.commit()

    st.success(f"Leave deletion for Teacher {teacher_id} on {wday} processed successfully.")


def display_teachers_on_leave():
    # Fetch data from LeaveTable to display teachers on leave
    query = "SELECT teacher_id, leave_day FROM LeaveTable"
    cursor.execute(query)
    leave_data = cursor.fetchall()

    if leave_data:
        st.subheader("Teachers on Leave:")
        leave_df = pd.DataFrame(leave_data, columns=[
                                "Teacher ID", "Leave Day"])
        st.table(leave_df)
    else:
        st.subheader("No teachers currently on leave.")


def add_teacher():
    st.title("Add Teacher")

    name = st.text_input("Name")
    teacher_id = st.text_input("Teacher ID")
    department = st.text_input("Department")
    email = st.text_input("Email")

    if st.button("Add Teacher"):
        try:
            query = f"INSERT INTO Teacher VALUES ('{teacher_id}', '{name}', '{department}', '{email}')"

            cursor.execute(query)
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
            query = f"DELETE FROM Teacher WHERE teacherid =  '{teacher_id}'"
            cursor.execute(query)
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
            query = f"UPDATE Teacher SET name = '{name}',dept = '{department}', email '{email}' WHERE teacherid = '{teacher_id}')"
            cursor.execute(query)
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
            # group by:
            query = f"SELECT teacherid,count(*) FROM Teaches group by teacherid having teacherid = '{teacher_id}'"
            cursor.execute(query)
            result = cursor.fetchone()

            # Create DataFrame directly
            # df = pd.DataFrame([result], columns=[
            #                   'teacherid', 'count of classes teaching'])
            # s = pd.DataFrame
            st.write(result[0], "teaches", str(result[1]), "batches")

        else:
            st.error("No entry found.")


def edit_batches():
    st.subheader("Edit Batches")
    # Add functionality to edit batch information in the database
    # You can use st.text_input, st.button, and other Streamlit components to create the form


def view_timetable():

    if st.session_state.logged_in:
        # display all tables
        st.title("View Tables")
        # radio button to select table
        selected_option = st.radio("Select Table", [
                                   "Student", "Teacher", "Subject", "Room", "Timetable"])
        
        if selected_option == "Student":
            student_details()

        
        elif selected_option == "Teacher":
            # add drop down menu box for batch
            
            # display student table according to batch
            query = f"SELECT * FROM Teacher"
            cursor.execute(query)
            result = cursor.fetchall()
            df = pd.DataFrame(result, columns=[ 'teacherid', 'name', 'dept', 'email'])
            st.dataframe(df, hide_index=True)

        elif selected_option == "Subject":
            # add drop down menu box for batch
            
            # display student table according to batch
            query = f"SELECT * FROM Subject"
            cursor.execute(query)
            result = cursor.fetchall()
            df = pd.DataFrame(result, columns=[ 'subjectcode', 'subjectname', 'semester'])
            st.dataframe(df, hide_index=True)

        elif selected_option == "Room":
            # add drop down menu box for batch
            
            # display student table according to batch
            query = f"SELECT * FROM Classroom"
            cursor.execute(query)
            result = cursor.fetchall()
            df = pd.DataFrame(result, columns=[ 'room_id', 'capacity'])
            st.dataframe(df, hide_index=True)

        elif selected_option == "Timetable":
            
            uid = st.text_input("Enter Student ID or BatchID")
            if uid:
                st.session_state.timetable_id = uid
            if st.session_state.timetable_id:
                st.write("Timetable for ", st.session_state.timetable_id)

            batch = False
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
                batch = st.session_state.timetable_id

            cursor.execute(original_query)
            original_result = cursor.fetchall()
            updated_result = 0

            # Updated Timetable Query

            if len(st.session_state.timetable_id) > 12:
                updated_query = f"""
                    SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname, t.batch_id
                    FROM UpdatedTables
                    JOIN subject s ON t.subjectcode = s.subjectcode
                    WHERE t.batch_id IN
                    (SELECT batchid FROM Student WHERE studentid = '{st.session_state.timetable_id}')
                """

            # NESTED AND JOIN
            elif len(st.session_state.timetable_id) > 10:
                updated_query = f"""
                    SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname, t.batch_id
                    FROM (SELECT * FROM UpdatedTables
                    NATURAL JOIN teaches
                    WHERE UpdatedTables.subjectcode = teaches.subjectcode
                    AND batchid = batch_id AND teacherid='{st.session_state.timetable_id}') AS t
                    NATURAL JOIN subject s
                    WHERE t.subjectcode = s.subjectcode
                """
            else:
                updated_query = f"""
                    SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname, t.batch_id
                    FROM UpdatedTables t
                    JOIN subject s ON t.subjectcode = s.subjectcode
                    WHERE t.batch_id = '{st.session_state.timetable_id}'
                """

                cursor.execute(updated_query)
                updated_result = cursor.fetchall()
                print(updated_result)
            if original_result or updated_result:
                st.write("Original Timetable:")
                updt = display_timetable(original_result, batch, "original")
                if updated_result:
                    st.write("\n Updated Timetable:")
                    updt = display_timetable(updated_result, batch, "updated")
                    # updt = display_timetable(original_result, batch)

                if st.button("update"):
                    print("\n\n\n\n\n-------\n\n\n")
                    # print(updt)
                    update_table(updt, batch)

            else:
                st.error("No entry found.")



    else:
        st.title("View TimeTable")
            
        uid = st.text_input("Enter Student ID or BatchID")
        if uid:
            st.session_state.timetable_id = uid
        if st.session_state.timetable_id:
            st.write("Timetable for ", st.session_state.timetable_id)

        batch = False
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
            batch = st.session_state.timetable_id

        cursor.execute(original_query)
        original_result = cursor.fetchall()
        updated_result = 0

        # Updated Timetable Query

        if len(st.session_state.timetable_id) > 12:
            updated_query = f"""
                SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname, t.batch_id
                FROM UpdatedTables
                JOIN subject s ON t.subjectcode = s.subjectcode
                WHERE t.batch_id IN
                (SELECT batchid FROM Student WHERE studentid = '{st.session_state.timetable_id}')
            """

        # NESTED AND JOIN
        elif len(st.session_state.timetable_id) > 10:
            updated_query = f"""
                SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname, t.batch_id
                FROM (SELECT * FROM UpdatedTables
                NATURAL JOIN teaches
                WHERE UpdatedTables.subjectcode = teaches.subjectcode
                AND batchid = batch_id AND teacherid='{st.session_state.timetable_id}') AS t
                NATURAL JOIN subject s
                WHERE t.subjectcode = s.subjectcode
            """
        else:
            updated_query = f"""
                SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname, t.batch_id
                FROM UpdatedTables t
                JOIN subject s ON t.subjectcode = s.subjectcode
                WHERE t.batch_id = '{st.session_state.timetable_id}'
            """

            cursor.execute(updated_query)
            updated_result = cursor.fetchall()
            print(updated_result)
        if original_result or updated_result:
            st.write("Original Timetable:")
            updt = display_timetable(original_result, batch, "original")
            if updated_result:
                st.write("\n Updated Timetable:")
                updt = display_timetable(updated_result, batch, "updated")
                # updt = display_timetable(original_result, batch)

            if st.button("update"):
                print("\n\n\n\n\n-------\n\n\n")
                # print(updt)
                update_table(updt, batch)

        else:
            st.error("No entry found.")


    

def student_details():
    # add drop down menu box for batch
            batches = st.selectbox("Select Batch", [
                                 "5A", "5B", "5C", "5D", "5E", "5F"])
            
            # display student table according to batch
            query = f"SELECT * FROM Student WHERE batchid = '{batches}'"
            cursor.execute(query)
            result = cursor.fetchall()
            df = pd.DataFrame(result, columns=[
                              'studentid', 'studentname', 'semester', 'section', 'batchid'])
            st.dataframe(df, hide_index=True)
 


 
def update_table(updated_vals, batchid):
    #     # Assuming updated_vals is a list of dictionaries
    #     # Example: [{'day': 'Monday', 'timing': '09:00-10:00', 'alloted': 'Subject [Room] (Batch)'}]

    #     tuples_list = [tuple(x)
    #                    for x in updated_vals.itertuples(index=False, name=None)]
    #     # column_names_tuple = tuple(updated_vals.columns)

    #     # timeslot = column_names_tuple[1:]
    #     # print(timeslot)
    #     # print(tuples_list)
    #     slotid = 1
    #     for day, *values in tuples_list:
    #         for subject in values:
    #             if subject:
    #                 try:
    #                     subjectNAME, room_id = subject.split(' [')
    #                     room_id = room_id[0:-1]
    #                     # print(tuple((slotid, subjectcode, room_id)))
    #                     # print(subject.split('['))
    #                     query = f"""
    #                     SELECT subjectcode from subject where subject.subjectname = '{subjectNAME}'
    #                     """
    #                     # print(batchid)
    #                     cursor.execute(query)
    #                     # print(query)
    #                     subjectcode = cursor.fetchone()[0]
    #                     # conn.commit()

    #                     print(subjectcode)
    #                     query = f"""
    #                     UPDATE UpdatedTables
    #                     SET room_id = '{room_id}',
    #                     subjectcode = '{subjectcode}'
    #                     WHERE slot_id = {slotid} AND batch_id = '{batchid}';
    #                     """
    #                     # print(batchid)
    #                     cursor.execute(query)
    #                     # print(query)
    #                     conn.commit()

    #                 except Exception as error:
    #                     st.error(error)
    #                 slotid = slotid+1
    #     st.success("Student updated successfully!")

    tuples_list = [tuple(x)
                   for x in updated_vals.itertuples(index=False, name=None)]
    # column_names_tuple = tuple(updated_vals.columns)

    # timeslot = column_names_tuple[1:]
    # print(timeslot)
    # print(tuples_list)
    slotid = 1
    for day, *values in tuples_list:
        for subject in values:
            if subject:
                try:
                    subjectNAME, room_id = subject.split(' [')

                    room_id = room_id[0:-1]
                    # print(tuple((slotid, subjectcode, room_id)))
                    # print(subject.split('['))
                    query = f"""
                    SELECT subjectcode from subject where subject.subjectname = '{subjectNAME}'
                    """
                    # print(batchid)
                    cursor.execute(query)
                    # print(query)
                    subjectcode = cursor.fetchone()[0]
                    # conn.commit()

                    # print(subjectcode)

                    query = f"""
                    Select slot_id from UpdatedTables
                    WHERE batch_id = '{batchid}';
                    """
                    cursor.execute(query)
                    exists = cursor.fetchall()
                    existingid = [x[0] for x in exists]
                    print(slotid in existingid, slotid)

                    if not (slotid in existingid):

                        query = f"""
                            INSERT INTO UpdatedTables (slot_id, room_id, batch_id, subjectcode, day, starttime, endtime)
                            SELECT *
                            FROM Timeslot ts
                            WHERE ts.batch_id = '{batchid}' and ts.slot_id={slotid};
                            """
                        cursor.execute(query)
                        conn.commit()

                    query = f"""
                        UPDATE UpdatedTables
                        SET room_id = '{room_id}',
                        subjectcode = '{subjectcode}'
                        WHERE slot_id = {slotid} AND batch_id = '{batchid}';
                        """
                    # print(batchid)
                    cursor.execute(query)
                    # print(query)
                    conn.commit()

                except Exception as error:
                    st.error(error)
                slotid = slotid+1
    st.success("Student updated successfully!")


def display_timetable(result, batch, s):
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
        updated_vals = st.data_editor(
            timetable, key='data_editor'+s, hide_index=True)
        # st.write(updated_vals)
        return updated_vals


def signup(username, password):

    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="adi1416",
    #     database="timetablemanager"
    # )

    query = f"""
            INSERT INTO admin (username, password, role) VALUES
            ('{username}','{password}', 'admin');')"""
    # print("SQL Query:", query)

    cursor.execute(query)
    conn.commit()
    st.success("Student added successfully!")


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

                # print("SQL Query:", query)
                signup(username, password)
                st.success("Signup successful! You can now login.")

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
