import pymysql

def prof_id(user_name, sifra):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
    "SELECT * " \
    "FROM eone.profesor " \
    "WHERE user_name = %s " \
    "AND sifra = %s"

    cursor.execute(sql, (user_name, sifra))
    result = cursor.fetchall()
    if len(result) > 0:
        return result[0][0]
    else:
        raise ValueError("pogresan login")

def stud_id(indeks, sifra):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
          "SELECT * " \
          "FROM eone.student " \
          "WHERE indeks = %s " \
          "AND sifra = %s"

    cursor.execute(sql, (indeks, sifra))
    result = cursor.fetchall()
    if len(result) > 0:
        return result[0][0]
    else:
        raise ValueError("pogresan login")

def pred_id(naziv):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
    "SELECT * " \
    "FROM eone.predmet " \
    "WHERE naziv = %s"

    cursor.execute(sql, naziv)
    result = cursor.fetchall()
    if len(result) > 0:
        return result[0][0]
    else:
        raise ValueError("nepostojeci predmet")

def rac_id(kod):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
    "SELECT * " \
    "FROM eone.racunar " \
    "WHERE kod = %s"

    cursor.execute(sql, kod)
    result = cursor.fetchall()
    if len(result) > 0:
        return result[0][0]
    else:
        raise ValueError("nepostojeci racunar")

def rac_stud_id(id_rac):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
    "SELECT * " \
    "FROM eone.koristi " \
    "WHERE id_rac = %s"

    cursor.execute(sql, id_rac)
    result = cursor.fetchall()
    if len(result) > 0:
        return result[0][1]
    else:
        raise ValueError("racunar nije zauzet")

def stud_stream_ip(id_stud):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
    "SELECT stream.id, stream.ip " \
    "FROM eone.pohadja, eone.predavanje, eone.stream " \
    "WHERE stream.id = predavanje.id_strm " \
    "AND predavanje.id_pred = pohadja.id_pred " \
    "AND pohadja.id_stud = %s"

    cursor.execute(sql, id_stud)
    result = cursor.fetchall()
    if len(result) > 0:
        return result[0][0], result[0][1]
    else:
        raise ValueError("nema aktivnog streama za datog studenta")

def provera_prof_pred(id_prof, id_pred):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
          "SELECT * " \
          "FROM eone.predaje " \
          "WHERE id_prof = %s " \
          "AND id_pred = %s "

    cursor.execute(sql, (id_prof, id_pred))
    result = cursor.fetchall()
    if len(result) > 0:
        return
    else:
        raise ValueError("profesor ne predaje dati predmet")

def rac_zauzet(id_rac):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
          "SELECT * " \
          "FROM eone.koristi " \
          "WHERE id_rac = %s "

    cursor.execute(sql, id_rac)
    result = cursor.fetchall()
    if len(result) > 0:
        raise ValueError("racunar je zauzet")

def unesi_stream(ip):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
          "INSERT INTO eone.stream " \
          "(ip) " \
          "VALUES (%s) "

    cursor.execute(sql, ip)
    conn.commit()
    id = cursor.lastrowid
    conn.close()
    return id

def unesi_predavanje(id_pred, id_strm):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
          "INSERT INTO eone.predavanje " \
          "(id_pred, id_strm) " \
          "VALUES (%s, %s) "

    cursor.execute(sql, (id_pred, id_strm))
    conn.commit()
    conn.close()

def unesi_koristi(id_stud, id_rac):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
          "INSERT INTO eone.koristi " \
          "(id_stud, id_rac) " \
          "VALUES (%s, %s) "

    cursor.execute(sql, (id_stud, id_rac))
    conn.commit()
    conn.close()

def unesi_prisustvo(id_stud, id_strm):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
          "INSERT INTO eone.prisustvo " \
          "(id_stud, id_strm) " \
          "VALUES (%s, %s) "

    cursor.execute(sql, (id_stud, id_strm))
    conn.commit()
    conn.close()

def stream_pokrenut(ip):
    conn = pymysql.connect(user="root", password="", host="localhost", database="eone")
    cursor = conn.cursor()

    sql = "" \
          "SELECT * " \
          "FROM eone.stream " \
          "WHERE ip = %s "

    cursor.execute(sql, ip)
    result = cursor.fetchall()
    return len(result) > 0

def all_users():
    sql = "" \
          "SELECT users.name, users.completeName, userstatuses.name, defaultstatuses.description, users.isDisturbing, users.actualNoiseLevel " \
          "FROM rnds.users " \
          "left JOIN rnds.userstatuses on  users.actualUserStatus = userstatuses.name " \
          "left JOIN rnds.defaultstatuses on userstatuses.Defaultstatus = defaultstatuses.name "
    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()
    users = []
    for t in result:
        user = {}
        user["userID"] = str(t[0])
        user["userName"] = t[1]
        user["currentStatusID"] = t[2]
        user["currentStatus"]= t[3]
        user["disturbing"]= t[4]
        user["noiseLevel"]=t[5]
        users.append(user)

    conn.close()
    return users

def put_user_status(username, status):
    sql1 = "UPDATE rnds.users set actualUserStatus=%s WHERE name = %s"

    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql1, (status, username))
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

def getUserNoiseLevel(name):
    sql1 = "SELECT users.name, users.actualUserStatus, lu_noise.dbmax " \
           "FROM rnds.users " \
           "LEFT JOIN rnds.usersettings on users.actualUserStatus = usersettings.name " \
           "LEFT JOIN rnds.lu_noise on lu_noise.name = usersettings.noiseLevel " \
           "WHERE users.name = %s"
    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")
    cursor = conn.cursor()
    cursor.execute(sql1, name)
    result = cursor.fetchall()
    conn.close()
    for t in result:
          NoiseLevel = {}
          NoiseLevel["userID"] = str(t[0])
          NoiseLevel["actualUserStatus"] = str(t[1])
          NoiseLevel["dbMax"] = t[2]
    return NoiseLevel