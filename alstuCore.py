import bs4
from multiprocessing import sys

def work(response, totalPeop, way, stF):
    data = []
    nll = []
    tmpPplCnt = 1
    #Начало обработки файла ========================================================
    #print(str(response.text))
    soup = bs4.BeautifulSoup(str(response.text), 'lxml') 
    
    response = 0
    #print(str(soup.prettify()))
    #sys.exit() 
    
    tableMain = bs4.BeautifulSoup(str(soup.find("table", {"id": "table_js"})), 'lxml')
    tableBody = bs4.BeautifulSoup(str(tableMain.find("tbody")), 'lxml')
    #print(tableMain.prettify())
    #sys.exit() 
    #===============================================================================
     
    tableTr = tableBody.findAll("tr")
    #print (tableTr.prettify())
    #sys.exit()
    
    for tr in tableTr: 
        #print(str(tr.prettify()))
        #sys.exit()
        
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
                
            while "</a>" in txt:
                txt = txt.replace("</a>", "")      
                                
            while "</div>" in txt:
                txt = txt.replace("</div>", "")
                
            txt = txt[txt.find(">") + 1 : ]      
            txt = txt[txt.find(">") + 1 : ]
            #добавление отредактированной строки   
            if(txt != nll): 
                trTmp.append(txt)
                #print(str(txt))
        
        #print("\n3>"+str(trTmp)) 
        #sys.exit()           
        #data ["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]
        #trtmp n фио id док согл катег балл результ
        
         
        tdTmp = [str(totalPeop+1), trTmp[0], trTmp[1], stF, "" , way, trTmp[3]]
        totalPeop += 1
        data.append(tdTmp)  
        tmpPplCnt += 1  
                 
        #print("2>"+str(tdTmp)) 
        #sys.exit()
             
        #print(".",end ='') 
        
    if(tmpPplCnt-1 == 0): 
        data.append([str(totalPeop), 0, "", stF, "" , way, ""])
        print("Всего: " + str(totalPeop)+" | Нет людей")
    else:
        print("Всего: " + str(totalPeop - tmpPplCnt +1)+" | Новых: "+str(tmpPplCnt-1))   
    
    return data        
