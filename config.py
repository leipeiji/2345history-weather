import random
# PC端浏览器
user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
            "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
            "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
            "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
            "Mozilla/2.02E (Win95; U)",
            "Mozilla/3.01Gold (Win95; I)",
            "Mozilla/4.8 [en] (Windows NT 5.1; U)",
            "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
            "HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
            "Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
            "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
            "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
            "Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
            "Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
            "Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
            "Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
            "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
            "Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
            "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
            "Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3",
            "Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
            "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
            "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
            "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
            "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
            "Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",

            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60 ",
            "Opera/8.0 (Windows NT 5.1; U; en) ",
            "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50 ",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50 ",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        ]
UA = random.choice(user_agent_list) #浏览器伪装
headers={'user-agent':UA}
# 移动端浏览器
user_agent_phone=[
             'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Mobile Safari/537.36',
             ' Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
             'Openwave/ UCWEB7.0.2.37/28/999',
            'NOKIA5700/ UCWEB7.0.2.37/28/999',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
            'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
            'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
            'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
             'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/61.0.3163.100 Mobile/13B143 Safari/601.1.46',
            'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
             'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',

    ]
UA_PHONE = random.choice(user_agent_list)

ROOT_DIR='X' # X是 配置大多文件保存的盘符，比如你想把数据文件 都保存到 D盘 这里  D
IS_HOME=0 # 在家里操作 写1， 公司写0

#生意经cookie 因为多文件在用 ，所以统一写到这里了
shengEjingCookie='route=0ccee3453e3a9df840aea485a40c7198; PHPSESSID=rcgnrlq8djjocc4jplmksh75u7'
TAOBAO_RANK={
    1:'1心',2:'2心',3:'3心',4:'4心',5:'5心',
    6:'1钻',7:'2钻',8:'3钻',9:'4钻',10:'5钻',
    11:'1皇冠',12:'2皇冠',13:'3皇冠',14:'4皇冠',15:'5皇冠',
    16:'1金冠',17:'2金冠',18:'3金冠',19:'4金冠',20:'5金冠',
}
weatherCityCode={'合肥': '58321', '安庆': '58424', '亳州': '58102', '蚌埠': '58221',
                 '滁州': '58236', '池州': '58427', '阜阳': '58203', '淮北': '58116',
                 '北京': '54511','重庆':'57516','上海':'58362','天津':'54527',
                 '淮南': '58224', '黄山': '70931', '六安': '58311', '马鞍山': '58336',
                 '宿州': '58122', '铜陵': '58429', '芜湖': '58334', '宣城': '58433',
                 '福州': '58847', '钓鱼岛': '71415', '龙岩': '58927', '南平': '58834',
                 '宁德': '58846', '莆田': '58946', '泉州': '59131', '三明': '58828',
                 '厦门': '59134', '漳州': '59126', '兰州': '52889', '甘南': '56080',
                 '陇南': '60472', '白银': '52896', '定西': '52995', '金昌': '52675',
                 '酒泉': '52533', '嘉峪关': '71129', '临夏': '52984', '平凉': '53915',
                 '庆阳': '53923', '天水': '57006', '武威': '52679', '张掖': '52652',
                 '广州': '59287', '潮州': '59312', '东莞': '59289', '佛山': '59288',
                 '河源': '59293', '惠州': '59297', '江门': '59473', '揭阳': '59315', '梅州': '59109', '茂名': '59659', '清远': '59280', '深圳': '59493', '汕头': '59316', '韶关': '59082', '汕尾': '59501', '阳江': '59663', '云浮': '59471', '珠海': '59488', '中山': '59485', '湛江': '59658', '肇庆': '59278',
                 '南宁': '59431', '北海': '59644', '百色': '59211', '崇左': '59425', '防城港': '59635',
                 '桂林': '57957', '贵港': '59249', '贺州': '59065', '河池': '59023', '柳州': '59046', '来宾': '59242', '钦州': '59632', '梧州': '59265', '玉林': '59453', '贵阳': '57816', '黔南': '57827', '黔东南': '57825', '安顺': '57806', '毕节': '57707', '六盘水': '56693', '黔西南': '70148', '铜仁': '57741', '遵义': '57713', '海口': '59758', '白沙': '59848', '保亭': '59945', '澄迈': '59843', '昌江': '59847', '儋州': '59845', '定安': '59851', '东方': '59838', '临高': '59842', '陵水': '59954', '乐东': '59940', '琼海': '59855', '琼中': '59849', '三亚': '59948', '三沙': '71444', '屯昌': '59854', '文昌': '59856', '万宁': '59951', '五指山': '60651', '石家庄': '53698', '保定': '54602', '承德市': '54423', '沧州': '54616', '衡水': '54702', '邯郸': '53892', '廊坊': '54515', '秦皇岛': '54449', '唐山': '54534', '邢台': '53798', '张家口': '54401', '郑州': '57083', '安阳': '53898', '鹤壁': '53990', '焦作': '53982', '济源': '53978', '开封': '57091', '洛阳': '57073', '漯河': '57186', '南阳': '57178', '濮阳': '54900', '平顶山': '71128', '三门峡': '57051', '商丘': '58005', '新乡': '53986', '许昌': '57089', '信阳': '57297', '周口': '57195', '驻马店': '57290', '哈尔滨': '50953', '大庆': '50842', '大兴安岭': '50442', '鹤岗': '50775', '黑河': '50468', '佳木斯': '50873', '鸡西': '50978', '牡丹江': '54094', '齐齐哈尔': '50745', '七台河': '50973', '双鸭山': '50884', '绥化': '50853', '伊春': '50774', '武汉': '57494', '鄂州': '57496', '恩施': '57447', '黄石': '58407', '黄冈': '57498', '荆州': '57476', '荆门': '57377', '潜江': '57475', '十堰': '57252', '随州': '57381', '神农架': '57362', '天门': '57483', '襄阳': '57278', '孝感': '57482', '咸宁': '57590', '仙桃': '57485', '宜昌': '57461', '长沙': '57687', '湘西': '60011', '常德': '57662', '郴州': '57972', '衡阳': '57872', '怀化': '57749', '娄底': '57763', '黔阳': '70356', '邵阳': '57766', '湘潭': '57773', '岳阳': '57584', '益阳': '57674', '永州': '57865', '株洲': '57780', '张家界': '57558', '长春': '54161', '白山': '54371', '白城': '50936', '吉林': '54172', '辽源': '54260', '四平': '54157', '松原': '50949', '通化': '54363', '延边': '71532', '南京': '58238', '常州': '58343', '淮安': '58141', '连云港': '58044', '南通': '58259', '苏州': '58357', '宿迁': '58131', '泰州': '58246', '无锡': '58354', '徐州': '58027', '盐城': '58151', '扬州': '58245', '镇江': '58248', '南昌': '58606', '抚州': '58617', '赣州': '57993', '九江': '58502', '景德镇': '58527', '吉安': '57799', '萍乡': '57786', '上饶': '58637', '新余': '57796', '鹰潭': '58627', '宜春': '57793', '沈阳': '54342', '鞍山': '54339', '本溪': '54346', '朝阳': '54433', '大连': '54662', '丹东': '54497', '抚顺': '54353', '阜新': '54237', '葫芦岛': '54453', '锦州': '54337', '辽阳': '54347', '盘锦': '54338', '铁岭': '54249', '营口': '54471', '呼和浩特': '53463', '乌兰察布': '60150', '锡林郭勒': '60149', '阿拉善盟': '60356', '包头': '53446', '赤峰': '54218', '鄂尔多斯': '71109', '呼伦贝尔': '71108', '巴彦淖尔': '60002', '通辽': '54135', '乌海': '53512', '兴安盟': '60001', '银川': '53614', '固原': '53817', '石嘴山': '53518', '吴忠': '53612', '中卫': '53704', '西宁': '52866', '共和': '71111', '海西': '71113', '平安': '52875', '果洛': '71729', '海北': '71112', '黄南': '71114', '海东': '71727', '海南': '71728', '玉树': '70552', '济南': '54823', '滨州': '54734', '东营': '54736', '德州': '54714', '菏泽': '54906', '济宁': '54915', '莱芜': '54828', '临沂': '54938', '聊城': '54806', '青岛': '54857', '日照': '54945', '泰安': '54827', '潍坊': '54843', '威海': '54774', '烟台': '54765', '淄博': '54830', '枣庄': '58024', '太原': '53772', '长治': '53882', '大同': '53487', '晋城': '53976', '晋中': '71115', '临汾': '53868', '吕梁': '71037', '朔州': '53578', '忻州': '53674', '阳泉': '53782', '运城': '53959', '西安': '57036', '安康': '57245', '宝鸡': '57016', '汉中': '57127', '商洛': '71031', '铜川': '53947', '渭南': '57045', '咸阳': '57048', '延安': '53845', '榆林': '53646', '杨凌': '71199', '成都': '56294', '阿坝': '56171', '巴中': '57313', '德阳': '56198', '达州': '57328', '广元': '57206', '广安': '57415', '甘孜': '56146', '泸州': '57602', '乐山': '56386', '凉山': '71118', '绵阳': '56196', '眉山': '56391', '内江': '57504', '南充': '57411', '攀枝花': '56666', '遂宁': '57405', '宜宾': '56492', '雅安': '56287', '自贡': '56396', '资阳': '56298', '拉萨': '55591', '阿里': '55437', '昌都': '56137', '林芝': '56312', '那曲': '70774', '日喀则': '55578', '山南': '55597', '乌鲁木齐': '51463', '巴州': '51656', '克州': '51704', '伊犁': '71709', '阿克苏': '51628', '阿勒泰': '51076', '阿拉尔': '51730', '博州': '51238', '巴音郭楞': '71708', '博尔塔拉': '71710', '昌吉': '51368', '哈密': '52203', '和田': '51828', '克拉玛依': '51243', '喀什': '51709', '石河子': '51356', '吐鲁番': '51573', '塔城': '51133', '图木舒克': '71712', '铁门关': '71715', '五家渠': '71713', '昆明': '56778', '迪庆': '70908', '西双版纳': '60839', '保山': '56748', '楚雄': '56768', '大理': '56751', '德宏': '71126', '红河': '56975', '丽江': '56651', '临沧': '56951', '怒江': '71127', '普洱': '70887', '曲靖': '56783', '思茅': '56964', '文山': '56994', '玉溪': '56875', '昭通': '56586', '杭州': '58457', '湖州': '58450', '嘉兴': '58452', '金华': '58549', '丽水': '58646', '宁波': '58465', '衢州': '58633', '绍兴': '58453', '台州': '58651', '温州': '58659', '舟山': '58477'}
#key是代码，value是城市 和上面相反
weatherCodeCity=dict(zip(weatherCityCode.values(),weatherCityCode.keys())) #实现和下面一样的输出
# weatherCodeCity={'58321': '合肥', '58424': '安庆', '58102': '亳州', '58221': '蚌埠',
#                   '54511':'北京',  '57516':'重庆', '58362': '上海', '54527':'天津' ,
#                  '58236': '滁州', '58427': '池州', '58203': '阜阳', '58116': '淮北',
#                  '58224': '淮南', '70931': '黄山', '58311': '六安', '58336': '马鞍山', '58122': '宿州', '58429': '铜陵', '58334': '芜湖', '58433': '宣城', '58847': '福州', '71415': '钓鱼岛', '58927': '龙岩', '58834': '南平', '58846': '宁德', '58946': '莆田', '59131': '泉州', '58828': '三明', '59134': '厦门', '59126': '漳州', '52889': '兰州', '56080': '甘南', '60472': '陇南', '52896': '白银', '52995': '定西', '52675': '金昌', '52533': '酒泉', '71129': '嘉峪关', '52984': '临夏', '53915': '平凉', '53923': '庆阳', '57006': '天水', '52679': '武威', '52652': '张掖', '59287': '广州', '59312': '潮州', '59289': '东莞', '59288': '佛山', '59293': '河源', '59297': '惠州', '59473': '江门', '59315': '揭阳', '59109': '梅州', '59659': '茂名', '59280': '清远', '59493': '深圳', '59316': '汕头', '59082': '韶关', '59501': '汕尾', '59663': '阳江', '59471': '云浮', '59488': '珠海', '59485': '中山', '59658': '湛江', '59278': '肇庆', '59431': '南宁', '59644': '北海', '59211': '百色', '59425': '崇左', '59635': '防城港', '57957': '桂林', '59249': '贵港', '59065': '贺州', '59023': '河池', '59046': '柳州', '59242': '来宾', '59632': '钦州', '59265': '梧州', '59453': '玉林', '57816': '贵阳', '57827': '黔南', '57825': '黔东南', '57806': '安顺', '57707': '毕节', '56693': '六盘水', '70148': '黔西南', '57741': '铜仁', '57713': '遵义', '59758': '海口', '59848': '白沙', '59945': '保亭', '59843': '澄迈', '59847': '昌江', '59845': '儋州', '59851': '定安', '59838': '东方', '59842': '临高', '59954': '陵水', '59940': '乐东', '59855': '琼海', '59849': '琼中', '59948': '三亚', '71444': '三沙', '59854': '屯昌', '59856': '文昌', '59951': '万宁', '60651': '五指山', '53698': '石家庄', '54602': '保定', '54423': '承德市', '54616': '沧州', '54702': '衡水', '53892': '邯郸', '54515': '廊坊', '54449': '秦皇岛', '54534': '唐山', '53798': '邢台', '54401': '张家口', '57083': '郑州', '53898': '安阳', '53990': '鹤壁', '53982': '焦作', '53978': '济源', '57091': '开封', '57073': '洛阳', '57186': '漯河', '57178': '南阳', '54900': '濮阳', '71128': '平顶山', '57051': '三门峡', '58005': '商丘', '53986': '新乡', '57089': '许昌', '57297': '信阳', '57195': '周口', '57290': '驻马店', '50953': '哈尔滨', '50842': '大庆', '50442': '大兴安岭', '50775': '鹤岗', '50468': '黑河', '50873': '佳木斯', '50978': '鸡西', '54094': '牡丹江', '50745': '齐齐哈尔', '50973': '七台河', '50884': '双鸭山', '50853': '绥化', '50774': '伊春', '57494': '武汉', '57496': '鄂州', '57447': '恩施', '58407': '黄石', '57498': '黄冈', '57476': '荆州', '57377': '荆门', '57475': '潜江', '57252': '十堰', '57381': '随州', '57362': '神农架', '57483': '天门', '57278': '襄阳', '57482': '孝感', '57590': '咸宁', '57485': '仙桃', '57461': '宜昌', '57687': '长沙', '60011': '湘西', '57662': '常德', '57972': '郴州', '57872': '衡阳', '57749': '怀化', '57763': '娄底', '70356': '黔阳', '57766': '邵阳', '57773': '湘潭', '57584': '岳阳', '57674': '益阳', '57865': '永州', '57780': '株洲', '57558': '张家界', '54161': '长春', '54371': '白山', '50936': '白城', '54172': '吉林', '54260': '辽源', '54157': '四平', '50949': '松原', '54363': '通化', '60361': '延边', '71532': '延边', '58238': '南京', '58343': '常州', '58141': '淮安', '58044': '连云港', '58259': '南通', '58357': '苏州', '58131': '宿迁', '58246': '泰州', '58354': '无锡', '58027': '徐州', '58151': '盐城', '58245': '扬州', '58248': '镇江', '58606': '南昌', '58617': '抚州', '57993': '赣州', '58502': '九江', '58527': '景德镇', '57799': '吉安', '57786': '萍乡', '58637': '上饶', '57796': '新余', '58627': '鹰潭', '57793': '宜春', '54342': '沈阳', '54339': '鞍山', '54346': '本溪', '54433': '朝阳', '54662': '大连', '54497': '丹东', '54353': '抚顺', '54237': '阜新', '54453': '葫芦岛', '54337': '锦州', '54347': '辽阳', '54338': '盘锦', '54249': '铁岭', '54471': '营口', '53463': '呼和浩特', '60150': '乌兰察布', '60149': '锡林郭勒', '60356': '阿拉善盟', '53446': '包头', '54218': '赤峰', '71109': '鄂尔多斯', '71108': '呼伦贝尔', '60002': '巴彦淖尔', '54135': '通辽', '53512': '乌海', '60001': '兴安盟', '53614': '银川', '53817': '固原', '53518': '石嘴山', '53612': '吴忠', '53704': '中卫', '52866': '西宁', '71111': '共和', '71113': '海西', '52875': '平安', '70529': '果洛', '71729': '果洛', '71112': '海北', '71114': '黄南', '71727': '海东', '71728': '海南', '70552': '玉树', '54823': '济南', '54734': '滨州', '54736': '东营', '54714': '德州', '54906': '菏泽', '54915': '济宁', '54828': '莱芜', '54938': '临沂', '54806': '聊城', '54857': '青岛', '54945': '日照', '54827': '泰安', '54843': '潍坊', '54774': '威海', '54765': '烟台', '54830': '淄博', '58024': '枣庄', '53772': '太原', '53882': '长治', '53487': '大同', '53976': '晋城', '71115': '晋中', '53868': '临汾', '71037': '吕梁', '53578': '朔州', '53674': '忻州', '53782': '阳泉', '53959': '运城', '57036': '西安', '57245': '安康', '57016': '宝鸡', '57127': '汉中', '71031': '商洛', '53947': '铜川', '57045': '渭南', '57048': '咸阳', '53845': '延安', '53646': '榆林', '71199': '杨凌', '56294': '成都', '56171': '阿坝', '57313': '巴中', '56198': '德阳', '57328': '达州', '57206': '广元', '57415': '广安', '56146': '甘孜', '57602': '泸州', '56386': '乐山', '71118': '凉山', '56196': '绵阳', '56391': '眉山', '57504': '内江', '57411': '南充', '56666': '攀枝花', '57405': '遂宁', '56492': '宜宾', '56287': '雅安', '56396': '自贡', '56298': '资阳', '55591': '拉萨', '55437': '阿里', '56137': '昌都', '56312': '林芝', '70774': '那曲', '55578': '日喀则', '55597': '山南', '51463': '乌鲁木齐', '51656': '巴州', '51704': '克州', '51431': '伊犁', '51628': '阿克苏', '51076': '阿勒泰', '51730': '阿拉尔', '51238': '博州', '71708': '巴音郭楞', '71710': '博尔塔拉', '51368': '昌吉', '52203': '哈密', '51828': '和田', '51243': '克拉玛依', '51709': '喀什', '51356': '石河子', '51573': '吐鲁番', '51133': '塔城', '71712': '图木舒克', '71715': '铁门关', '71713': '五家渠', '71709': '伊犁', '56778': '昆明', '70908': '迪庆', '60839': '西双版纳', '56748': '保山', '56768': '楚雄', '56751': '大理', '71126': '德宏', '56975': '红河', '56651': '丽江', '56951': '临沧', '71127': '怒江', '70887': '普洱', '56783': '曲靖', '56964': '思茅', '56994': '文山', '56875': '玉溪', '56586': '昭通', '58457': '杭州', '58450': '湖州', '58452': '嘉兴', '58549': '金华', '58646': '丽水', '58465': '宁波', '58633': '衢州', '58453': '绍兴', '58651': '台州', '58659': '温州', '58477': '舟山'}












