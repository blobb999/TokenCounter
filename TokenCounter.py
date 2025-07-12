import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import tiktoken  # pip install tiktoken
import os

class TokenCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Projekt-Token-Zähler")
        self.root.geometry("600x400")
        
        # Encoding-Modell (für GPT-4, anpassbar)
        self.encoding = tiktoken.get_encoding("cl100k_base")
        
        # GUI-Elemente
        self.setup_ui()
    
    def setup_ui(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="Einzelne Datei auswählen", command=self.select_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Ordner auswählen (rekursiv)", command=self.select_folder).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Mehrere Dateien auswählen", command=self.select_multiple_files).pack(side=tk.LEFT, padx=5)
        
        # Ergebnis-Textfeld
        self.result_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, height=15)
        self.result_text.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Status
        self.status_label = ttk.Label(frame, text="Bereit")
        self.status_label.pack(anchor=tk.W)
    
    def count_tokens_in_file(self, file_path):
        """Zählt Tokens in einer Datei."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            tokens = len(self.encoding.encode(content))
            return tokens
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Lesen von {file_path}: {str(e)}")
            return 0
    
    def process_files(self, paths):
        """Verarbeitet Dateien/Ordner und zählt Tokens."""
        self.result_text.delete(1.0, tk.END)
        total_tokens = 0
        file_count = 0
        
        for path in paths:
            if os.path.isfile(path):
                tokens = self.count_tokens_in_file(path)
                total_tokens += tokens
                file_count += 1
                self.result_text.insert(tk.END, f"{path}: {tokens} Tokens\n")
            elif os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        if file.endswith(('.py', '.txt', '.md')):  # Anpassbar: Nur Python/Text-Dateien
                            file_path = os.path.join(root, file)
                            tokens = self.count_tokens_in_file(file_path)
                            total_tokens += tokens
                            file_count += 1
                            self.result_text.insert(tk.END, f"{file_path}: {tokens} Tokens\n")
        
        self.result_text.insert(tk.END, f"\nGesamt: {total_tokens} Tokens in {file_count} Dateien\n")
        self.status_label.config(text=f"Fertig: {total_tokens} Tokens")
    
    def select_file(self):
        path = filedialog.askopenfilename(title="Datei auswählen", filetypes=[("Python-Dateien", "*.py"), ("Alle Dateien", "*.*")])
        if path:
            self.process_files([path])
    
    def select_folder(self):
        path = filedialog.askdirectory(title="Ordner auswählen")
        if path:
            self.process_files([path])
    
    def select_multiple_files(self):
        paths = filedialog.askopenfilenames(title="Mehrere Dateien auswählen", filetypes=[("Python-Dateien", "*.py"), ("Alle Dateien", "*.*")])
        if paths:
            self.process_files(paths)

if __name__ == "__main__":
    root = tk.Tk()
    app = TokenCounterApp(root)
    root.mainloop()
