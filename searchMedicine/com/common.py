import re
from flask import session
from com.sqlinit import sql_init, sql_commit


def login_result(result):
    user_id = result['user_id']
    user_pw = result['user_pw']

    # SQL문 실행
    curs = sql_init()
    sql = "select * " \
          " from mymedicine_user " \
          " where ID='" + user_id + "' and PWD=md5('"+user_pw+"'); "  # "LIMIT 100"
    curs.execute(sql)
    rows = curs.fetchall()
    cnt  = len(rows)
    if int(cnt) == 1:
        session['user_id'] = user_id
        session['user_name'] = rows[0][2]
        session['level'] = rows[0][3]
        return_txt = "login"
    else:
        return_txt = "Dot"
    return return_txt


def logout_result():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('level', None)
    return


def session_check():
    if 'user_id' in session and 'level' in session:
        return True
    else:
        return False

# 텍스트에 포함되어 있는 특수 문자 제거
def cleanText(readData):
    # 텍스트에 포함되어 있는 특수 문자 제거
    #text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    text = re.sub('[\\‘`\'…》,]', '', readData)
    # 앞뒤공백 제거
    text = text.strip()
    text = text.replace("nan","")
    return text

# 순서유지 LIST 중복 제거
def OrderedSet(list):
    my_set = set()
    res = []
    for e in list:
        if e not in my_set:
            res.append(e)
            my_set.add(e)
    return res

# 사용자 정보 변경
def chg_user_info(mode, id, pwd, name, level):
    sql = ""
    conn, curs = sql_commit()
    if mode == "chg_pwd":
        sql = "update mymedicine_user " \
              "set PWD = md5('"+pwd+"') " \
              " where ID='"+id+"'"

    if mode == "E":
        sql = "update mymedicine_user " \
              "set PWD = md5('"+pwd+"') " \
              ", NAME = '"+name+"' " \
              ", LEVEL = '"+level+"' " \
              " where ID='"+id+"'"
    if mode == "I":
        sql = "insert into mymedicine_user " \
              "(ID, PWD, NAME, LEVEL) " \
              "values ('"+id+"',md5("+pwd+"),'"+name+"','"+level+"')"
    if mode == "D":
        sql = "delete from mymedicine_user " \
              " where ID='"+id+"'"

    curs.execute(sql)
    # 데이터 변화 적용
    conn.commit()

    return "ok"

#계정 리스트 레벤 5이하만 볼수있음
def user_list_select(level):
    if level < 5:
        curs = sql_init()
        sql = "select * " \
              " from mymedicine_user " \
              " where  ID <> 'version' and ID <> 'admin' ORDER BY ID DESC;"

        curs.execute(sql)

        # 데이타 Fetch
        rows = curs.fetchall()

        return rows
