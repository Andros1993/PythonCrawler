import xlwt;
import xlrd;
#import xlutils;
from xlutils.copy import copy;

# this is create new file
# styleBoldRed = xlwt.easyxf('font: color-index red, bold on');
# headerStyle = styleBoldRed;
# wb = xlwt.Workbook();
# ws = wb.add_sheet('sheetName');
# ws.write(0, 0, "Header", headerStyle);
# ws.write(0, 1, "CatalogNumber", headerStyle);
# ws.write(0, 2, "PartNumber", headerStyle);
# wb.save('fileName.xls');

# open existed xls file
# newWb = xlutils.copy(gConst['xls']['fileName']);
# newWb = copy(gConst['xls']['fileName']);
oldWb = xlrd.open_workbook('fileName.xls', formatting_info=True);
print
oldWb;  # <xlrd.book.Book object at 0x000000000315C940>
newWb = copy(oldWb);
print
newWb;  # <xlwt.Workbook.Workbook object at 0x000000000315F470>
newWs = newWb.get_sheet(0);
newWs.write(2, 0, "value1");
newWs.write(2, 1, "value2");
newWs.write(2, 2, "value3");
print
"write new values ok";
newWb.save('fileName.xls');
print
"save with same name ok";