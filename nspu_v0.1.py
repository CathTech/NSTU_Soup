import csv, datetime, requests, sys, urllib3
import nspuCore
from asyncio.tasks import wait

data = [["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]]
name = "usersNSPU.csv" 
totalPeop = 1 #счетчик людей

#Куски страниц =================================================================
pageStart = "https://nspu.ru/priemka/kg_win1251.php"

#===============================================================================

#Запуск
now = datetime.datetime.now()
print( "####################################\n    [" + now.strftime(" %d-%m-%Y | %H:%M:%S") + "] \n " + "========== CI.Soup NSPU v0.1  ==========" + "\n")
#===============================================================================
pc = 1 #счетчик сайтов
#Работа с веб ==================================================================
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for pagePart in nspuCore.urlList:
    print(">>>Страница "+ str(pc) + " A", end='')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116', 'cookie': 'PHPSESSID=c48788a2cb797ba5b3110b30800eace6'}
    print("==>", end='')
    
    
    response = requests.get(str(pageStart+pagePart[0]), headers=headers, verify=False)
    print("B")
    #print(str(pageStart+pagePart[0]))
    #print(str(response.text))
    #sys.exit()
    
    #Обработка сайта
    for item in nspuCore.work(response, totalPeop, [pagePart[1],pagePart[2]]):
        data.append(item)
        
    #print(str(data))
    pc += 1
    if(str(data[data.__len__()-1][1]) != "На направлении"):
         totalPeop += int(data[data.__len__()-1][1])
#sys.exit()
#===============================================================================

#генерация CSV
print("Сохранение CSV ")
with open(name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";") 
        writer.writerows(data)

print("Выполнено.\nCI.Soup NSPU v0.1\nCathx.tech")