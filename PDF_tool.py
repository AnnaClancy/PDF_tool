import Tkinter
from Tkinter import Frame
from Tkinter import LEFT, BOTTOM
from PyPDF2 import PdfFileReader, PdfFileWriter 

def creLabel(wd, txt):
	label = Tkinter.Label(wd, text=txt, bg='grey', font=('Arial', 14), width=16, height=1)
	label.pack(side=LEFT)

def creLabel2(wd, txt):
	label = Tkinter.Label(wd, text=txt, bg='grey', font=('Arial', 14), width=10, height=1)
	label.pack(anchor="w")

def creButton(wd, fuc, wb):
	b = Tkinter.Button(wd, text=wb, width=15, height=1, command=fuc)
	b.pack(padx=10, pady=10)

def creEntry(wd):
	pos = Tkinter.Entry(wd, show=None, font=('Arial', 14))
	pos.pack()
	return pos

# 生成一组 Label&Entry
def positionGet(wd, txt):
	posframe = Frame(wd)
	creLabel(posframe, txt)
	single = creEntry(posframe)
	posframe.pack(padx=5, pady=5)
	return single

# 生成两组 Label&Entry
def papeGet(wd, spt, ept):
	posframe = Frame(wd)
	creLabel2(posframe, spt)
	sta = creEntry(posframe)
	creLabel2(posframe, ept)
	end = creEntry(posframe)
	posframe.pack()
	return sta, end
	
# ---------------------------------------

def printData():
	print(pos.get())

def split_pdf():
	print("enter split_pdf")
	if(pos.get()==''):	# 默认在桌面
		path = 'C:\\Users\\Administrator\\Desktop\\' + org.get() + '.pdf'
	else:
		path = pos.get() + '\\' + org.get() + ".pdf"
	pdf_input = PdfFileReader(open(path, 'rb')) 
	pdf_output = PdfFileWriter()

	page_count = pdf_input.getNumPages()

	# 默认从第1页到指定页数剪切
	# if(int(end.get())==0):
	#	for i in range(int(sta.get())-1, page_count):
	#		pdf_output.addPage(pdf_input.getPage(i)) 
	# else:

	for i in range(int(sta.get())-1, int(end.get())):
		pdf_output.addPage(pdf_input.getPage(i)) 
	
	pdf_output.write(open('outfn.pdf', 'wb'))

def merge_pdf():
        print("enter merge_pdf")
        if(pos.get()==''):	# 默认在桌面
		path1 = 'C:\\Users\\Administrator\\Desktop\\' + org.get() + '.pdf'
		path2 = 'C:\\Users\\Administrator\\Desktop\\' + org2.get() + '.pdf'
	else:
		path1 = pos.get() + '\\' + org.get() + ".pdf"
		path2 = pos.get() + '\\' + org2.get() + ".pdf"

        pdf_output = PdfFileWriter()
        
        pdf_input = PdfFileReader(open(path1, 'rb'))
        page_count = pdf_input.getNumPages()
        for i in range(0, page_count):
		pdf_output.addPage(pdf_input.getPage(i)) 

        pdf_input = PdfFileReader(open(path2, 'rb'))
        page_count = pdf_input.getNumPages()
        for i in range(0, page_count):
		pdf_output.addPage(pdf_input.getPage(i))

	pdf_output.write(open('outfn.pdf', 'wb')) 

def initial(wd):
	wd.title("pdf cutting tool by Anna")
	wd.geometry('500x330')
	pos = positionGet(wd, "源文件位置:")
	org = positionGet(wd, "源文件名称:")
	org2 = positionGet(wd, "源文件2名称:")
	sta, end = papeGet(wd, "起始页码:", "结束页码:")
	return pos, org, org2, sta, end

if __name__ == '__main__':
	window = Tkinter.Tk()
	pos, org, org2, sta, end = initial(window)
	creButton(window, split_pdf, "剪切")
	creButton(window, merge_pdf, "合并")
	window.mainloop()
	input()
