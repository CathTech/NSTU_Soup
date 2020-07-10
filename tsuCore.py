import bs4
from multiprocessing import sys

def work(response, totalPeop, faculty):
    data = []
    tmpPplCnt = 1
    #Начало обработки файла ========================================================
    #print(str(response.text))
    soup = bs4.BeautifulSoup(str(response.text), 'lxml')
    
    
    response = 0
    print("Людей: "+str(totalPeop)+ " | Обработка")
    #print(str(soup.text))
    #импорт заголовка 
    
    divMain = bs4.BeautifulSoup(str(soup.find("div", {"class": "content-table"})), 'lxml')
    divs = bs4.BeautifulSoup(str(divMain), 'lxml')
   
           
    for div_part in divs:                      
        if(str(div_part.text).find("По данному запросу ничего не найдено") != -1):
            print("Нет людей \n")
            #data ["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]
            return [[str(totalPeop-1),'0',"", "", str(faculty), "", ""]]
    #===============================================================================
    #print(str(divs.prettify()))
    #информационная таблица
    table = bs4.BeautifulSoup(str(soup.find("table", {"id": "sites"})), 'lxml')  
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
                
            while "</td>" in txt:
                txt = txt.replace("</td>", "")      
                
            while "<td>" in txt:
                txt = txt.replace("<td>", "")    
                
            while "<td>" in txt:
                txt = txt.replace("<td>", "")  
                
            while "</div>" in txt:
                txt = txt.replace("</div>", "")  
                
            while "</label>" in txt:
                txt = txt.replace("</label>", "")                  
               
            while txt.find("\">") != -1:
                txt = txt[txt.find("\">")+2:]            
            
            #добавление отредактированной строки   
            trTmp.append(txt)
            #print(str(txt))
        
        #print(str(trTmp))            
        #data ["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]
        #trtmp №    ФИО    Тип документа    Категория приёма    Форма обучения    Направление    Программа
        if(trTmp != data):
            tdTmp = [str(totalPeop), tmpPplCnt, trTmp[1], trTmp[4], str(faculty), trTmp[5], trTmp[2]]
            totalPeop += 1
            data.append(tdTmp)  
            tmpPplCnt += 1           
            #print(str(tdTmp))   
            
        print(".",end ='') 
    print("\nОбработано, ", end = '') 
    
    print("Людей: "+str(tmpPplCnt-1)+"\n") 
    return data        
