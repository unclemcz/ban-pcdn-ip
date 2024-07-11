# 对ipdb.txt的内容进行去重和排序，并输出到ipdb.txt中

# 将ipdb.txt备份为ipdb_日期_时间.txt 格式
import datetime

date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
with open('ipdb.txt', 'r') as f:
    lines = f.readlines()
    with open(f'ipdb_{date}.txt', 'w') as f:
        f.write(''.join(lines))
        print('备份完成！')

with open('ipdb.txt', 'r') as f:
    # 读取内容，并将每行的数据进行排序
    lines = f.readlines()
    lines_without_newlines = [line.strip() for line in lines]
    # 对lines_without_newlines进行去重
    lines_without_newlines = list(set(lines_without_newlines))
    # 剔除lines_without_newlines中空的元素和#开头的元素
    lines_without_newlines = [line for line in lines_without_newlines if line and not line.startswith('#')]
    #print(lines_without_newlines)
    lines_without_newlines.sort()
    # 在lines_without_newlines开头插入新元素
    lines_without_newlines.insert(0, '# IP段清单')
    #print(lines_without_newlines)
    # 将排序后的内容写入文件，要求每个元素一行
    with open('ipdb.txt', 'w') as f:
        f.write('\n'.join(lines_without_newlines))
    print('排序完成，更新完成！')

