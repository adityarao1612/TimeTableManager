import streamlit as st
import mysql.connector
import time
import pandas as pd

# Establish a connection to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="adi1416",
    database="timetablemanager"
)
cursor = conn.cursor()


# check admin username and password:
def authenticate(username, password):
    query = f"SELECT * FROM admin WHERE username = '{
        username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result is not None


# Function to display the admin dashboard
def admin_dashboard():
    st.title("Admin Dashboard")
    st.write("welcome,", st.session_state.user[0])


def view_timetable():
    st.title("View TimeTable")
    uid = st.text_input("Enter Student ID or BatchID")
    if uid:
        st.session_state.timetable_id = uid
    if st.session_state.timetable_id:
        st.write("Timetable for ",
                 st.session_state.timetable_id)
    # Modify the SQL query to include JOIN with the subjects table
    if len(st.session_state.timetable_id) > 10:
        query = f"""
            SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname
            FROM timeslot t
            JOIN subject s ON t.subjectcode = s.subjectcode
            WHERE t.batch_id in
            (SELECT batchid from Student where studentid = '{st.session_state.timetable_id}')
        """
    else:
        query = f"""
            SELECT t.day, t.starttime, t.endtime, t.subjectcode, t.room_id, s.subjectname
            FROM timeslot t
            JOIN subject s ON t.subjectcode = s.subjectcode
            WHERE t.batch_id = '{st.session_state.timetable_id}'
        """

    cursor.execute(query)
    result = cursor.fetchall()

    if result:
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
