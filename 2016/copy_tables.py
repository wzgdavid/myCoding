# encoding: utf-8

'''
相同的表结构
'''
import os
import psycopg2
import pprint

class Settings(object):
    CONN_FROM = {
        'database':"expat", 
        'user':"david", 
        'password':"1", 
        'host':"localhost", 
        'port':"5432"
    }
    CONN_TO = {
        'database':"test", 
        'user':"david", 
        'password':"1", 
        'host':"localhost", 
        'port':"5432"
    }


class Carrier(object):
    def __init__(self, conn_from, conn_to):
        self.conn_from = psycopg2.connect(**conn_from)
        self.cur_from = self.conn_from.cursor() 
        self.conn_to = psycopg2.connect(**conn_to) 
        self.cur_to = self.conn_to.cursor()

    def copy(self, table_name):

        self.cur_from.execute('''
            select * from %s
        ''' % table_name)
        rows_from = self.cur_from.fetchall() 

        if len(rows_from) == 0:
            print 'blank table'
            return
        columns = len(rows_from[0])
        
        sql_head = 'insert into %s values (' % table_name
        for row in rows_from:

            insert_sql = sql_head + str('%s, '*(columns-1)) + str('%s') + ')', row
            print insert_sql
            self.cur_to.execute(*insert_sql)


        self.cur_from.close()
        self.cur_to.close()
        

    def __del__(self):
        
        self.conn_from.commit()
        self.conn_from.close()
        #self.cur_to.close()
        self.conn_to.commit()
        self.conn_to.close()


if __name__ == '__main__':
    c = Carrier(Settings.CONN_FROM, Settings.CONN_TO)
    print c.copy('article_articlecategory')
