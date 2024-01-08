import mysql.connector


def create_connector(host: str, user: str, password: str, database: str):
    database = mysql.connector.connect (
        host = host,
        user = user,
        password = password,
        database = database
    )
    return database

connector = create_connector('localhost', 'root', 'depgcP@123', 'video_games')
cursor = connector.cursor()
cursor.execute('SELECT * FROM game_publisher')
result = cursor.fetchall()

for row in result:
    print(row)
