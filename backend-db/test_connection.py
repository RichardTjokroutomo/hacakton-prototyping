import mysql.connector

# Connection details
host = '13.251.35.253'
host = 'localhost'
database = 'CARGO'
user = 'username'
password = 'password'
table = 'shipment'


def createEntry(location, origin, destination, status, name, customer_id, id_type, notes, flags):
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    
    cursor = connection.cursor()
    
    
    
    #query = f"INSERT INTO " + table + " (location, origin, destination, status, name, customer_id, id_type, notes, flags) VALUES ({location}, {origin}, {destination}, {status}, {name}, {customer_id}, {id_type}, {notes}, {flags})"
    query = "INSERT INTO " + table + " (location, origin, destination, status, name, customer_id, id_type, notes, flags) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d)" % (location, origin, destination, status, name, customer_id, id_type, notes, flags)
    print(query)
    cursor.execute(query)
    connection.commit()
    
    cursor.execute("SELECT * FROM " + table  + " ORDER BY rfid DESC LIMIT 1")
    rfid = cursor.fetchone()[0]
    
    cursor.close()
    connection.close()
    
    return rfid

def deleteEntry(rfid):
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    
    cursor = connection.cursor()
    cursor.execute("DELETE FROM " + table  + " WHERE rfid = " + str(rfid))
    connection.commit()
    cursor.close()
    connection.close()
    
    return

def getEntry(rfid):
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM " + table  + " WHERE rfid = " + str(rfid))
    
    fetch = cursor.fetchall()
    result = ()
    if(len(fetch)!=0):
        result = fetch[0]
        
    cursor.close()
    connection.close()
    
    #print(result)
    return result
    [(x, y), (x, y)]
def getAllEntry():
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM " + table)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    
    
    return result
    
deleteEntry(10)
getEntry(10)
#print(getAllEntry())
#print(createEntry('SHD', 'ASD', 'FGS', 'flying', 'Carl', '1234', 'passport', 'None', 0))
