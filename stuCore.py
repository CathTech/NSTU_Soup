import bs4
from multiprocessing import sys

def work(response, totalPeop, stForm):
    data = []
    nll = []
    tmpPplCnt = 1
    #Начало обработки файла ========================================================
    #print(str(response.text))
    soup = bs4.BeautifulSoup(str(response.text), 'lxml') 
    
    response = 0
    print("Людей: "+str(totalPeop)+ " | Обработка")
    #print(str(soup.prettify()))
    #sys.exit() 
    
    divMain = bs4.BeautifulSoup(str(bs4.BeautifulSoup(str(soup.find("div", {"id": "page_text"})), 'lxml')), 'lxml')
    #импорт заголовка
    h3s = bs4.BeautifulSoup(str(divMain.findAll("h3")), 'lxml')
    #вытаскивание текста
    tmpStr = []
    tNull = []
    #print (str(divMain.prettify()))
    for h3 in h3s:
        txt = h3.text
        #чистка
        while "," in txt:
            txt = txt.replace(",", "\n")
            
        while "]" in txt:
            txt = txt.replace("]", "")
            
        tmpStr.append(txt.split("\n"))
        #print ("5>"+str(h3.text))
        
    #print ("1>"+str(tmpStr))
    
    #sys.exit()
    #===============================================================================
    
    #print(str(divs.prettify()))
    
    #информационная таблица
    table = bs4.BeautifulSoup(str(soup.find("table")), 'lxml')  
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
                
            while "]" in txt:
                txt = txt.replace("]", "")  
                
            while "</label>" in txt:
                txt = txt.replace("</label>", "")    
                
            while "коп." in txt:
                txt = txt.replace("коп.", "Копия")  
                
            while "ориг." in txt:
                txt = txt.replace("ориг.", "Оригинал")                
               
            while txt.find("\">") != -1:
                txt = txt[txt.find("\">")+2:]            
            
            #добавление отредактированной строки   
            if(txt != nll): 
                trTmp.append(txt)
                #print(str(txt))
        
        #print("3>"+str(trTmp)) 
        #sys.exit()           
        #data ["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]
        #trtmp №    ФИО    Тип документа    Категория приёма    Форма обучения    Направление    Программа
        if(trTmp != tNull):
            #print("3>"+str(trTmp)) 
            #print("4>"+str(tmpStr)) 
            tdTmp = [str(totalPeop), trTmp[0], trTmp[1], str(stForm), "" , tmpStr[0][1], trTmp[7]]
            totalPeop += 1
            data.append(tdTmp)  
            tmpPplCnt += 1           
            #print("2>"+str(tdTmp))   
            
        #print(".",end ='') 
    print("\nОбработано, ", end = '') 
    
    print("Людей: "+str(tmpPplCnt-1)+"\n") 
    return data        
