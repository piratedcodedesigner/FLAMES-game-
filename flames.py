import tkinter as tk

def calculate_flames(name1, name2):
    common_letters = set(name1.lower()) & set(name2.lower())
    for letter in common_letters:
        name1 = name1.replace(letter, '', 1)
        name2 = name2.replace(letter, '', 1)

    count = len(name1) + len(name2)

    flames_map = {1: 'F', 2: 'L', 3: 'A', 4: 'M', 5: 'E', 0: 'S'}
    return flames_map[count % 6]

def get_input_names():
    name1 = name1_entry.get()
    name2 = name2_entry.get()
    return name1, name2

def update_result_label(result):
    result_label.config(text=f"FLAMES result: {result}")

def submit_names():
    name1, name2 = get_input_names()
    result = calculate_flames(name1, name2)
    update_result_label(result)

root = tk.Tk()
root.title("FLAMES Game")

label1 = tk.Label(root, text="Enter first name:")
label1.pack()

name1_entry = tk.Entry(root, width=45)  
name1_entry.pack()

label2 = tk.Label(root, text="Enter second name:")
label2.pack()

name2_entry = tk.Entry(root, width=45)  
name2_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_names)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop() 
# guys u can have fun using this code if u want u can edit