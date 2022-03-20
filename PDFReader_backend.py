
import tabula as tb
import pandas as pd
import random
import tkinter.filedialog
from FrontENd import win


f = tkinter.filedialog.askopenfilename()

#provide inputs
top = 1.99
left = 0.67
bottom = 11.43
right = 7.92

pgs = 'all'
#to be used later in read_pdf
def ConvertToPdfunits(i,j,k,l):
    n = 0#
    lst = [i,j,k,l] #provide inches for x,y,z. Remember coordinates measured from top left.
    for x in lst:
        lst[n] = x*72
        n += 1
    return lst

#note 1/ 72 pdf unit = 1 inch

a = ConvertToPdfunits(top,left,bottom,right)

#file path seems to not work with Turkish filenames???

ReadPDF = tb.read_pdf(f, pages = pgs,area = a, stream = True) #collection of dataframes

pgs = pd.concat(ReadPDF, axis = 0)


def OutPut(inp):
    Extension = '.xlsx' #for applying DRY

    try:
        fName = inp
        final = fName + Extension

        return pgs.to_excel(final) 
    except:
        fName = inp + str(random.randint(0,9))
        final = fName + Extension

        return pgs.to_excel(final)

Res = OutPut('test')

win.destroy()



