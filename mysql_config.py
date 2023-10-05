import mysql.connector

conn = None


def setup_mysql():
    global conn

    if not conn:
        print('setting up mysql connection...')
        config = {
            'user': 'root',
            'password': '428493',
            'host': 'localhost',
            'database': 'flytranslate'
        }

        try:
            conn = mysql.connector.connect(**config)
            print('connection successful!')
        except Exception as e:
            print(f'{e}')

    return conn
