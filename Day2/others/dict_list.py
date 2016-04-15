
init_list = [11,22,33,44,55,66,77,88,99,90]
init_dict = {}
'''
print(init_list)
list_little=[]
list_biger=[]
for i in init_list:
    if i <= 60:
        list_little.append(i)
    else:
        list_biger.append(i)
dict_tem = {'<=60':list_little,'>60':list_biger}
init_dict.update(dict_tem)
print(init_dict)
'''
for i in init_list:
    if i > 66:
        if 'k1' in init_dict.keys():
            init_dict['k1'].append(i)
        else:
            init_dict['k1']=[i]
    else:
        if 'k2' in init_dict.keys():
            init_dict['k2'].append(i)
        else:
            init_dict['k2']=[i]
print(init_dict)