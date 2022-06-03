import mysql.connector

print("THIS SCRIPT ALLOWS YOU TO ESTABLISH A CONNECTION BETWEEN TWO DATABASES AND COPY titles TABLE.")

database1 = input("Input the name of the first database: ")
ip_addr1 = input("Input IP address of DB1: ")
port1 = input("Input port number of DB1: ")
user_name1 = input("Input username of DB1: ")
passwd1 = input("Input password of DB1: ")

database2 = input("Input the name of the second database: ")
ip_addr2 = input("Input IP address of DB2: ")
port2 = input("Input port number of DB2: ")
user_name2 = input("Input username of DB2: ")
passwd2 = input("Input password of DB2: ")

connection1 = mysql.connector.connect(host=ip_addr1, port=port1, user=user_name1, password=passwd1, database=database1)
connection2 = mysql.connector.connect(host=ip_addr2, port=port2, user=user_name2, password=passwd2, database=database2)
cur1 = connection1.cursor()
cur2 = connection2.cursor()

if connection1.is_connected() and connection2.is_connected():
    print("Connection established.")
    cur1.execute("SELECT * FROM titles")
    query1 = cur1.fetchall()

    for i in range(len(query1)):
        cur2.execute("INSERT INTO titles (emp_no, title, from_date, to_date) VALUES (%s, %s, %s, %s)", query1[i])
        connection2.commit()

    print("All data has been transferred.")


