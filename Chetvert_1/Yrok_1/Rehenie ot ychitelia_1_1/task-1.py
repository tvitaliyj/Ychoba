##Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах. Формат вывода результата:
##- до минуты: <s> сек;
##- до часа: <m> мин <s> сек;
##- до суток: <h> час <m> мин <s> сек;
##- в остальных случаях: <d> дн <h> час <m> мин <s> сек.
##**Примеры:**
##duration = 53
##53 сек
##duration = 153
##2 мин 33 сек
##duration = 4153
##1 час 9 мин 13 сек
##duration = 400153
##4 дн 15 час 9 мин 13 сек



time = 4153
if 0 <= time < 60:
    print(time, "сек")
elif 60 <= time < 3600:
    minutes = time//60
    seconds = time%60
    print(minutes,"мин", seconds, "сек" )
elif 3600 <= time < 24*3600:
    hours = time//3600
    time_remain = time-hours*3600
    # minutes = time%60//60 - вместо time_remain
    minutes = time_remain//60
    seconds = time_remain%60
    print(hours,"час", minutes, "мин", seconds, "сек" )
else:
    days = time//(24*3600)
    time_remain = time-days*24*3600
    hours = time_remain//3600
    time_remain = time_remain-hours*3600
    minutes = time_remain//60
    seconds = time_remain%60
    print(days, "дн", hours,"час", minutes, "мин", seconds, "сек" )