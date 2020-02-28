# Movie Chooser Version 2
# Demonstrates radio buttons

from tkinter import *

class Application(Frame):
    """ GUI Application for favourite movie types. """
    def __init__(self, master):
        """ Initialize Frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """ Create widgets for movie type choices. """
        # create description label
        Label(self,
        text = "Choose your favourite type of movie"
        ).grid(row = 0, column = 0, sticky = W)
        # create instruction label
        Label(self,
        text = "Select one:"
        ).grid(row = 1, column = 0, sticky = W)
        # create variable or single, favourite type of movie
        self.favourite = StringVar()

        # create Comedy radio button
        Radiobutton(self,
        text = "Comedy",
        variable = self.favourite,
        value = "comedy.",
        command = self.update_text
        ).grid(row = 2, column = 0, sticky = W)

        # create Drama radio button
        Radiobutton(self,
        text = "Drama",
        variable = self.favourite,
        value = "drama.",
        command = self.update_text
        ).grid(row = 3, column = 0, sticky = W)

        # create Romance radio button
        Radiobutton(self,
        text = "Romance",
        variable = self.favourite,
        value = "drama.",
        command = self.update_text
        ).grid(row = 3, column = 0, sticky = W)

        # create text field to display result
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
    def update_text(self):
        """ Update text area and display user's favourite movie type. """
        message = "Your favourite type of movie is: "
        message += self.favourite.get()
        self.results_txt.delete(0.0 END)
        self.results_txt.insert(0.0, message)

# main
root = Tk()
root.title("Movie Chooser 2")
app = Application(root)
root.mainloop()
