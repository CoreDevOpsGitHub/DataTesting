import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING

from tkinter.scrolledtext import ScrolledText


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('DataBase Query and Expected value')
        # Wioth x Height
        self.geometry("800x400")

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

        # Data Base Input Value
        query_entry = ttk.Entry(self, textvariable=self.query_string, width=50)
        # query_entry.place(width=150, height=150,relx = 0.4, rely = 0.05)
        query_entry.grid(column=1, row=0, **padding)

        # query_entry = ScrolledText(self,wrap=tk.WORD)
        # self.query_entry = tk.Text(self, width=40, height=2, **padding)
        # self.query_entry.grid(column=0, row=1)
        query_entry.focus()

        # label
        ttk.Label(self, text='Expected Value Query:').grid(column=0, row=3, **padding)

        # Expected value Input Value
        expected_value_entry = ttk.Entry(self, textvariable=self.expected_value)
        expected_value_entry.grid(column=1, row=3, **padding)
        expected_value_entry.focus()

        # label
        ttk.Label(self, text='Database Name:').grid(column=0, row=4, **padding)

        # Data Base Name Input Value
        database_entry = ttk.Entry(self, textvariable=self.database_string)
        database_entry.grid(column=1, row=4, **padding)
        database_entry.focus()

        # label
        ttk.Label(self, text='Server Name:').grid(column=0, row=5, **padding)

        # ServerName (Receiving Input Value)
        server_entry = ttk.Entry(self, textvariable=self.server_string)
        # ServerName (Location Configurations)
        server_entry.grid(column=1, row=5, **padding)
        server_entry.focus()

        # Button
        submit_button = ttk.Button(self, text='Submit', command=lambda: [self.submit(), self.confirm()])
        # Button Location Configurations
        submit_button.grid(column=0, row=6, **padding)

        # Output label
        # self.output_label = ttk.Label(self)
        # self.output_label.grid(column=0, row=1, columnspan=3, **padding)

    def confirm(self):
        showinfo(
            title='Query Form Status',
            message='The query data was successfully filled')
        if tk.messagebox.OK:
            self.destroy()

    def submit(self):
        # Extract Query String From Form When Selecting Submit
        self.query_string_value = self.query_string.get()
        query_string_text = self.query_string_value

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
        # print(query_string_text)
        # print(self.query_string_value)
        # self.expected_string_value = self.expected_value.get()
        # return query_string_text
        # self.query_string.get(), self.expected_value.get()

    def results(self):
        value = 100
        return value

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
# def results(self):
#   value="100"
#  return value


# query_string = "select count from [3_patient_summary_frequent_events] where patient_ecd_str =  940034766 and icd_major =  'G47'"
# expected_value = 3
