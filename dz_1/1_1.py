for i in range(4):
    duration = int(input('Введи количество секунд: '))
    time_list = [duration % 60, duration // 60 % 60, duration // 3600 % 24, duration // 86400]
    print(time_list[3], 'дней', time_list[2], 'часов', time_list[1], 'минут', time_list[0], 'секунд')
