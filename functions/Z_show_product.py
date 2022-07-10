import pandas as pd
import numpy as np
from functions.get_prod_inventory import MaterialName, Action


def cur_product_to_dict():
    data = pd.read_excel(r'C:\Users\guosi\PycharmProjects\pythonProject\data\cur_product.xlsx', engine='openpyxl')
    # print(data)
    # change DF to a dict type
    list_data = data.values.tolist()
    materials = dict()
    for i in range(len(list_data)):
        key = (list_data[i][0], list_data[i][1])
        value = [i]
        for action in list_data[i][2:]:
            if type(action) != str:
                continue
            action = action.split("/")
            value.append(Action(action[0], action[1], action[2], action[3]))
        materials[key] = value
    print(materials)
    return materials


# def dict_to_cur_product(materials):
def dict_to_cur_product():
    materials = dict()
    action1 = Action(1, 2, 3, 1)
    action2 = Action(2, 2, 3, 1)
    materials[(1, 1)] = [1, action1, action2]
    materials[(1, 2)] = [2, action2, action1]
    data = []
    for key in materials:
        curr_row = list(key)
        for action in materials[key][1:]:
            action_str = '/'.join([str(action.num), str(action.price), str(action.action_time), str(action.order_id)])
            curr_row.append(action_str)
        data.append(curr_row)
    print(data)
    data_array = np.array(data)
    df = pd.DataFrame(data_array)
    print(df)
    # write to excel
    path = r'C:\Users\guosi\PycharmProjects\pythonProject\data\cur_product_1.xlsx'
    writer = pd.ExcelWriter(path)
    df.to_excel(writer, index=False)
    writer.save()


def add_action_to_excel(row, col, action):
    path = r'C:\Users\guosi\PycharmProjects\pythonProject\data\cur_product.xlsx'
    data = pd.read_excel(path, engine='openpyxl')
    # print(data)
    # print(data.shape)
    # print(row, col)
    if row <= data.shape[0] - 1 and col <= data.shape[1] - 1:
        print("Do not need to expand the excel")
        data.iloc[row, col] = '/'.join(
            [str(action.num), str(action.price), str(action.action_time), str(action.order_id)])
    elif row <= data.shape[0] - 1 and col > data.shape[1] - 1:
        print("Need to expand the excel")
        index = data.shape[1] - 2
        data["行为." + str(index)] = None
        data.iloc[row, col] = '/'.join(
            [str(action.num), str(action.price), str(action.action_time), str(action.order_id)])
    else:
        print("cannot insert a non-exist product")
    print(data)
    writer = pd.ExcelWriter(path)
    data.to_excel(writer, index=False)
    writer.save()
