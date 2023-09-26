import sqlite3

def tuple2list(tuple_item):
    return [*tuple_item,]



def part_1_initialisation():
    con = sqlite3.connect("tp_pass_force.db")
    cur = con.cursor()

    #cur.execute("CREATE TABLE user(login, password)")
    cur.execute("INSERT INTO user(login, password) VALUES ('Bob','123456'),('Tom','azerty'),('Tim','marseille1993'),('Kay','dauphinBleu'),('Zed','dragon42'),('May','naruto#7')")
    res = cur.execute("SELECT * FROM user")
    fetch = res.fetchall()

    for item in fetch:
        print(item[1])
    return fetch