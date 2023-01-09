import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('DataBase Query and Expected value')
        self.geometry("300x100")

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
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=1, columnspan=3, **padding)

    def submit(self):
        query_string_value = self.query_string.get()
        expected_string_value = self.expected_value.get()
        print(query_string_value)
        print(expected_string_value)
        return query_string_value, expected_string_value


if __name__ == "__main__":
    app = App()
    app.mainloop()
    exec = app.submit()
    print(exec)

# query_string = "select count from [3_patient_summary_frequent_events] where patient_ecd_str =  940034766 and icd_major =  'G47'"
# expected_value = 3
