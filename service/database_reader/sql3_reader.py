import sqlite3

class DatabaseConnector():

    def __init__(self, db_name, *args, **kwargs):
        self.connector = sqlite3.connect(db_name)
        self.cursor = self.connector.cursor()

    def close_connexion(self):
        self.connector.close()

    def execute_and_return(self, sql_command):

        try:
            self.cursor.execute(sql_command)
            self.connector.commit()
        except sqlite3.OperationalError as e:
            print('Sqlite error: '+str(e))
            exit(-1)

        return self.cursor.fetchall()

    def retrieve_all_data(self, table_name, fields = None):
        db_fields = "*" if fields is None else "" + ", ".join(fields) + ""
        sql_command = "SELECT " + db_fields + " FROM `" + table_name + "`"

        return self.execute_and_return(sql_command)

    def retrieve_all_data_with_join(self, table_name, join_table_name, join_attributes, fields = None):
        db_fields = "*" if fields is None else "" + ", ".join(fields) + ""
        sql_command = "SELECT " + db_fields + " FROM `" + table_name + "` t1 JOIN `" + join_table_name + "` t2 ON t1." + join_attributes[0] + "=t2." + join_attributes[1]

        return self.execute_and_return(sql_command)