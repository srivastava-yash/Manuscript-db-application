## utility file to store all db related utility functions
import constants

def get_where_query(table_name, column_names, value_tuple):
    query = f"SELECT * from {table_name} where "
    value_list = column_names.split(",")
    for i in range(len(value_list)):
        if value_tuple[i].isnumeric():
            value = int(value_tuple[i])
            query += (value_list[i] + "=" + value_tuple[i] + " and ")
        else:
            query += (value_list[i] + "=" + "'" + value_tuple[i] + "'" + " and ")

    query = query[:-4]
    return query



if __name__ == "__main__":
    get_where_query("Person", constants.PERSON_VALUE_LIST, tuple(["Cardi", "B", "cardi.b@gmail.com"]))