import csv
import pandas as pd
try:
    # for Python2
    from Tkinter import *  
    import Tkinter as tk
    from Tkinter import filedialog, messagebox
except ImportError:
    # for Python3
    from tkinter import *
    import tkinter as tk
    from tkinter import filedialog, messagebox


root= tk.Tk()
# All These are inputs Holders we will be using Later
yearTxtZone = StringVar()
nameOfHeader = StringVar()
monthTxtZone = StringVar()
dayTxtZone = StringVar()
typesTextZone = StringVar()


def readData ():
    global reader, header
    # We read the content of the file 
    try:

        open(import_file_path)
        file = open(import_file_path)
        reader = csv.reader(file)
        header = next(reader)
        return True
    except :
        return False
       # getFilePath ()

def showSumResult (mrSum, MrType):
    # MrType is the the of Date : Day/ year / month 
    messagebox.showinfo('Final Sum', 'The Sum For this {0} is: {1}'.format(MrType, str(mrSum)))

  
def getFilePath ():
    
    global import_file_path
    
    # we will use Panda to convert the file to csv and we will use csv for the rest of the work
    import_file_path = filedialog.askopenfilename()
    if import_file_path:
        try:
            a = readData()
            
            if a:
                tk.messagebox.showinfo('Sucess Importing File','Your File has Been imported\nHere is the Headers of your File\nPlease check the headers at the top menu')
                checkHeaders()
            else:
                tk.messagebox.showinfo("Wrong Extension", "The File You Have Picked Isn\'t CSV!\nPlease Convert it or Choose Another File with CSV Extension!")

        except :
            tk.messagebox.showinfo("Wrong Extension", "The File You Have Picked Isn\'t CSV!\nPlease Convert it or Choose Another File with CSV Extension!")
      

def creatDict(head_er):
    global prefs, counter
    readData ()
    counter = 0

    def creation(head_er):
     # To find the index the user choosed to use 
        hedIndex = header.index(head_er)
        for line in reader:

            Fdate = str(line[0]).split(' ')
            fulldate = Fdate[0].split('/')
        
            day = fulldate[0]
        
            if fulldate[1].startswith('0'):
                month = fulldate[1][1]
            elif not fulldate[1].startswith('0'):
                month = fulldate[1]
            
            year = fulldate[2]
        
            hour = Fdate[1]
    
            head_er = (line[hedIndex])
    
    
        # Here we just set the which means how the Dictionary should Look 
            prefs.setdefault(year, {})
            prefs[year].setdefault(month, {})
            prefs[year][month].setdefault(day, {})
            prefs[year][month][day].setdefault(hour, {})
        # Here we fill it with the data we took from the csv file
            prefs[year][month][day][hour] = head_er
        
        return prefs
    
    
    if counter != 0:
        del prefs
        prefs = {}
        creation(choosedHeader)
    else:
        prefs = {}
        creation(choosedHeader)
        counter += 1
    
    return prefs
    

def showYears ():
    a = yearss.copy()
    
    messagebox.showinfo('Years', *a) 


def chooseTypeOfAnalytics ():
    global yearss , prefss, choosedHeader
    choosedHeader = nameOfHeader.get()
    prefss = creatDict(choosedHeader)
    
    yearss = [i for i in prefss]

    if choosedHeader in header[1:]:

        def chooseWhatTo():
            
            typoSum = typesTextZone.get()
            yero = yearTxtZone.get()
            montho = monthTxtZone.get()
            dayo = dayTxtZone.get()
            # Depends on the User input we will check
            if typoSum == 'Yearly':
                Calc_Yearly_Moyen()
            elif typoSum == 'Monthly':
                Calc_Monthly_Moyen()
            else:
                Calc_Daily_Moyen()

        def revealDays():
            
            
            l =['Yearly', 'Monthly', 'Daily']
            # here we will just try to find the number of days depends on the month and year
            try:
                yero = yearTxtZone.get()
                montho = monthTxtZone.get()
                dayss = [i for i in prefss[str(yero)][montho]]

                dropdays = OptionMenu(root, dayTxtZone, *dayss)
                dropdays.config(pady=10,padx= 6, bg= '#DAF7A6')
                canvas1.create_window(280, 340, window=dropdays)

                dropTypes = OptionMenu(root, typesTextZone,*l)
                canvas1.create_window(370, 340, window=dropTypes)
                dailyButton.destroy()

                ButtonowseButton_Excel = tk.Button(text="Select Type", command=chooseWhatTo, bg='#fff8d6', fg='#7fa471', font=('helvetica', 12, 'bold'))
                canvas1.create_window(500, 340, window=ButtonowseButton_Excel)
                return dayss

            except KeyError:
                messagebox.showerror('ERROR', 'Please Check the Date!')
        
        
        yearTxtZone.set(None)
        monthTxtZone.set(None)
        dayTxtZone.set(None)


        typesLab = tk.Label(root, text='In order to pick a specific day you need to choose months and year first', bg = '#699e9b')
        typesLab.config(font=('helvetica', 10, 'bold'))
        canvas1.create_window(250, 290, window=typesLab)

        dropYears = OptionMenu(root, yearTxtZone, *yearss)
        dropYears.config(pady=10,padx= 6, bg= '#DAF7A6')
        canvas1.create_window(100, 340, window=dropYears)

        Monthi = [i for i in range(1,13)]
        
        dropmonths = OptionMenu(root, monthTxtZone, *Monthi)
        dropmonths.config(pady=10,padx= 6, bg= '#DAF7A6')
        canvas1.create_window(190, 340, window=dropmonths)

        
        dailyButton = tk.Button(text="     Select to reveal days    ", command=revealDays, bg='#fff8d6', fg='#7fa471', font=('helvetica', 12, 'bold'))
        canvas1.create_window(480, 340, window=dailyButton)


def checkHeaders ():
    
    readData()
    # Here it does check if the file has been imported or not
    if readData():
    
        chooseLab = tk.Label(root, text='to do any analytics on your file you need to choose the header to work with', bg = '#699e9b')
        chooseLab.config(font=('helvetica', 10, 'bold'))
        canvas1.create_window(250, 200, window=chooseLab)


        # To get the name of the header to work with('Tempature,humidity...')
        nameOfHeader.set(str(header[1]))
        headerName = OptionMenu(root, nameOfHeader , *header[1:])
        headerName.config(pady=10,padx= 6, bg= '#DAF7A6')
        canvas1.create_window(150, 250, window=headerName)
        
        selectHeadButton = tk.Button(text="      Select This Header     ", command=chooseTypeOfAnalytics, bg='#fff8d6', fg='#7fa471', font=('helvetica', 12, 'bold'))
        canvas1.create_window(300, 250, window=selectHeadButton)

    else : 
        tk.messagebox.askretrycancel('Erro', 'You Did not imported any File yet\nPlease try again!')
        
            

def Calc_Daily_Moyen(years = None, months = None, days = None):
    
    def secondEscapeLoL(years, months, days):
        sumOfDays = 0
        comp = 0
        tempatures =[]
        finalSum = 0
        
        try:
            for i in prefs[years][months][days]:
        
                # Sometime there is an empty spot in the file we catch the error and handle it
                try:
                    tempatures.append(float(prefs[years][months][days][i]))
                except ValueError:
                    pass
            # here we just count how many days in this specific month    
            for i in tempatures:
                sumOfDays += i

            # same catching error!    
            try:
                finalSum = sumOfDays/float(len(tempatures))
                
                return finalSum
    
            except ZeroDivisionError:
                return 0
        except:
            messagebox.showerror('Invalid Date!', 'The Date Year : {0} / Month: {1} / Day: {2}\n -_-'.format(yearso,montho,dayo))
            

    if years and months and days != None:
        DailySumLeL = secondEscapeLoL(years, months, days)
        
        return DailySumLeL
         
        
    else:
        dayo = dayTxtZone.get()

        montho = monthTxtZone.get()
        yearso = yearTxtZone.get()
        DailySumLeL = secondEscapeLoL(yearso, montho, dayo)
        
        showSumResult (DailySumLeL, 'Day')
    
def Calc_Monthly_Moyen(years = None, months = None ):
        montho = monthTxtZone.get()
        yearso = yearTxtZone.get()
        
        monthly_tempatures =[]
        def ecapeErrorCalc(years, months):
            summ = 0
            dayss = 0
            year = str(years)
            month = str(months)
            try:
                for i in prefss[years][months]:
                            # For less coding we just use the Daily function (:
                            daily = Calc_Daily_Moyen(years, months,i)
                            dayss += 1
                            summ += daily
                MonthlySum = summ/float(dayss)
            
                # return is used if you going to use it in another function result
                return MonthlySum
            except KeyError:
                messagebox.showerror('Invalid Date!', 'The Date Year : {0} / Month: {1} \n -_-'.format(yearso,montho))
                      
        if months != None:
            MonthlySumLeL = ecapeErrorCalc(years,months)
            return MonthlySumLeL
        elif montho:
            MonthlySumLeL = ecapeErrorCalc(yearso,montho)
            showSumResult (MonthlySumLeL, 'Month')
                  
        


def Calc_Yearly_Moyen():
    theYear = yearTxtZone.get()
    years = str(theYear)
    summ = 0
    months = 0
    YearlySum = 0
    try:
        for i in prefss[years]:
            # Same here we use the same function :D
            monthly = Calc_Monthly_Moyen(years, i)
            months += 1
            summ += monthly
        
        YearlySum = summ/float(months)
        
        showSumResult (YearlySum, 'Year')
    except KeyError:

        messagebox.showerror('Invalid Date!', 'The Date Year : {0} \n -_-'.format(yearso))
        
# This Part is for Converting the Files
def fileConverter():
    Convo= tk.Tk()

    def destroy():
        Convo.destroy()
    def getExcel ():
        global read_file
        try:
            import_file_path = filedialog.askopenfilename()
            messagebox.showinfo('Converter Info', 'Your File has been imported Succefully')
            read_file = pd.read_excel (import_file_path)
            
            
        except FileNotFoundError:
            messagebox.showerror('ERROR', 'File Not Found')
    def convertToCSV ():
        global read_file
        export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        read_file.to_csv (export_file_path, index = None, header=True)
        messagebox.showinfo('Converter Info', 'Your File hve been Converted and saved Succefully')
    def exitApplication():
        MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
        if MsgBox == 'yes':
            Convo.destroy()
    Canvo1 = tk.Canvas(Convo, width = 550, height = 350, bg = '#699e9b', relief = 'raised')
    Canvo1.pack()

    label1 = tk.Label(Convo, text='You have to Convert your Files to CSV!', bg = '#699e9b')
    label1.config(font=('helvetica', 14))
    Canvo1.create_window(260, 75, window=label1)


    
    browseButton_Excel = tk.Button(Convo,text="      Import csv File     ", command=getExcel, bg='#fff8d6', fg='#7fa471', font=('helvetica', 12, 'bold'))
    Canvo1.create_window(300, 130, window=browseButton_Excel)

    saveAsButton_CSV = tk.Button(Convo,text='Convert Excel to CSV', command=convertToCSV, bg='#fff8d6', fg='#7fa471', font=('helvetica', 12, 'bold'))
    Canvo1.create_window(300, 180, window=saveAsButton_CSV)

    exitButton = tk.Button (Convo, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
    Canvo1.create_window(300, 230, window=exitButton) 

# This the main Gui how it should look 
canvas1 = tk.Canvas(root, width = 600, height = 600, bg = '#699e9b', relief = 'raised')
canvas1.pack()

# This is the Title of the Gui
label1 = tk.Label(root, text='Average Files Counter', bg = '#699e9b', font=('helvetica', 20, 'bold'))

# 300 and 60 for the positining
canvas1.create_window(300, 30, window=label1)




# This is the Title of the Gui
label2 = tk.Label(root, text='** This Software only works with CSV files!\n\t\t\t\t \t** If You have an Excel file Please be Free to use the Built-in converter located in File.', bg = '#699e9b', font=('helvetica', 10, 'bold'))

# 300 and 60 for the positining
canvas1.create_window(140, 100, window=label2)

# This Button to get the desire file

browseButton_Excel = tk.Button(text="      Select CSV File     ", command=getFilePath, bg='#fff8d6', fg='#7fa471', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

def aboutUs():

    messagebox.showinfo('About Us', 'This App was Developped By Mohamed Shili.\nAll Rights reserved')

my_menu = Menu(root)
root.config(menu=my_menu)

# Creat items for the menu
file_menu = Menu(my_menu)
file_menu.config(font=('helvetica', 12, 'bold'))
# Add the Name of the options on the menu
my_menu.add_cascade(label = 'File', menu=file_menu )
# add the options inside the "File" menu
file_menu.add_command(label="Open CSV File", command= getFilePath)
# To add a line between options for better looking design :)
file_menu.add_separator()
file_menu.add_command(label="Convert File To CSV", command= fileConverter)

view_menu = Menu(my_menu)
view_menu.config(font=('helvetica', 12, 'bold'))
my_menu.add_cascade(label = 'View', menu=view_menu)
view_menu.add_command(label="Show Headers of the File", command= checkHeaders)
view_menu.add_separator()
view_menu.add_command(label="Show Years of the File", command= showYears)

help_menu = Menu(my_menu)
my_menu.add_cascade(label = 'Help', menu=help_menu)
help_menu.config(font=('helvetica', 12, 'bold'))
# THIS BUTTON NEED TO BE FIXED
help_menu.add_command(label="About Us", command= aboutUs)

root.mainloop()

