import sqlite3
def get_pictures():
    # Соеденяемся с БД
    conn = sqlite3.connect("db galery crocodilo.db")

    cursor = conn.cursor()
    sql = "SELECT * FROM picture"

    result = cursor.execute(sql)

    data = result.fetchall()
    print(data)
get_pictures()