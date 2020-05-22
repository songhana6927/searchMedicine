# -*- coding:utf-8 -*-
from datetime import time, datetime

from flask import Flask, render_template, request, url_for, flash, session, jsonify
from werkzeug.utils import redirect
import re

from com.sqlinit import version_check, secret_code
from com.search_medicine import search_google
from com.mylist_behind import mylist_select, select_item_product, mylist_upload, myView_select, my_update
from com.common import login_result, logout_result, session_check, OrderedSet, chg_user_info, user_list_select
import pandas as pd
import xlrd

app = Flask(__name__)
app.secret_key = secret_code()


@app.route('/')
@app.route('/login')
def login():
    version = 1
    version_result = version_check(version)
    if not version_result:
        flash('새로운버전이 나왔습니다. 다운로드를 진행하세요.')
        check = False
    else:
        check = True

    return render_template('/login.html', version_check=check)


@app.route('/logout')
def logout():
    logout_result()
    return redirect(url_for('login'))


@app.route('/chg_pwd', methods=['POST', 'GET'])
def chg_pwd():
    if request.method == 'POST':
        result = request.form
        mode = "chg_pwd"
        id = session['user_id']
        pwd = result['chg_pwd']
        name = session['user_name']
        level = session['level']
        chg_user_info(mode, id, pwd, name, level)
    flash('다시 로그인 해 주세요.')
    return redirect(url_for('login'))


@app.route('/login_action', methods=['POST', 'GET'])
def login_action():
    if request.method == 'POST':
        result = request.form
        login_re = login_result(result)
        if login_re == "login":
            return redirect(url_for('search'))
        else:
            flash('아이디와 비밀번호를 확인하세요.')
            return redirect(url_for('login'))


@app.route('/search')
def search():
    if not session_check():
        flash('재로그인 해주세요')
        return redirect(url_for('login'))

    return render_template('/search_main.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if not session_check():
        flash('재로그인 해주세요')
        return redirect(url_for('login'))

    if request.method == 'POST':
        result = request.form
        search_product = result['search_product'].split('\r\n')
        for idx, search_item in enumerate(search_product):
            # 특수문자제거, 공백제거
            search_product[idx] = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', search_item).replace(' ',
                                                                                                                    '')

        # 중복제거
        search_product = OrderedSet(search_product)
        s_data = []
        for item in search_product:
            # 글자수가 1글자 이상일때만 검색
            if len(item) > 0:
                korean_nm = ""
                start = 0
                # 없을시 다음페이지 3 페이지 까지만
                while len(korean_nm) < 1 and start < 30:
                    gSearch_result = search_google(item, start, "druginfo")
                    korean_nm = gSearch_result['korean_nm']
                    start = start + 10
                # 그래도 없을 시 kmle로 검색 (kmle 우리랑 성분명 표시하는방법이달라서 내 리스트 잘 못골라옴)
                start = 0
                while len(korean_nm) < 1 and start < 30:
                    gSearch_result = search_google(item, start, "kmle")
                    korean_nm = gSearch_result['korean_nm']
                    start = start + 10

                print(start, gSearch_result)
                s_data.append(gSearch_result)
        return render_template("/result_main.html", result=s_data)


@app.route('/my_view')
def my_view():
    result = request.args.get('idx')
    viewItem = myView_select(result)
    return render_template('/my_view.html', result=viewItem)


@app.route('/my_edit', methods=['POST', 'GET'])
def my_edit():
    if not session_check():
        flash('재로그인 해주세요')
        return redirect(url_for('login'))

    if request.method == 'POST':
        result = request.form
        rtn_message = my_update(result)
        print(rtn_message)
        e_idx = result["IDX"]
    return redirect(url_for('my_view', idx=e_idx))


@app.route('/list')
def list():
    if not session_check():
        flash('재로그인 해주세요')
        return redirect(url_for('login'))

    mylist = mylist_select('ADMIN')
    return render_template('/my_list.html', result=mylist)


@app.route('/result_test')
def result_test():
    return render_template('/result_test.html')


@app.route('/listupload', methods=['POST', 'GET'])
def listupload():
    if not session_check():
        flash('재로그인 해주세요')
        return redirect(url_for('login'))

    if request.method == 'POST':
        f = request.files['file']
        data_xls = pd.read_excel(f, sheet_name='Sheet1')
        insert_qry = mylist_upload('ADMIN', data_xls)
    return render_template('/my_list_upload.html', result=insert_qry)


@app.route('/select_item', methods=['POST', 'GET'])
def select_item():
    if request.method == 'POST':
        search_text = request.form['value']
        resp = select_item_product(search_text)
    return jsonify(resp)


@app.route('/user')
def user():
    if not session_check():
        flash('재로그인 해주세요')
        return redirect(url_for('login'))

    user_list = user_list_select(session['level'])
    return render_template('/user_list.html', result=user_list)


@app.route('/user_edit', methods=['POST', 'GET'])
def user_edit():
    if not session_check():
        flash('재로그인 해주세요')
        return redirect(url_for('login'))

    if request.method == 'POST':
        result = request.form
        mode = result['mode']
        edit_id = result['edit_id']
        edit_name = result['edit_name']
        edit_level = result['edit_level']
        resp = chg_user_info(mode, edit_id, '1234', edit_name, edit_level)

    return redirect(url_for('user'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(host='0.0.0.0', debug='True')
    # app.run(debug=True)
