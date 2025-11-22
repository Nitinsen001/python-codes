import tkinter as tk
from tkinter import messagebox

# ----------------- PicShare (Instagram-like UI, safe) with logo -----------------
def try_login(event=None):
    user = username_var.get().strip()
    pwd = password_var.get().strip()

    if not user or not pwd:
        messagebox.showwarning("Missing", "Please enter username and password.")
        return

    # SAFE: do NOT store or send credentials — just simulate a successful login
    messagebox.showinfo("Welcome", f"Hello {user}! (This is a UI-only demo.)")
    username_var.set("")
    password_var.set("")

# Window
root = tk.Tk()
root.title("PicShare — Sign In")
root.geometry("420x620")
root.resizable(False, False)

# Gradient background using Canvas
canvas = tk.Canvas(root, width=420, height=620, highlightthickness=0)
canvas.pack(fill="both", expand=True)
# simple vertical gradient
for i in range(620):
    r = 255 - int((i/620) * 70)
    g = 200 - int((i/620) * 60)
    b = 240 - int((i/620) * 80)
    canvas.create_line(0, i, 420, i, fill=f'#{r:02x}{g:02x}{b:02x}')

# Card (center)
card_w, card_h = 360, 520
card_x = (420 - card_w) // 2
card_y = 40
card = tk.Frame(root, bg="white", bd=0, highlightthickness=0)
card.place(x=card_x, y=card_y, width=card_w, height=card_h)

# Subtle shadow effect (behind card)
shadow = tk.Frame(root, bg="#c9c9c9")
shadow.place(x=card_x+6, y=card_y+8, width=card_w, height=card_h)
card.lift()

# ---------- Logo (Canvas-based) ----------
logo_canvas = tk.Canvas(card, width=140, height=100, bg="white", highlightthickness=0)
logo_canvas.pack(pady=(18, 2))

# draw rounded square (camera body)
x0, y0, x1, y1 = 10, 6, 130, 86
r = 18  # corner radius
# draw four arcs for rounded rectangle
logo_canvas.create_arc(x0, y0, x0+2*r, y0+2*r, start=90, extent=90, fill="#5a39a6", outline="#5a39a6")
logo_canvas.create_arc(x1-2*r, y0, x1, y0+2*r, start=0, extent=90, fill="#5a39a6", outline="#5a39a6")
logo_canvas.create_arc(x0, y1-2*r, x0+2*r, y1, start=180, extent=90, fill="#5a39a6", outline="#5a39a6")
logo_canvas.create_arc(x1-2*r, y1-2*r, x1, y1, start=270, extent=90, fill="#5a39a6", outline="#5a39a6")
# fill rectangles to complete rounded rect
logo_canvas.create_rectangle(x0+r/2, y0, x1-r/2, y1, fill="#5a39a6", outline="#5a39a6")
logo_canvas.create_rectangle(x0, y0+r/2, x1, y1-r/2, fill="#5a39a6", outline="#5a39a6")

# camera lens (outer)
logo_canvas.create_oval(44, 26, 96, 78, fill="#ffffff", outline="#ffffff")
# lens inner
logo_canvas.create_oval(54, 36, 86, 68, fill="#3b1f6b", outline="#3b1f6b")
# small flash rectangle
logo_canvas.create_rectangle(98, 16, 118, 36, fill="#ffb74d", outline="#ffb74d")
# small white dot to add shine
logo_canvas.create_oval(72, 44, 78, 50, fill="#ffffff", outline="#ffffff")

# App text next to or under logo (keep consistent)
title_lbl = tk.Label(card, text="PicShare", font=("Helvetica", 20, "bold"), bg="white", fg="#3b1f6b")
title_lbl.pack(pady=(4, 2))
subtitle = tk.Label(card, text="Share your moments", font=("Helvetica", 10), bg="white", fg="#666")
subtitle.pack(pady=(0, 10))

# divider
divider = tk.Frame(card, bg="#efefef", height=1)
divider.pack(fill="x", padx=20, pady=(6, 12))

# Large input style area
username_var = tk.StringVar()
password_var = tk.StringVar()

def make_label_entry(parent, label_text, text_var, ypad=6, show=None):
    lbl = tk.Label(parent, text=label_text, anchor="w", bg="white", fg="#333", font=("Arial", 10, "bold"))
    lbl.pack(fill="x", padx=28, pady=(0, 4))
    ent_bg = tk.Frame(parent, bg="#f3f3f3", bd=0)
    ent_bg.pack(fill="x", padx=24, pady=(0, ypad))
    ent = tk.Entry(ent_bg, textvariable=text_var, bd=0, font=("Arial", 14), relief="flat", show=show)
    ent.pack(ipady=10, ipadx=6, fill="x")
    return ent

u_entry = make_label_entry(card, "Username or email", username_var)
p_entry = make_label_entry(card, "Password", password_var, show="*")

# Bind Enter key to login
root.bind("<Return>", try_login)

# Forgot / helper
help_frame = tk.Frame(card, bg="white")
help_frame.pack(fill="x", padx=24, pady=(4, 8))
tk.Label(help_frame, text="Forgot password?", fg="#4a2fa6", bg="white", font=("Arial", 9, "underline")).pack(anchor="e")

# Big Login button
def on_enter(e):
    login_btn.config(bg="#3b1f6b")
def on_leave(e):
    login_btn.config(bg="#5a39a6")

login_btn = tk.Button(card, text="Log In", font=("Arial", 14, "bold"),
                      bg="#5a39a6", fg="white", bd=0, padx=10, pady=10,
                      activebackground="#3b1f6b", activeforeground="white", command=try_login, cursor="hand2")
login_btn.pack(fill="x", padx=24, pady=(12, 6))
login_btn.bind("<Enter>", on_enter); login_btn.bind("<Leave>", on_leave)

# OR divider with lines
or_frame = tk.Frame(card, bg="white")
or_frame.pack(fill="x", padx=24, pady=(6, 10))
tk.Frame(or_frame, bg="#ddd", height=1).pack(side="left", expand=True, padx=(0,10), pady=6)
tk.Label(or_frame, text="or", bg="white", fg="#999").pack(side="left")
tk.Frame(or_frame, bg="#ddd", height=1).pack(side="left", expand=True, padx=(10,0), pady=6)

# Social login buttons (dummy)
social_frame = tk.Frame(card, bg="white")
social_frame.pack(fill="x", padx=24)
fb_btn = tk.Button(social_frame, text="Continue with Connect", font=("Arial", 10, "bold"),
                   bg="#1877f2", fg="white", bd=0, pady=8, cursor="hand2")
fb_btn.pack(fill="x", pady=(0,6))

# Small signup hint
signup_frame = tk.Frame(root, bg=root["bg"])
signup_frame.place(x=card_x, y=card_y+card_h+6, width=card_w, height=40)
left = tk.Label(signup_frame, text="Don't have an account?", bg=root["bg"], fg="#111", font=("Arial", 10))
left.pack(side="left", padx=(14,6))
right = tk.Label(signup_frame, text="Sign up", bg=root["bg"], fg="#4a2fa6", font=("Arial", 10, "underline"), cursor="hand2")
right.pack(side="left")

# Footer small note
footer = tk.Label(root, text="PicShare demo — UI only. No data is stored.", bg=root["bg"], fg="#222", font=("Arial", 9))
footer.place(x=12, y=600)

# Focus first field
u_entry.focus_set()

root.mainloop()
