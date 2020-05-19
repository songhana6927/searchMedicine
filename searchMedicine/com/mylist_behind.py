import time

from flask import session

from com.sqlinit import sql_init, sql_commit
from com.common import cleanText


def mylist_select(u_id):
    # SQL문 실행
    curs = sql_init()
    sql = "select * " \
          " from mymedicine_product " \
          " where INSERT_ID='" + u_id + "' and USE_YB='Y' "  # "LIMIT 100"
    curs.execute(sql)

    # 데이타 Fetch
    rows = curs.fetchall()
    # 전체 rows
    # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
    # print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')

    return rows


def myMedi_select(ingredient):
    # SQL문 실행
    curs = sql_init()
    ingredient_replace = ingredient.replace(" ", "").replace(",", "").lower()
    sql = "select * " \
          " from mymedicine_product " \
          " where USE_YB='Y' and LOWER(replace(INGREDIENT,' ','')) LIKE '%" + ingredient_replace + "%' ORDER BY YOYUL DESC"

    curs.execute(sql)

    # 데이타 Fetch
    rows = curs.fetchall()
    # 전체 rows
    # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
    # print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')

    return rows


def mylist_upload(u_id, upload_file):
    NO = upload_file['NO']
    BOKGI = upload_file['복지분류']
    CATEGORY_1 = upload_file['대분류']
    CATEGORY_2 = upload_file['소분류']
    CATEGORY_3 = upload_file['종류']
    SALARY = upload_file['급여구분']
    INGREDIENT = upload_file['성분〮함량']
    PRODUCT = upload_file['제품명']
    MADEBY = upload_file['제조사명']
    MATCH_MEDICINE = upload_file['대조약']
    PRICE = upload_file['약가']
    INS_CODE = upload_file['보험청구코드']
    PACKET = upload_file['포장단위']
    YOYUL = upload_file['요율']
    BIGO = upload_file['비고']
    TOTAL_CNT = len(NO)
    # SQL문 실행 만들기
    sql = "update mymedicine_product set USE_YB='N' where insert_id = '" + u_id + "'; \n"
    sql = sql + "INSERT INTO mymedicine_product " \
          + "(BOKGI,CATEGORY_1,CATEGORY_2,CATEGORY_3,SALARY,INGREDIENT,PRODUCT,MADEBY,MATCH_MEDICINE,PRICE," \
          + "INS_CODE,PACKET,YOYUL,BIGO,INSERT_ID) " \
          + "VALUES "
    for i in range(0, TOTAL_CNT):
        sql = sql + "('" + cleanText(str(BOKGI[i])) \
              + "','" + cleanText(str(CATEGORY_1[i])) \
              + "','" + cleanText(str(CATEGORY_2[i])) \
              + "','" + cleanText(str(CATEGORY_3[i])) \
              + "','" + cleanText(str(SALARY[i])) \
              + "','" + cleanText(str(INGREDIENT[i])).replace("/","").replace(" ", "").replace(",", "").replace("㎎", "mg").replace("으로서", "").replace("로서", "") \
              + "','" + cleanText(str(PRODUCT[i])) \
              + "','" + cleanText(str(MADEBY[i])) \
              + "','" + cleanText(str(MATCH_MEDICINE[i])) \
              + "',0" + cleanText(str(PRICE[i])) \
              + ",'" + cleanText(str(INS_CODE[i])) \
              + "','" + cleanText(str(PACKET[i])) \
              + "',0" + cleanText(str(YOYUL[i])) \
              + ",'" + cleanText(str(BIGO[i])) \
              + "','" + u_id + "'), \n"

    return sql

# 약 상세보기
def myView_select(idx):
    # SQL문 실행
    curs = sql_init()
    sql = "select * " \
          " from mymedicine_product " \
          " where USE_YB='Y' and IDX =" + idx

    curs.execute(sql)

    # 데이타 Fetch
    rows = curs.fetchall()
    # 전체 rows
    # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
    # print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')

    return rows

# 판매약찾기 검색결과 > 추가품목 (제품명, 성분)
def select_item_product(search_text):
    # SQL문 실행
    curs = sql_init()
    sql = "select * " \
          " from mymedicine_product " \
          " where USE_YB='Y' and " \
          "(PRODUCT like '%"+search_text+"%' or INGREDIENT like '%"+search_text+"%' or MATCH_MEDICINE like '%"+search_text+"%' ) " \
          "ORDER BY PRODUCT DESC"

    curs.execute(sql)

    # 데이타 Fetch
    rows = curs.fetchall()
    # 전체 rows
    # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
    # print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')

    return rows

# 품목 수정
def my_update(obj):
    IDX         = obj['IDX']
    BOKGI       = obj['BOKGI']
    CATEGORY_1  = obj['CATEGORY_1']
    CATEGORY_2  = obj['CATEGORY_2']
    CATEGORY_3  = obj['CATEGORY_3']
    SALARY      = obj['SALARY']
    INGREDIENT  = obj['INGREDIENT']
    PRODUCT     = obj['PRODUCT']
    MADEBY      = obj['MADEBY']
    MATCH_MEDICINE = obj['MATCH_MEDICINE']
    PRICE       = obj['PRICE']
    INS_CODE    = obj['INS_CODE']
    PACKET      = obj['PACKET']
    YOYUL       = obj['YOYUL']
    BIGO        = obj['BIGO']

    conn,curs = sql_commit()
    sql = "update mymedicine_product " \
          "set BOKGI='"+BOKGI+"', " \
          " CATEGORY_1='"+CATEGORY_1+"', " \
          " CATEGORY_2='"+CATEGORY_2+"', " \
          " CATEGORY_3='"+CATEGORY_3+"', " \
          " SALARY='"+SALARY+"', " \
          " INGREDIENT='"+INGREDIENT+"', " \
          " PRODUCT='"+PRODUCT+"', " \
          " PRODUCT='"+PRODUCT+"', " \
          " MADEBY='"+MADEBY+"', " \
          " MATCH_MEDICINE='"+MATCH_MEDICINE+"', " \
          " PRICE='"+PRICE+"', " \
          " INS_CODE='"+INS_CODE+"', " \
          " PACKET='"+PACKET+"', " \
          " YOYUL='"+YOYUL+"', " \
          " BIGO='"+BIGO+"', " \
          " MODIFYDATE=NOW(), " \
          " MODIFY_ID='"+session['user_id']+"' " \
          " where IDX="+IDX
    curs.execute(sql)
    # 데이터 변화 적용
    conn.commit()

    return "ok"