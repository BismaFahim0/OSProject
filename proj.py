import datetime
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import stat
import shutil
import zipfile
from shutil import copyfile, move, rmtree
import gzip
import subprocess
from tkinter import simpledialog
import platform
import cryptography
from cryptography.fernet import Fernet
import base64
import hashlib
def next_button_click():
 # Function to handle the next button click
 root.destroy() # Destroy the GUI window
root = Tk()
root.title("File Management System")
root.configure(bg="black")
# Set background color of root window
# Main Frame
main_frame = Frame(root, bg="black")
main_frame.pack(padx=20,pady=20)
# Project Title
title_label = Label(main_frame, text="File Management System", font=("Ubuntu", 20), fg="#C0C0C0",
bg="black")
title_label.pack(padx=10,pady=10)
# Group Members & Enrollment
members_frame = Frame(main_frame, bg="black")
members_frame.pack()
members_label = Label(members_frame, text="Group Members & Enrollment", font=("Ubuntu", 16, "bold"),
fg="white", bg="black")
members_label.grid(row=0, column=0, columnspan=2, pady=10)
member1_label = Label(members_frame, text="Bisma Hashmi (02-136212-005)",font=("Ubuntu", 12, "bold"),
fg="white", bg="black")
member1_label.grid(row=1, column=0, sticky="w", padx=10)
member2_label = Label(members_frame, text="Memoona Masood (02-136212-014)",font=("Ubuntu", 12, "bold"),
fg="white", bg="black")
member2_label.grid(row=2, column=0, sticky="w", padx=10)
member3_label = Label(members_frame, text="Syeda Fizza Batool Zaidi (02-136212-043)",font=("Ubuntu", 12,
"bold"), fg="white", bg="black")
member3_label.grid(row=3, column=0, sticky="w", padx=10)
# Lab Instructor
instructor_frame = Frame(main_frame, bg="black")
instructor_frame.pack()
instructor_label = Label(instructor_frame, text="Lab Instructor", font=("Ubuntu", 16, "bold"), fg="white",
bg="black")
instructor_label.grid(row=0, column=0, pady=10)
instructor_name_label = Label(instructor_frame, text="Miss Fatima Zafar",font=("Ubuntu", 12, "bold"), fg="white",
bg="black")
instructor_name_label.grid(row=1, column=0, padx=10)
next_button = Button(main_frame, text="Next", font=("Ubuntu", 16), command=next_button_click,
bg="#C0C0C0", fg="black")
next_button.pack(pady=20)
root.mainloop()



class FileManagerGUI():
 def __init__(self, root):
     self.root = root
     self.root.title("File Manager")
     self.primary_color = "black"
     self.secondary_color = "white"
     self.main_page_color = "black"
     self.user_authenticated = False
     self.authenticate_user()
     self.path = StringVar()
     self.create_widgets()
     self.root.configure(bg=self.main_page_color)

 def create_widgets(self):
     path_entry = Entry(self.root, textvariable=self.path)
     path_entry.pack(pady=20)
     browse_button = Button(self.root, text="Browse", command=self.browse_directory, bg=self.primary_color,fg="white")
     browse_button.pack(pady=5)
     operations_frame = LabelFrame(self.root, text="File Operations",bg="#C0C0C0", padx=5, pady=5)
     operations_frame.pack(pady=20)
     create_file_button = Button(operations_frame, text="Create File", command=self.create_file,bg=self.primary_color, fg="white")
     create_file_button.grid(row=0, column=0, padx=5, pady=5)
     rename_file_button = Button(operations_frame, text="Rename File", command=self.rename_file,bg=self.primary_color, fg="white")
     rename_file_button.grid(row=0, column=1, padx=5, pady=5)
     delete_file_button = Button(operations_frame, text="Delete File", command=self.delete_file,bg=self.primary_color, fg="white")
     delete_file_button.grid(row=0, column=2, padx=5, pady=5)
     create_directory_button = Button(operations_frame, text="Create Directory", command=self.create_directory,bg=self.primary_color, fg="white")
     create_directory_button.grid(row=1, column=0, padx=5, pady=5)
     rename_directory_button = Button(operations_frame, text="Rename Directory",command=self.rename_directory,bg=self.primary_color, fg="white")
     rename_directory_button.grid(row=1, column=1, padx=5, pady=5)
     delete_directory_button = Button(operations_frame, text="Delete Directory", command=self.delete_directory,bg=self.primary_color, fg="white")
     delete_directory_button.grid(row=1, column=2, padx=5, pady=5)
     search_entry = Entry(self.root, textvariable=self.search_entry)
     search_entry.pack(pady=5)
     search_files_button = Button(operations_frame, text="Search Files", command=self.search_files,bg=self.primary_color, fg="white")
     search_files_button.grid(row=1, column=3, padx=5, pady=5)
     edit_file_button = Button(operations_frame, text="Edit File", command=self.edit_file,bg=self.primary_color, fg="white")
     edit_file_button.grid(row=2, column=1, padx=5, pady=5)
     encrypt_file_button = Button(operations_frame, text="Encrypt File", command=self.encrypt_file,bg=self.primary_color, fg="white")
     encrypt_file_button.grid(row=2, column=2, padx=5, pady=5)
     decrypt_file_button = Button(operations_frame, text="Decrypt File", command=self.decrypt_file,bg=self.primary_color, fg="white")
     decrypt_file_button.grid(row=2, column=3, padx=5, pady=5)
     compress_file_button = Button(operations_frame, text="Compress File", command=self.compress_file,bg=self.primary_color, fg="white")
     compress_file_button.grid(row=3, column=0, padx=5, pady=5)
     decompress_file_button = Button(operations_frame, text="Decompress File", command=self.decompress_file,bg=self.primary_color, fg="white")
     decompress_file_button.grid(row=3, column=1, padx=5, pady=5)
     open_file_button = Button(operations_frame, text="Open File", command=self.open_file,bg=self.primary_color, fg="white")
     open_file_button.grid(row=0, column=3, padx=5, pady=5)
     move_file_button = Button(operations_frame, text="Move File", command=self.move_file,bg=self.primary_color, fg="white")
     move_file_button.grid(row=2, column=0, padx=5, pady=5)
     copy_file_button = Button(operations_frame, text="Copy File", command=self.copy_file,bg=self.primary_color, fg="white")
     copy_file_button.grid(row=3, column=3, padx=5, pady=5)
     batch_delete_files_button = Button(operations_frame, text="Batch Delete Files",command=self.batch_delete_files,bg=self.primary_color, fg="white")
     batch_delete_files_button.grid(row=4, column=0, padx=5, pady=5)
     batch_delete_directory_button = Button(operations_frame, text="Batch Delete Directory",command=self.batch_delete_directory,bg=self.primary_color, fg="white")
     batch_delete_directory_button.grid(row=4, column=1, padx=5, pady=5)
     show_content_button = Button(operations_frame, text="Show File Content",command=self.show_file_content,bg=self.primary_color, fg="white")
     show_content_button.grid(row=3, column=2, padx=5, pady=5)
     get_properties_button = Button(operations_frame, text="Get Properties", command=self.get_file_properties,bg=self.main_page_color, fg="white")
     get_properties_button.grid(row=4, column=4, padx=5, pady=5)
     clear_button = Button(operations_frame, text="Clear", command=self.clear_display,bg=self.primary_color, fg="white")
     clear_button.grid(row=4, column=3, padx=5, pady=5)
     search_query_var = StringVar()
     search_query_entry = Entry(self.root, textvariable=search_query_var)
     search_query_entry.pack(pady=5)
     search_criteria_options = ["File Name", "File Size", "Creation Time", "Permissions", "Extension"]
     search_criteria_var = StringVar()
     search_criteria_var.set(search_criteria_options[0])
     search_criteria_dropdown = OptionMenu(self.root, search_criteria_var, *search_criteria_options)
     search_criteria_dropdown.pack(pady=5)
     search_button = Button(self.root, text="Search Files (Advanced)",command=lambda: self.search_files_advanced(search_query_var.get(),search_criteria_var.get()),bg=self.primary_color, fg="white")
     search_button.pack(pady=5)
     browse_file_button = tk.Button(self.root, text="Browse Files", command=self.browse_files, bg=self.primary_color,fg="white")
     browse_file_button.pack(pady=5)
     change_permissions_button = Button(operations_frame, text="Change Permissions",command=self.change_permissions,bg=self.primary_color, fg="white")
     change_permissions_button.grid(row=4, column=2, padx=5, pady=5)
     quit_button = Button(self.root, text="Quit", command=self.quit_application, bg="black", fg="white")
     quit_button.pack(pady=20)
     self.display = Text(self.root, height=50, width=150,bg="#C0C0C0")
     self.display.pack(pady=10)


 def browse_directory(self):
         directory = filedialog.askdirectory()
         self.path.set(directory)

 def browse_files(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File")
     self.path.set(file_path)

 def authenticate_user(self):
     username = simpledialog.askstring("Authentication", "Enter your username:")
     password = simpledialog.askstring("Authentication", "Enter your password:",show ='*')

     # For simplicity, using hardcoded username and password (replace with your authentication logic)
     if username == "bisma" and password == "123":
         self.user_authenticated = True
     else:
         messagebox.showerror("Authentication Failed", "Invalid username or password")


 def create_file(self):
     file_name = simpledialog.askstring("Create File", "Enter the file name:")
     if file_name:
         file_path = os.path.join(self.path.get(), file_name)
         if not os.path.exists(file_path):
             try:
                 with open(file_path, 'w'):
                     pass
                 messagebox.showinfo("Success", "File created successfully!")
             except Exception as e:
                 messagebox.showerror("Error", str(e))
         else:
             messagebox.showerror("Error", "File already exists!")

 def search_files_advanced(self, search_query, search_criteria):
     path = self.path.get()
     if path:
         try:
             matching_files = []
             for file_name in os.listdir(path):
                 file_path = os.path.join(path, file_name)

                 # Check if the file matches the search criteria
                 if search_criteria == "File Name" and search_query.lower() in file_name.lower():
                     matching_files.append(file_path)
                     # Check if the file matches the search criteria
                     if search_criteria == "File Name" and search_query.lower() in file_name.lower():
                         matching_files.append(file_path)
                         if search_criteria == "File Name" and search_query.lower() in file_name.lower():
                             matching_files.append(file_path)
                 elif search_criteria == "File Size" and os.path.isfile(file_path):
                             size = os.path.getsize(file_path)
                             size_kb = size / 1024  # Convert size to kilobytes
                             #print(f"File: {file_name}, Size: {size} bytes, Size (KB): {size_kb} KB")

                             if search_query.lower().endswith('kb'):
                                 try:
                                     query_value = float(search_query[:-2])  # Remove 'KB' suffix
                                     rounded_size_kb = round(size_kb)  # Round off the size to the nearest whole number
                                     print(f"Query Value: {query_value} KB, Rounded Size: {rounded_size_kb} KB")
                                     if rounded_size_kb == query_value:
                                         matching_files.append(file_path)
                                 except ValueError as e:
                                     print(f"Error: {e}")
                             elif size == int(search_query):
                                 matching_files.append(file_path)
                             print(f"Matching Files: {matching_files}")
                 elif search_criteria == "Creation Time" and os.path.exists(file_path):
                     creation_time = os.path.getctime(file_path)
                     if datetime.fromtimestamp(creation_time).strftime('DD/MM/YYYY %H:%M AM/PM') == search_query:
                         matching_files.append(file_path)
                 elif search_criteria == "Permissions" and os.path.exists(file_path):
                     permissions = stat.filemode(os.stat(file_path).st_mode)
                     if permissions == search_query:
                         matching_files.append(file_path)
                 elif search_criteria == "Extension" and os.path.isfile(file_path):
                     _, extension = os.path.splitext(file_name)
                     if extension.lower() == search_query.lower():
                         matching_files.append(file_path)

             if matching_files:
                 result = "\n".join(matching_files)
                 messagebox.showinfo("Search Results", "Matching files:\n" + result)
             else:
                 messagebox.showinfo("Search Results", "No matching files found!")
         except Exception as e:
             messagebox.showerror("Error", str(e))
     else:
         messagebox.showerror("Error", "Please select a directory!")
 def search_entry(self):
     if not self.user_authenticated:
         self.authenticate_user()

     if self.user_authenticated:
         query = self.search_query.get()
         if query:
             try:
                 matches = []
                 for root, dirs, files in os.walk(self.path.get()):
                     for file in files:
                         if query in file:
                             matches.append(os.path.join(root, file))
                 if matches:
                     result = "\n".join(matches)
                     messagebox.showinfo("Search Results", "Matching files:\n" + result)
                 else:
                     messagebox.showinfo("Search Results", "No matching files found!")
             except Exception as e:
                 messagebox.showerror("Error", str(e))

 def rename_file(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File to Rename")
     if file_path:
         new_file_name = simpledialog.askstring("Rename File", "Enter the new file name:")
         if new_file_name:
             new_file_path = os.path.join(self.path.get(), new_file_name)
             try:
                 os.rename(file_path, new_file_path)
                 messagebox.showinfo("Success", "File renamed successfully!")
             except Exception as e:
                 messagebox.showerror("Error", str(e))

 def delete_file(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File to Delete")
     if file_path:
         try:
             os.remove(file_path)
             messagebox.showinfo("Success", "File deleted successfully!")
         except Exception as e:
             messagebox.showerror("Error", str(e))

 def create_directory(self):
     directory_name = simpledialog.askstring("Create Directory", "Enter the directory name:")
     if directory_name:
         directory_path = os.path.join(self.path.get(), directory_name)
         if not os.path.exists(directory_path):
             try:
                 os.mkdir(directory_path)
                 messagebox.showinfo("Success", "Directory created successfully!")
             except Exception as e:
                 messagebox.showerror("Error", str(e))
         else:
             messagebox.showerror("Error", "Directory already exists!")

 def rename_directory(self):
     directory_path = filedialog.askdirectory(initialdir=self.path.get(), title="Select Directory to Rename")
     if directory_path:
         new_directory_name = simpledialog.askstring("Rename Directory", "Enter the new directory name:")
         if new_directory_name:
             new_directory_path = os.path.join(os.path.dirname(directory_path), new_directory_name)
             try:
                 os.rename(directory_path, new_directory_path)
                 messagebox.showinfo("Success", "Directory renamed successfully!")
             except Exception as e:
                 messagebox.showerror("Error", str(e))

 def delete_directory(self):
     directory_path = filedialog.askdirectory(initialdir=self.path.get(), title="Select Directory to Delete")
     if directory_path:
         try:
             rmtree(directory_path)
             messagebox.showinfo("Success", "Directory deleted successfully!")
         except Exception as e:
             messagebox.showerror("Error", str(e))

 # ... (rest of the code remains unchanged)

 def search_files(self):
     query = simpledialog.askstring("Search Files", "Enter the search query:")
     if query:
         try:
             matches = []
             for root, dirs, files in os.walk(self.path.get()):
                 for file in files:
                     if query in file:
                         matches.append(os.path.join(root, file))
             if matches:
                 result = "\n".join(matches)
                 messagebox.showinfo("Search Results", "Matching files:\n" + result)
             else:
                 messagebox.showinfo("Search Results", "No matching files found!")
         except Exception as e:
             messagebox.showerror("Error", str(e))



 def edit_file(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File to Edit")
     if file_path:
         if file_path.endswith('.enc'):
             password = simpledialog.askstring("Decrypt File", "Enter the decryption password:")
             if password:
                 try:
                     with open(file_path, 'rb') as file:
                         encrypted_data = file.read()
                         key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())
                         fernet = Fernet(key)
                         decrypted_data = fernet.decrypt(encrypted_data)
                         decrypted_file_path = file_path[:-4]  # Remove the '.enc' extension
                         with open(decrypted_file_path, 'wb') as decrypted_file:
                             decrypted_file.write(decrypted_data)
                         file_path = decrypted_file_path  # Update file path to open the decrypted file
                         messagebox.showinfo("Success", "File decrypted successfully:\n{}".format(decrypted_file_path))
                 except cryptography.fernet.InvalidToken:
                     messagebox.showerror("Error", "Invalid password!")
                 except Exception as e:
                     messagebox.showerror("Error", str(e))
             else:
                 return  # If no password provided, do not open the file

         # Create a new window for editing and saving the file
         edit_window = Toplevel(self.root)
         file_name = os.path.basename(file_path)
         edit_window.wm_title(format(file_name))

         # Text Editor
         text_editor = Text(edit_window)
         text_editor.pack(fill=BOTH, expand=True)
         with open(file_path, 'r') as file:
             text_editor.insert(END, file.read())

         # Save Button
         def save_file():
             new_content = text_editor.get("1.0", END)
             try:
                 with open(file_path, 'w') as file:
                     file.write(new_content)
                 messagebox.showinfo("Success", "File saved successfully!")
             except Exception as e:
                 messagebox.showerror("Error", str(e))
             edit_window.destroy()  # Close the edit window

         save_button = Button(edit_window, text="Save", command=save_file, bg=self.primary_color, fg="black")
         save_button.pack(pady=5)

 # The rest of the code remains unchanged

 def encrypt_file(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File to Encrypt")
     if file_path:
         password = simpledialog.askstring("Encrypt File", "Enter the encryption password:")
         if password:
             try:
                 with open(file_path, 'rb') as file:
                     encrypted_file_path = file_path + '.enc'
                     key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())
                     fernet = Fernet(key)
                     encrypted_data = fernet.encrypt(file.read())
                 with open(encrypted_file_path, 'wb') as encrypted_file:
                     encrypted_file.write(encrypted_data)
                 messagebox.showinfo("Success", "File encrypted successfully:\n{}".format(encrypted_file_path))
             except Exception as e:
                 messagebox.showerror("Error", str(e))

 def decrypt_file(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File to Decrypt")
     if file_path:
         password = simpledialog.askstring("Decrypt File", "Enter the decryption password:")
         if password:
             try:
                 with open(file_path, 'rb') as file:
                     encrypted_data = file.read()
                     key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())
                     fernet = Fernet(key)
                     decrypted_data = fernet.decrypt(encrypted_data)
                     decrypted_file_path = file_path[:-4]  # Remove the '.enc' extension
                 with open(decrypted_file_path, 'wb') as decrypted_file:
                     decrypted_file.write(decrypted_data)
                 messagebox.showinfo("Success", "File decrypted successfully:\n{}".format(decrypted_file_path))
             except cryptography.fernet.InvalidToken:
                 messagebox.showerror("Error", "Invalid password!")
             except Exception as e:
                 messagebox.showerror("Error", str(e))

 def compress_file(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File to Compress")
     if file_path:
         try:
             with open(file_path, 'rb') as file:
                 data = file.read()
                 compressed_file_path = file_path + '.gz'
             with gzip.open(compressed_file_path, 'wb') as file:
                 file.write(data)
             messagebox.showinfo("Success", "File compressed successfully!")
         except Exception as e:
             messagebox.showerror("Error", str(e))

 def decompress_file(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File to Decompress")
     if file_path:
         try:
             decompressed_file_path = os.path.splitext(file_path)[0]
             with gzip.open(file_path, 'rb') as file:
                 data = file.read()
             with open(decompressed_file_path, 'wb') as file:
                 file.write(data)
             messagebox.showinfo("Success", "File decompressed successfully!")
         except Exception as e:
             messagebox.showerror("Error", str(e))

 def open_file(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File to Open")
     if file_path:
         try:
             # subprocess.call(['open', file_path]) # On macOS
             subprocess.call(['xdg-open', file_path])  # On Linux
             # subprocess.call(['start', file_path], shell=True) # On Windows
         except Exception as e:
             messagebox.showerror("Error", str(e))

 def move_file(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File to Move")
     if file_path:
         try:
             destination = filedialog.askdirectory(initialdir=self.path.get(), title="Select Destination Directory")
             if destination:
                 shutil.move(file_path, destination)
                 messagebox.showinfo("Success", "File moved successfully to:\n" + destination)
         except Exception as e:
             messagebox.showerror("Error", str(e))

 def copy_file(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File to Copy")
     if file_path:
         try:
             destination = filedialog.askdirectory(initialdir=self.path.get(), title="Select Destination Directory")
             if destination:
                 shutil.copy2(file_path, destination)
                 messagebox.showinfo("Success", "File copied successfully to:\n" + destination)
         except Exception as e:
             messagebox.showerror("Error", str(e))

 def batch_delete_files(self):
     file_paths = filedialog.askopenfilenames(initialdir=self.path.get(), title="Select Files to Delete")
     if file_paths:
         try:
             confirm = messagebox.askyesno("Confirm Delete","Are you sure you want to delete the selected files?")
             if confirm:
                 file_count = 0
                 for file_path in file_paths:
                     os.remove(file_path)
                     file_count += 1
                 messagebox.showinfo("Success", "Deleted {} file(s).".format(file_count))
         except Exception as e:
             messagebox.showerror("Error", str(e))


 def batch_delete_directory(self):
    directory_path = filedialog.askdirectory(initialdir=self.path.get(), title="Select Directory")
    if directory_path:
        try:
            confirm = messagebox.askyesno("Confirm Delete","Are you sure you want to delete the directory and its contents:\n{}".format(directory_path))
            if confirm:
                rmtree(directory_path)
                messagebox.showinfo("Success", "Directory deleted successfully:\n{}".format(directory_path))
        except Exception as e:
            messagebox.showerror("Error", str(e))

 def get_file_properties(self):
     file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File or Directory")
     if file_path:
         properties = self.retrieve_file_properties(file_path)
         self.show_properties_dialog(properties)

 def retrieve_file_properties(self, file_path):
     file_properties = {}

     try:
         # Get file stats
         stat_info = os.stat(file_path)

         # File name
         file_properties['File Name'] = os.path.basename(file_path)

         # File type
         file_properties['File Type'] = 'Directory' if os.path.isdir(file_path) else 'File'

         # Permissions
         file_properties['Permissions'] = stat.filemode(stat_info.st_mode)

         # Owner and Group
         file_properties['Owner'] = stat_info.st_uid
         file_properties['Group'] = stat_info.st_gid

         # Size in bytes
         file_properties['Size (Bytes)'] = stat_info.st_size

         # Timestamps
         file_properties['Access Time'] = datetime.fromtimestamp(stat_info.st_atime).strftime('%Y-%m-%d %H:%M:%S')
         file_properties['Modification Time'] = datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
         file_properties['Change Time'] = datetime.fromtimestamp(stat_info.st_ctime).strftime('%Y-%m-%d %H:%M:%S')

         # Inode and Link Count
         file_properties['Inode'] = stat_info.st_ino
         file_properties['Link Count'] = stat_info.st_nlink

     except FileNotFoundError:
         file_properties['Error'] = 'File not found'
     except Exception as e:
         file_properties['Error'] = str(e)

     return file_properties

 def show_properties_dialog(self, properties):
     properties_window = Toplevel(self.root)
     properties_window.title("File Properties")

     properties_text = Text(properties_window, height=15, width=50, wrap=WORD)
     properties_text.pack(padx=10, pady=10)

     for key, value in properties.items():
         properties_text.insert(END, f"{key}: {value}\n")
 def create_display(self):
    # Create a Text widget for displaying file content
    self.display = Text(self.root, height=10, width=50)
    self.display.pack(pady=10)


 def show_file_content(self):
    file_path = filedialog.askopenfilename(initialdir=self.path.get(), title="Select File")
    if file_path:
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                self.display.delete("1.0", END)
                self.display.insert(END, content)
        except Exception as e:
            messagebox.showerror("Error", str(e))


 def clear_display(self):
    self.display.delete("1.0", END)

 def change_permissions(self):
    path = self.path.get()
    if path:
        permissions = simpledialog.askstring("Change Permissions", "Enter permissions in octal form (e.g., 755):")
        if permissions:
            try:
                permissions = int(permissions, 8)
                os.chmod(path, permissions)
                messagebox.showinfo("Success", "Permissions changed successfully!")
            except ValueError:
                messagebox.showerror("Error", "Invalid permissions entered!")
        else:
            messagebox.showerror("Error", "Please select a file or directory!")

 def get_default_editor(self):
    if platform.system() == "Darwin":  # macOS
        return "open"
    elif platform.system() == "Windows":  # Windows
        return "notepad.exe"
    else:  # Linux
        return "gedit"

 def quit_application(self):
    self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    file_manager = FileManagerGUI(root)
    root.mainloop()