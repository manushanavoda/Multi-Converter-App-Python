import customtkinter as ctk
from tkinter import messagebox

# මෘදුකාංගයේ තේමාව (Theme) සැකසීම
ctk.set_appearance_mode("System")  # "Dark" හෝ "Light" ලෙසද දිය හැක
ctk.set_default_color_theme("blue")

class ConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Modern Multi-Converter Pro")
        self.geometry("500x650")

        # මාතෘකාව
        self.label_title = ctk.CTkLabel(self, text="All-in-One Converter", font=("Roboto", 24, "bold"))
        self.label_title.pack(pady=20)

        # වර්ගය තෝරන්න (Dropdown)
        self.option_type = ctk.CTkOptionMenu(self, values=["Distance (Km/M)", "Weight (Kg/G)", "Temp (C/F)"], width=250)
        self.option_type.pack(pady=10)

        # Radio Buttons සඳහා Frame එකක්
        self.radio_var = ctk.IntVar(value=1)
        self.radio_1 = ctk.CTkRadioButton(self, text="Option 1 (Km->M / Kg->G / C->F)", variable=self.radio_var, value=1)
        self.radio_1.pack(pady=5)
        self.radio_2 = ctk.CTkRadioButton(self, text="Option 2 (M->Km / G->Kg / F->C)", variable=self.radio_var, value=2)
        self.radio_2.pack(pady=5)

        # අගය ඇතුළත් කරන පෙට්ටිය
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter the value", width=250, height=40, font=("Roboto", 16))
        self.entry.pack(pady=20)

        # බොත්තම්
        self.btn_convert = ctk.CTkButton(self, text="Calculate", command=self.convert, font=("Roboto", 14, "bold"), height=40)
        self.btn_convert.pack(pady=5)

        self.btn_clear = ctk.CTkButton(self, text="Erase", command=self.clear, fg_color="transparent", border_width=2)
        self.btn_clear.pack(pady=5)

        # පිළිතුර පෙන්වන ස්ථානය
        self.label_result = ctk.CTkLabel(self, text="Result: --", font=("Roboto", 22, "bold"), text_color="#2ecc71")
        self.label_result.pack(pady=20)

        # History
        self.history_box = ctk.CTkTextbox(self, width=400, height=150)
        self.history_box.pack(pady=10)
        self.history_box.insert("0.0", "--- History ---\n")

    def convert(self):
        try:
            val = float(self.entry.get())
            choice = self.option_type.get()
            res, unit = 0, ""

            if "Distance" in choice:
                res = val * 1000 if self.radio_var.get() == 1 else val / 1000
                unit = "m" if self.radio_var.get() == 1 else "km"
            elif "Weight" in choice:
                res = val * 1000 if self.radio_var.get() == 1 else val / 1000
                unit = "g" if self.radio_var.get() == 1 else "kg"
            elif "Temp" in choice:
                res = (val * 9/5) + 32 if self.radio_var.get() == 1 else (val - 32) * 5/9
                unit = "°F" if self.radio_var.get() == 1 else "°C"

            result_str = f"{round(res, 2)} {unit}"
            self.label_result.configure(text=f"Result: {result_str}")
            self.history_box.insert("2.0", f"{val} -> {result_str}\n")
        except:
            messagebox.showerror("Error", "Enter the correct value.")

    def clear(self):
        self.entry.delete(0, 'end')
        self.label_result.configure(text="Result: --")

if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()