import calendar

#! example file working with calendars, import calendar module above. ^^^

#! plain text calendar
c=calendar.TextCalendar(calendar.MONDAY)
# st=c.formatmonth(2021, 11, 22,0)
# print(st)

#! html formatted calendar
# hc=calendar.HTMLCalendar(calendar.SUNDAY)
# hst=hc.formatmonth(2021, 11)
# print(hst)

#! loop over the days of the month
#! zeros mean that the day of the week is an overlapping month 

# for i in c.itermonthdates(2021, 11):
#     print(i)
# for name in calendar.month_name:
#     print(name)
# for day in calendar.day_name:
#     print(day)

#! when the first friday of each month

print("team meeting will be on:")
for m in range(1,13):
    cal=calendar.monthcalendar(2021, m)
    weekone=cal[0]
    weektwo=cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday=weekone[calendar.FRIDAY]
    else:
        meetday= weektwo[calendar.FRIDAY]

    print("%10s %2d" %(calendar.month_name[m], meetday))