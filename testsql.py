import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host = 'localhost',
                                         database = 'knn_daging',
                                         user = 'root',
                                         password = '')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print('Connected to MySQL Server version ', db_Info)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM data_mentah')
        record = cursor.fetchall()
        print(*record[0])
        # aList = list(record[0])
        # print("You're connected to database: ", aList)

except Error as e:
    print("Error while connecting to MySQL ", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")