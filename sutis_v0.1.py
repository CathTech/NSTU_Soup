import csv, datetime, requests, sys, urllib3
import sutisCore

data = [["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]]
name = "usersSUTIS.csv" 
totalPeop = 1 #счетчик людей

#Куски страниц =================================================================
pageStart = "https://sibsutis.ru/abitur/konkursnye-spiski/bachelor/?competitiveGroupID="
pageEnd = "&ajax=Y"
pageCut = ["3253233",
            "3253236",
            "3253234",
            "3253235",
            "3253212",
            "3253213",
            "3253214",
            "3253216",
            "3253215",
            "3253223",
            "3196589",
            "3253224",
            "3196590",
            "3253241",
            "3253244",
            "3253242",
            "3253243",
            "3253245",
            "3253248",
            "3253246",
            "3253247",
            "3253225",
            "3253228",
            "3253226",
            "3253227",
            "3253218",
            "3253249",
            "3253252",
            "3253250",
            "3253251",
            "3253229",
            "3253232",
            "3253230",
            "3253231",
            "3253217",
            "3253261",
            "3253264",
            "3253262",
            "3253263",
            "3253237",
            "3253240",
            "3253238",
            "3253239",
            "3196586",
            "3196585",
            "3196587",
            "3196588",
            "3253257",
            "3253260",
            "3253258",
            "3253259",
            "3253219",
            "3253222",
            "3253220",
            "3253221",
            "3253253",
            "3253256",
            "3253254",
            "3253255"]

wayList = ["ИБ-бюджет (10.03.01 Информационная безопасность)",
"ИБ-внебюджет (10.03.01 Информационная безопасность)",
"ИБ-особое право (10.03.01 Информационная безопасность)",
"ИБ-целевой прием (10.03.01 Информационная безопасность)",
"ИБТС-бюджет (10.05.02 Информационная безопасность телекоммуникационных систем)",
"ИБТС-внебюджет (10.05.02 Информационная безопасность телекоммуникационных систем)",
"ИБТС-особое право (10.05.02 Информационная безопасность телекоммуникационных систем)",
"ИБТС-УВЦ-целевой прием (10.05.02 Информационная безопасность телекоммуникационных систем)",
"ИБТС-целевой прием (10.05.02 Информационная безопасность телекоммуникационных систем)",
"ИВТ-бюджет (09.03.01 Информатика и вычислительная техника)",
"ИВТ-внебюджет (09.03.01 Информатика и вычислительная техника)",
"ИВТ-особое право (09.03.01 Информатика и вычислительная техника)",
"ИВТ-целевой прием (09.03.01 Информатика и вычислительная техника)",
"ИКТСС-1-бюджет (11.03.02 Инфокоммуникационные технологии и системы связи)",
"ИКТСС-1-внебюджет (11.03.02 Инфокоммуникационные технологии и системы связи)",
"ИКТСС-1-особое право (11.03.02 Инфокоммуникационные технологии и системы связи)",
"ИКТСС-1-целевой прием (11.03.02 Инфокоммуникационные технологии и системы связи)",
"ИКТСС-2-бюджет (11.03.02 Инфокоммуникационные технологии и системы связи)",
"ИКТСС-2-внебюджет (11.03.02 Инфокоммуникационные технологии и системы связи)",
"ИКТСС-2-особое право (11.03.02 Инфокоммуникационные технологии и системы связи)",
"ИКТСС-2-целевой прием (11.03.02 Инфокоммуникационные технологии и системы связи)",
"ИСТ-бюджет (09.03.02 Информационные системы и технологии)",
"ИСТ-внебюджет (09.03.02 Информационные системы и технологии)",
"ИСТ-особое право (09.03.02 Информационные системы и технологии)",
"ИСТ-целевой прием (09.03.02 Информационные системы и технологии)",
"ИТССС-УВЦ-целевой прием (11.05.04 Инфокоммуникационные технологии и системы специальной связи)",
"КТЭС-бюджет (11.03.03 Конструирование и технология электронных средств)",
"КТЭС-внебюджет (11.03.03 Конструирование и технология электронных средств)",
"КТЭС-особое право (11.03.03 Конструирование и технология электронных средств)",
"КТЭС-целевой прием (11.03.03 Конструирование и технология электронных средств)",
"ПИ-бюджет (09.03.03 Прикладная информатика)",
"ПИ-внебюджет (09.03.03 Прикладная информатика)",
"ПИ-особое право (09.03.03 Прикладная информатика)",
"ПИ-целевой прием (09.03.03 Прикладная информатика)",
"РСК-УВЦ-целевой прием (11.05.01 Радиоэлектронные системы и комплексы)",
"РСО-бюджет (42.03.01 Реклама и связи с общественностью)",
"РСО-внебюджет (42.03.01 Реклама и связи с общественностью)",
"РСО-особое право (42.03.01 Реклама и связи с общественностью)",
"РСО-целевой прием (42.03.01 Реклама и связи с общественностью)",
"РТ-бюджет (11.03.01 Радиотехника)",
"РТ-внебюджет (11.03.01 Радиотехника)",
"РТ-особое право (11.03.01 Радиотехника)",
"РТ-целевой прием (11.03.01 Радиотехника)",
"СРС-бюджет (11.05.02 Специальные радиотехнические системы)",
"СРС-внебюджет (11.05.02 Специальные радиотехнические системы)",
"СРС-особое право (11.05.02 Специальные радиотехнические системы)",
"СРС-целевой прием (11.05.02 Специальные радиотехнические системы)",
"ТБ-бюджет (20.03.01 Техносферная безопасность)",
"ТБ-внебюджет (20.03.01 Техносферная безопасность)",
"ТБ-особое право (20.03.01 Техносферная безопасность)",
"ТБ-целевой прием (20.03.01 Техносферная безопасность)",
"ФИИТ-бюджет (02.03.02 Фундаментальная информатика и информационные технологии)",
"ФИИТ-внебюджет (02.03.02 Фундаментальная информатика и информационные технологии)",
"ФИИТ-особое право (02.03.02 Фундаментальная информатика и информационные технологии)",
"ФИИТ-целевой прием (02.03.02 Фундаментальная информатика и информационные технологии)",
"ЭН-бюджет (11.03.04 Электроника и наноэлектроника)",
"ЭН-внебюджет (11.03.04 Электроника и наноэлектроника)",
"ЭН-особое право (11.03.04 Электроника и наноэлектроника)",
"ЭН-целевой прием (11.03.04 Электроника и наноэлектроника)"]

#===============================================================================

#Запуск
now = datetime.datetime.now()
print( "####################################\n    [" + now.strftime(" %d-%m-%Y | %H:%M:%S") + "] \n " + "========== CI.Soup SibSUTIS v0.1  ==========" + "\n")
#===============================================================================
pc = 1 #счетчик сайтов
#Работа с веб ==================================================================
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for pagePart in pageCut:
    print(">>>Страница "+ str(pc) + " A", end='')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116', 'cookie': 'PHPSESSID=c48788a2cb797ba5b3110b30800eace6'}
    print("==>", end='')
    
    
    response = requests.get(str(pageStart+pagePart+pageEnd), headers=headers, verify=False)
    
    print("B")
    #print(str(response.text))
    #sys.exit()
    
    #Обработка сайта
    for item in sutisCore.work(response, totalPeop, wayList[pc-1]):
        data.append(item)
        
    pc += 1
    totalPeop += int(data[data.__len__()-1][1])
    #sys.exit()
#===============================================================================

#генерация CSV
print("Сохранение CSV ")
with open(name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";") 
        writer.writerows(data)

print("Выполнено.\nCI.Soup SibSUTIS v0.1\nCathx.tech")