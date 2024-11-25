import sqlite3 as sqlite
import traceback

connection = None
cursor = None

def initDBConnection():
    global connection, cursor
    connection = sqlite.connect("medimanager_db.db")
    cursor = connection.cursor()
    createDoctorTable()
    createPatientTable()
    createBedTable()  # Ensure bed table creation
    createBillingTable()  # Ensure billing table creation

def createDoctorTable():
    global connection, cursor
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS DOCTOR (
        name TEXT NOT NULL,
        specialization TEXT NOT NULL,
        mobile TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """
    try:
        cursor.execute(create_table_sql)
        connection.commit()
    except Exception as e:
        print(e)
        traceback.print_exc()

def createPatientTable():
    global connection, cursor
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS PATIENT (
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        diagnosis TEXT NOT NULL,
        admission_date TEXT NOT NULL,
        discharge_date TEXT NOT NULL
    );
    """
    try:
        cursor.execute(create_table_sql)
        connection.commit()
    except Exception as e:
        print(e)
        traceback.print_exc()

def createBedTable():
    global connection, cursor
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS BED (
        single INTEGER NOT NULL,
        twin_sharing INTEGER NOT NULL,
        dormitory INTEGER NOT NULL,
        icu INTEGER NOT NULL
    );
    """
    try:
        cursor.execute(create_table_sql)
        connection.commit()
    except Exception as e:
        print(e)
        traceback.print_exc()

def createBillingTable():
    global connection, cursor
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS BILLING (
        patient_name TEXT NOT NULL,
        doctor_fees FLOAT NOT NULL,
        bed_charges FLOAT NOT NULL,
        medicine_cost FLOAT NOT NULL,
        miscellaneous FLOAT NOT NULL
    );
    """
    try:
        cursor.execute(create_table_sql)
        connection.commit()
    except Exception as e:
        print(e)
        traceback.print_exc()

def add_doctor(name, specialization, mobile, email):
    global connection, cursor
    PARAMETERS = (name, specialization, mobile, email)
    SQL = "INSERT INTO DOCTOR (name, specialization, mobile, email) VALUES (?, ?, ?, ?)"
    try:
        cursor.execute(SQL, PARAMETERS)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

def add_patient(name, age, gender, diagnosis, admission_date, discharge_date):
    global connection, cursor
    PARAMETERS = (name, age, gender, diagnosis, admission_date, discharge_date)
    SQL = "INSERT INTO PATIENT (name, age, gender, diagnosis, admission_date, discharge_date) VALUES (?, ?, ?, ?, ?, ?)"
    try:
        cursor.execute(SQL, PARAMETERS)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        traceback.print_exc()
        return False

def closeDBConnection():
    global connection, cursor
    cursor.close()
    connection.close()

# Initialize the database connection
initDBConnection()

# Close the database connection
closeDBConnection()
