import sqlite3


con = sqlite3.connect('sql_bd.sqlite')  # подключение или создание
cur = con.cursor()  # курсор

res = cur.execute("""select * from films where year=? and duration>90""", (2010, )).fetchall()
print(len(res))
print(*(i for i in res), sep='\n')

cur.execute("""insert into genres values (43,'байки'), (44,'басни')""")
cur.execute("""update films SET duration='283' where title='Аватар'""")
cur.execute("""delete from genres where id=44""")


# create new table

cur.execute("""create table if not exists users(userid int primary key, fname text, lname text, gender text)""")
cur.execute("""create table if not exists orders(orderid int primary key, date date, userid int, total real)""")

cur.execute("""delete from users"""), cur.execute("""delete from orders""")

user = [(1, 'John', 'Smith', 'male'), (2, 'Lois', 'Griffin', 'male'), (3, 'Kara', 'Voug', 'female'),
        (4, 'Elena', 'Gilbert', 'female'), (5, 'Stefan', 'Salvatore', 'male'), (6, 'Karoline', 'Forbes', 'female')]
cur.executemany("""insert into users values (?,?,?,?)""", user)

order = [(1, '12.01.2022', 1, 3000.50), (2, '14.01.2022', 2, 120.99), (3, '16.01.2022', 3, 1500),
         (4, '18.01.2022', 4, 50.50), (5, '20.01.2022', 5, 1800), (6, '29.04.1999', 2, 600.90)]
cur.executemany("""insert into orders values (?,?,?,?)""", order)

a = cur.execute('select sum(total) from orders where userid=(select userid from users where fname="Lois")').fetchall()
b = cur.execute('select users.fname, users.lname from orders left join users on users.userid = orders.userid').fetchall()
c = cur.execute('select fname, lname from users where userid=(select userid from orders where total=1800)').fetchall()
d = cur.execute('select fname, lname from users where userid=(select userid from orders where total=1800)').fetchall()[0]
e = cur.execute('select max(userid) from users').fetchone()

cur.execute(f'insert into users (userid, fname, lname, gender) values({e[0]+1}, "Mann", "Unn", "male")')

print(a[0][0], b, c[0], d, *e, sep='\n')

con.commit()
con.close()
