import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('DataBase Query and Expected value')
        # Wioth x Height
        self.geometry("850x250")

        # Variable Declaration

        self.query_string = tk.StringVar()
        self.expected_value = tk.StringVar()
        self.database_string = tk.StringVar()
        self.server_string = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 10}
        # label
        ttk.Label(self, text='Database Query:').grid(column=0, row=0, **padding)

        # Data Base Query Input Value
        query_entry = ttk.Entry(self, textvariable=self.query_string, width=120)
        query_entry.grid(column=1, row=0, **padding)
        query_entry.focus()

        # label
        ttk.Label(self, text='Expected Value Query:').grid(column=0, row=3, **padding)

        # Expected value Input Value
        expected_value_entry = ttk.Entry(self, textvariable=self.expected_value, width=5)
        expected_value_entry.grid(column=1, row=3, **padding)
        expected_value_entry.focus()

        # label
        ttk.Label(self, text='Database Name:').grid(column=0, row=5, **padding)

        # Data Base Name Dropdown Value
        database_values = [
            "sleepstudy",
            "Example1",
            "Example2",
            "Example3"]
        combo = ttk.Combobox(self, textvariable=self.database_string)
        combo.set("Pick an Data Base name")
        combo['values'] = database_values
        combo['state'] = 'readonly'
        combo.place(x=400, y=90, width=200)

        # label
        ttk.Label(self, text='Server Name:').grid(column=0, row=6, **padding)

        # Server Name Dropdown Value
        server_values = [
            "EC2AMAZ-O7K498H\SQLEXPRESS",
            "Example1",
            "Example2",
            "Example3"]
        combo = ttk.Combobox(self, textvariable=self.server_string)
        combo.set("Pick a Server Option")
        combo['values'] = server_values
        combo['state'] = 'readonly'
        combo.place(x=400, y=130, width=200)

        # Button
        submit_button = ttk.Button(self, text='Submit', command=lambda: [self.confirm(), self.submit()])
        # Button Location Configurations
        submit_button.grid(column=1, row=7, **padding)


    def confirm(self):
        msg_box = tk.messagebox.askquestion('Query Form Status',
                                            'Are you sure you want to submit these values Received',
                                            icon='warning')
        if msg_box == 'yes':
            self.destroy()
        else:
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')

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



# if __name__ == "__main__":
# app = App()
# app.mainloop()
# test_pilot_gasstation_pricing(fixed_driver)

############################
# Historical Code
############################
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

 #database_entry = ttk.Entry(self, textvariable=self.database_string, width=13)
 #database_entry.grid(column=1, row=5, **padding)
 #database_entry.focus()

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
