from functions.db_handle import DataBaseHandle


def get_prod_inventory(product_type, product_series):
    # in this function, we get the current product inventory
    db_host = 'rm-bp1702sge93bz98k1uo.mysql.rds.aliyuncs.com'
    DbHandle = DataBaseHandle(db_host, 'zflm', '1qaz!QAZ', 'easy_store_zflm', 3306)
    # check insert product item id
    select_sql = "SELECT * FROM `table1_metadata` where item_type='" + \
                 product_type + "' and item_series='" + product_series + "'"
    if not DbHandle.selectDb(select_sql):
        print("无法查询不存在物料库存,请先加入对应物料")

    else:
        (item_id, curr_storage) = DbHandle.selectDb(select_sql)
        print(product_type + "-" + product_series + "当前的库存为" + curr_storage)
    DbHandle.closeDb()
