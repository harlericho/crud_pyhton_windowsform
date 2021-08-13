from config import get_connection

def get_list():
    try:
        db= get_connection()
        cur = db.cursor()
        cur.execute("SELECT * FROM persons")
        return cur.fetchall()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def save_data(names, email):
    try:
        db = get_connection()
        cur = db.cursor()
        sql = "INSERT INTO persons (names,email) VALUES(?,?)"
        cur.execute(sql, [names, email])
        db.commit()
        return True
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def update_data(names, email, id):
    try:
        db = get_connection()
        cur = db.cursor()
        sql = "UPDATE persons SET names=?, email=? WHERE id=?"
        cur.execute(sql, [names, email,id])
        db.commit()
        return True
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def delete_data(id):
    try:
        db = get_connection()
        cur = db.cursor()
        sql ="DELETE FROM persons WHERE id =?"
        cur.execute(sql, [id])
        data =db.commit()
        return True
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()