import csv, datetime, requests, sys, urllib3
import tsuCore

data = [["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]]
name = "usersTSU.csv" 
totalPeop = 1 #счетчик людей

#Куски страниц =================================================================
pageStart = "http://abiturient.tsu.ru/statements?l=1"
pageEnd = "&c=1&ef=1"

pageFacs = [["&d=01.03.01","&d=02.03.01","&d=01.03.03"],        
["&d=10.05.01","&d=10.05.01","&d=09.03.03","&d=01.03.02","&d=02.03.02"],
["&d=12.03.05","&d=12.03.02","&d=03.03.03","&d=11.05.01","&d=12.03.03"],    
["&d=09.03.02","&d=03.03.02"],    
["&d=04.05.01","&d=04.03.01"],    
["&d=05.03.02","&d=05.03.01","&d=05.03.04","&d=05.03.06"],
["&d=35.03.04","&d=06.03.01","&d=35.03.10","&d=35.03.01","&d=06.03.02","&d=05.03.06"],
["&d=09.03.04"],
["&d=24.03.03","&d=15.03.06","&d=15.03.03","&d=16.03.01"],
["&d=27.03.05","&d=09.04.02","&d=27.03.02"],
["&d=27.03.05"],
["&d=37.05.01","&d=39.03.03","&d=37.03.01","&d=42.03.01"],
["&d=38.04.04","&d=38.03.02","&d=38.04.03","&d=38.04.08","&d=38.03.01","&d=38.05.01"],
["&d=39.03.02","&d=39.03.01","&d=47.03.01"],
["&d=40.05.01","&d=40.03.01"],
["&d=46.03.03","&d=46.03.02","&d=41.03.01","&d=46.03.01","&d=41.03.05","&d=41.03.04","&d=41.03.02"],
["&d=42.03.03","&d=52.05.04","&d=52.05.04"],
["&d=42.03.02"],
["&d=51.03.06","&d=54.05.03","&d=54.03.01","&d=53.05.01","&d=51.03.01","&d=51.03.04","&d=53.05.04","&d=44.03.01","&d=53.05.02"],
["&d=45.03.02","&d=45.05.01","&d=45.03.03"],
["&d=49.03.03","&d=49.03.01"],
["&d=05.04.06"],
["&d=41.04.02"],
["&d=41.04.05"],
["&d=46.04.03"],
["&d=03.04.02"],
["&d=03.04.02"],
["&d=04.04.01"],
["&d=01.04.02"],
["&d=47.04.01"],
["&d=09.04.03"],
["&d=45.04.03"],
["&d=06.06.01","&d=09.06.01","&d=10.06.01","&d=46.06.01","&d=02.06.01","&d=51.06.01","&d=35.06.02","&d=01.06.01","&d=05.06.01","&d=44.06.01","&d=41.06.01","&d=37.06.01","&d=03.06.01","&d=16.06.01","&d=49.06.01","&d=47.06.01","&d=04.06.01","&d=38.06.01","&d=40.06.01","&d=45.06.01"],
["&d=40.03.01"],
["&d=40.03.01"]]

facList = ["Механико-математический факультет",
"Институт прикладной математики и компьютерных наук",
"Радиофизический факультет",
"Физический факультет",
"Химический факультет",
"Геолого-географический факультет",
"Институт биологии, экологии, почвоведения, сельского и лесного хозяйства (Биологический институт)",
"Научно-образовательный центр (Высшая ИТ школа)",
"Физико-технический факультет",
"Факультет инновационных технологий",
"Институт (Умные материалы и технологии)",
"Факультет психологии",
"Институт экономики и менеджмента",
"Философский факультет",
"Юридический институт",
"Факультет исторических и политических наук",
"Филологический факультет",
"Факультет журналистики",
"Институт искусств и культуры",
"Факультет иностранных языков",
"Факультет физической культуры",
"Автономная образовательная программа Изучение Сибири и Арктики",
"Автономная образовательная программа Сибирь: ресурсы и современные практики развития региона",
"Автономная образовательная программа Евразийская интеграция: политика, право, торгово-экономическое взаимодействие",
"Автономная образовательная программа Миграционные исследования",
"Автономная образовательная программа Биофотоника",
"Автономная образовательная программа Инновации и общество: наука, техника, медицина",
"Автономная образовательная программа Трансляционные химические и биомедицинские технологии",
"Автономная образовательная программа Интеллектуальный анализ больших данных",
"Автономная образовательная программа Гуманитарная информатика",
"Автономная образовательная программа Цифровые технологии в издательском деле",
"Автономная образовательная программа Компьютерная и когнитивная лингвистика",
"Кадры высшей квалификации",
"Новосибирский юридический институт(филиал)Томского государственного университета",
"Институт биологии,экологии,почвоведения,сельского и лесного хозяйства (Биологический институт)"]


#===============================================================================

#Запуск
now = datetime.datetime.now()
print( "####################################\n    [" + now.strftime(" %d-%m-%Y | %H:%M:%S") + "] \n " + "========== CI.Soup TSU v0.1  ==========" + "\n")
#===============================================================================
pc = 1 #счетчик сайтов
#Работа с веб ==================================================================


for pagePart in pageFacs:
    pp = 1
    for pageCut in pagePart:
        print(">>>Страница " + str(pc) + "." + str(pp) + " A", end='')
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116', 'cookie': 'PHPSESSID=c48788a2cb797ba5b3110b30800eace6'}
        print("==>", end='')
        pp += 1
        
        response = requests.get(str(pageStart+"&f="+str(pc)+pageCut+pageEnd), headers=headers)
        
        print("B")
        #print(str(pageStart+"&f="+str(pc)+pageCut+pageEnd)+"\n")
        #print(str(response.text))
        #sys.exit()
        
        #Обработка сайта
        for item in tsuCore.work(response, totalPeop, facList[pc-1]):
            data.append(item)
            
        totalPeop += int(data[data.__len__()-1][1])
    pc += 1
        #sys.exit()
#===============================================================================

#генерация CSV
print("Сохранение CSV ")
with open(name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";") 
        writer.writerows(data)

print("Выполнено.\nCI.Soup TSU v0.1\nCathx.tech")