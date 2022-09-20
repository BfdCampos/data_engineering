import json

inp = input("\nEnter the path to the .json file needed to flatten: \n \n")

column = input("\nEnter the name of the column you plan to flatten: \n \n")

def flatten_json_alias(y):
    out = {}

    def flatten_alias(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten_alias(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten_alias(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten_alias(y)
    return out

def flatten_json_address(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + '\"' + a + '\"' + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, '\"' + name + '\"' + '[' + str(i) + ']' + '.')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


with open(inp) as f:
    test_file = json.load(f)

print('\n')

dictkeys_alias = list(flatten_json_alias(test_file).keys())

dictkeys_address = list(flatten_json_address(test_file).keys())

print('\n')

for i in range(len(dictkeys_address)):
    dictkeys_address[i] = '\"' + column.lower() + '\":' + dictkeys_address[i] + ' AS ' + column.upper() + '_' + dictkeys_alias[i].upper()
 
print(dictkeys_address)

print('\n')

print('With a bit of cleaning, you\'re ready to flatten your way to victory!')

print('\n')
