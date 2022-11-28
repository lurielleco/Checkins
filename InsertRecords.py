import sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def insert_checkin(conn, checkin):
    """
    Insert records into the Timesheet_checkin table
    """
    sql = ''' INSERT INTO Timesheet_checkin(id, user, date_checkin, hours,project)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, checkin)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"C:\Users\lurie\Documents\ThinkingMachines\ThinkingMachines_Proj\DataOpExam\db.sqlite3"

    # data
    checkins = pd.read_csv(r'C:\Users\lurie\Documents\ThinkingMachines\dailycheckins_updated.csv')
    # create a database connection
    conn = create_connection(database)
    with conn:
        # loop through rows of csv
        for i in checkins.itertuples(index=True, name='Pandas'):
            checkin = i
            ins_checkin = insert_checkin(conn, checkin)

if __name__ == '__main__':
    main()