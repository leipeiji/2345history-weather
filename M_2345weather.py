# -*- coding: utf-8 -*-
from config import *
import os
import requests
import re
import  time
from multiprocessing import Pool
from openpyxl import Workbook
import datetime
# http://tianqi.2345.com/t/wea_history/js/57083_20129.js
# http://tianqi.2345.com/t/wea_history/js/57083_201209.js

MYCOUNT=0
# =================得到每月的天气数据===============
def getEveryMonthWeatherList(cityCode,date,Mcount=MYCOUNT):
    global MYCOUNT
    try:
        # query = {'app': 'shopsearch', 'ie': '	utf8',
        #          }
        dateFirst = str(date.split('-')[0])+ str(int(date.split('-')[1]))
        dateTwo=str(date.split('-')[0])+str(date.split('-')[1])
        requestFirst = 'http://tianqi.2345.com/t/wea_history/js/{}_{}.js'.format(cityCode,dateFirst)
        requestTwo = 'http://tianqi.2345.com/t/wea_history/js/{}/{}_{}.js'.format(dateTwo,cityCode, dateTwo)
        headers = {'user-agent': UA}
        try:
            r = requests.get(requestFirst, headers=headers)
            if r.status_code != 200:
                # print( '老地址出错了，请求新地址')
                r = requests.get(requestTwo, headers=headers)
        except Exception as e:
            print(e,'error')
        print(r.status_code, r.url)
        if r.status_code == 200:
            # print(r.text)
            # print(r.headers)

            pattern=r'var weather_str=(.*?),{}]'
            newPattern=re.compile(pattern,re.S)
            myAllList = re.findall(newPattern, r.text)[0] #得到完整的就送格式数据
            secondP=r"ymd:'(.*?)',bWendu:'(.*?)',yWendu:'(.*?)',tianqi:'(.*?)',fengxiang:'(.*?)',fengli:'(.*?)'"
            newList=re.compile(secondP, re.S).findall(myAllList)
            # print(len(newList),newList)
            # print(type(newList))
            return newList
        else:
            print('可能输入日期有误')
            return None

    except Exception as e:
        MYCOUNT+=1
        print(e,'第\t%d次\t请求链接出现问题，正在请求下一次链接......'%MYCOUNT)
        #对于一些无法预料的错误的处理 比如淘宝不让搜索 sisy私服 这个，如果不加判断条件，程序就会一直请求，死循环了
        if MYCOUNT<6:
            getEveryMonthWeatherList(cityCode, date, Mcount=MYCOUNT)
        else:
            MYCOUNT = 0
            print('出错次数达到上限，程序结束，请检查函数 ')
            return None

# =============得到城市和对应的编码，这个开始运行，把数据保存到 config.py文件中，以后就不用运行了 这个数据是死的，一般不会变
def getCityCodeAjax(Mcount=MYCOUNT):
    global MYCOUNT
    try:
        # query = {'app': 'shopsearch', 'ie': '	utf8',
        #          }
        requestFirst = 'http://tianqi.2345.com/js/citySelectData.js'
        headers = {'user-agent': UA}
        try:
            r = requests.get(requestFirst, headers=headers)
        except Exception as e:
            print(e,'error')

        print(r.status_code, r.url)
        if r.status_code == 200:
            # print(r.text)
            pattern=r'var prov=new Array.*?台湾-36\'.*?(.*?)var provqx'
            # pattern =''
            newPattern=re.compile(pattern,re.S)
            myAllList = re.findall(newPattern, r.text)[0] #得到完整的就送格式数据
            # print(len(myAllList),type(myAllList), myAllList)
            secondP="'(.*?)'"
            # secondP=r"ymd:'(.*?)',bWendu:'(.*?)',yWendu:'(.*?)',tianqi:'(.*?)',fengxiang:'(.*?)',fengli:'(.*?)'"
            newList=re.compile(secondP, re.S).findall(myAllList)
            # print(len(newList),newList)
            print('===============================')
            print(type(newList))
            return newList
        else:
            print('得到城市和对应编码错误')
            return None
    except Exception as e:
        MYCOUNT+=1
        print(e,'第\t%d次\t请求链接出现问题，正在请求下一次链接......'%MYCOUNT)
        #对于一些无法预料的错误的处理 比如淘宝不让搜索 sisy私服 这个，如果不加判断条件，程序就会一直请求，死循环了
        if MYCOUNT<6:
            getCityCodeAjax(Mcount=MYCOUNT)
        else:
            MYCOUNT = 0
            return None


# ============处理城市和对应编码数据，变成一个字典，存放到 config.py文件中，开始运行，以后不需要了======
def cityCodeList(cityCodeList=getCityCodeAjax()):
    allDict={}
    outersingleListCity=[]
    outersingleListCode=[]
    for city in cityCodeList:
        print(city)
        everyCityList=city.split('|')
        singleListCity=[]
        singleListCode=[]
        for mycity in everyCityList:
            try:
                singleCity=mycity.split(' ')[1]
                singleListCity.append(singleCity.split('-')[0])
                singleListCode.append(singleCity.split('-')[1])
                outersingleListCity+=singleListCity
                outersingleListCode+=singleListCode
            except Exception as e:
                print(e,'-------处理城市和编码时 error-----------------')
                continue
    print(len(outersingleListCode),outersingleListCode)
    # allDict=dict(zip(outersingleListCity,outersingleListCode))
    allDict = dict(zip( outersingleListCode,outersingleListCity))
    print(len(allDict),type(allDict),allDict)
    return allDict


# =================得到一个城市给定日期范围的 所有天气数据列表=================
def manyDateDataList(cityCode):
    try:
        dateList = createDateList(startDate,endDate)
        bigDataList = []
        for date in dateList:
            try:
                smallList=getEveryMonthWeatherList(cityCode, date)
                print(smallList)
                bigDataList += smallList
            except Exception as e:
                print(e, 'error')
                continue
            time.sleep(1)
        print(len(bigDataList),bigDataList)
        return bigDataList
    except Exception as e:
        print(e)


#===========================店铺信息存到excel文件 这个用在excel 2007及以上的版本=====================
def EveryPageWriteExcel2016(cityInfoList,cityCode,sheetName='data'):
    try:
        curCity = weatherCodeCity[cityCode]
        print('开始保存\t%s\t城市数据.....'%curCity)
        AllExcelHead = ['0日期', '1最高气温', '2最低气温', '3天气', '4风向风力', '5空气质量指数',]
        # 从城市编码反过来 得到城市名字

        print(curCity,'============================---------------')
        filePath=r'{}\{}'.format(SavePath, str(curCity))
        if not os.path.exists(filePath):
            os.makedirs(filePath)
        # fetchDate = time.strftime("%Y-%m-%d", time.localtime())
        doc = r'{}\{}{}_{}.{}'.format(filePath, curCity,startDate,endDate, 'xlsx')
        # 在内存创建一个工作簿obj
        wb = Workbook()
        ws=wb.active
        #给sheet明个名
        ws.title = sheetName
        # 向第一个sheet页写数据吧 格式 ws2['B1'] = 4
        ws.append(AllExcelHead)
        k = 0
        for line in cityInfoList:
            try:
                print(line)
                ws.append(line)
                k += 1
                print('写入第%d条记录完毕' % (k))
            except Exception as e:
                print(e,'第%d条记录有问题，已经忽略' % k)
                continue
        else:
            print('###############恭喜你，写入完毕#####################')
        wb.save(doc)
        print('\t{}\t城市数据保存完毕,文件路径是\t{}'.format(curCity,doc))
    except Exception as e:
        print(e ,'函数 \tEveryPageWriteExcel2016\t出现问题了')
        pass


# ======================得到类似 ['2012-01', '2012-02', '2012-03']===========
def createDateList(startDate,endDate):
    try:
        yearList = [year for year in range(int(startDate.split('-')[0]),int(endDate.split('-')[0])+1)]
        print(yearList)
        # yearList=['2012','2013','2014','2015','2016']
        # yearList = ['2012', '2013']
        monthList=['01','02','03','04','05','06','07','08','09','10','11','12']
        allDateList=[]
        startYear=int(startDate.split('-')[0])
        startMonth = int(startDate.split('-')[1])
        for year in yearList:
            tempList=[]
            # 保证第一年的起始月是对的
            if year==startYear:
                newMonthList=monthList[startMonth-1:]
            else:
                newMonthList=monthList

            for month in newMonthList:
                yearMonth='{}-{}'.format(year,month)
                tempList.append('{}-{}'.format(year,month))
                if endDate == yearMonth:
                    break #结束本轮里层的 for循环，下面的循环不在执行，但外的循环还是继续执行
            allDateList+=tempList
        print(len(allDateList),allDateList)
        return allDateList
    except Exception as e:
        print(e,'创建日期列表出错了,这里只查询了 开始和结束日期....')
        return [startDate,endDate]


# ===================从城市名字获取城市代码================
def fromCityGetCityCode(needCityList):
    cityCodeLs=[]
    try:
        for curCity in needCityList:
            try:
                # weatherCityCode 是一个字典 在config.py文件中，存放城市和编码的字典
                cityCode = weatherCityCode[curCity]
                cityCodeLs.append(cityCode)
            except Exception as e:
                print(e,'得到城市代码错误...')
                continue
        print(len(cityCodeLs),cityCodeLs)
        return cityCodeLs
    except Exception as e:
        print(e,'从城市名字获取城市编码出错了')
        return None

#=========== 主函数===================
def main(cityCode):
    #得到一个城市 给定日期范围的 所有天气数据
    cityInfoList= manyDateDataList(cityCode)
    #同步写入文件 以城市和日期命名的
    EveryPageWriteExcel2016(cityInfoList,cityCode=cityCode)

# ---------------------功能---------  获取2345天气--------------更新时间  2017-09-05 ----------
start = datetime.datetime.now()
SavePath='{}:\天气信息'.format(ROOT_DIR)

#下面输入的日期是 月份 按照标准格式

startDate='2017-09' #必须的
endDate='2017-09' #必须的
needCityList=['济南','郑州','北京','深圳','上海','广州','杭州','青岛','南京','沈阳','石家庄','武汉','西安'] #必须的
# needCityList=['济南'] #必须的
# needCityList=['新乡','平顶山','天津']
# createDateList(startDate,endDate)

if __name__ == '__main__':
    cityCodeLs = fromCityGetCityCode(needCityList)
    myp = Pool()
    myp.map(main, cityCodeLs)
    end = datetime.datetime.now()
    print('☺☺☺☺☺☺恭喜你，全部信息保存完毕用时 %s ☺☺☺☺☺☺' % (end - start))

