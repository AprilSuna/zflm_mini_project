from functions.db_handle import DataBaseHandle


def insert_new_product(product_type, product_series):
    # in this function, we will insert new product into
    db_host = 'rm-bp1702sge93bz98k1uo.mysql.rds.aliyuncs.com'
    DbHandle = DataBaseHandle(db_host, 'zflm', '1qaz!QAZ', 'easy_store_zflm', 3306)
    # remove duplicate item+type / series
    select_sql = "SELECT * FROM `table1_metadata` where item_type='" + product_type + \
                 "' and item_series='" + product_series + "'"
    print(select_sql)
    if DbHandle.selectDb(select_sql):
        print(DbHandle.selectDb(select_sql))
        print("cannot add exit product " + product_type + product_series)
        return
    # after checking good insert into the table
    else:
        sql = "insert into `table1_metadata`(item_type, item_series, item_storage) values ('" \
              + str(product_type) + "','" + str(product_series) + "', '0')"
        print(sql)
        DbHandle.insertDB(sql)
    DbHandle.closeDb()
