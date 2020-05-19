import pymysql


# 앱 시크릿코드
def secret_code():
    return b'_5#y2L"F4Q8Az\n\xec]/'

# select 용
def sql_init():
    # MySQL Connection 연결
    conn = pymysql.connect(host='db.hana6927.gabia.io', user='hana6927', password='hana1209!@',
                           db='dbhana6927', charset='utf8')

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()
    return curs

# update, insert, del 용
def sql_commit():
    # MySQL Connection 연결
    conn = pymysql.connect(host='db.hana6927.gabia.io', user='hana6927', password='hana1209!@',
                           db='dbhana6927', charset='utf8')

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()
    return conn,curs


def version_check(version):
    # user table에 id version 으로 md5안걸고 해놓음
    curs = sql_init()
    sql = "select * " \
          " from mymedicine_user " \
          " where ID='version' and PWD='" + str(version) + "'; "
    curs.execute(sql)
    rows = curs.fetchall()
    cnt = len(rows)
    print(int(cnt))
    if int(cnt) == 1:
        return True
    else:
        return False

