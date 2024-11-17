import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def merge_pdfs(pdf_list, output):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output, 'wb') as out_file:
        pdf_writer.write(out_file)

def select_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if files:
        pdf_list.extend(files)
        file_listbox.delete(0, tk.END)
        for file in pdf_list:
            file_listbox.insert(tk.END, file)

def merge_files():
    if not pdf_list:
        messagebox.showwarning("No files", "Please select at least one PDF file to merge.")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_file:
        try:
            merge_pdfs(pdf_list, output_file)
            messagebox.showinfo("Success", f"PDF files merged successfully into {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDF files: {e}")

def clear_files():
    pdf_list.clear()
    file_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("PDF Merger")

pdf_list = []

# Create and place widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

select_button = tk.Button(frame, text="Select PDFs", command=select_pdfs)
select_button.pack(side=tk.LEFT, padx=5, pady=5)

merge_button = tk.Button(frame, text="Merge PDFs", command=merge_files)
merge_button.pack(side=tk.LEFT, padx=5, pady=5)

clear_button = tk.Button(frame, text="Clear", command=clear_files)
clear_button.pack(side=tk.LEFT, padx=5, pady=5)

file_listbox = tk.Listbox(root, width=80, height=10)
file_listbox.pack(padx=10, pady=10)

# Run the application
root.mainloop()
