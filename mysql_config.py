import mysql.connector

conn = None

# Configurations hidden for safety
def setup_mysql():
    global conn

    if not conn:
        print('setting up mysql connection...')
        config = {
            'user': 'root',
            'password': 'pass',
            'host': 'localhost',
            'database': 'flytranslate'
        }

        try:
            conn = mysql.connector.connect(**config)
            print('connection successful!')
        except Exception as e:
            print(f'{e}')

    return conn
