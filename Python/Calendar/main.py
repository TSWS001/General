import CalendarData, CalendarStyle
import calendar
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

#Set Values and functions
CalendarData.SetYearValues(ws)

#Set Styles
CalendarStyle.CellMergeStyle(ws)
CalendarStyle.YearBorderStyle(ws)

wb.save('Calendar.xlsx')