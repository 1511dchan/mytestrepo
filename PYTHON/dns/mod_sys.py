# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- # Функция заменяет в файле содержимое строки. Точнее удаляет всю строку с номером и вставляет новую строку в это же место
# Пример: LineReplace("/var/cache/bind/dnssec/cs.cln.su/cln.su", zone_namber, 3)
# Где:
# file_name - путь к файлу в котором надо заменить строку
# line_text - сама строка на которую надо заменить
# line_namber - номер строки в файле строки номеруются c 0
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def LineReplace(file_name, line_text, line_namber):
    
    f = open (file_name, "r")        # Открываем файл на чтение
    lines = f.readlines()            # Читаем весь файл построчно и записываем в переменную ввиде кортежа
    f.close()                        # Закрываем файл
    lines[line_namber] = line_text   # Изменяем значение строки с указанным номером. В картеже нумерация с ноля
    f = open (file_name,"w")         # Открываем файл на запись
    f.writelines(lines)              # Записываем в файл построчно весь кортеж из переменной
    f.close()                        # Закрываем файл

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Функция подписывает зону
# Пример: DnsSec("sc.cln.su")
# Где: 
# dns_zone_name - имя подписываемой зоны
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def DnsSec(dns_zone_name):
    from subprocess import Popen, PIPE
    import os, glob, linecache, re, time

    dns_root_dir = "/var/cache/bind/dnssec/" # Папка где хронятся все подписываемые зоны
    dns_root_zone = "cln.su"                 # Папка корневой зоны, в ней будем искать файл корневой зоны куда и  будем скаладывать ключи подписанной дочерней зоны
    os.chdir(dns_root_dir+dns_zone_name)     # Меняем текущую дирректорию на дирректорию с редактируемой зоной

#    for filename in glob.glob("K"+dns_zone_name+"*"): # Ищем наличие старых ключей два файла, поэтому пользуемся поиском
#        if os.path.exists(filename):                  # Если существуют, то
#            os.remove(filename)                       # Удаляем их

#    if os.path.exists("dsset-"+dns_zone_name+"."): # Ищем наличие старого файла с записями DNSSEC
#        os.remove("dsset-"+dns_zone_name+".")      # Если существует, то удаляем его

#    if os.path.exists(dns_zone_name+".signed"): # Проверяем наличие файла подписанной зоны
#        os.remove(dns_zone_name+".signed")      # Если существует, то удаляем его

#    Popen("dnssec-keygen -a RSASHA1 -b 1024 -n ZONE "+dns_zone_name, shell=True).wait()        # Генерируем публичный ключ и ждем завершения генерации
#    Popen("dnssec-keygen -a RSASHA1 -b 2048 -f KSK -n ZONE "+dns_zone_name, shell=True).wait() # Генерируем секретный ключ зоны и тоже ждем
#    Popen("dnssec-signzone -S -N INCREMENT "+dns_zone_name, shell=True).wait()                 # Подписываем зону, создается файл с DNSSEC записями

    if os.path.exists(dns_root_dir+dns_zone_name+"/dsset-"+dns_zone_name+"."):                                       # Проверяем наличие файла с DNSSEC записями
#        f=open (dns_root_dir+"cs.cln.su/"+dns_root_zone,"a")                                                         # Если он существует, то открываем его на дозапись
#        f.write("\n")                                                                                                # И добавляем пустую строку что бы отделить эстетически записи
#        i = 1                                                                                                        # Устанавливаем номер строки c которой начнем чтение файла построчно 
#        while i < 3:                                                                                                 # Добавляем вконец файлае ключи зоны. Для этого запускаем цикл читающий файл с ключами построчно. Делим каждую строку
#            f.write(                                                                                                 # на две части разделителем "DS" и вытаскиваем вторую часть в ней хранится сам ключ, после чего собираем всю строку.
#            (dns_zone_name).ljust(24, " ") +                                                                         # расставляя правильное количество пробелов между элементами, для этетической красоты отступов в строке файла.
#            ("IN").ljust(8, " ") + ("DS").ljust(8, " ") +                                                            # Функция ljust добавляет пробелы справа от символов до нужного количества символов в строке - второй параметр.
#            linecache.getline(dns_root_dir+dns_zone_name+"/dsset-"+dns_zone_name+".",i).partition("DS")[2].lstrip()) # Функция lstrip удаляет все пробелы вначале строки
#            i = i + 1                                                                                                # Увеличиваем номер строки и переходим в начала цикла
#        f.close()                                                                                                    # Закрываем файл
        
        f = open (dns_root_dir+"cs.cln.su/"+dns_root_zone,"r")                         # Если он существует, то открываем его на дозапись
        lines = f.readlines()
        f.close()
        for line in lines:
            if "IN      NS" in line:
                i = lines.index(line)
        j = 0
        while j < 5:
            lines.insert(i+1+j, ("cs").ljust(24, " ")+("IN").ljust(8, " ")+("NS").ljust(8, " ")+"ns"+str(j)+"."+dns_root_zone+".\n")
            j = j + 1

        f = open (dns_root_dir+dns_zone_name+"/dsset-"+dns_zone_name+".","r")
        keys = f.readlines()
        f.close()
        for key in keys:
            lines.append((dns_zone_name+".").ljust(24, " ")+("IN").ljust(8, " ")+("DS").ljust(8, " ")+key.partition("DS")[2].lstrip())
        f.close()

        f = open (dns_root_dir+"cs.cln.su/"+dns_root_zone,"w")
        f.writelines(lines)
        f.close()


        zone_namber = int(linecache.getline(dns_root_dir+"cs.cln.su/"+dns_root_zone,3)[-3:-1],10)+1 # Считываем строку с номером зоны и выделяем две последних цифры, увеличиваем на единицу. 
                                                                                                    # В номере сначала идет дата а потом две цифры серии их будем увеличивать
        if zone_namber < 10:                                                                 # Если номер меньше 10, то есть односимвольный, то
            zone_namber = (time.strftime('%Y%m%d')+"0"+str(zone_namber)).rjust(42, " ")+"\n" # Добывляем к номеру один ноль вначале, далее перед номером добавляем дату, а перед датой добиваем пустое место пробелами до 42 символов
        elif zone_namber > 99:                                                               # Если номер больше 99, то обнуляем его
            zone_namber = (time.strftime('%Y%m%d')+"00").rjust(42, " ")+"\n"                 # И добавляем вместо номера просто два ноля
        else:                                                                                # Во всех остальных случаях
            zone_namber = (time.strftime('%Y%m%d')+str(zone_namber)).rjust(42, " ")+"\n"     # Просто добавляем к дате серию зоны из двух символов и добиваем в начало строки пробелы

        f = open (dns_root_dir+"cs.cln.su/"+dns_root_zone,"r")  # Открываем файл на чтение
        lines = f.readlines()                                   # Считываем все строки файла в список
        f.close()                                               # Закрываем файл
        lines.pop(2)                                            # Удаляем третью строку с номером зоны
        lines.insert(2, zone_namber)                            # Вставляем новый серийный номер в третью стоку
        f = open (dns_root_dir+"cs.cln.su/"+dns_root_zone,"w")  # Открываем файл на запись
        f.writelines(lines)                                     # Записываем в него список строк
        f.close()                                               # Закрываем файл
#        LineReplace(dns_root_dir+"cs.cln.su/"+dns_root_zone, zone_namber, 2) # Вызываем функцию замены строки в файле, что бы поменять в зоне порядковый номер зоны.

        Popen("service bind9 restart", shell=True)                           # Перезапускаем DNS сервер что бы зона перечиталась

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def DnsSecTest(dns_zone_name):
    from subprocess import Popen, PIPE
    import os, glob, linecache, re, time

    dns_root_dir = "/var/cache/bind/dnssec/" # Папка где хронятся все подписываемые зоны
    dns_root_zone = "cln.su"                 # Папка корневой зоны, в ней будем искать файл корневой зоны куда и  будем скаладывать ключи подписанной дочерней зоны
    os.chdir(dns_root_dir+dns_zone_name)     # Меняем текущую дирректорию на дирректорию с редактируемой зоной

    f = open (dns_root_dir+"cs.cln.su/"+dns_root_zone,"r")                         # Если он существует, то открываем его на дозапись

    lines = f.readlines()
    f.close()
    for line in lines:
        if "IN      NS" in line:
            i = lines.index(line)
    j = 0
    while j < 5:
        lines.insert(i+1+j, ("cs").ljust(24, " ")+("IN").ljust(8, " ")+("NS").ljust(8, " ")+"ns"+str(j)+"."+dns_root_zone+"\n")
        j = j + 1
    f = open (dns_root_dir+"cs.cln.su/"+dns_root_zone,"w")
    f.writelines(lines)
    f.close()


    f = open (dns_root_dir+dns_zone_name+"/dsset-"+dns_zone_name+".","r")
    keys = f.readlines()
    f.close()

    f = open (dns_root_dir+"cs.cln.su/"+dns_root_zone,"r")
    lines = f.readlines()
    lines.append("\n")
    for key in keys:
        lines.append((dns_zone_name).ljust(24, " ")+("IN").ljust(8, " ")+("DS").ljust(8, " ")+key.partition("DS")[2].lstrip())
    f.close()
    f = open (dns_root_dir+"cs.cln.su/"+dns_root_zone,"w")
    f.writelines(lines)
    f.close()

#    print(str(i))
#    print(str(lines[i]))
#    dns_record = ("cs").ljust(24, " ") + ("IN").ljust(8, " ") + ("DS").ljust(8, " ") + "ns" + "0." + dns_root_zone + "\n" 
#lines[i]+"\n"+"test"
#    print(dns_record)
    
#    f = open (dns_root_dir+"cs.cln.su/"+dns_root_zone,"w")
#    LineReplace(dns_root_dir+"cs.cln.su/"+dns_root_zone, str(lines[i]+"\n"), i)
#    j = 0
#    while j < 5:
#        LineReplace(dns_root_dir+"cs.cln.su/"+dns_root_zone, "\n"+("cs").ljust(24, " ")+("IN").ljust(8, " ")+("NS").ljust(8, " ")+"ns"+str(j)+"."+dns_root_zone+"\n", i+j+1)
#        j = j + 1
#    LineReplace(dns_root_dir+"cs.cln.su/"+dns_root_zone, dns_record, 69)
#    f.close()
#T.index(2, 2)
#.count("A")
#    f.close()
