import pymysql
db_host = 'instancia-290.clmgw0m0cn3m.us-east-1.rds.amazonaws.com'
db_user = 'Andres'
db_passw = 'Redbogota1'

try:
    connection = pymysql.connect (
        host = db_host,
        user = db_user,
        password = db_passw
    )
    print ("succesful connection to database")
except Exception as err:
    print("Error:", err)
    connection = None
def add_user():
    instruction_sql = "insert into db_users.users(id, actividad, name, fecha) values (1,'ANDRES', 'VELANDIA', '1990-09-26')"
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        connection.commit()
        print("user added")
    except Exception as err:
        print("Error:",err)
