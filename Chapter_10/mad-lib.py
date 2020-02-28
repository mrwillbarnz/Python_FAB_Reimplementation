# Mad Lib
# Create a story based on user input

from Tkinter import *

class Application(Frame):
    """ GUI Application that creates a story based on user input."""
    def __init__(self, master):
        """ Initialize Frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    # create instruction label
    def create_widgets(self):
        Label(self,
             text = "Enter information for a new story."
             ).grid(row = 0, column = 0, sticky = W)

    # create a label and text entry for the name of a person
        Label(self,
             text = "Person:"
             ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

    # create a label and text entry for a Plural Noun
        Label(self,
              text = "Plural Noun:"
              ).grid(row = 2, column = 0, sticky = W)
    # create a label and text entry for a Verb
        Label(self,
              text = "Verb:"
              ).grid(row = 3, column = 0, sticky = W)
    # create a label and text entry for adjectives check buttons
        Label(self,
              text = "Adjective(s):"
              ).grid(row = 3, column = 0, sticky = W)
    # Create itchy text button
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "itchy",
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)
    # create joyous check button
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text = "joyous",
                    variable = self.is_joyous
                    ).grid(row = 5, column = 1, sticky = W)
    # create electric check button
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "electric",
                    variable = self.is_electric
                    ).grid(row = 5, column = 1, sticky = W)
    # create a label for body parts button
        self.body_part = StringVar()
    # create body part radio buttons
        body_parts = ["bellybutton", "big toe", "medulla oblongata"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part\
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1
    # create a submit button
        Button(self,
               text = "Click for story",
               command = self.tell_story
              ).grid(row = 6, column = 0, sticky = W)
    def tell_story(self):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "itchy, "
        if self.is_itchy.get():
            adjectives += "joyous, "
        if self.is_electric.get():
            adjectives += "electric, "
        body_part = self.body_part.get()
    # create the story
    story = "The famous explorer"
    story += person
    story += " had nearly given up a life-long quest to find the Lost City of "
    story += noun.title()
    story += " when one day, the "
    story += noun
    story += " found "
    story += person + ". "
    story += "A strong, "
    story += adjectives
    story += "peculiar feeling overwhelmed the explorer. "
    story += "After all this time, the quest was finally over. A tear came to "
    story += person + "'s"
    story += body_part + ". "
    story += "And then, the "
    story += noun
    story += " promptly devoured "
    story += person + ". "
    story += "The moral of the story? Be careful what you "
    story += verb
    story += " for."

    # display the story
    self.story_txt.delete(0.0, END)
    self.story_txt.insert(0.0, story)

# main
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()