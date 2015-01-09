# encoding: utf-8

import os

class SearchPath(object):

    @classmethod
    def get(cls, search_path, key_word, search_type='file'):
        '''指定路径搜索，多个关键字用list'''
        if not os.path.exists(search_path):
            print 'no this path'
            return []
        type_dict = {'file': 2, 'dir': 1}
        result = []
        for info in os.walk(search_path):
            for name in info[type_dict[search_type]]:
                if isinstance(key_word, str):
                    if key_word in name:
                        result.append(info[0] + '/' + name)

                if isinstance(key_word, list):
                    if all([n in name for n in key_word]):
                        result.append(info[0] + '/' + name)
        return result       



if __name__ == '__main__':
    
    print SearchPath.get('/Users/myc/desktop/books', 'dive')
    print SearchPath.get('/Users/myc/desktop/books', ['pl', 'al'])
    SearchPath.get('/Users/myc/desktop/books', 'stage', search_type='dir')
