from tkinter import *
from odessa_chat import get_message, chatbot_name

#Colors for the application:
BACKGROUND_MAIN = "#3486eb"
BACKGROUND_SECOND = "#eed9c4"
TEXT_COLOR = "#EAECEE"

#Fonts for the application:
FONT = "Verdana"
BOLD_FONT = "Verdana 16 bold"

#Creation of the application:
class OdessaApplication:

    #Basic constructor:
    def __init__(self):
        self.window = Tk() #Instantiated the first instance of a window
        self._setup_main_window()

    #This method is what runs the window of the UI to display the design of the chat
    def run(self):
        self.window.mainloop()

    #This methods involves the setting up of Odessa whenever it is started up by the user
    def _setup_main_window(self):
        self.window.title("Odessa Chat")
        self.window.resizable(width=False, height=False) #Do not want the window to be resizable, so both dimensions are false
        self.window.config(width=800, height=550, bg=BACKGROUND_MAIN) #configure is how we give different attributes to the widgets in our application



        #Head Label:
        head_label = Label(self.window, bg=BACKGROUND_MAIN, fg=TEXT_COLOR,
                           text="Chat with Odessa: A Healthcare AI", font=BOLD_FONT, pady=10)
        head_label.place(relwidth=1) #relwidth is between 0 and 1, representing how much of the label will take up the location it is in


        #Divider:
        line = Label(self.window, width=450, bg=BACKGROUND_SECOND)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #Text Field: This is where the text will be displayed
        #Using an instance variable so we can use it later
        self.text_widget = Text(self.window, width=20, height=2, bg=BACKGROUND_MAIN, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5) #20 characters can will up one line, use two lines for it

        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.config(cursor="arrow", state=DISABLED)

        #Scroll Bar:
        scroll_bar = Scrollbar(self.text_widget)
        scroll_bar.place(relheight=1, relx=0.974)
        scroll_bar.config(command=self.text_widget.yview) #Need a command or else the scroll bar will not work; what it
        #does is change the y position of the text_widget, so scrolling up and down is enabled

        #Bottom Label: Background for bottom area
        bottom_label = Label(self.window, bg=BACKGROUND_SECOND, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        #Text Input Field: Where the user will be able to enter their responses
        self.text_input = Entry(bottom_label, bg="#808080", fg=TEXT_COLOR, font=FONT)
        self.text_input.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.text_input.focus() #Whenever the app starts, the entry box is in focus/selected so that user can start typing
        self.text_input.bind("<Return>", self._on_enter_pressed) #Allows for a message to be sent

        #Send Button: How the user will be able to send messages to Odessa
        send_button = Button(bottom_label, text="Send", font=BOLD_FONT, width=20, bg=BACKGROUND_SECOND,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relw=0.22)







    #Upon the user clicking "Send," the method _insert_message is run to display the message exchange
    #in the chat field area.
    def _on_enter_pressed(self, event):
        message = self.text_input.get() #Gets input text as a string; whenever you user .get() on an Entry widget, the
        #text within the field is what gets stored or pulled
        self._insert_message(message, "You")

    #Adds the user and Odessa's messages to the chat field area
    def _insert_message(self, message, sender):
        if not message:
            return #Say if not text is written, this would occur

        self.text_input.delete(0, END) #Remove text from input field when send it
        main_message = (f'{sender}: {message}\n\n') #This represents the user
        self.text_widget.config(state=NORMAL)
        self.text_widget.insert(END, main_message)
        self.text_widget.config(state=DISABLED)

        second_message = (f'{chatbot_name}: {get_message(message)}\n\n') #This reprents Odessa
        self.text_widget.config(state=NORMAL)
        self.text_widget.insert(END, second_message)
        self.text_widget.config(state=DISABLED)

        self.text_widget.see(END) #This scrolls to the end, so we are always able to see the last/first message.


#This section ultimately is what you will use to run Odessa
if __name__ == "__main__":
    app = OdessaApplication()
    app.run()




