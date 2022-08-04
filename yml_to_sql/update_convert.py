import yaml
from datetime import datetime

print('\n')

filename = input('Type the name(+address) of yaml files WITHOUT EXTENSION to be converted: ')

print('\n')

with open(str(filename) + '.yml') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

update_template = "UPDATE SAMPLE SET PVALUE={} WHERE PNAME=\'{}\'"
update_statements = [update_template.format(nv['value'], nv['name']) for nv in data['Config']]

print('\n')

with open("converted_" + str(filename) + "_output_file_" + str(datetime.today()) + ".sql", 'w') as f:
    for statement in update_statements:
        f.write(statement + '\n')

print('Done!')

print('\n')
