from tkinter import *

from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


def LocalServ():
	httpd = HTTPServer(('localhost', 8080), Serv)
	httpd.serve_forever()

root = Tk()


LocalPortcnt = StringVar()
LocalPort = StringVar()
LocalUrlcnt = StringVar()
LocalUrl = StringVar()
LocalUrl.set('Localhost')


CreatserverFrame = Frame(root, highlightthickness = 4,  highlightbackground ='blue')
CreatserverFrame.grid(row = 0, column = 1, padx = 5 , pady = 2 , sticky = 'nw')
# Buttons
Label(CreatserverFrame, text = 'For Test Purpose You Can Creat a Local Server\n For Default Setting Leave The Url to Localhost!').grid(row = 0, column = 0 )
utlTxt = Label(CreatserverFrame, text = 'URL: ').grid(row = 1, column = 0 )
urlEnt = Url = Entry(CreatserverFrame, textvariable = LocalUrl, bg = '#54848C' , fg = '#8BFF00', font=("Courier", 12) ).grid(row = 1, column = 1)
Label(CreatserverFrame, text = 'PORT: ').grid(row = 2, column = 0 )
portTxt = Label(CreatserverFrame, text = 'URL: ').grid(row = 1, column = 0 )
portEnt = Url = Entry(CreatserverFrame, textvariable = LocalPort, bg = '#54848C' , fg = '#8BFF00', font=("Courier", 12) ).grid(row = 2, column = 1)
localcnct = Button(CreatserverFrame, text="Creat Server", fg="green"  , command = LocalServ).grid(row = 1, column = 2, rowspan= 2 , ipady = 10, ipadx = 5)
# Buttons For Showing Server Statue
serverstate  = Button(CreatserverFrame, text="Server Down", fg="Black", bg = 'red', state = DISABLED)
serverstate.grid(row = 4, column = 0, ipady = 10, ipadx = 5)


root.mainloop()
