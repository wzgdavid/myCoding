#coding=utf-8

import copy

data = {
    'name': 'python',
    'age': 20,
}

copy_data = copy.deepcopy(data) 


def edit_name(new_name):
    copy_data['name'] = new_name


def edit_age(new_age):
    try:
        copy_data['age'] = new_age/2
    except:
        raise Exception



if __name__ == '__main__':
    try:
        # edit_age的参数应该是 int, 改成其他类型会报错, 执行之后data的数据还是老样子,
        # 但edit_age的参数正确时,两个方法都没出错, 执行之后 data 的数据改了
        edit_age('d')
        edit_name('hello')
        data.update(copy_data)
    except :
        pass
    
    print data



