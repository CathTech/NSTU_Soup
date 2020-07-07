import csv, time
import datetime
import pathlib
import bs4
#===============================================================================
def compress(inArr):
    tmpLinesOut = [""]
    for item in inArr:
        #избавление от пробелов
        while "  " in item:
            item= item.replace("  ", " ")
        #фильтрация   
        while "общий конкурс" in item:
            item= item.replace("общий конкурс", "")
        while "ПВЗ" in item:
            item= item.replace("ПВЗ", "")
        while " ." in item:
            item= item.replace(" .", "")
            
        if (item != '') and (item != " "):
            tmpLinesOut.append(item)
            
    return tmpLinesOut 

data = [["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление"]]
name = "users.csv" 
temp1 = ""
#===============================================================================

#https://pypi.org/project/selenium/
#https://chromedriver.chromium.org/getting-started
#https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/

#==========FIX SYNTAX ERROR=====================================================
#from String import String as IOStream
#(webelement:37)
#===============================================================================
totalPeop = 1 #счетчик людей

#Запуск
now = datetime.datetime.now()
line = "####################################\n    [" + now.strftime(" %d-%m-%Y | %H:%M:%S") + "] \n " + "========== CI.Soup NSU v0.5 =========="
print(line + '\n')

#Работа с веб ==================================================================
from selenium import webdriver
from selenium.webdriver import ActionChains
print("Запуск chrome\n")
#путь к webDriver
driver = webdriver.Chrome(executable_path=str(pathlib.Path().absolute()) + r"\chromedriver83.exe")  # Optional argument, if not specified will search path.

# Блок 1 =======================================================================
#Сайт
print("Работа с сайтом")
driver.get('https://abiturient.nsu.ru/');

#Заполнение формы
ActionChains(driver).click(driver.find_element_by_id('vs1__combobox')).perform()
ActionChains(driver).click(driver.find_element_by_xpath("//*[contains(text(), 'Подавшие заявления')]")).perform()

ActionChains(driver).click(driver.find_element_by_id('vs2__combobox')).perform()
ActionChains(driver).click(driver.find_element_by_xpath("//*[contains(text(), 'Бюджет')]")).perform()

ActionChains(driver).click(driver.find_element_by_xpath("//*[contains(text(), 'Посмотреть')]")).perform()

#Ожидание загрузки
print("Ожидание информации")
ActionChains(driver).click(driver.find_element_by_xpath("//*[contains(text(), 'Списки абитуриентов')]")).perform()

#получение страницы бюджетников
print("Получение страницы бюджетников")
main_page_bu = driver.page_source
#===============================================================================

# Блок 2 =======================================================================

#Сайт
print("")
print("Работа с сайтом")
driver.get('https://abiturient.nsu.ru/');
#Заполнение формы
ActionChains(driver).click(driver.find_element_by_id('vs1__combobox')).perform()
ActionChains(driver).click(driver.find_element_by_xpath("//*[contains(text(), 'Подавшие заявления')]")).perform()

ActionChains(driver).click(driver.find_element_by_id('vs2__combobox')).perform()
ActionChains(driver).click(driver.find_element_by_xpath("//*[contains(text(), 'Платное поступление')]")).perform()

ActionChains(driver).click(driver.find_element_by_xpath("//*[contains(text(), 'Посмотреть')]")).perform()

#Ожидание загрузки
print("Ожидание информации")
ActionChains(driver).click(driver.find_element_by_xpath("//*[contains(text(), 'Списки абитуриентов')]")).perform()

#получение страницы контрактников
print("Получение страницы контрактников")
main_page_co = driver.page_source
driver.quit()
#===============================================================================


#Начало обработки файла ========================================================
#обработка списка бюджетников
print("\nНачало работы парсера 1")
soup = bs4.BeautifulSoup(main_page_bu, 'lxml')
print("\nПолучен файл") 
main_page_bu = 0
    
#Парсинг 
facs = []
print("Обработка")
#Направление факультет
specDiv = soup.findAll("div", {"class": "mt-1 mb-1 text-center text font-bold size-small"})   

print("\nФильтрация факультетов")
for itemFac in specDiv: 
    fac = bs4.BeautifulSoup(str(itemFac), 'lxml')
    tmpLines = fac.div.text.split('\n')         
    #Вынос первой строки
    facs.append(compress(tmpLines)) 
    print(".",end ='') 
print("")
    
#Люди
print("\nФильтрация людей и объединение с факультетами")
cardDiv = soup.findAll("div", {"class": "card"})   
facCnt = -1
pplCnt = 0
for item in cardDiv:
    #Нужные поля
    studNum = bs4.BeautifulSoup(str(item.find("div", {"class": "number"})), 'lxml')       
    studFIO = bs4.BeautifulSoup(str(item.find("div", {"class": "col-12 col-lg-5"})), 'lxml') 
    #проверка факультетов по численности
    if(studNum.div.text == "1"):
        if(pplCnt !=0 ): 
            print(str(pplCnt))           
            pplCnt = 0
        print(str(facCnt+2) + ") ",end = "")
        facCnt += 1
     
    #формирование записи
    tmp1 = [int(totalPeop), str(studNum.div.text), str(studFIO.div.text), "Бюджет", str(facs[facCnt][1]), str(facs[facCnt][3])] 
    
    data.append(tmp1)
    pplCnt += 1
    totalPeop += 1
print(str(pplCnt))     
print("")
#===============================================================================
soup = 0
#Начало обработки файла ========================================================
print("Начало работы парсера 2")
#обработка списка контрактников
soup = bs4.BeautifulSoup(main_page_co, 'lxml')
print("Получен файл") 
main_page_co = 0

#Парсинг 
facs = []
print("\nОбработка")
#Направление факультет
specDiv = soup.findAll("div", {"class": "mt-1 mb-1 text-center text font-bold size-small"})   

print("\nФильтрация факультетов")
for itemFac in specDiv: 
    fac = bs4.BeautifulSoup(str(itemFac), 'lxml')
    tmpLines = fac.div.text.split('\n')         
    #Вынос первой строки
    facs.append(compress(tmpLines)) 
    print(".",end ='') 
print("")
    
#Люди
print("\nФильтрация людей и объединение с факультетами")
cardDiv = soup.findAll("div", {"class": "card"})   
facCnt = -1
pplCnt = 0
for item in cardDiv:
    #Нужные поля
    studNum = bs4.BeautifulSoup(str(item.find("div", {"class": "number"})), 'lxml')       
    studFIO = bs4.BeautifulSoup(str(item.find("div", {"class": "col-12 col-lg-5"})), 'lxml') 
    
    #проверка факультетов по численности
    if(studNum.div.text == "1"):
        if(pplCnt !=0 ): 
            print(str(pplCnt))           
            pplCnt = 0
        print(str(facCnt+2) + ") ",end = "")
        facCnt += 1
     
    #формирование записи
    tmp1 = [int(totalPeop), str(studNum.div.text), str(studFIO.div.text), "Контракт", str(facs[facCnt][1]), str(facs[facCnt][3])]    
    data.append(tmp1)
    pplCnt += 1
    totalPeop += 1
print(str(pplCnt))     
print("")
#===============================================================================
#===============================================================================

#генерация CSV
print("Сохранение CSV ")
with open(name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";") 
        writer.writerows(data)

print("Выполнено.\nCI.Soup NSU v0.5\nCathx.tech")
