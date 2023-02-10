import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Box Title
        self.title('DataBase Query and Expected value')
        self.text_box = tk.Text()


        # Width x Height
        self.geometry("850x250")

        # Variable Declaration

        self.query_string = tk.StringVar()
        self.expected_value = tk.StringVar()
        self.database_string = tk.StringVar()
        self.server_string = tk.StringVar()

        # Variable Configurations
        self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # Creating Widget
        self.create_widgets()

    def create_widgets(self):

        # Spacing Functions

        padding = {'padx': 10, 'pady': 10}

        ###################################
        # Database Query
        ###################################

        # label
        ttk.Label(self, text='Database Query:').grid(column=0, row=0,  **padding)

        # Creating Variable For "Database Query" String Received From User Input Form
        #query_entry = ttk.Entry(self, textvariable=self.query_string, width=120)
        self.text_box.grid(row=0, column=1, sticky="nsew", columnspan=2)
        self.grid_rowconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=5)





        # Apply Spacing Functions
        #query_entry.grid(column=1, row=0, **padding)

        #query_entry.focus()

        ###################################
        # Expected Value
        ###################################

        # label
        ttk.Label(self, text='Expected Value Query:').grid(column=0, row=3, **padding)

        # Creating Variable For "Expected Value" String Received From User Input Form
        expected_value_entry = ttk.Entry(self, textvariable=self.expected_value, width=5)

        # Apply Spacing Functions
        expected_value_entry.grid(column=1, row=3, **padding, columnspan=2)

        expected_value_entry.focus()

        ###################################
        # Database Name
        ###################################

        # label
        ttk.Label(self, text='Database Name:').grid(column=0, row=5, **padding)

        # Create List Variable "Database_Values" that contains selectable options
        database_values = [
            "sleepstudy",
            "Example1",
            "Example2",
            "Example32"]

        # Creating Variable For "Database Name String" String Received From User Input Form
        Database_Combo_Variable = ttk.Combobox(self, textvariable=self.database_string)

        # Apply List Variable to Combo
        Database_Combo_Variable['values'] = database_values

        # Set Initial Dropdown Title
        Database_Combo_Variable.set("Select From Database List")

        # Set State to Read Only
        Database_Combo_Variable['state'] = 'readonly'

        # Set Location
        Database_Combo_Variable.place(x=400, y=140, width=200)

        ###################################
        # Server Name
        ###################################

        # label
        ttk.Label(self, text='Server Name:').grid(column=0, row=6, **padding)

        # Create List Variable "Server_Values" that contains selectable options
        server_values = [
            "EC2AMAZ-O7K498H\SQLEXPRESS",
            "Example1",
            "Example2",
            "Example3"]

        # Creating Variable For "Server String" String Received From User Input Form
        combo = ttk.Combobox(self, textvariable=self.server_string)

        # Apply List Variable to Combo
        combo['values'] = server_values

        # Set Initial Dropdown Title
        combo.set("Pick a Server Option")

        # Set State to Read Only
        combo['state'] = 'readonly'

        # Set Location
        combo.place(x=400, y=175, width=200)

        ###################################
        # Button
        ###################################

        # Button
        submit_button = ttk.Button(self, text='Submit', command=lambda: [self.confirm(), self.submit()])

        # Button Location Configurations
        submit_button.grid(column=1, row=7, **padding)

    ####################################
    # CONFIRMATION SELECTION FUNCTION
    ###################################

    def confirm(self):
                                            #TITLE /#MESSAGE / ICON
        msg_box = tk.messagebox.askquestion('Query Form Status',
                                            'Are you sure you want to submit these values Received'
                                            , icon='warning')

        # If User Has Selected Yes, Continue Submit Function
        if msg_box == 'yes':
            self.destroy()

        # If User Has Selected No, Return User to Original Form
        else:
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')


    #######################
    # SUBMIT BUTTON FUNCTION
    ########################

    def submit(self):

        # Extract Query String From Form When Selecting Submit
        self.query_string_value = self.query_string.get()
        query_string_text = self.query_string_value
        print(query_string_text)

        # Extract Expected Value From Form When Selecting Submit
        self.expected_string_value = self.expected_value.get()
        expected_value_text = self.expected_string_value

        # Extract Expected DataBase Name From Form When Selecting Submit
        self.database_string_value = self.database_string.get()
        database_value_text = self.database_string_value

        # Extract Expected Server Name From Form When Selecting Submit
        self.server_string_value = self.server_string.get()
        server_value_text = self.server_string_value

        return query_string_text, expected_value_text, database_value_text, server_value_text



############################
# Historical Code
############################

# if __name__ == "__main__":
# app = App()
# app.mainloop()
# test_pilot_gasstation_pricing(fixed_driver)


# print("test")
# exec(test_01_pilot_gas_pricing.py)
# print(query_string_text)
# print(self.query_string_value)
# self.expected_string_value = self.expected_value.get()
# return query_string_text
# self.query_string.get(), self.expected_value.get()

# query_entry = ttk.Entry(self, textvariable=self.query_string, width=120)
# query_entry.place(width=150, height=150,relx = 0.4, rely = 0.05)
# query_entry.grid(column=0, row=1, **padding)

# database_entry = ttk.Entry(self, textvariable=self.database_string, width=13)
# database_entry.grid(column=1, row=5, **padding)
# database_entry.focus()

# query_entry = ScrolledText(self,wrap=tk.WORD)
# self.query_entry = tk.Text(self, width=40, height=2, **padding)
# self.query_entry.grid(column=0, row=1)
# query_entry.focus()

# print(query_string_text)
# print(self.query_string_value)
# self.expected_string_value = self.expected_value.get()
# return query_string_text
# self.query_string.get(), self.expected_value.get()


# query_string = "select count from [3_patient_summary_frequent_events] where patient_ecd_str =  940034766 and icd_major =  'G47'"
# expected_value = 3
