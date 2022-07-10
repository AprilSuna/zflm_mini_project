# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from functions.add_inventory import add_inventory
from functions.db_handle import DataBaseHandle
from functions.get_prod_inventory import get_prod_inventory
from functions.insert_new_product_series import insert_new_product
from functions.utils import clean_DB
from functions.withdraw_inventory import withdraw_inventory


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # insert_new_product("sxr", "001")
    # add_inventory("sxr", "001", "000001", 300, 8.5)
    # add_inventory("sxr", "001", "000002", 350, 11)
    # get_prod_inventory("sxr", "001")
    withdraw_inventory("sxr", "001", 150)
    # withdraw_inventory("郭思宏", "003", 300)
    # withdraw_inventory("郭思宏", "003", 100)
    # clean_DB()

    # todo: 加总价; 出库的时候需要对应的入库订单号; 看当前所有库存;


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
