# 对ipdb.txt的内容进行去重和排序，并输出到ipdb.txt中

# 将ipdb.txt备份为ipdb_日期_时间.txt 格式
import datetime

def main(filename='ipdb.txt'):
    date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(f"{filename.split('.')[0]}_{date}.txt")
        with open(f"{filename.split('.')[0]}_{date}.txt", 'w') as f:
            f.write(''.join(lines))
            print('备份完成！')

    with open(filename, 'r') as f:
        # 读取内容，并将每行的数据进行排序
        lines = f.readlines()
        lines_without_newlines = [line.strip() for line in lines]
        # 对lines_without_newlines进行去重
        lines_without_newlines = list(set(lines_without_newlines))
        # 剔除lines_without_newlines中空的元素和#开头的元素
        lines_without_newlines = [line for line in lines_without_newlines if line and not line.startswith('#')]
        # 将ip清单中的每个ip地址按照点分十进制进行排序
        lines_without_newlines.sort(key=lambda x: tuple(map(int, x.split('/')[0].split('.'))))
        # 在lines_without_newlines开头插入新元素
        lines_without_newlines.insert(0, '# IP段清单')
        print(lines_without_newlines)
        # 打印lines_without_newlines的长度
        print(len(lines_without_newlines))
        # 将排序后的内容写入文件，要求每个元素一行
        with open(filename, 'w') as f:
            f.write('\n'.join(lines_without_newlines))
        print('排序完成，更新完成！')



if __name__ == '__main__':
    main()