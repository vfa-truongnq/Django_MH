import psycopg2
def import_data():
    constr = "dbname='MH' user='postgres' host='localhost' password='Bekute210'"
    conn = psycopg2.connect(constr)
    cur = conn.cursor()
    with open('E:\Django_MH\MH\MH.csv','r',encoding='utf-8') as f:
        next(f)
        cur.copy_from(f,'mh',sep=',')
    conn.commit()

import_data()