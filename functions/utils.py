from functions.db_handle import DataBaseHandle


def clean_DB():
    db_host = 'rm-bp1702sge93bz98k1uo.mysql.rds.aliyuncs.com'
    DbHandle = DataBaseHandle(db_host, 'zflm', '1qaz!QAZ', 'easy_store_zflm', 3306)
    truncate_sql_1 = "TRUNCATE TABLE `table2_in_storage_action`"
    truncate_sql_2 = "TRUNCATE TABLE `table1_metadata`"
    truncate_sql_3 = "TRUNCATE TABLE `table3_out_storage_record`"
    DbHandle.updateDb(truncate_sql_1)
    DbHandle.updateDb(truncate_sql_2)
    DbHandle.updateDb(truncate_sql_3)
    DbHandle.closeDb()