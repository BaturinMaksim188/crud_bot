import sqlite3 as sql
from aiogram.dispatcher import FSMContext
from bot_dp import bot, admin_id


# open/create sql table
def sql_start():
    global base, cursor
    base = sql.connect("userdata.db")
    cursor = base.cursor()
    if base:
        print("DB connected")
    base.execute('CREATE TABLE IF NOT EXISTS userdata(userid TEXT, login TEXT, password TEXT, question TEXT, answer TEXT, datetime TEXT)')
    base.commit()


# sql add
async def sql_add_userdata(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO userdata VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


# sql add an application
async def sql_get_userdata(state):
    outlist = []
    async with state.proxy() as data:

        cursor.execute('SELECT login FROM userdata where userid = (?)', (data['userid'],))
        login = cursor.fetchall()
        for i in login:
            s = ''.join(i)
            outlist.append(s)

        cursor.execute('SELECT password FROM userdata where userid = (?)', (data['userid'],))
        password = cursor.fetchall()
        for i in password:
            s = ''.join(i)
            outlist.append(s)

        cursor.execute('SELECT question FROM userdata where userid = (?)', (data['userid'],))
        question = cursor.fetchall()
        for i in question:
            s = ''.join(i)
            outlist.append(s)

        cursor.execute('SELECT answer FROM userdata where userid = (?)', (data['userid'],))
        answer = cursor.fetchall()
        for i in answer:
            s = ''.join(i)
            outlist.append(s)

        cursor.execute('SELECT datetime FROM userdata where userid = (?)', (data['userid'],))
        datetime = cursor.fetchall()
        for i in datetime:
            s = ''.join(i)
            outlist.append(s)

        return outlist


# Deleting a record from the database and moving the index up
async def on_delete_func(state):
    async with state.proxy() as data:
        cursor.execute('DELETE from userdata where userid = (?)', (data['userid'],))
        base.commit()


async def check_user(msg):
    cursor.execute('SELECT userid FROM userdata')
    id = cursor.fetchall()
    for i in id:
        s = ''.join(i)
        if str(s) == str(msg):
            return True
    return False
