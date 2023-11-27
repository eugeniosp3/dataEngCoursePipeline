import mysql.connector
import json
from dbCreds import USERNAME, PASSWORD, HOST, DATABASE, PORT

dbConfiguration = {
    'user': USERNAME,
    'password': PASSWORD,
    'host': HOST,
    'database': DATABASE,
    'port': PORT,
    "raise_on_warnings": True
}


def writeDataToDB(df, query_function, config=dbConfiguration):
    """
    df = dataframe
    config = dbConfiguration, holding password username and all of the stuff needed to connect to the database
    """
    # Parse the JSON data
    data = df
    print("Data Parsed to JSON")

    sql_query, data_passed = query_function(data)
    print("Read Query from Function")
    # Connect to the database
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Insert data into deviceInformation table

    cursor.execute(sql_query, data_passed)
    print("Executing Query")
    # Commit and close
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Successfully Inserted/Updated Data")
    return {
        'statusCode': 200,
        'body': json.dumps('Device information inserted/updated successfully')
    }


# write mysql function that tests the connection to the database
def testDatabaseConnection(config=dbConfiguration):
    """
    Tests Connection to Database -- 

    Test: Connection Passed We're good to go to start writing.
    """
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("describe deviceInformation")
    result = cursor.fetchone()
    return result

    print("Connection Passed")
