# Copy from CNDS
# FileName : DBHandle.py
# Author   : Adil
# DateTime : 2018/11/29 2:03 PM
# SoftWare : PyCharm

import pymysql


# username : zflm
# password : 1qaz!QAZ


class DataBaseHandle(object):
    # 定义一个 MySQL 操作类

    def __init__(self, host, username, password, database, port):
        # 初始化数据库信息并创建数据库连接
        # 下面的赋值其实可以省略，connect 时 直接使用形参即可
        self.cursor = None
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.db = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, port=self.port, charset='utf8')

    #  这里 注释连接的方法，是为了 实例化对象时，就创建连接。不许要单独处理连接了。
    #
    # def connDataBase(self):
    #     ''' 数据库连接 '''
    #
    #     self.db = pymysql.connect(self.host,self.username,self.password,self.port,self.database)
    #
    #     # self.cursor = self.db.cursor()
    #
    #     return self.db

    def insertDB(self, sql):
        # 插入数据库操作

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def deleteDB(self, sql):
        # 操作数据库数据删除
        self.cursor = self.db.cursor()

        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql) # 返回 删除数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def updateDb(self, sql):
        # 更新数据库操作

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql) # 返回 更新数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def selectDb(self, sql):
        # 数据库查询
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)  # 返回 查询数据 条数 可以根据 返回值 判定处理结果

            data = self.cursor.fetchall()  # 返回所有记录列表
            # print(data)
            # 结果遍历
            for row in data:
                sid = row[0]
                storage = row[3]
                # 遍历打印结果
                # print('sid = %s,  name = %s' % (sid, name))
                return sid, storage

        except:
            print('Error: unable to fetch data')
        finally:
            self.cursor.close()

    def selectDb_get_all(self, sql):
        # 数据库查询
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)  # 返回 查询数据 条数 可以根据 返回值 判定处理结果

            data = self.cursor.fetchall()  # 返回所有记录列表
            print(data)
            return data
        except:
            print('Error: unable to fetch data')
        finally:
            self.cursor.close()

    def closeDb(self):
        # 数据库连接关闭
        self.db.close()
