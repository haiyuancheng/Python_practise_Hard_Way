#!/usr/bin/env python2.7
# coding:utf-8
'''
Created on: 2016年12月3日

@author: Jason

Version: 1.0

Description: 三层菜单
                1、菜单一共三级即：省，市，区县
                2、每一级菜单输入的如果输入的是菜单里的选项则进入下级菜单
                3、第1级菜单输入q退出系统
                4、第2、3级菜单输入q退出系统，输入b返回上级菜单
                5、三级菜单全部正确打印最后的全部选择结果，否则继续循环该机菜单

Help:
'''


if __name__ == '__main__':
    '''
    @parameters:
        provinces：定义省一级菜单，格式为字典，{"菜单序号":"省名称", ...}
        citys：定义省一级菜单，格式为二级嵌套字典{"省名称":{"菜单序号":"市名称"}, ...}
        area：定义区县一级菜单，格式为二级嵌套字典{"市名称":{"菜单序号":"区县名称"}, ...}
        app_info：系统信息，主要用于显示
    '''
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

    app_info = '''
       +-----------------------------------+
       |           Welcome to DevOps       |
       |           Version: 1.0            |
       |           Author: Jason           |
       +-----------------------------------+
 '''
    # 初始化菜单列表，主要是做了一次排序，解决字典无序的问题，这里的d[0]表示对key做排序，int表示先转换成整数，
    # 也就是按照整数的顺序进行排序否则如果序号超过10，会出现1后面的是10而不是2
    province_list = sorted(provinces.items(), key = lambda d:int(d[0]))
    # 初始化省一级菜单循环开关
    province_flag = True
    # 省一级菜单循环
    while province_flag:
        # 初始化市一级菜单的循环开关
        city_flag = True
        print("\033[1;31;40m  ----------This is show Some Infor Begin----------\n %s\033[1;m") % app_info
        print("\033[1;31;40m  ----------This is show Some Infor End------------\033[1;m") 
        # 打印当前用户的位置
        print("\033[1;31;40m home >\033[1;m")
        # 打印省一级菜单
        print("\033[1;32;40m+-----------------------------------+\033[1;m")
        for province_item in province_list:
            print("\033[1;32;40m  %s: %s \033[1;m" ) % province_item
        print("\033[1;32;40m+-----------------------------------+\033[1;m")
        # 获取用户输入的选项
        province = raw_input("\033[1;32;40m请输入你的省份（输入'q'退出系统）：\033[1;m").strip()
        # 判断用户的输入
        if province == 'q':
            # 如果用户输入的是q关闭省一级菜单循环开关，也就是退出系统
            province_flag = False
        elif province in provinces:
            # 如果输入的是菜单的序号执行
            # 获取省的名称
            province_name = provinces[province]
            # 初始化市一级菜单，同省一样对key进行排序
            city_list = sorted(citys[province_name].items(), key = lambda  d:int(d[0]))
            # 市一级菜单循环
            while city_flag:
                # 打印用户位置
                print("\033[1;31;40m home >%s >\033[1;m" % province_name)
                # 打印市一级菜单
                print("\033[1;32;40m+-----------------------------------+\033[1;m")
                for city_item in city_list:
			 print("\033[1;32;40m  %s: %s \033[1;m" ) % city_item
		print("\033[1;32;40m+-----------------------------------+\033[1;m")
                # 获取用户输入
                city = raw_input("\033[1;32;40m 请输入你的城市（输入'q'退出系统，输入'b'返回上一级菜单）：\033[1;m").strip()
                # 判断用户输入
                if city == 'q':
                    # 如果输入q关闭省一级和市一级循环开关，也就是退出系统
                    province_flag = False
                    city_flag = False
                elif city == 'b':
                    # 如果用户输入的是b，关闭市一级循环开关，继续省一级循环
                    city_flag = False
                elif city in citys[province_name]:
                    # 如果用户输入的是正确的菜单项
                    # 初始化区县一级循环开关
                    area_flag = True
                    # 获取市的名称
                    city_name = citys[province_name][city]
                    # 初始户区县菜单
                    area_list = sorted(areas[city_name].items(), key = lambda  d:int(d[0]))
                    # 区县一级循环
                    while area_flag:
                        # 打印用户位置
                        print(" \033[1;31;40m home home>%s >%s > \033[1;m" % (province_name,city_name))
                        # 打印区县菜单
 			print("\033[1;32;40m+-----------------------------------+\033[1;m")
                        for area_item in area_list:
                            print("\033[1;32;40m %s: %s" % area_item)
			print("\033[1;32;40m+-----------------------------------+\033[1;m")
                        # 获取用户输入
                        area = raw_input("\033[1;32;40m 请输入你的区/县（输入'q'退出系统，输入'b'返回上一级菜单）：\033[1;m").strip()
                        # 判断用户输入
                        if area == 'q':
                            # 如果是q，关闭省、市、区县一级循环开关，也就是退出系统
                            area_flag = False
                            city_flag = False
                            province_flag = False
                        elif area == 'b':
                            # 如果是b，关闭县一级循环开关，继续市循环
                            area_flag = False
                        elif area in areas[city_name]:
                            # 如果输入正确
                            # 获取区县名称
                            area_name = areas[city_name][area]
                            # 输出完整的三级菜单选择信息
                            raw_input('\033[1;31;40m 您选择的是: %s-%s-%s \n 请按任意键退出\033[1;m' %(province_name, city_name, area_name))
                            # 关闭省、市、区县循环开关，退出系统
                            area_flag = False
                            city_flag = False
                            province_flag = False
                        else:
                            # 如果区县选项输入错误提示错误
                            raw_input("\033[1;32;40m 输入错误请重新输入，输入任意键继续\033[1;m")
                else:
                    # 如果市选项输入错误提示错误
                    raw_input("\033[1;32;40m 输入错误请重新输入，输入任意键继续\033[1;m")
        else:
            # 如果省选项输入错误提示错误
           raw_input("\033[1;32;40m 输入错误请重新输入，输入任意键继续 \033[1;m")
