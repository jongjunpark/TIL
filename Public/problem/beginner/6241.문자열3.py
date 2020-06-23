a = input()
tmp = ''
protocol = ''
host = ''
others = ''
for i in a:
    if i == '/':
        host += tmp
        tmp = ''
    elif i == ':':
        protocol += tmp
        tmp = ''
    elif i != ':' or i != '/':
        tmp += i
others += tmp

print('protocol: {}'.format(protocol))
print('host: {}'.format(host))
print('others: {}'.format(others))