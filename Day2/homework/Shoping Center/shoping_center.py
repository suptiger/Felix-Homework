
curt_list = []
def show_curt_list(init_list):
    print("*-----------------------------------------*")
    print("* 编号 * 品名 * 库存数量 * 单价(￥) * 单位*")
    print("*-----------------------------------------*")
    for i in init_list:
        print(i.strip().replace(',','      '))

def show_init_list():
    with open("./database/inventory", encoding='UTF-8') as inventory:
        init_list = inventory.readlines()
        return init_list

def show_wellcom():
    print('Wellcom to Shoping Center')

def is_not_exist(curt_list,input_num):
    list_num = []
    for i in curt_list:
        list_num.append(i.split(',')[0])
    if input_num in list_num:
        return False
    else:
        return True

def buy_process(input_num):
    buy_result = []
    input_num = input('You select %s,Please select ')

def main():
    show_wellcom()
    curt_list = show_init_list()
    show_curt_list(curt_list)
    while True:
        input_num = input('Please input The number what you want to buy!\n ').strip()
        while is_not_exist(curt_list,input_num):
            input_num = input('Please input right num for Buy!').strip()
        if input_num == '01':
        elif input_num == '02':
        elif input_num == '03':


if __name__ == '__main__':
    main()


