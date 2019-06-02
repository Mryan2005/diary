import random
import time
print('你好，欢迎使用日记程序')
print('正在启动')
print('启动完成')
diary_id = random.randint(1, 100)
time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print('请选择接下来的操作')
print('[1] 打开原来的日记')
print('[2] 创建一个日记')
choose = int(input('>>'))
if choose == 1:
    pass
elif choose == 2:
    print('正在加载读写系统')
    def dx(nr):
        if(nr in '/'):
            file.write('\n')
            file.write('    ')
        else:
            file.write(nr)
    print('当前日记id为: ',diary_id)
    print('日期为: ',time)
    h = str(time)+'-'+str(diary_id)+'.txt'
    file = open(h,'w+')
    print('创建完成，现在可以开始编写了！')
    nr = input()
    file.write('     ')
    for word in nr:
        dx(word)