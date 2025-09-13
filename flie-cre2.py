import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
import threading
import time

class ModernFolderCreator:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_variables()
        self.create_widgets()
        self.setup_styles()
        
    def setup_window(self):
        self.root.title("📂 Modern Folder Structure Creator")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Set modern colors
        self.colors = {
            'primary': '#667eea',
            'secondary': '#764ba2', 
            'success': '#4CAF50',
            'warning': '#ff9800',
            'error': '#f44336',
            'bg_light': '#f8f9fa',
            'bg_dark': '#2d3748',
            'text_primary': '#2c3e50',
            'text_light': '#ecf0f1',
            'accent': '#e74c3c'
        }
        
        self.root.configure(bg=self.colors['bg_light'])
        
    def setup_variables(self):
        self.base_path_var = tk.StringVar()
        self.folder_name_var = tk.StringVar()
        self.start_year_var = tk.StringVar(value=str(datetime.now().year))
        self.end_year_var = tk.StringVar(value=str(datetime.now().year + 1))
        
        self.months = [
            "01_January", "02_February", "03_March", "04_April", "05_May", "06_June",
            "07_July", "08_August", "09_September", "10_October", "11_November", "12_December"
        ]
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure styles
        self.style.configure('Header.TLabel', 
                           font=('Segoe UI', 24, 'bold'),
                           foreground=self.colors['primary'],
                           background=self.colors['bg_light'])
        
        self.style.configure('Subtitle.TLabel',
                           font=('Segoe UI', 12),
                           foreground=self.colors['text_primary'],
                           background=self.colors['bg_light'])
        
        self.style.configure('Modern.TLabel',
                           font=('Segoe UI', 11, 'bold'),
                           foreground=self.colors['text_primary'],
                           background=self.colors['bg_light'])
        
        self.style.configure('Modern.TEntry',
                           font=('Segoe UI', 10),
                           fieldbackground='white',
                           borderwidth=2,
                           relief='solid')
        
        self.style.configure('Success.TButton',
                           font=('Segoe UI', 12, 'bold'),
                           foreground='white',
                           background=self.colors['success'])
        
        self.style.configure('Primary.TButton',
                           font=('Segoe UI', 10, 'bold'),
                           background=self.colors['primary'])
        
        self.style.configure('Warning.TButton',
                           font=('Segoe UI', 9),
                           background=self.colors['warning'])
        
    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg_light'], padx=30, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header Section
        header_frame = tk.Frame(main_frame, bg=self.colors['bg_light'])
        header_frame.pack(fill=tk.X, pady=(0, 30))
        
        title_label = ttk.Label(header_frame, text="📂 Modern Folder Creator", style='Header.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(header_frame, text="Create organized year and month folders with style", style='Subtitle.TLabel')
        subtitle_label.pack(pady=(5, 0))
        
        # Input Section
        input_frame = tk.LabelFrame(main_frame, text="📝 Configuration", font=('Segoe UI', 12, 'bold'),
                                   fg=self.colors['primary'], bg=self.colors['bg_light'], padx=20, pady=15)
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Base Path
        path_frame = tk.Frame(input_frame, bg=self.colors['bg_light'])
        path_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(path_frame, text="📍 Base Directory:", style='Modern.TLabel').pack(anchor='w')
        path_input_frame = tk.Frame(path_frame, bg=self.colors['bg_light'])
        path_input_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.path_entry = ttk.Entry(path_input_frame, textvariable=self.base_path_var, 
                                   style='Modern.TEntry', font=('Segoe UI', 10))
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        browse_btn = ttk.Button(path_input_frame, text="📂 Browse", command=self.browse_path,
                               style='Primary.TButton')
        browse_btn.pack(side=tk.RIGHT)
        
        # Folder Name
        name_frame = tk.Frame(input_frame, bg=self.colors['bg_light'])
        name_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(name_frame, text="📁 Main Folder Name:", style='Modern.TLabel').pack(anchor='w')
        name_entry = ttk.Entry(name_frame, textvariable=self.folder_name_var,
                              style='Modern.TEntry', font=('Segoe UI', 10))
        name_entry.pack(fill=tk.X, pady=(5, 0))
        
        # Year Range
        year_frame = tk.Frame(input_frame, bg=self.colors['bg_light'])
        year_frame.pack(fill=tk.X)
        
        start_frame = tk.Frame(year_frame, bg=self.colors['bg_light'])
        start_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        ttk.Label(start_frame, text="📅 Start Year:", style='Modern.TLabel').pack(anchor='w')
        start_entry = ttk.Entry(start_frame, textvariable=self.start_year_var,
                               style='Modern.TEntry', font=('Segoe UI', 10), width=15)
        start_entry.pack(fill=tk.X, pady=(5, 0))
        
        end_frame = tk.Frame(year_frame, bg=self.colors['bg_light'])
        end_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        
        ttk.Label(end_frame, text="📅 End Year:", style='Modern.TLabel').pack(anchor='w')
        end_entry = ttk.Entry(end_frame, textvariable=self.end_year_var,
                             style='Modern.TEntry', font=('Segoe UI', 10), width=15)
        end_entry.pack(fill=tk.X, pady=(5, 0))
        
        # Action Buttons
        button_frame = tk.Frame(main_frame, bg=self.colors['bg_light'])
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.create_btn = ttk.Button(button_frame, text="🚀 Create Folder Structure", 
                                    command=self.run_creation, style='Success.TButton')
        self.create_btn.pack(side=tk.LEFT, padx=(0, 10), ipadx=20, ipady=8)
        
        clear_btn = ttk.Button(button_frame, text="🗑️ Clear Output", 
                              command=self.clear_output, style='Warning.TButton')
        clear_btn.pack(side=tk.LEFT, ipadx=10, ipady=5)
        
        # Progress Bar
        self.progress = ttk.Progressbar(button_frame, mode='indeterminate', length=200)
        self.progress.pack(side=tk.RIGHT)
        
        # Output Section
        output_frame = tk.LabelFrame(main_frame, text="📋 Creation Log", font=('Segoe UI', 12, 'bold'),
                                    fg=self.colors['primary'], bg=self.colors['bg_light'], padx=20, pady=15)
        output_frame.pack(fill=tk.BOTH, expand=True)
        
        # Text widget with scrollbar
        text_frame = tk.Frame(output_frame, bg=self.colors['bg_light'])
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        self.output_text = tk.Text(text_frame, height=15, font=('Consolas', 10),
                                  bg=self.colors['bg_dark'], fg=self.colors['text_light'],
                                  insertbackground=self.colors['text_light'], relief='flat',
                                  padx=15, pady=15)
        
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure text tags for colors
        self.output_text.tag_configure("success", foreground="#4CAF50", font=('Consolas', 10, 'bold'))
        self.output_text.tag_configure("error", foreground="#f44336", font=('Consolas', 10, 'bold'))
        self.output_text.tag_configure("warning", foreground="#ff9800", font=('Consolas', 10, 'bold'))
        self.output_text.tag_configure("info", foreground="#2196F3", font=('Consolas', 10, 'bold'))
        self.output_text.tag_configure("folder", foreground="#FFA726")
        self.output_text.tag_configure("year", foreground="#4FC3F7")
        self.output_text.tag_configure("month", foreground="#81C784")
        
        # Welcome message
        self.log_message("🎉 Welcome to Modern Folder Structure Creator!", "success")
        self.log_message("Fill in the form above and click 'Create Folder Structure' to begin.", "info")
        self.log_message("=" * 60, "info")
        
    def browse_path(self):
        path = filedialog.askdirectory(title="Select Base Directory")
        if path:
            self.base_path_var.set(path)
            self.log_message(f"📂 Base directory selected: {path}", "info")
    
    def log_message(self, message, tag=""):
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        self.output_text.insert(tk.END, full_message, tag)
        self.output_text.see(tk.END)
        self.root.update_idletasks()
        
    def clear_output(self):
        self.output_text.delete(1.0, tk.END)
        self.log_message("🧹 Output cleared!", "warning")
        
    def validate_inputs(self):
        base_path = self.base_path_var.get().strip()
        main_folder = self.folder_name_var.get().strip()
        
        if not base_path:
            self.log_message("❌ Please select a base directory!", "error")
            return False
            
        if not main_folder:
            self.log_message("❌ Please enter a main folder name!", "error")
            return False
            
        if not os.path.exists(base_path):
            self.log_message("❌ Selected base directory does not exist!", "error")
            return False
            
        try:
            start_year = int(self.start_year_var.get())
            end_year = int(self.end_year_var.get())
        except ValueError:
            self.log_message("❌ Start and End year must be valid numbers!", "error")
            return False
            
        if start_year > end_year:
            self.log_message("❌ Start year must be less than or equal to end year!", "error")
            return False
            
        if end_year - start_year > 50:
            self.log_message("❌ Maximum 50 years allowed to prevent excessive folders!", "error")
            return False
            
        return True
        
    def create_folders_threaded(self, base_path, main_folder, start_year, end_year):
        try:
            # Create main folder
            main_path = os.path.join(base_path, main_folder)
            os.makedirs(main_path, exist_ok=True)
            self.log_message(f"📂 Created main folder: {main_path}", "folder")
            
            total_folders = 1
            created_folders = 1
            total_years = end_year - start_year + 1
            total_expected = 1 + total_years + (total_years * 12)  # Main + years + months
            
            # Create year and month folders
            for year in range(start_year, end_year + 1):
                year_path = os.path.join(main_path, str(year))
                os.makedirs(year_path, exist_ok=True)
                created_folders += 1
                self.log_message(f"   📂 Created year folder: {year}", "year")
                
                for month in self.months:
                    month_path = os.path.join(year_path, month)
                    os.makedirs(month_path, exist_ok=True)
                    created_folders += 1
                    self.log_message(f"      └── 📁 {month}", "month")
                    time.sleep(0.01)  # Small delay for visual effect
                    
            self.log_message("=" * 60, "info")
            self.log_message(f"✅ SUCCESS! Created {created_folders} folders total!", "success")
            self.log_message(f"📊 Structure created in: {main_path}", "success")
            self.log_message("🎉 All done! You can now organize your files.", "success")
            
            # Show success dialog
            self.root.after(100, lambda: messagebox.showinfo(
                "🎉 Success!", 
                f"Folder structure created successfully!\n\nTotal folders: {created_folders}\nLocation: {main_path}",
                icon='info'
            ))
            
        except Exception as e:
            error_msg = f"❌ Error occurred: {str(e)}"
            self.log_message(error_msg, "error")
            self.root.after(100, lambda: messagebox.showerror("Error", error_msg))
        finally:
            # Stop progress bar and re-enable button
            self.root.after(100, self.creation_finished)
            
    def creation_finished(self):
        self.progress.stop()
        self.create_btn.configure(text="🚀 Create Folder Structure", state='normal')
        
    def run_creation(self):
        if not self.validate_inputs():
            return
            
        base_path = self.base_path_var.get().strip()
        main_folder = self.folder_name_var.get().strip()
        start_year = int(self.start_year_var.get())
        end_year = int(self.end_year_var.get())
        
        self.log_message("🚀 Starting folder creation process...", "info")
        self.log_message(f"📍 Base Path: {base_path}", "info")
        self.log_message(f"📁 Main Folder: {main_folder}", "info")
        self.log_message(f"📅 Year Range: {start_year} - {end_year}", "info")
        self.log_message("=" * 60, "info")
        
        # Start progress bar and disable button
        self.progress.start()
        self.create_btn.configure(text="⏳ Creating...", state='disabled')
        
        # Run folder creation in separate thread
        thread = threading.Thread(
            target=self.create_folders_threaded,
            args=(base_path, main_folder, start_year, end_year)
        )
        thread.daemon = True
        thread.start()

def main():
    root = tk.Tk()
    app = ModernFolderCreator(root)
    
    # Center window on screen
    root.eval('tk::PlaceWindow . center')
    
    # Add icon if available (optional)
    try:
        root.iconbitmap('')  # You can add an .ico file path here
    except:
        pass
        
    root.mainloop()

if __name__ == "__main__":
    main()