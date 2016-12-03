#/!/usr/bin/python
#-*- coding: UTF-8  -*-

# import os
#
# account_file_path = 'account.db'
#
# if os.path.exists(account_file_path):
#     account_file = open(account_file_path, 'r')
#
# else:
#     print ("Error account file account.db is not exist, please check")
#     exit(1)
#
# accounts = {}
# for line in account_file.readlines():
#     account = line.strip().split()
#     print account
#     accounts[account[0]] = account[1:]
#     print accounts
#     account_file.close()
# print accounts

provinces = {
        "1":"北京",
        "2":"上海",
        "3":"湖北省",
    }
citys = {
        "北京":{"1":"北京市区","2":"北京市郊区"},
        "上海":{"1":"上海市区"},
        "湖北省":{"1":"武汉市", "2":"宜昌市", "3":"孝感市"}
    }
areas = {
        "北京市区":{"1":"东城区", "2":"西城区", "3":"海淀区", "4":"朝阳区", "5":"丰台区", "6":"石景山区"},
        "北京市郊区":{ "1":"通州区", "2":"顺义区", "3":"房山区", "4":"大兴区", "5":"昌平区", "6":"怀柔区", "7":"平谷区", "8":"门头沟区", "9":"密云县", "10":"延庆县"},
        "上海市区":{"1":"黄浦区", "2":"卢湾区", "3":"徐汇区", "4":"长宁区", "6":"静安区", "7":"普陀区", "8":"闸北区", "9":"虹口区", "11":"杨浦区", "12":"宝山区"},
        "武汉市":{"1":"武昌", "2":"洪山", "3":"江夏", "4":"东西湖", "5":"硚口", "6":"汉阳", "7":"汉口", "8":"黄陂", "9":"蔡甸", "10":"新洲"},
        "宜昌市":{"1":"西陵区", "2":"伍家岗区", "3":"点军区", "4":"猇亭区", "5":"夷陵区"},
        "孝感市":{"1":"孝南区", "2":"孝昌县", "3":"大悟县", "4":"云梦县", "5":"应城市", "6":"安陆市", "7":"汉川市"}
    }

province_list = sorted(provinces.items(), key = lambda d:int(d[0])) #列表
#print  province_list
#[('1', '\xe5\x8c\x97\xe4\xba\xac'), ('2', '\xe4\xb8\x8a\xe6\xb5\xb7'), ('3', '\xe6\xb9\x96\xe5\x8c\x97\xe7\x9c\x81')]输出结果
#是元组

# for province_item in province_list:
#     print province_item

for province in provinces:
    #print province
    province_name = provinces[province]
    print  province_name
    city_list = sorted(citys[province_name].items(), key=lambda d: int(d[0]))
    #print city_list
    for city in citys[province_name]:
        print city #返回3个city key值
        city_name = citys[province_name][city] #
        print city_name #按照3个city key值对应 city名字
        area_list = sorted(areas[city_name].items(), key=lambda d: int(d[0])) #返回列表
        print area_list
        for area_item in area_list:
            print  area_item #元组
        for area in areas[city_name]:
            print area
            area_name = areas[city_name][area]
            print area_name
