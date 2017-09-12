# encoding: utf-8
import re


def get_file_text(file_name):
    file = open(file_name)
    text = file.read()
    file.close()
    return text


def find_ip(text):
    pattern = re.compile(r'\w{1,3}\.\w{1,3}\.\w{1,3}\.\w{1,3}')
    findlist = re.findall(pattern, text)
    return set(findlist)

def find_ip_in_log():
    text = get_file_text('test.log')
    ips = find_ip(text)
    print ips

if __name__ == "__main__":
    find_ip_in_log()


