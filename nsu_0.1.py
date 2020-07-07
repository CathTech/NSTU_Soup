import csv
import datetime

#===============================================================================
def compress(inArr):
    tmpLinesOut = [""]
    for item in inArr:
        #избавление от пробелов
        while "  " in item:
            item= item.replace("  ", " ")
            
        if (item != '') and (item != " "):
            tmpLinesOut.append(item)
            
    return tmpLinesOut 

data = [[]]
name = "users.csv" 
temp1 = ""
#===============================================================================


#Запуск
now = datetime.datetime.now()
line = "####################################\n    [" + now.strftime(" %d-%m-%Y | %H:%M:%S") + "] \n " + "========== CI.Soup NSU v0.1 =========="
print(line + '\n')

print("Поиск input.html в корне")
#обработка input.html в корне скрипта
from bs4 import BeautifulSoup
with open("input.html", "r", encoding='utf-8') as f:
    
    #открытие input.html и его чтение
    contents = f.read() 
    soup = BeautifulSoup(contents, 'lxml')
    print("Получен входной файл") 
    

#Парсинг =======================================================================
facs = []
print("\nОбработка")
#Направление факультет
specDiv = soup.findAll("div", {"class": "mt-1 mb-1 text-center text font-bold size-small"})   

print("\nФильтрация факультетов")
for itemFac in specDiv: 
    fac = BeautifulSoup(str(itemFac), 'lxml')
    tmpLines = fac.div.text.split('\n')         
    #Вынос первой строки
    facs.append(compress(tmpLines)) 
    print(".",end ='') 
print("")
    
#Люди
print("\nФильтрация людей и объединение с факультетами")
cardDiv = soup.findAll("div", {"class": "card"})   
facCnt = 0
pplCnt = 0
for item in cardDiv:
    #Нужные поля
    studNum = BeautifulSoup(str(item.find("div", {"class": "number"})), 'lxml')       
    studFIO = BeautifulSoup(str(item.find("div", {"class": "col-12 col-lg-5"})), 'lxml') 
    #формирование записи
    tmp1 = [str(studNum.div.text), str(studFIO.div.text)] 
    if(studNum.div.text == "1"):
        if(pplCnt !=0 ): 
            print(str(pplCnt))           
            pplCnt = 0
        print(str(facCnt) + ") ",end = "")
        data.append(facs[facCnt])
        facCnt += 1
        
    data.append(tmp1)
    pplCnt += 1
print(str(pplCnt))     
print("")

#===============================================================================

#Сборка=========================================================================

#===============================================================================

#генерация CSV
print("Сохранение CSV ")
with open(name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";") 
        writer.writerows(data)

print("Выполнено.")

print("CI.Soup NSU v0.1")
