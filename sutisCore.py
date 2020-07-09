import bs4
from multiprocessing import sys

def work(response, totalPeop, direction):
    data = []
    tmpPplCnt = 1
    #Начало обработки файла ========================================================
    soup = bs4.BeautifulSoup(str(response.text), 'lxml')
    response = 0
    print("Людей: "+str(totalPeop)+ " | Обработка")
    
    #импорт заголовка 
    
    h2Text = bs4.BeautifulSoup(str(soup.find("h2")), 'lxml')
    if(h2Text.text == "None"):
        print("Нет людей \n")
        return [[str(totalPeop-1),'0',"", "Очная", "", str(direction), ""]]
    #===============================================================================
    
    #информационная таблица
    table = bs4.BeautifulSoup(str(soup.find("table", {"id": "master-list"})), 'lxml')  
    soup = 0
    #print(str(table.prettify()))
    tableTr = table.findAll("tr")    
    
    for tr in tableTr: 
        td = tr.findAll("td")
        trTmp =[]
        for tmp in td:
            txt = str(tmp)
            #Очистка
            while "  " in txt:
                txt = txt.replace("  ", "")
                
            while "\n" in txt:
                txt = txt.replace("\n", "")                
                
            while "<td class=\"PROPERTY_FIZICHESKOELITSO_VALUE\">" in txt:
                txt = txt.replace("<td class=\"PROPERTY_FIZICHESKOELITSO_VALUE\">", "")
                
            while "<span class=\"mob\">" in txt:
                txt = txt.replace("<span class=\"mob\">", "")
                
            while "Физическое лицо" in txt:
                txt = txt.replace("Физическое лицо", "")
                
            while "Конкурсная группа" in txt:
                txt = txt.replace("Конкурсная группа", "")
                
            while "Причина отказа" in txt:
                txt = txt.replace("Причина отказа", "")
                
            while "Состояние" in txt:
                txt = txt.replace("Состояние", "")
                
            while "</span>" in txt:
                txt = txt.replace("</span>", "")
                
            while "<span>" in txt:
                txt = txt.replace("<span>", "")
                
            while "</td>" in txt:
                txt = txt.replace("</td>", "")
                
            while "<td class=\"PROPERTY_KONKURSNAYAGRUPPA_VALUE\">" in txt:
                txt = txt.replace("<td class=\"PROPERTY_KONKURSNAYAGRUPPA_VALUE\">", "")
                
            while "<td class=\"PROPERTY_PRICHINAOTKAZA_VALUE hide\">" in txt:
                txt = txt.replace("<td class=\"PROPERTY_PRICHINAOTKAZA_VALUE hide\">", "")
                
            while "<td class=\"PROPERTY_SOSTOYANIE_VALUE\">" in txt:
                txt = txt.replace("<td class=\"PROPERTY_SOSTOYANIE_VALUE\">", "")
                            
            
            #добавление отредактированной строки   
            trTmp.append(txt)
            #print(str(txt))
        
        #print(str(trTmp))            
        #data ["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]
        #trtmp Физическое лицо    Конкурсная группа    Причина отказа    Состояние
        if(trTmp != data):
            tdTmp = [str(totalPeop), tmpPplCnt, trTmp[0], "Очная", "", str(direction), trTmp[3]]
            totalPeop += 1
            data.append(tdTmp)  
            tmpPplCnt += 1           
            #print(str(tdTmp))   
            
        print(".",end ='') 
    print("\nОбработано, ", end = '') 
    
    print("Людей: "+str(totalPeop-1)+"\n") 
    return data        
