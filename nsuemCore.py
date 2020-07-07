import bs4

def work(response, totalPeop):
    data = []
    #Начало обработки файла ========================================================
    soup = bs4.BeautifulSoup(str(response.text), 'lxml')
    response = 0
    print("Людей: "+str(totalPeop)+" | Получен файл") 
    #импорт таблицы
    #заголовочная таблица
    tableHead = bs4.BeautifulSoup(str(soup.find("div", {"class": "widget-content"})), 'lxml')
    tableHead = bs4.BeautifulSoup(str(tableHead.find("table")), 'lxml')
    
    tableInfoTr = tableHead.findAll("tr") 
    facTmp =[]  
    #print("1")
    #обработка таблицы заголовка ==================================================
    for tr in tableInfoTr: 
        td = tr.findAll("td")
        trTmp =[]
        for tmp in td:
            txt = str(tmp)
            #Очистка
            while "  " in txt:
                txt = txt.replace("  ", "")
                
            while "\n" in txt:
                txt = txt.replace("\n", "")
                            
            while "<td style=\"vertical-align: top;\" width=\"40%\">" in txt:
                txt = txt.replace("<td style=\"vertical-align: top;\" width=\"40%\">", "")
                            
            while "<td colspan=\"3\">" in txt:
                txt = txt.replace("<td colspan=\"3\">", "")
                
            while "<td style=\"vertical-align: top;\">" in txt:
                txt = txt.replace("<td style=\"vertical-align: top;\">", "")
                
            while "\xa0" in txt:
                txt = txt.replace("\xa0", "")
                
            while "Название конкурса: " in txt:
                txt = txt.replace("Название конкурса: ", "")
                
            while "квота лиц с особыми правами " in txt:
                txt = txt.replace("квота лиц с особыми правами ", "Бюджет")
                
            while "целевой прием " in txt:
                txt = txt.replace("целевой прием ", "Бюджет")
                
            while "общий конкурс " in txt:
                txt = txt.replace("общий конкурс ", "Бюджет")
                
            while "общий конкурс " in txt:
                txt = txt.replace("общий конкурс ", "Контракт")                
                
            while "(за счет ассигнований федерального бюджета)" in txt:
                txt = txt.replace("(за счет ассигнований федерального бюджета)", "")
                
            while "Вид приема:" in txt:
                txt = txt.replace("Вид приема:", "")
                
            while "</td>" in txt:
                txt = txt.replace("</td>", "")
                
            while "<td>" in txt:
                txt = txt.replace("<td>", "")
                
            while "<nobr>" in txt:
                txt = txt.replace("<nobr>", "")
                
            while "</nobr>" in txt:
                txt = txt.replace("</nobr>", "")
            #добавление отредактированной строки   
            if(txt != ""):
                trTmp.append(txt)
    
        #print(str(trTmp))
        #print(str(trTmp))
        facTmp.append(trTmp)
        #изъятие данных
        
    #print("1")
    stForm = facTmp[6][0]
    faculty = facTmp[2][0]
    direction = facTmp[4][0]
    print("\nПолучены данные форм обучения") 
    #===============================================================================
    
    #информационная таблица
    table = bs4.BeautifulSoup(str(soup.find("table", {"class": "container-table"})), 'lxml')  
    soup = 0
    
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
                            
            while "<td class=\"header-table\" style=\"width: 1px;\">" in txt:
                txt = txt.replace("<td class=\"header-table\" style=\"width: 1px;\">", "")
                
            while "<td class=\"header-table\">" in txt:
                txt = txt.replace("<td class=\"header-table\">", "")
                
            while "</td>" in txt:
                txt = txt.replace("</td>", "")
                
            while "<td>" in txt:
                txt = txt.replace("<td>", "")
                
            while "<nobr>" in txt:
                txt = txt.replace("<nobr>", "")
                
            while "</nobr>" in txt:
                txt = txt.replace("</nobr>", "")
            #добавление отредактированной строки   
            trTmp.append(txt)
            
            
        #data ["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]
        #trtmp ['№', 'Фамилия, имя, отчество', 'Конкурсные баллы', 'Баллы за ВИ', 'Баллы за ИД', 'Детализация баллов ВИ', 'Детализация баллов ИД', 'Документы', 'Согласие на зачисление', 'Состояние']
        if(trTmp[0] !="№"):
            tdTmp = [str(totalPeop), trTmp[0], trTmp[1], str(stForm), str(faculty), str(direction), trTmp[7]]
            totalPeop += 1
            data.append(tdTmp) 
        
        print(".",end ='') 
    print("\nПолучены данные студентов") 
    
    print("Людей: "+str(totalPeop-1)+"\n") 
    return data        
