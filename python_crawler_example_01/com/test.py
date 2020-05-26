# -*- coding:utf-8 -*-
from datetime import time, datetime

from flask import Flask, render_template, request, url_for, flash, session, jsonify
from werkzeug.utils import redirect
import pandas as pd
import xlrd
import re
"""
from com.sqlinit import version_check, secret_code
from com.search_medicine import search_google
from com.mylist_behind import mylist_select, select_item_product, mylist_upload, myView_select, my_update
from com.common import login_result, logout_result, session_check, OrderedSet, chg_user_info, user_list_select

"""

app = Flask(__name__)


@app.route('/')
def main():

    return "한글테스트"



if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(host='0.0.0.0', debug='True')
    # app.run(debug=True)
