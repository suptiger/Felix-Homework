#Date: 20160410
#author: felix wang

#读取用户账号数据
udata= open("./db/userdata","r")
userData = udata.readlines()
udata.close()

#读取用户锁定数据
ldata = open("./db/logdata","r")
logData = ldata.readlines()
ldata.close()

#去除读取用户账号数据时附带的换行符
for i in range(0,len(userData)):
    userData[i]= userData[i].strip()

#定义用户名列表，并将用户数据中的用户名取出，后面用来判断是否为已注册用户
user = []
for i in range(0,len(userData)):
    user_list = userData[i].split(",")
    user.append(user_list[0])

#读取用户输入的账号和密码，并连接为字符串，作为认证关键字
userName = (input("Please input your registered name.\n")).strip()
userPassword = (input("Please input your password.\n")).strip()
userinfo = userName + ","+userPassword
countInput = 0

#判断用户输入的信息，是否为锁定数据，或者不存在用户，若为这两者，则进行密码认证
if userName in logData:
    print("Your accout already locked,Please contact administrator unlock. ")
elif userName not in user:
    print("Your accout not registered,Please Contact administrator registered.")
else:
    #使用for循环，在2次内进行循环，加上第一次循环，总计3次输入
    for i in range(2):
        print("your name or your password is error.")
        userName = (input("Please input your registered name again.\n")).strip()
        userPassword = (input("Please input your password again.\n")).strip()
        userinfo = userName + "," + userPassword
        #每次用户输入的账号和密码是否正确，在录入错误用户名后，给予提示，请使用正确的用户名
        if userName not in user:
            print("Your accout not registered,Please Contact administrator confirm, or try laster right name.")
        elif userinfo in userData:
            print("Wellcom, you are verygood.")
            break
        countInput += 1
    else:
        print("Your try too more.")
        #用户使用了正确用户名，却三次内未登录成功的，对账号进行锁定，并给予提示
        fileData = open("./db/logdata","w")
        fileData.write(userName)
        fileData.close()
        print("Your accout: %s already locked.\n"%(userName))