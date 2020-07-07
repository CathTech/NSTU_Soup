import csv, datetime, pathlib, bs4, requests, sys
import nsuemCore

data = [["Всего","На направлении","ФИО", "Форма обучения", "Факультет", "Направление", "Документы"]]
name = "usersNSUEM.csv" 
totalPeop = 1 #счетчик людей

#Куски страниц =================================================================
pageStart = "https://onlinebs.nsuem.ru/app?back=352633995838&bc=baf09d3bfeb83a7127a147a809339537&bp=H4gl7cgruBTA8naCzQeCIUdncZ2qU-fpxkcoj"
pageEnd = "&service=bcs"
pageCut = ["PoHmboyHrE4zZ4Z4b99e5ju9XXlgYGh2g2yBWxU",
"PoHmboyHrE4zZ4Z4b7KxjpXWVId232HvoA3zpLU",
"PoHmboyHrE4zZ4Z4b4sRIKcgi37NIrwE_g0xlmE",
"PoHmbowe6XgbKe1lBFAfHSSHa80kcXt8Y9M3-X4",
"PoHmbowe6XgbKe1lBGAxDrdbL8yRIrwE_g0xlmE",
"PoHmbowe6XgbKe1lBB7ODGf4yTjRT3X7pBY9Umw",
"PoHmbowe6XgbKe1lBKuwTSompS3194ouZyxOn6s",
"PoHmbowcHMguiSiXq5xPwDc4i4WQT3X7pBY9Umw",
"PoHmboxgwLIP-aClBbegvzfBoXxNjjzfcx5InLs",
"PoHmbowwTPU1Tu3E7U9BXZDq3_vAIrwE_g0xlmE",
"PoHmboyU4xL7ilHaCBzpMIQhgiAWQaHnvUYGFp4",
"PoHmboyU4xL7ilHaCDwzWJDkoyelfvuppSB9uDs",
"PoHmboyU4xL7ilHaCP-r5e6ZhElyU3lh1_UGzc4",
"PoHmbozb1Sfi9ztAlLaMX06i2B76uTxO_kXwxEM",
"PoHmbozb1Sfi9ztAlOgxBPfwE6dq1dzSAK3ucco",
"PoHmbowALIV7Tuu1uoT7Zk7W0VV91dzSAK3ucco",
"PoHmbowALIV7Tuu1ulP3uuXYpuS-PhqpVSl6U1w",
"PoHmbowY9tsH1nOrNlcO_uYK1DFIuTxO_kXwxEM",
"PoHmbow7HoC8hSYD94OIng6JMzbUsFc0HvSTJf8",
"PoHmbow7HoC8hSYD99HesZe0i61QytcUOqLj0eo",
"PoHmbow7HoC8hSYD9-B3LLri-ApGcXt8Y9M3-X4",
"PoHmbozd0x8X8iln4j12z9prh0GjsFc0HvSTJf8",
"PoHmbowKFjaTZWbzSIgGa7Q8ZOeUPhqpVSl6U1w",
"PoHmbowKFjaTZWbzSE9Mf4w4_YKU4OKiQwH4EvY",
"PoHmbowKFjaTZWbzSPPVXZZ_ZjRCHNEAtXzpx1c",
"PoHmboxqEj1PNnKrZSgagc4znCYcIbIAsXldbLg",
"PoHmbozS6Q34XzCH3UHwlekew7aLYGh2g2yBWxU",
"PoHmbozS6Q34XzCH3UDXH-lOnB5G32HvoA3zpLU",
"PoHmboy39AAFDfwsrXanIHJwLMhoEplN_cRt9pI",
"PoHmboy39AAFDfwsrQCfhYGWXJJGIbIAsXldbLg",
"PoHmboy39AAFDfwsra01TcgMLwciJgeG5uxawhQ",
"PoHmbowSTBi90GPs9m4Hdho1sxKbT3X7pBY9Umw",
"PoHmbowSTBi90GPs9jqph-OI9zBD94ouZyxOn6s",
"PoHmbowSTBi90GPs9t2eyxDf79gkjjzfcx5InLs",
"PoHmboxI65CCeqBqtvefOw7Ga2l1jjzfcx5InLs",
"PoHmboxI65CCeqBqtklLvhAF2b5EQQ7CimRn8OM",
"PoHmbozv_ozrry49eIo0xoXd13XlPhqpVSl6U1w",
"PoHmbowGmZ4wVHeob4UpbYPqYYzSjjzfcx5InLs",
"PoHmbowGmZ4wVHeob2bceseLpxlFQQ7CimRn8OM",
"PoHmbowGmZ4wVHeobxjznBDIAn95g-xc536fBnM",
"PoHmboyhRvjqq_0Y0gP0UgFe0z-N1dzSAK3ucco",
"PoHmboyhRvjqq_0Y0lRf_8LRLUZ2QaHnvUYGFp4",
"PoHmboyhRvjqq_0Y0gN8iEKSMLG_fvuppSB9uDs",
"PoHmbox_gyM1b13e1ZJpnkRqiToLIbIAsXldbLg",
"PoHmbox_gyM1b13e1dMfW9OZgmGPjjzfcx5InLs",
"PoHmbox_gyM1b13e1TUdWX1d6YnpJgeG5uxawhQ",
"PoHmbox_gyM1b13e1Sdfnxyfup4X16dno-FSq4I",
"PoHmboxTMFCLZLy87gAIonh6RIjvg-xc536fBnM",
"PoHmboxTMFCLZLy87sCyTIGrgdcLS4DmZ5SSrdY",
"PoHmboxTMFCLZLy87uLnjhEXsfczQaHnvUYGFp4",
"PoHmboz-sXmD7k6L-zDtYXooYzzQsFc0HvSTJf8",
"PoHmboz-sXmD7k6L--4XbWPK5qdMytcUOqLj0eo",
"PoHmboz-sXmD7k6L-4ibAd98oF6YcXt8Y9M3-X4"]
#===============================================================================

#Запуск
now = datetime.datetime.now()
print( "####################################\n    [" + now.strftime(" %d-%m-%Y | %H:%M:%S") + "] \n " + "========== CI.Soup NSUEM v0.1  ==========" + "\n")
#===============================================================================
pc = 1 #счетчик сайтов
#Работа с веб ==================================================================
for pagePart in pageCut:
    print("#######Получение страницы "+ str(pc))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116'}
    response = requests.get(str(pageStart+pagePart+pageEnd), headers=headers)
    print("Ок")
    
    #Обработка сайта
    for item in nsuemCore.work(response, totalPeop):
        data.append(item)
    pc += 1
    totalPeop += int(data[data.__len__()-1][1])
#===============================================================================

#генерация CSV
print("Сохранение CSV ")
with open(name, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";") 
        writer.writerows(data)

print("Выполнено.\nCI.Soup NSUEM v0.2\nCathx.tech")






