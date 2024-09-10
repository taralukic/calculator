
import tkinter as tk

calculation = ""
decimalUsed = False
operatorUsed = False


def addToCalculation(symbol1):
    global calculation
    global operatorUsed
    operatorUsed = False
    calculation += str(symbol1)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def operator(symbol2):
    global decimalUsed
    global operatorUsed
    global calculation
    if not operatorUsed:
        calculation += symbol2
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        decimalUsed = False
        operatorUsed = True


def addDecimal():
    global decimalUsed
    global operatorUsed
    global calculation
    if not decimalUsed:
        calculation += "."
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        decimalUsed = True


def evaluateCalculation():
    global calculation
    try:
        current_text = text_result.get(1.0, "end")
        calculation = str(eval(current_text))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, "=" + calculation)
    except:
        clearField()
        text_result.insert(1.0, "Error")


def clearField():
    global calculation
    global decimalUsed
    global operatorUsed
    calculation = ""
    decimalUsed = False
    operatorUsed = False
    btn_decimal.config(state=tk.NORMAL)
    text_result.delete(1.0, "end")


def backspace():
    global calculation
    current_text = text_result.get(1.0, "end-1c")
    if current_text:
        calculation = current_text[:-1]
        text_result.delete(0.0, "end")
        text_result.insert("end", calculation)


def keyPress(event):
    key = event.char
    if key.isdigit():
        addToCalculation(key)
    elif key == ".":
        addDecimal()
    elif key in "+-*/":
        operator(key)
    elif key == "\r":
        evaluateCalculation()
    elif key == "\b":
        backspace()


root = tk.Tk()
root.title("Calculator")
root.geometry("300x275")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)
w = 300
h = 275
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2) - 100
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


btn1 = tk.Button(root, text="1", command=lambda: addToCalculation(
    1), width=5, font=("Arial", 14))
btn1.grid(row=2, column=1)

btn2 = tk.Button(root, text="2", command=lambda: addToCalculation(
    2), width=5, font=("Arial", 14))
btn2.grid(row=2, column=2)

btn3 = tk.Button(root, text="3", command=lambda: addToCalculation(
    3), width=5, font=("Arial", 14))
btn3.grid(row=2, column=3)

btn4 = tk.Button(root, text="4", command=lambda: addToCalculation(
    4), width=5, font=("Arial", 14))
btn4.grid(row=3, column=1)

btn5 = tk.Button(root, text="5", command=lambda: addToCalculation(
    5), width=5, font=("Arial", 14))
btn5.grid(row=3, column=2)

btn6 = tk.Button(root, text="6", command=lambda: addToCalculation(
    6), width=5, font=("Arial", 14))
btn6.grid(row=3, column=3)

btn7 = tk.Button(root, text="7", command=lambda: addToCalculation(
    7), width=5, font=("Arial", 14))
btn7.grid(row=4, column=1)

btn8 = tk.Button(root, text="8", command=lambda: addToCalculation(
    8), width=5, font=("Arial", 14))
btn8.grid(row=4, column=2)

btn9 = tk.Button(root, text="9", command=lambda: addToCalculation(
    9), width=5, font=("Arial", 14))
btn9.grid(row=4, column=3)

btn0 = tk.Button(root, text="0", command=lambda: addToCalculation(
    0), width=5, font=("Arial", 14))
btn0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: operator(
    "+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: operator(
    "-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_mul = tk.Button(root, text="*", command=lambda: operator(
    "*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda: operator(
    "/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda: addToCalculation(
    "("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: addToCalculation(
    ")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", command=clearField,
                      width=5, font=("Arial", 14), bg="red")
btn_clear.grid(row=6, column=1)

btn_equal = tk.Button(
    root, text="=", command=evaluateCalculation, width=5, font=("Arial", 14), bg="lightgreen")
btn_equal.grid(row=6, column=3)

btn_backspace = tk.Button(
    root, text="⌫", command=backspace, width=5, font=("Arial", 14), bg="orange")
btn_backspace.grid(row=6, column=2)

btn_decimal = tk.Button(
    root, text=".", command=lambda: addDecimal(), width=5, font=("Arial", 14))
btn_decimal.grid(row=6, column=4)

root.bind('<Key>', keyPress)
root.mainloop()
