import bs4
from multiprocessing import sys

def work(response, totalPeop):
    data = []
    nll = []
    tmpPplCnt = 1
    #Начало обработки файла ========================================================
    #print(str(response.text))
    soup = bs4.BeautifulSoup(str(response.text), 'lxml') 
    
    response = 0
    #print(str(soup.prettify()))
    #sys.exit() 
    
    divMain = bs4.BeautifulSoup(str(bs4.BeautifulSoup(str(soup.find("div", {"class": "__asu__"})), 'lxml')), 'lxml')
    divFac = bs4.BeautifulSoup(str(bs4.BeautifulSoup(str(soup.find("div", {"class": "box4 t_gray"})), 'lxml')), 'lxml')
    
    #print(str(divFac.text))
    #sys.exit()
    
    #tmpMrk = 0
    tNull = []
    #print ( str(divMain.prettify()))
    #sys.exit()
    #===============================================================================
    
    #print(str(divs.prettify()))
    
    #информационная таблица
    table = divMain.findAll("table") 
    soup = 0
    #print("#########################")
    #print(str(table[0]))
    #print("#########################")
    #print(str(table[1]))
    #print("#########################")
    #print(str(table[2]))
    #print("#########################")
    #sys.exit()
    
    
    stInfo = ["1"]
    
    tmpTxt = str(divFac.text)
    #Очистка
    while "  " in tmpTxt:
        tmpTxt = tmpTxt.replace("  ", "")
    while "\n\n" in tmpTxt:
        tmpTxt = tmpTxt.replace("\n\n", "")
    while ":\n" in tmpTxt:
        tmpTxt = tmpTxt.replace(":\n", ":")
        
    tmp2 = tmpTxt.split('\n')
    for txt in tmp2:
        txt = txt[txt.find(":") + 1 : ]     
        stInfo.append(txt)
        
    #print(str(stInfo))
    #sys.exit()    
        
    #print(str(headTableTr[0].text))
    if (stInfo[4] != 'Бакалавр'):
        data.append([str(totalPeop), 0, "", "", "", "", ""])
        print("Всего: " + str(totalPeop)+" | Не бакалавр")
        tmpPplCnt = 0
        return data  
        
    #print("33>"+str(stInfo)) 
    #sys.exit()
    try:
        tableTr = bs4.BeautifulSoup(str(table[2]), 'lxml').findAll("tr") 
    except IndexError:  
        tableTr = bs4.BeautifulSoup(str(table[1]), 'lxml').findAll("tr") 
    #print(str(tableTr[1]))
    #sys.exit()
    
    
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
                
            while "</div>" in txt:
                txt = txt.replace("</div>", "")  
                
            txt = txt[txt.find(">") + 1 : ]
                
            while "</div>" in txt:
                txt = txt.replace("</div>", "")      
            
            #добавление отредактированной строки   
            if(txt != nll): 
                trTmp.append(txt)
                #print(str(txt))
        
        #print("3>"+str(trTmp)) 
        #sys.exit()           
        #data ["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]
        #trtmp n фио балл доки рекоменд согл зачислен
        
                
            
        if(trTmp != tNull):
            #print("3>"+str(trTmp)) 
            #print("4>"+str(tmpStr)) 
            tdTmp = [str(totalPeop), trTmp[0], trTmp[1], stInfo[6], stInfo[2] , stInfo[3], trTmp[3]]
            totalPeop += 1
            data.append(tdTmp)  
            tmpPplCnt += 1           
            #print("2>"+str(tdTmp)) 
             
        #print(".",end ='') 
        
    if(tmpPplCnt-1 == 0): 
        data.append([str(totalPeop), 0, "", stInfo[5], stInfo[2] , stInfo[3], ""])
        print("Всего: " + str(totalPeop)+" | Нет людей")
    else:
        print("Всего: " + str(totalPeop - tmpPplCnt +1)+" | Новых: "+str(tmpPplCnt-1))   
    
    return data        
