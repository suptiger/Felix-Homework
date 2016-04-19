
curt_list = []
result = ['yes','no']

#读取商品清单
def show_init_list():
    with open("./database/inventory", encoding='UTF-8') as inventory:
        init_list = inventory.readlines()
        return init_list

# 第一次进入系统时，提示系统欢迎信息
def show_wellcom():
    print('Wellcom Felix to Shoping Center')

#打印初始商品清单,使用字符串格式话输出时，遇到中文字体，不知道应该如何处理；
def show_curt_list(init_list):
    print("*-----------------------------------------*")
    print("* 编号 * 品名 * 库存数量 * 单价(￥) * 单位*")
    print("*-----------------------------------------*")
    for i in init_list:
        i_list = i.strip().split(',')
        print('|   %s   |   %s   |   %s   |   %s   |   %s   |'%(i_list[0].ljust(5),i_list[1].ljust(8),i_list[2].ljust(8),i_list[3].ljust(8),i_list[4].ljust(5)))

#定义函数，判断选择的商品编号是否在商品列表中存在，返回布尔值，存在返回False，不存在返回True
def is_not_exist(curt_list,input_num):
    list_num = []
    for i in curt_list:
        list_num.append(i.split(',')[0])
    if input_num in list_num:
        return False
    else:
        return True

#定义函数，传入商品编号，计算出此商品在curt_list中的索引号，返回此商品品名,库存数量,单价，单位等
def curt_num(curt_list,input_num):
    for i in curt_list:
        if i.split(',')[0] == input_num:
            curt_index = curt_list.index(i)
            return curt_list[curt_index].split(',')[1],curt_list[curt_index].split(',')[2],curt_list[curt_index].split(',')[3],curt_list[curt_index].split(',')[4].strip()


#定义函数，传入商品编号和本次购买的数量，返回此次购买数量是否大于库存数，是否为整数
def is_not_beyond(curt_list,input_num,select_num):
    select_inventory = curt_num(curt_list,input_num)
    if int(select_num) < int(select_inventory[1]) and select_num.isdigit():
        return False
    else:
        return True

#定义函数，传入本次购买的商品编号和购买数量，返回剩余库存量清单
def now_list(curt_list,input_num,select_num):
    for i in curt_list:
        if i.split(',')[0] == input_num:
            curt_index = curt_list.index(i)
            curt_list[curt_index] = input_num+','+curt_list[curt_index].split(',')[1]+','+str(int(curt_list[curt_index].split(',')[2])-int(select_num))+','+curt_list[curt_index].split(',')[3]+','+curt_list[curt_index].split(',')[4]
            return curt_list

#定义函数，传入商品编号，返回用户的购物清单
def buy_process(curt_list,input_num,select_num):
    select_inventory = curt_num(curt_list,input_num)
    print('Inventory:%s,Quantity:%s your selected!'%(select_inventory[0],select_num))
    print('%d Money you must Pay!\n'%(int(select_num)*float(select_inventory[2])))


def main():
    show_wellcom()#显示欢迎信息
    curt_list = show_init_list()#将初始化商品清单赋值给变量
    show_curt_list(curt_list)#打印初始化商品清单
    while True:
        input_num = input('Please input The number what you want to buy，or input exit exit shopping center!\n').strip().lower()
        if input_num == 'exit':
            exit()
        while is_not_exist(curt_list,input_num):#判断用户录入的商品编号是否存在
            input_num = input('Please input right num for Buy,or input exit exit shopping center!\n').strip().lower()
            if  input_num == 'exit':
                exit()
        a = curt_num(curt_list, input_num)
        select_num = input('%s is you want to buy,Please input many you want to buy!\n' % (a[0])).strip()
        while is_not_beyond(curt_list,input_num,select_num):#判断用户录入的购买数量是否合法，是否为正整数且小于库存量
            select_num = input('Many Error,Please input right number!\n').strip()
        buy_process(curt_list,input_num,select_num)#返回用户购物清单
        user_result = input('If you will buy,Please input yes,else,input no!\n').strip().lower()
        while user_result not in result:
            user_result = input('Please input right choice,If you will buy,Please input yes,else,input no!\n').strip().lower()
        if user_result == 'yes':#假如用户选择了购买，则计算出当前的库存量
            curt_list = now_list(curt_list,input_num,select_num)#计算出当前的库存量清单
            show_curt_list(curt_list)#打印出库存清单
        else:#加入用户不进行购买，则显示原始商品清单
            show_curt_list(curt_list)
if __name__ == '__main__':
    main()


