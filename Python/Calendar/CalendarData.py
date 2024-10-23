import calendar
from datetime import date

def SetMonthValues(workSheet, month, year=date.today().year):
  colIni = (month-1)*5+1
  days_month = calendar.monthrange(year, month)[1]
  maxRow = 5 + days_month

  for col in range(colIni,colIni+5):
    for row in range(5, maxRow+1):
      cell = workSheet.cell(row, col)
      if col==colIni+1:
        if row==5:
          cell.value = calendar.month_name[month]
        else:
          day_week = calendar.weekday(year, month, row-5)
          cell.value = calendar.day_name[day_week]
      elif col==colIni+2 and row > 5:
        cell.value = row-5
      elif col==colIni+3 and row == 5:
        cell.value = "HOURS"

  cell=workSheet.cell(maxRow+1,colIni+2,"HOURS")
  cell=workSheet.cell(maxRow+2,colIni+2,"DAYS")
  cell=workSheet.cell(maxRow+4,colIni+2,"SALARY")
  

def SetMonthFunctions(workSheet, month, year=date.today().year):
  col = (month)*5-1
  days_month = calendar.monthrange(year, month)[1]
  maxRow = 5 + days_month

  InitialCell = workSheet.cell(6,col)
  EndCell = workSheet.cell(maxRow,col)

  totalHourCell = workSheet.cell(maxRow+1,col,f"=SUM({InitialCell.coordinate}:{EndCell.coordinate})")
  totalDaysCell=workSheet.cell(maxRow+2,col,f"={totalHourCell.coordinate}/9")

  workSheet.cell(maxRow+4,col,f"={totalDaysCell.coordinate}*108")


def SetWekeendCross(workSheet, month, year=date.today().year):
  days_month = calendar.monthrange(year, month)[1]
  maxRow = 5 + days_month
  dayWeekCol=(month)*5-3
  dataCol = (month)*5-1
  iniRow=6

  for row in range(iniRow, maxRow):
    currentCell = workSheet.cell(row,dayWeekCol)
    if(currentCell.value=="Saturday"):
      workSheet.cell(row, dataCol,"X")
      workSheet.cell(row+1, dataCol,"X")
      

def SetYearValues(workSheet):
  for month in range(1,13):
    #Set Values
    SetMonthValues(workSheet, month)
    #Set Functions
    SetMonthFunctions(workSheet, month)
    SetWekeendCross(workSheet, month)

