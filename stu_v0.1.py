import csv, datetime, requests, sys, urllib3
import stuCore

data = [["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]]
name = "usersSTU.csv" 
totalPeop = 1 #счетчик людей

#Куски страниц =================================================================
pageStart = "https://www.stu.ru/abiturient/abiturients_table.php?uroven_podgotovki=1&forma_obucheniya="

listType = [
"&type=podavshie_obshii_bud",    
"&type=podavshie_obshii_pvz",
"&type=podavshie_celev",
"&type=podavshie_lgoti",
"&type=podavshie_bez_ispitanii"]

forms = ["Бюджет","Контракт","Целевой","Особое право","Без испытаний"]

mainList = [
["-", "&napravlenie=%C3%EE%F1%F3%E4%E0%F0%F1%F2%E2%E5%ED%ED%EE%E5%20%E8%20%EC%F3%ED%E8%F6%E8%EF%E0%EB%FC%ED%EE%E5%20%F3%EF%F0%E0%E2%EB%E5%ED%E8%E5", "-", "&napravlenie=%C3%EE%F1%F3%E4%E0%F0%F1%F2%E2%E5%ED%ED%EE%E5%20%E8%20%EC%F3%ED%E8%F6%E8%EF%E0%EB%FC%ED%EE%E5%20%F3%EF%F0%E0%E2%EB%E5%ED%E8%E5", "&napravlenie=%C3%EE%F1%F3%E4%E0%F0%F1%F2%E2%E5%ED%ED%EE%E5%20%E8%20%EC%F3%ED%E8%F6%E8%EF%E0%EB%FC%ED%EE%E5%20%F3%EF%F0%E0%E2%EB%E5%ED%E8%E5"],
["&specializ=9233344",     "&specializ=9233344", "&specializ=9233344", "&specializ=9233344", "-"],
["-", "&specializ=8910700", "-", "-", "-"],
["-", "&specializ=8910714", "-", "-", "-"],
["-", "&specializ=8910693", "-", "-", "-"],
["&specializ=9233345", "&specializ=9233345", "-", "&specializ=9233345", "-"],
["-", "&napravlenie=%CF%F1%E8%F5%EE%EB%EE%E3%E8%FF", "-", "&napravlenie=%CF%F1%E8%F5%EE%EB%EE%E3%E8%FF", "-"],
["-", "&specializ=9233347", "-", "&specializ=9233347", "-"],
["&specializ=8910689", "&specializ=8910689", "-", "-", "-"],
["&specializ=9233361", "&specializ=9233361", "-", "-", "-"],
["&specializ=8910001", "&specializ=8910001", "-", "-", "-"],
["&specializ=9233333", "&specializ=9233333", "-", "-", "-"],
["&specializ=8910650", "&specializ=8910650", "-", "&specializ=8910650", "-"],
["-", "&napravlenie=%D3%EF%F0%E0%E2%EB%E5%ED%E8%E5%20%EF%E5%F0%F1%EE%ED%E0%EB%EE%EC", "-", "-", "-"],
["-", "&specializ=8910691", "-", "-", "-"],
["-", "&specializ=8910695", "-", "-", "-"],
["-", "&specializ=9233353", "-", "-", "-"],
["-", "&specializ=8910696", "-", "-", "-"],
["-", "&specializ=9233351", "-", "&specializ=9233351", "-"],
["-", "&specializ=9233340", "-", "-", "-"],
["&specializ=8910718", "&specializ=8910718", "-", "&specializ=8910718", "-"],
["-", "&napravlenie=%DE%F0%E8%F1%EF%F0%F3%E4%E5%ED%F6%E8%FF", "-", "-", "-"]]



#===============================================================================

#Запуск
now = datetime.datetime.now()
print( "####################################\n    [" + now.strftime(" %d-%m-%Y | %H:%M:%S") + "] \n " + "========== CI.Soup STU v0.1  ==========" + "\n")
#===============================================================================
pc = 0 #счетчик сайтов
cnt = 0 # счетчик форм обучения

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#Работа с веб ==================================================================

for stForm in forms:    
    for pagePart in mainList:
        print(">>>" + str(stForm) +": Страница: "+ str(pc+1) + " A", end='')
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116', 'cookie': 'PHPSESSID=c48788a2cb797ba5b3110b30800eace6'}
        
        #print("["+str(pc)+":"+str(cnt)+"]")
        
        #пропуск отсутствующих направлений на форме обучения
        if(mainList[pc][cnt] == "-"):
            print("-X")
        
        if(mainList[pc][cnt] != "-"):
            print("==>", end='') 
            response = requests.get(str(pageStart+"1"+listType[0]+mainList[pc][cnt]), headers=headers, verify=False)
            print("B")
        #print(str(response.text))
        #sys.exit()
        
        #Обработка сайта
            for item in stuCore.work(response, totalPeop,str(stForm)):
                data.append(item)            
        
            totalPeop += int(data[data.__len__()-1][1])
        pc += 1
        #sys.exit()
    pc = 0
    cnt += 1    
#===============================================================================

#генерация CSV
print("\nСохранение CSV ")
with open(name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";") 
        writer.writerows(data)

print("Выполнено.\nCI.Soup STU v0.1\nCathx.tech")