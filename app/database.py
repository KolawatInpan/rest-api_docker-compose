import mysql.connector
import json
import os


def ConnectorMysql():
    host = os.environ.get('DATABASE_HOST')
    user = os.environ.get('DATABASE_USER')
    password = os.environ.get('DATABASE_PASSWORD')
    database = os.environ.get('DATABASE_NAME')
    if not all([host, user, password, database]):
        raise ValueError(
            "One or more required environment variables are missing",
            f"DATABASE_HOST: {host}",
            f"DATABASE_USER: {user}",
            f"DATABASE_PASSWORD: {password}",
            f"DATABASE_NAME: {database}")

    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        auth_plugin='mysql_native_password'
    )
    return mydb


def get_all_users():
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return result


def get_user(uid):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    query = "SELECT * FROM users WHERE uid = %s"
    cursor.execute(query, (uid,))
    result = cursor.fetchone()
    return result


def create_user(name, email):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    mydb.commit()
    return "User created successfully!"


def update_user(uid, name, email):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    query = "UPDATE users SET name = %s, age = %s WHERE uid = %s"
    cursor.execute(query, (name, email, uid))
    mydb.commit()
    return "User updated successfully!"


def delete_user(uid):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    query = "DELETE FROM users WHERE uid = %s"
    cursor.execute(query, (uid,))
    mydb.commit()
    return "User deleted successfully!"
