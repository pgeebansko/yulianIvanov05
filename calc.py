import tkinter as tk

buttons = {
    'row_1': ('%', 'CE', 'C', 'BACK'),
    'row_2': ('1/X', 'X2', '2X', '/'),
    'row_3': ('7', '8', '9', '*'),
    'row_4': ('4', '5', '6', '-'),
    'row_5': ('1', '2', '3', '+'),
    'row_6': ('+-', '0', ',', '=')
}
number_buttons = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
clear_buttons = {'CE', 'C'}
operator_buttons = {'+', '-', '*', '/'}

last_num = 0
current_operation = ''
should_clear_result = False
should_clear_tip = False


def clear_result():
    set_result('')


def set_result(text):
    result['text'] = text


def add_to_result(text):
    new_text = result['text']
    new_text += text
    set_result(new_text)


def get_result():
    return result['text']


def clear_tip():
    tip['text'] = ''


def add_to_tip(text):
    tip['text'] += text


def operation(operation_type, num_1, num_2):
    if operation_type == '+':
        return num_1 + num_2
    elif operation_type == '-':
        return num_1 - num_2
    elif operation_type == '*':
        return num_1 * num_2
    elif operation_type == '/':
        return num_1 / num_2


class Button:
    def __init__(self, text, grid_props):
        self.text = text
        self.grid_props = grid_props
        self.is_number = self.text in number_buttons
        self.is_clear = self.text in clear_buttons
        self.is_operator = self.text in operator_buttons
        self.is_equal = self.text == '='
        self.is_back = self.text == 'BACK'
        self.is_float = self.text == '',
        self.init_button = tk.Button(text=self.text, font=['Arial', 15, 'bold'], bg='white', command=self.pressed)
        self.init_button.grid(self.grid_props)

    def pressed(self):
        global result, current_operation, last_num, should_clear_result, should_clear_tip
        if self.is_number:
            if current_operation != '' and should_clear_result:
                clear_result()
                should_clear_result = False
            add_to_result(self.text)
        elif self.is_clear:
            clear_result()
            clear_tip()
        elif self.is_operator:
            if should_clear_tip:
                clear_tip()
                should_clear_tip = False
            current_result = float(get_result())
            set_result(operation(current_operation, last_num, current_result))
            last_num = float(get_result())
            current_operation = self.text
            should_clear_result = True
            add_to_tip(f'{current_result} {current_operation} ')
        elif self.is_equal:
            temp_result = operation(current_operation, last_num, float(get_result()))
            add_to_tip(f'{float(get_result())} = {temp_result}')
            set_result(temp_result)
            last_num = 0
            current_operation = ''
            should_clear_tip = True
        elif self.is_back:
            current = get_result()
            if type(current) != 'str':
                return
            set_result(current[:-1])
        elif self.is_float:
            current = get_result()
            set_result(f'{current}.')


win = tk.Tk()
win.title("Calculator")
win.geometry("320x445+600+200")
win.minsize(320, 445)
win.maxsize(320, 445)
win.config(
    bg='white'
)

win.grid_columnconfigure(0, minsize=80)
win.grid_columnconfigure(1, minsize=80)
win.grid_columnconfigure(2, minsize=80)
win.grid_columnconfigure(3, minsize=80)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)
win.grid_rowconfigure(6, minsize=60)
win.grid_rowconfigure(7, minsize=60)

tip = tk.Label(win, text='', anchor='e', font=['Arial', 13, 'bold'], padx=10, bg='white')
tip.grid(row=0, column=0, sticky='ew', columnspan=4, )

result = tk.Label(win, text='', anchor='e', font=['Arial', 25, 'bold'], padx=10, bg='white')
result.grid(row=1, column=0, sticky='ew', columnspan=4, )


def create_row(info, row_index):
    for index, button_label in enumerate(info):
        btn = Button(button_label, {'column': index, 'row': row_index + 1, 'sticky': 'swen'})


for i in range(1, 7):
    create_row(buttons.get(f'row_{i}'), i)


win.mainloop()


