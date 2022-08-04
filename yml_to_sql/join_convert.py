import yaml
from datetime import datetime

print('\n')

filename = input('Type the name(+address) of yaml files WITHOUT EXTENSION to be converted: ')

print('\n')

with open(str(filename) + '.yml') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

join_template = "SELECT * FROM {} JOIN {}"
# ON {} = {} AND {} = {}"

join_statements = [join_template.format(nv['table']) for nv in data['models']]

#update_template = "UPDATE SAMPLE SET PVALUE={} WHERE PNAME=\'{}\'"
#update_statements = [update_template.format(nv['value'], nv['name']) for nv in data['Config']]

print('\n')

#template_choice_id = input('Choose your template:\n1 for Update\n2 for Join: ')

#def statements():
#    if template_choice_id == 1:
#        return 'update_statements'
#    else: return 'join_statements'
     

with open("converted_" + str(filename) + "_output_file_" + str(datetime.today()) + ".sql", 'w') as f:
    for statement in join_statements:
        f.write(statement)

print('Done!')

print('\n')
