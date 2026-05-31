import sqlite3

connection = sqlite3.connect(" videos.sq3", 5)

cur = connection.cursor()

# cur.execute("CREATE TABLE many_videos (name TEXT, duration TEXT, size)")
cur.execute("INSERT INTO many_videos (name, duration, size) VALUES (\"First_video\", \"30:00\", \"4GB\")")
cur.execute("SELECT name, duration, size FROM many_videos WHERE duration==\"20:00 \";")

print(cur.fetchall())

connection.commit()
connection.close()