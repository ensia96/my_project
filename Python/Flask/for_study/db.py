import pymysql

db_set = {
    "host": "wecode-project.cyfp0gaqdrrv.ap-northeast-2.rds.amazonaws.com",
    "user": "root",
    "pswd": "dptmzbdpf",
    "base": "converse",
    "cset": "utf8mb4",
}


class DatabaseForFlask:
    def __init__(self, db_set):
        self.conn = pymysql.connect(
            host=db_set["host"],
            user=db_set["user"],
            password=db_set["pswd"],
            db=db_set["base"],
            charset=db_set["cset"],
        )
        self.curs = self.conn.cursor()

    # this is for reading
    def get(self, target):

        self.curs.execute(f"show full columns from {target}")
        a = [i[0] for i in self.curs.fetchall()][1:]
        print(a)
        self.curs.execute(f"select * from {target}")
        b = [j for i in [i[1:] for i in self.curs.fetchall()] for j in i]

    "c", "r", "u", "d"


db = DatabaseForFlask(db_set)

db.get("products")
