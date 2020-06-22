from tkinter import *
import requests
import bs4
from bs4 import BeautifulSoup
import yfinance as yf



#Create a stock app class
class Stockapp:

    
    

    def __init__(self, master=None):

        '''
        DOCSTRING: Define what to do on initialization
        '''
        #Assign reference to the main window of the application
        self.master=master
        
        #Add a name to our application
        master.title('Stock Price App')

        #Create a main screen layout
        self.createCanvas()

        #Create a frame for widgets in the upper part of the app
        self.upperFrame()

        #Create a widget to get user input
        self.entryLine()

        #Create a button that will execute the search
        self.searchButton()

        #Create a frame for widgets in the lower part of the app
        self.lowerFrame()

        #Create an area to display the results of the search
        self.lowerLabel()

        
        

    def createCanvas(self):

        '''
        DOCSTRING: Method that creates the main screen layout
        INPUT: Nothing
        OUTPUT: Creates the layout for the main screen
        '''

        self.canvas=Canvas(self.master, height=200, width=400, bg='#0E8AEC')
        self.canvas.pack()

        
        

    def upperFrame(self):

        '''
        DOCSTRING: Method that creates the upper frame layout
        INPUT: Nothing
        OUTPUT: Creates the layout for the frame for widgets
        in the upper part of the screen
        '''

        self.upper_frame=Frame(self.master, bg='#0E8AEC')
        self.upper_frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor='n')

        
        

    def entryLine(self):
        
        '''
        DOCSTRING: Method that creates the widget to get user input
        INPUT: Nothing
        OUTPUT: Creates the window 
        '''

        self.entryline=Entry(self.upper_frame)
        self.entryline.place(relwidth=0.65, relheight=1)


        
        
    def searchButton(self):

        '''
        DOCSTRING: Method that creates the search button
        INPUT: Nothing
        OUTPUT: Creates the "Search" button 
        '''

        self.searchbutton=Button(self.upper_frame, text='Search', command=lambda: self.getStock(self.entryline.get()))
        self.searchbutton.place(relwidth=0.3, relx=0.7, relheight=1)


    def lowerFrame(self):

        '''
        DOCSTRING: Method that creates the lower frame layout
        INPUT: Nothing
        OUTPUT: Creates the layout for the frame for widgets
        in the upper part of the screen
        '''

        self.lowerframe=Frame(self.master)
        self.lowerframe.place(relwidth=0.75, relheight=0.5, relx=0.5, rely=0.3, anchor='n')


        
        
    def lowerLabel(self):

        '''
        DOCSTRING: Method that creates the output widget layout
        INPUT: Nothing
        OUTPUT: Creates the layout for the output in the lower frame
        '''

        self.label=Label(self.lowerframe, bg='white')
        self.label.place(relwidth=1, relheight=1)

        
        

    def getStock(self, symbol):

        '''
        DOCSTRING: Method that creates the output widget layout
        INPUT: Symbol that we get from the user input line
        OUTPUT: Creates an answer that includes the most recent stock price
        '''

        try:
            ticker = yf.Ticker(symbol.upper())
            price=ticker.info['regularMarketPreviousClose']
            answer = 'The latest price of '+symbol.upper()+' stock is ($) '+str(price)
        except:
            answer="Couldn't find this stock ticker. Please try again"
        self.label['text']=answer




#Execution
if __name__ == '__main__':

    #Create the main window of an application
    root=Tk()

    #Tell our calculator class to use this window
    app=Stockapp(root)

    #Executable loop on the application, waits for user input
    root.mainloop()
