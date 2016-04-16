curt_list = []
def show_init_list():
    with open("inventory.txt", encoding='UTF-8') as inventory:
        init_list = inventory.readlines()
        return init_list

# 第一次进入系统时，提示系统欢迎信息
def show_wellcom():
    print('Wellcom to Shoping Center')

#打印初始商品清单
def show_curt_list(init_list):
    print("*-----------------------------------------*")
    print("* 编号 * 品名 * 库存数量 * 单价(￥) * 单位*")
    print("*-----------------------------------------*")
    for i in init_list:
        print(i.strip().replace(',','      '))

def is_not_exist(curt_list,input_num):
    list_num = []
    for i in curt_list:
        list_num.append(i.split(',')[0])
    if input_num in list_num:
        return False
    else:
        return True

def curt_num(curt_list,input_num):
    for i in curt_list:
        if i.split(',')[0] == input_num:
            curt_index = curt_list.index(i)
            return curt_list[curt_index].split(',')[1],curt_list[curt_index].split(',')[2]

def main():
    show_wellcom()
    curt_list = show_init_list()
    show_curt_list(curt_list)
    while True:
        input_num = input('Please input The number what you want to buy!\n ').strip()
        while is_not_exist(curt_list,input_num):
            input_num = input('Please input right num for Buy!\n').strip()
        a = curt_num(curt_list,input_num)
        select_num = input('%s is you want to buy,Please input many you want to buy!'%(a[0])).strip()
        while

if __name__ == '__main__':
    main()
