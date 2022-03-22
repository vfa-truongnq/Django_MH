# import psycopg2
# def import_data():
#     constr = "dbname='MH' user='postgres' host='localhost' password='P@ssw0rld'"
#     conn = psycopg2.connect(constr)
#     cur = conn.cursor()
#     try:
#         with open('E:\Django_MH\MH\MH.csv','r',encoding='utf-8') as f:
#             next(f)
#             cur.copy_from(f,'mh',sep=',')
#         conn.commit()
#     except IOError:
#         print('Unable to open file')

# import_data()

def load_csv_file(path):
    with open(path) as file_obj:
        reader = csv.reader(file_obj)
        for row in reader:
            MH_tb.objects.create(
                housing_area_code=row[0],
                facility_key=row[1],
                shape_wkt=Point(row[2]),
                facility_type=row[3],
                ordinal_number = row[4],
                structure_type = row[5],
                shape = row[6],
                fabricated_type_code = row[7],
                pref = row[8],
                create_by = row[9],
                create_at = DateTime(row[10]),
                update_by = row[11],
                update_at = DateTime(row[12])
            )
