from utilities.configurations import *


conn = open_dbConnection()
print(conn.is_connected())

cursor = conn.cursor()

# Fetch
cursor.execute('select * from CustomerInfo')
row = cursor.fetchone()  # cursor is here so it will skip first record after if u use fetch all
print(row)
print(row[3])
rowAll = cursor.fetchall()
print(rowAll)
print(rowAll[1][0])

cursor.execute('select Amount from CustomerInfo')
values = cursor.fetchall()
print(values)
sum = 0
for val in values:
    sum += val[0]
print(sum)
assert sum == 241

# Update
query = 'update CustomerInfo set Location = %s where CourseName = %s;'
data = ('UK', 'Jmeter')
cursor.execute(query, data)
conn.commit()

cursor.execute('select * from CustomerInfo')
d = cursor.fetchall()
print(d)

# Delete
# query = "delete from %s where courseName = %s;"
# data = ('customerInfo', 'Protractor')
# cursor.execute(query, data)
# conn.commit()
#
# cursor.execute('select * from CustomerInfo')
# d = cursor.fetchall()
# print(d)

conn.close()