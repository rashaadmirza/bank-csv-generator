import tkinter as tk
from tkinter import filedialog, messagebox
import processor


def browse_file():
    path = filedialog.askopenfilename(
        title="Select Employee Salaries Excel File",
        filetypes=[("Excel Files", "*.xlsx *.xls")]
    )
    if path:
        file_path_var.set(path)
        status_label.config(text="", fg="black")


def generate():
    excel_path = file_path_var.get().strip()

    if not excel_path:
        messagebox.showwarning("No File", "Please select an Excel file first.")
        return

    try:
        status_label.config(text="Processing...", fg="blue")
        root.update_idletasks()
        output_path = processor.process(excel_path)
        status_label.config(text=f"Done! Saved to:\n{output_path}", fg="green")
    except ValueError as e:
        status_label.config(text=f"Error: {e}", fg="red")
    except Exception as e:
        status_label.config(text=f"Unexpected error: {e}", fg="red")


root = tk.Tk()
root.title("Bank CSV Generator")
root.resizable(False, False)
root.geometry("500x220")

padding = {"padx": 20, "pady": 8}

tk.Label(root, text="Employee Salaries Excel File:", anchor="w").pack(fill="x", **padding)

file_frame = tk.Frame(root)
file_frame.pack(fill="x", padx=20)

file_path_var = tk.StringVar()
tk.Entry(file_frame, textvariable=file_path_var, width=45).pack(side="left", padx=(0, 8))
tk.Button(file_frame, text="Browse", command=browse_file).pack(side="left")

tk.Button(root, text="Generate Bank CSV", command=generate, bg="#0078D4", fg="white",
          font=("Arial", 10, "bold"), padx=10, pady=4).pack(pady=12)

status_label = tk.Label(root, text="", wraplength=460, justify="center")
status_label.pack(**padding)

root.mainloop()