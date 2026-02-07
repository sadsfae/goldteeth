import os
import queue
import re
import signal
import shutil
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk


class GoldTeethGUI:
    def __init__(self, root):
        self.load_env_vars()

        self.root = root
        self.root.title("goldteeth GUI")
        # Reduced width since we removed the 3rd column
        self.root.geometry("600x650")

        self.process = None
        self.running = False
        self.log_queue = queue.Queue()
        self.dark_mode = True

        self.create_widgets()
        self.apply_theme()
        self.check_queue()

    def load_env_vars(self):
        """
        Manually source ~/.bashrc and update os.environ.
        Strictly looks for: FINNHUB_API_KEY, COINGECKO_API_KEY,
        and COINGECKO_PRO_API_KEY.
        """
        bashrc_path = os.path.expanduser("~/.bashrc")
        if not os.path.exists(bashrc_path):
            return

        target_keys = {
            "FINNHUB_API_KEY",
            "COINGECKO_API_KEY",
            "COINGECKO_PRO_API_KEY"
        }

        cmd = (
            f"PS1='ignore' source {bashrc_path} >/dev/null 2>&1 && env"
        )

        try:
            result = subprocess.run(
                ['bash', '-c', cmd],
                capture_output=True,
                text=True
            )

            for line in result.stdout.splitlines():
                if '=' in line:
                    key, value = line.split('=', 1)
                    if key in target_keys:
                        os.environ[key] = value

        except Exception as e:
            print(
                f"Warning: Failed to load env from .bashrc: {e}",
                file=sys.stderr
            )

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(
            row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S)
        )
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Middle column (1) expands to fill space
        self.main_frame.columnconfigure(1, weight=1)

        # --- Asset Row (Row 0) ---
        ttk.Label(
            self.main_frame, text="Asset (e.g., BTC, ETH, TSLA):"
        ).grid(row=0, column=0, sticky=tk.W)

        self.asset_var = tk.StringVar(value="BTC")
        ttk.Entry(
            self.main_frame, textvariable=self.asset_var, width=30
        ).grid(row=0, column=1, pady=5, sticky="ew")

        # --- Theme Button (Row 1) ---
        # Placed under the Asset entry, aligned right
        self.theme_btn = ttk.Button(
            self.main_frame, text="Theme", command=self.toggle_theme
        )
        self.theme_btn.grid(row=1, column=1, pady=(0, 10), sticky=tk.E)

        # --- Mode Rows (Rows 2-4) ---
        ttk.Label(self.main_frame, text="Mode:").grid(
            row=2, column=0, sticky=tk.W
        )
        self.mode_var = tk.StringVar(value="above")

        ttk.Radiobutton(
            self.main_frame,
            text="Above",
            variable=self.mode_var,
            value="above",
        ).grid(row=2, column=1, sticky=tk.W)

        ttk.Radiobutton(
            self.main_frame,
            text="Below",
            variable=self.mode_var,
            value="below",
        ).grid(row=3, column=1, sticky=tk.W)

        ttk.Radiobutton(
            self.main_frame,
            text="Volatility",
            variable=self.mode_var,
            value="vol",
        ).grid(row=4, column=1, sticky=tk.W)

        # --- Target Row (Row 5) ---
        ttk.Label(
            self.main_frame, text="Target (price or pct-mins):"
        ).grid(row=5, column=0, sticky=tk.W)

        self.target_var = tk.StringVar(value="100000")
        ttk.Entry(
            self.main_frame, textvariable=self.target_var, width=30
        ).grid(row=5, column=1, pady=5, sticky="ew")

        # --- Audio File Row (Row 6) ---
        ttk.Label(self.main_frame, text="Alert WAV file:").grid(
            row=6, column=0, sticky=tk.W
        )

        default_wav = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "goldteeth",
            "alert.wav",
        )
        if not os.path.exists(default_wav):
            default_wav = "alert.wav"

        self.wav_var = tk.StringVar(value=default_wav)
        ttk.Entry(
            self.main_frame, textvariable=self.wav_var, width=30
        ).grid(row=6, column=1, sticky="ew")

        # --- Browse Button (Row 7) ---
        # Placed under the WAV entry, aligned right
        ttk.Button(
            self.main_frame, text="Browse", command=self.browse_wav
        ).grid(row=7, column=1, pady=(0, 10), sticky=tk.E)

        # --- Unified Toggle Button (Row 8) ---
        self.toggle_btn = ttk.Button(
            self.main_frame,
            text="Start Monitoring",
            command=self.toggle_monitoring,
        )
        self.toggle_btn.grid(row=8, column=0, columnspan=2, pady=10)

        # --- Console Output (Row 9) ---
        self.console = scrolledtext.ScrolledText(
            self.main_frame, height=15, state="disabled"
        )
        self.console.grid(
            row=9,
            column=0,
            columnspan=2,  # Spans the 2 columns
            pady=10,
            sticky=(tk.W, tk.E, tk.N, tk.S),
        )
        self.main_frame.rowconfigure(9, weight=1)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        style = ttk.Style()
        style.theme_use("clam")

        if self.dark_mode:
            bg_color = "#2b2b2b"
            fg_color = "#ffffff"
            entry_bg = "#3c3f41"
            button_bg = "#454545"
            button_active = "#5c5c5c"
            console_bg = "#1e1e1e"
            console_fg = "#00ff00"
            select_bg = "#404040"
        else:
            bg_color = "#f0f0f0"
            fg_color = "#000000"
            entry_bg = "#ffffff"
            button_bg = "#e1e1e1"
            button_active = "#c7c7c7"
            console_bg = "#ffffff"
            console_fg = "#000000"
            select_bg = "#b4d5fe"

        self.root.configure(bg=bg_color)

        style.configure(".", background=bg_color, foreground=fg_color)
        style.configure(
            "TLabel", background=bg_color, foreground=fg_color
        )
        style.configure("TFrame", background=bg_color)

        style.configure(
            "TButton",
            background=button_bg,
            foreground=fg_color,
            borderwidth=1,
            focuscolor="none",
        )
        style.map(
            "TButton",
            background=[("active", button_active)],
            foreground=[("active", fg_color)],
        )

        style.configure(
            "TEntry",
            fieldbackground=entry_bg,
            foreground=fg_color,
            insertcolor=fg_color,
        )

        style.configure(
            "TRadiobutton",
            background=bg_color,
            foreground=fg_color,
            indicatorcolor=entry_bg,
        )
        style.map(
            "TRadiobutton",
            background=[("active", bg_color)],
            foreground=[("active", fg_color)],
            indicatorcolor=[
                ("selected", "#007acc"),
                ("pressed", "#005c99")
            ],
        )

        self.console.configure(
            bg=console_bg,
            fg=console_fg,
            insertbackground=fg_color,
            selectbackground=select_bg,
            selectforeground=fg_color,
        )

    def browse_wav(self):
        filename = filedialog.askopenfilename(
            filetypes=[("WAV files", "*.wav")]
        )
        if filename:
            self.wav_var.set(filename)

    def strip_ansi(self, text):
        ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
        return ansi_escape.sub("", text)

    def send_notification(self, title, message):
        if shutil.which("notify-send"):
            try:
                subprocess.Popen(["notify-send", title, message])
            except Exception:
                pass

    def check_queue(self):
        try:
            while True:
                message = self.log_queue.get_nowait()
                clean_message = self.strip_ansi(message)

                if "!!!" in clean_message:
                    self.send_notification(
                        "Gold Teeth Alert", clean_message
                    )

                self.console.config(state="normal")
                self.console.insert(tk.END, clean_message + "\n")
                self.console.see(tk.END)
                self.console.config(state="disabled")
        except queue.Empty:
            pass
        self.root.after(100, self.check_queue)

    def toggle_monitoring(self):
        """Unified handler for the single button."""
        if self.running:
            self.stop_monitoring()
        else:
            self.start_monitoring()

    def start_monitoring(self):
        asset = self.asset_var.get().upper()
        mode = self.mode_var.get()
        target_str = self.target_var.get()
        wav = self.wav_var.get()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, "goldteeth_cli.py")

        if not os.path.exists(script_path):
            messagebox.showerror(
                "Error", f"Script not found: {script_path}"
            )
            return

        if not os.path.isfile(wav):
            messagebox.showerror("Error", f"WAV not found: {wav}")
            return

        args = [asset, mode, target_str, wav]

        self.running = True
        self.toggle_btn.config(text="Stop Monitoring")  # Update Text

        thread = threading.Thread(
            target=self.run_script,
            args=(script_path, args),
            daemon=True
        )
        thread.start()
        self.log_queue.put("Monitoring started...")

    def run_script(self, script_path, args):
        cmd = [sys.executable, "-u", script_path] + args
        try:
            if os.name == "posix":
                proc = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    preexec_fn=os.setsid,
                )
            else:
                proc = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                )
            self.process = proc

            for line in proc.stdout:
                self.log_queue.put(line.strip())

            proc.stdout.close()
            return_code = proc.wait()

            if self.running:
                self.log_queue.put(
                    f"Process finished with code {return_code}"
                )

        except Exception as e:
            self.log_queue.put(f"Error executing process: {e}")
        finally:
            # Revert state on finish/crash
            self.running = False
            self.process = None
            # Schedule button update on main thread
            self.root.after(
                0, lambda: self.toggle_btn.config(text="Start Monitoring")
            )

    def stop_monitoring(self):
        if self.process and self.running:
            try:
                if os.name == "posix":
                    os.killpg(
                        os.getpgid(self.process.pid), signal.SIGTERM
                    )
                else:
                    self.process.terminate()
            except ProcessLookupError:
                pass
            self.log_queue.put("Stopping...")
            # Revert button text immediately
            self.toggle_btn.config(text="Start Monitoring")
        else:
            self.log_queue.put("Nothing to stop.")


if __name__ == "__main__":
    root = tk.Tk()
    app = GoldTeethGUI(root)
    root.mainloop()
