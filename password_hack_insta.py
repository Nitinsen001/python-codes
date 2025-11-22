# import tkinter as tk

# root = tk.Tk()
# root.title("key")
# def display(event):
#     print(f"your password is : {event.char}",)
    
# root.bind("<Key>",display)
# root.mainloop()

import customtkinter as ctk
from tkinter import messagebox

# 1. मुख्य सेटिंग्स
ctk.set_appearance_mode("Dark")  # डार्क मोड थीम
ctk.set_default_color_theme("blue") # नीले रंग का थीम

class RegistrationForm(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # विंडो कॉन्फ़िगरेशन
        self.title("🔥 कट्टर नख रजिस्ट्रेशन फॉर्म 🔥")
        self.geometry("500x550")
        self.resizable(False, False) # विंडो का साइज़ फिक्स

        # 2. मेन फ्रेम (पूरे फॉर्म के लिए कंटेनर)
        # corner_radius=15 से गोल किनारे मिलेंगे
        self.main_frame = ctk.CTkFrame(self, width=400, height=500, corner_radius=15)
        self.main_frame.pack(pady=40, padx=40, fill="both", expand=True)

        # 3. फॉर्म टाइटल
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="नया अकाउंट बनाएँ", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=20)

        # 4. इनपुट फ़ील्ड्स

        # यूजरनेम
        self.username_entry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="यूजरनेम (4-12 अक्षर)", 
            width=300, 
            height=35,
            corner_radius=10
        )
        self.username_entry.pack(pady=10)

        # ईमेल
        self.email_entry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="ईमेल आईडी", 
            width=300, 
            height=35,
            corner_radius=10
        )
        self.email_entry.pack(pady=10)

        # पासवर्ड
        self.password_entry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="पासवर्ड", 
            show="*", 
            width=300, 
            height=35,
            corner_radius=10
        )
        self.password_entry.pack(pady=10)

        # पासवर्ड दोबारा डालें
        self.confirm_password_entry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="पासवर्ड कन्फर्म करें", 
            show="*", 
            width=300, 
            height=35,
            corner_radius=10
        )
        self.confirm_password_entry.pack(pady=10)
        
        # 5. चेकबॉक्स (शर्तें स्वीकार करें)
        self.terms_checkbox = ctk.CTkCheckBox(
            self.main_frame, 
            text="मैं सभी नियम और शर्तें स्वीकार करता हूँ",
            checkbox_height=20,
            checkbox_width=20
        )
        self.terms_checkbox.pack(pady=15)

        # 6. सबमिट बटन
        self.submit_button = ctk.CTkButton(
            self.main_frame, 
            text="रजिस्टर करें", 
            command=self.register_user, 
            width=200, 
            height=45,
            corner_radius=10,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.submit_button.pack(pady=20)

    # 7. बटन क्लिक होने पर यह फंक्शन चलेगा (Action on button click)
    def register_user(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        terms_accepted = self.terms_checkbox.get()

        # सिंपल वैलिडेशन (Validation)
        if not username or not email or not password or not confirm_password:
            messagebox.showerror("त्रुटि", "सभी फ़ील्ड भरना अनिवार्य है!")
            return

        if password != confirm_password:
            messagebox.showerror("त्रुटि", "पासवर्ड मेल नहीं खा रहे हैं।")
            return

        if not terms_accepted:
            messagebox.showerror("त्रुटि", "रजिस्टर करने के लिए नियम और शर्तें स्वीकार करें।")
            return
            
        # अगर सब सही है (Success Message)
        messagebox.showinfo(
            "सफलता", 
            f"Registration Successful!\nयूजर: {username}\nईमेल: {email}"
        )
        # आप यहां डेटाबेस में डेटा सेव करने का कोड जोड़ सकते हैं

# फॉर्म चलाएं
if __name__ == "__main__":
    app = RegistrationForm()
    app.mainloop()