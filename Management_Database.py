import sqlite3

connection = sqlite3.connect('management.db')
print('Database connection successful')


TABLE_NAME = 'employee_details'
EMP_ID = 'id'
EMP_NAME = 'name'
EMP_ADDRESS = 'address'
EMP_phone = 'phone'

create_table_query = " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + EMP_ID + \
                    " INTEGER PRIMARY KEY AUTOINCREMENT, " + EMP_NAME + " TEXT, " + \
                    EMP_ADDRESS + " TEXT, " + EMP_phone + " INTEGER );"

connection.execute(create_table_query)

print('Table created successfully')


def save_record(name,address,phone):
    detail_query = " INSERT INTO " + TABLE_NAME + " ( " + EMP_NAME + " , " + EMP_ADDRESS + \
               ", " + EMP_phone + " ) VALUES ( '" + name + "', '" + address + "', " + \
               str(phone) + " );"

    connection.execute(detail_query)


print('Values save successfully')


def display_records():

    detail_query = "SELECT * FROM " + TABLE_NAME + " ;"

    cursor = connection.execute(detail_query)
    return cursor
    # connection.commit()


