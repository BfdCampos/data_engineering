import re

def convert_update_to_select(update_query):
    # Split the query into lines
    lines = update_query.strip().split('\n')

    # Extract the table name and the columns to be updated from the first line
    table_name = re.search( r'update\s+(\S+)\s+set\s+(\S+)\s*=',lines[0]).group(1)
    columns = re.findall(r'(\S+)\s*=\s*(\S+)', lines[1])

    # Extract the source table and join condition from the last line
    from_table = re.search(r'from\s+(\S+)\s+where', lines[-1]).group(1)
    join_condition = re.search(r'where\s+(\S+)\s*=\s*(\S+)', lines[-1]).group(1, 2)

    # Build the SELECT query
    select_query = 'SELECT\n'
    select_query += ',\n'.join([f'{col[1]} AS {col[0]}' for col in columns]) + '\n'
    select_query += f'FROM\n{from_table}\n'
    select_query += f'JOIN {table_name} ON {join_condition[0]} = {join_condition[1]};'

    return select_query

update_query_file = input("\nEnter the path to the .sql file that needs to be made into a SELECT statement for dbt: \n \n \n")

print('\n \n')

with open(update_query_file, 'r') as file:
    # Read the contents of the file
    sql = file.read()
    # Print the contents of the file
    print("This is the SQL file you want to convert: \n \n" + sql)

print('\n \n')

print(convert_update_to_select(sql))

