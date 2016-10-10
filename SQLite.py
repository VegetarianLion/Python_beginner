
Python 3.4.2 (default, Oct 19 2014, 13:31:11)
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
<sqlite3.Cursor object at 0x74d423a0>
>>> cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
<sqlite3.Cursor object at 0x74d423a0>
>>> cursor.rowcount
1
>>> cursor.close()
>>> conn.commit()
>>> conn.close()
>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
>>> cursor.execute('select * from user where id=?', ('1',))
<sqlite3.Cursor object at 0x74d424a0>
>>> values = cursor.fetchall()
>>> values
[('1', 'Michael')]
>>> cursor.close()
>>> conn.close()
