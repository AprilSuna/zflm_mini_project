from datetime import datetime
from functions.db_handle import DataBaseHandle


def add_inventory(product_type, product_series, order_id, amount, unit_price):
    # in this function, we record add inventory action
    db_host = 'rm-bp1702sge93bz98k1uo.mysql.rds.aliyuncs.com'
    DbHandle = DataBaseHandle(db_host, 'zflm', '1qaz!QAZ', 'easy_store_zflm', 3306)
    # check insert product item id
    select_sql = "SELECT * FROM `table1_metadata` where item_type='" +\
                 product_type + "' and item_series='" + product_series + "'"
    print(select_sql)
    if not DbHandle.selectDb(select_sql):
        print("无法添加不存在物料库存,请先加入对应物料")
    else:
        (item_id, curr_storage) = DbHandle.selectDb(select_sql)
        # insert action into table2
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_sql = "insert into `table2_in_storage_action`(item_id, order_time, order_id, amount, unit_price) " \
                     "values ('" + str(item_id) + "', '" + now + "', '" + str(order_id) + "', '" + str(amount) + \
                     "', '" + str(unit_price) + "')"
        print(insert_sql)
        DbHandle.insertDB(insert_sql)
        # insert the current amount into table 1
        curr_storage = int(curr_storage)
        curr_storage += amount
        update_sql = "UPDATE `table1_metadata` SET item_storage = " + str(curr_storage) + " WHERE item_id = " + \
                     str(item_id)
        print(update_sql)
        DbHandle.updateDb(update_sql)

    DbHandle.closeDb()
