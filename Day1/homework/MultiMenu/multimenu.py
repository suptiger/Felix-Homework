#
#定义省份数据结构
dic_province = {'1':'浙江省','2':'甘肃省','3':'北京市','4':'上海市'}
#定义市数据结构
dic_city = {'1-1':'杭州','1-2':'宁波','1-3':'温州','1-4':'绍兴','1-5':'湖州',
            '2-1':'兰州','2-2':'嘉峪关','2-3':'金昌','2-4':'白银',
            '3-1':'东城','3-2':'西城','3-3':'海淀','3-4':'朝阳',
            '4-1':'黄浦','4-2':'浦东','4-3':'徐汇','4-4':'长宁'
            }
#定义区或者街道数据结构
dic_district = {'1-1-1':'上城','1-1-2':'下城','1-1-3':'江干','1-1-4':'拱墅',
                '1-2-1':'海曙','1-2-2':'江东','1-2-3':'江北','1-2-4':'北仑',
                '1-3-1':'鹿城','1-3-2':'龙湾','1-3-3':'瓯海','1-3-4':'洞头',
                '1-4-1':'越城','1-4-2':'柯桥','1-4-3':'上虞','1-4-4':'诸暨','1-4-5':'嵊州',#模拟5个区的
                '1-5-1':'吴兴','1-5-2':'南浔','1-5-3':'德清','1-5-4':'长兴',
                '2-1-1':'城关','2-1-2':'七里河','2-1-3':'西固','2-1-4':'安宁',
                '2-2-1':'雄关','2-2-2':'长城','2-2-3':'镜铁',
                '2-3-1':'金川','2-3-2':'永昌',#模拟2个区的
                '2-4-1':'白银','2-4-2':'平川','2-4-3':'会宁','2-4-4':'靖远','2-4-5':'景泰',
                '3-1-1':'东华门','3-1-2':'景山','3-1-3':'交道口','3-1-4':'安定门',
                '3-2-1':'西长安街','3-2-2':'新街口','3-2-3':'月坛','3-2-4':'展览路',
                '3-3-1':'万寿路','3-3-2':'羊坊店','3-3-3':'甘家口','3-3-4':'八里庄',
                '3-4-1':'朝外','3-4-2':'劲松','3-4-3':'建外','3-4-4':'呼家楼',
                '4-1-1':'南京东路','4-1-2':'外滩','4-1-3':'半淞园路','4-1-4':'小东门',
                '4-2-1':'潍坊新村','4-2-2':'陆家嘴','4-2-3':'周家渡','4-2-4':'塘桥',
                '4-3-1':'湖南路','4-3-2':'天平路','4-3-3':'枫林路','4-3-4':'徐家汇'
                #假设4-4长宁下面是没有区的
                }


def show_province():
    for i in dic_province:
        print(i, dic_province[i])

def show_city():
    for i in dic_city:
        print(i,dic_city[i])

def show_district():
    for i in dic_district:
        print(i,dic_district[i])

def show_city_list():
    for i in dic_city.keys():
        print(i, dic_district[i])



def main():
    print("欢迎使用三级菜单查询系统！")
    while True:
        show_province()#打印省份
        input_province = input('请输入序号进行查询,使用exit退出整个查询!\n').strip()
        if input_province == 'exit':
            exit()
        elif input_province not in dic_province.keys():
            print("请输入合法数字!")
        else:
            for i in dic_city.keys():#循环输出当前选择的省份下的市
                province_num = i.split('-')[0]
                if input_province == province_num:
                    print(i.split('-')[1],dic_city[i])
        while True:
            input_city = input("请输入查询的城市编号\n").strip()
            if input_city == 'quit':
                break
            elif input_city == 'exit':
                exit()
            else:
                for i in dic_district.keys():#循环输出当前选择的市下的街道或者区
                    district_num = i.split('-')[0] + i.split('-')[1]
                    if input_province + input_city == district_num:
                        print(i.split('-')[2], dic_district[i])
            while True:
                input_operate = input("请输入您想操作的内容,使用quit返回上级，使用exit退出程序.\n").strip()
                if input_operate == 'quit':
                    break
                elif input_operate == 'exit':
                    exit()
                else:
                    print("请输入合法数字!\n")

if __name__ =='__main__':
    main()
