import tkinter, logView
import tkinter.messagebox

# Globals for window positioning
w = 280
h = 170
x = 10
y = 10

def main_log(winner = "N/A"):

    class userLogGUI:
        def __init__(self):

            # Main window
            self.window = tkinter.Tk()

            # Title for window
            self.window.title("Show Your Friends!")

            # 4 Frames/Containers of the window
            self.top_frame = tkinter.Frame()
            self.mid_frame = tkinter.Frame()
            self.bottom_frame = tkinter.Frame()
            self.final_frame = tkinter.Frame()


            # Creates the top frame widgets
            self.prompt_label = tkinter.Label(self.top_frame, \
                        text='Your name:')
            self.raw_user_input = tkinter.Entry(self.top_frame, \
                                            width=20)

            # Packing widgets.
            self.prompt_label.pack(side='left')
            self.raw_user_input.pack(side='left')

            # Creates the middle frame widgets
            self.descr_label = tkinter.Label(self.mid_frame, \
                                     text='Converted to miles:')
            
            # We need a StringVar object to associate with
            # an output label. Use the object's set method
            # to store a string of blank characters.
            self.value = tkinter.StringVar()

            # Create a label and associate it with the
            # StringVar object. Any value stored in the
            # StringVar object will automatically be displayed
            # in the label.
            self.miles_label = tkinter.Label(self.mid_frame, \
                                        textvariable="self.value")

            # Packing widgets.
            self.descr_label.pack(side='left')
            self.miles_label.pack(side='left')

            # Creates the bottom frame widgets
            self.calc_button = tkinter.Button(self.bottom_frame, \
                                         text='Save Entry', \
                                         command=self.convert)

            # Packing button
            self.calc_button.pack(side='left')

            # Creates the final frame widgets (View logs or quit)
            self.my_button = tkinter.Button(self.final_frame, \
                                            text='Click To See What Others Got!', \
                                            command=self.view_logs)
            self.quit_button = tkinter.Button(self.final_frame, \
                                              text='Quit', \
                                              command=self.window.destroy)

            # Packing buttons
            self.my_button.pack()
            self.quit_button.pack()
    #

            # Packing all 4 frames
            self.top_frame.pack()
            self.mid_frame.pack()
            self.bottom_frame.pack()
            self.final_frame.pack()

            # Positioning window (Prevents pop-up from hiding behind main pygame window)
            self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

            # Entering main tkinter loop
            tkinter.mainloop()


        # Class member function that simply displays all previous entries in the "out.txt" file
        def view_logs(self):
            logView.display()      
            

        # Class member function that saves the user's name and respective candidate to a text file
        # This text file is opened and displayed on the screen if the user wants to see what candidates others chose.        
        def convert(self):
            # Get user input
            name = str(self.raw_user_input.get())

            # Convert miles to a string and store it
            # in the StringVar object. This will automatically
            # update the miles_label widget.
            self.value.set(name)

            if self.value.get() != "" and self.value.get() != " " and winner != "N/A":

                # Opening output file (Previous users and their respective candidates stored here)
                outputFile = open('out.txt', 'a')
                # Writing formatted username to end of file
                outputFile.write(self.value.get())
                # Just properly formatting
                outputFile.write(":  ")
                # Writing respective candidate next to username
                outputFile.write(winner)
                outputFile.write("\n\n")
                outputFile.close()

    # Create an instance of the userLogGUI class.
    userLog = userLogGUI()

if __name__ == "__main__":
    main_log()