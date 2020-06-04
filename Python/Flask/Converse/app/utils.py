import pymysql

from setting import db_set


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

    order = {
        "table_name": "mango",
        "columns": [["name", "varchar(20)", True],],
    }

    def make_table(self, order):
        self.curs.execute(f"create table {order.table_name} ()")

    # this is for reading
    def get(self, target):

        self.curs.execute(f"show full columns from {target}")
        a = [i[0] for i in self.curs.fetchall()][1:]
        print(a)
        self.curs.execute(f"select * from {target}")
        b = [j for i in [i[1:] for i in self.curs.fetchall()] for j in i]

    # now on working -> read
    # create
    # read
    # update
    # delete


# from here, you're in testing zone

db = DatabaseForFlask(db_set)

db.get("products")
