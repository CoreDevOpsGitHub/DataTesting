import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('DataBase Query and Expected value')
        self.geometry("300x100")

        # Variable Declaration

        self.query_string = tk.StringVar()
        self.expected_value = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Database Query:').grid(column=0, row=0, **padding)

        # Data Base
        query_entry = ttk.Entry(self, textvariable=self.query_string)
        query_entry.grid(column=1, row=0, **padding)
        query_entry.focus()

        # label
        ttk.Label(self, text='Expected Value Query:').grid(column=0, row=1, **padding)

        # Expected value
        expected_value_entry = ttk.Entry(self, textvariable=self.expected_value)
        expected_value_entry.grid(column=1, row=1, **padding)
        expected_value_entry.focus()

        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=0, **padding)

        # Output label
        # self.output_label = ttk.Label(self)
        # self.output_label.grid(column=0, row=1, columnspan=3, **padding)

    def submit(self):
        # Extract Query String From Form When Selecting Submit
        self.query_string_value = self.query_string.get()
        query_string_text = self.query_string_value

        # Extract Expected Value From Form When Selecting Submit
        self.expected_value = self.expected_value.get()
        expected_value_text = self.expected_value

        return query_string_text, expected_value_text
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

