from functions.db_handle import DataBaseHandle


def withdraw_inventory(product_type, product_series, amount):
    # in this function, we will insert new product into
    db_host = 'rm-bp1702sge93bz98k1uo.mysql.rds.aliyuncs.com'
    DbHandle = DataBaseHandle(db_host, 'zflm', '1qaz!QAZ', 'easy_store_zflm', 3306)
    # get the product item_id we would like to withdraw
    get_prod_sql = "SELECT * FROM `table1_metadata` where item_type='" + product_type + \
                   "' and item_series='" + product_series + "'"
    print(get_prod_sql)
    (item_id, curr_storage) = DbHandle.selectDb(get_prod_sql)
    print(item_id, curr_storage)
    if int(curr_storage) < amount:
        print("库存不足,仅剩" + curr_storage)
        return

    # update current inventory
    curr_storage = int(curr_storage)
    curr_storage -= amount
    update_sql = "UPDATE `table1_metadata` SET item_storage = " + str(curr_storage) + " WHERE item_id = " + \
                 str(item_id)
    print(update_sql)
    DbHandle.updateDb(update_sql)

    # step 1: 从table3中找 batch id以及从哪个in_storage_id开始找
    select_sql_1 = "select * from  `table3_out_storage_record` where item_id = " + str(item_id)
    print(select_sql_1)
    data1 = DbHandle.selectDb_get_all(select_sql_1)
    batch_id = 0
    latest_in_storage_id = 0
    remain_amt = 0
    unit_price = 0
    for row in data1:
        if row[2] > batch_id:
            batch_id = row[2]
    for row in data1:
        if row[3] >= latest_in_storage_id:
            latest_in_storage_id = row[3]
            unit_price = row[5]
            remain_amt = row[6]
    batch_id += 1
    print(remain_amt, amount)
    # step 2: 遍历 table 2 并且insert 到 table 3
    # 如果当前remain的可以解决
    if remain_amt >= amount > 0:
        remain_amt -= amount
        insert_sql = "insert into `table3_out_storage_record`(item_id, batch_id, in_storage_id, " \
                     "out_amount, out_unit_price, remaining) values ('" + str(item_id) + "', '" + str(batch_id) + "', '" + \
                     str(latest_in_storage_id) + "', '" + str(amount) + "', '" + str(unit_price) + "', '" + \
                     str(remain_amt) + "')"
        print(insert_sql)
        DbHandle.insertDB(insert_sql)
    # 如果当前的remain无法解决
    else:
        # 如果上次的storage_id还有余额,先扣减掉
        if amount > remain_amt > 0:
            amount -= remain_amt
            insert_sql = "insert into `table3_out_storage_record`(item_id, batch_id, in_storage_id, " \
                         "out_amount, out_unit_price, remaining) values ('" + str(item_id) + "', '" + str(batch_id) + "', '" + \
                         str(latest_in_storage_id) + "', '" + str(remain_amt) + "', '" + str(unit_price) + "', '" + str(0) + "')"
            print(insert_sql)
            DbHandle.insertDB(insert_sql)

        # 搜下一个余额的
        select_item_action_in_table2_sql = "select * from  `table2_in_storage_action` where item_id = " \
                                           + str(item_id) + " and id > " + str(latest_in_storage_id)
        print(select_item_action_in_table2_sql)
        data = DbHandle.selectDb_get_all(select_item_action_in_table2_sql)
        need_to_meet_amount = amount
        for row in data:
            curr_in_action_amt = row[4]
            unit_price = row[5]
            in_storage_id = row[0]
            if need_to_meet_amount <= curr_in_action_amt:
                out_amount = need_to_meet_amount
                remain_amount = curr_in_action_amt - need_to_meet_amount
                insert_sql = "insert into `table3_out_storage_record`(item_id, batch_id, in_storage_id, " \
                             "out_amount, out_unit_price, remaining) values ('" + str(item_id) + "', '" + \
                             str(batch_id) + "', '" + str(in_storage_id) + "', '" + str(out_amount) + "', '" \
                             + str(unit_price) + "', '" + str(remain_amount) + "')"
                print(insert_sql)
                DbHandle.insertDB(insert_sql)
                break
            elif need_to_meet_amount > curr_in_action_amt:
                out_amount = curr_in_action_amt
                remain_amount = 0
                need_to_meet_amount -= out_amount
                insert_sql = "insert into `table3_out_storage_record`(item_id, batch_id, in_storage_id, " \
                             "out_amount, out_unit_price, remaining) values ('" + str(item_id) + "', '" + \
                             str(batch_id) + "', '" + str(in_storage_id) + "', '" + str(out_amount) + "', '" \
                             + str(unit_price) + "', '" + str(remain_amount) + "')"
                print(insert_sql)
                DbHandle.insertDB(insert_sql)
                continue

    DbHandle.closeDb()
