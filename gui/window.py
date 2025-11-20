import tkinter as tk
from tkinter import ttk

# --------------------------
# FUNCIONES
# --------------------------
def rounded_rect(canvas, x1, y1, x2, y2, radius=45, **kwargs):
    """Dibuja un rectángulo con esquinas redondeadas en un canvas."""
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, splinesteps=36, **kwargs)

def update_slider_from_sound(pitch_value):
    """Actualiza la posición del slider basado en un valor de entrada."""
    x = ((pitch_value + 50) / 100) * 260 + 20
    x = min(max(x, 20), 280)
    slider_canvas.coords(slider_handle, x - 10, 8, x + 10, 28)

# --- FUNCIONES PARA LA BARRA DE TÍTULO PERSONALIZADA ---
def start_move(event):
    window._drag_start_x = event.x
    window._drag_start_y = event.y

def do_move(event):
    x = event.x_root - window._drag_start_x
    y = event.y_root - window._drag_start_y
    window.geometry(f"+{x}+{y}")

def close_window():
    window.destroy()

# ------------------------------
# VENTANA
# ------------------------------
window = tk.Tk()
window_width = 600
window_height = 500

# Obtener tamaño de pantalla y calcular posición central
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg="#1c1f3b")
window.update()  # Asegura que geometry funcione correctamente con overrideredirect
window.overrideredirect(True) 

# ------------------------------
# BARRA DE TÍTULO PERSONALIZADA
# ------------------------------
title_bar = tk.Frame(window, bg="#2a2f5a", relief="raised", bd=0, height=40)
title_bar.pack(fill="x")

title_label_custom = tk.Label(title_bar, text="Pitch2Score Tuner", bg="#2a2f5a", fg="white", font=("Calibri", 12))
title_label_custom.pack(side="left", padx=10)

# Botón de cerrar con efecto hover
close_button = tk.Button(
    title_bar, 
    text="✕", 
    bg="#2a2f5a", 
    fg="white", 
    activebackground="red", 
    activeforeground="white", 
    relief="flat", 
    bd=0, 
    font=("Calibri", 14), 
    command=close_window
)
close_button.pack(side="right", padx=10)

def on_enter(event):
    close_button.config(bg="red")

def on_leave(event):
    close_button.config(bg="#2a2f5a")

close_button.bind("<Enter>", on_enter)
close_button.bind("<Leave>", on_leave)

# Vincular eventos de ratón para mover la ventana
title_bar.bind("<ButtonPress-1>", start_move)
title_bar.bind("<B1-Motion>", do_move)
title_label_custom.bind("<ButtonPress-1>", start_move)
title_label_custom.bind("<B1-Motion>", do_move)

# ------------------------------
# CONTENIDO PRINCIPAL DE LA APP
# ------------------------------
main_content = tk.Frame(window, bg="#1c1f3b")
main_content.pack(expand=True, fill="both", pady=(10,0))

# CUADRADO REDONDEADO
canvas = tk.Canvas(main_content, width=220, height=220, bg="#1c1f3b", highlightthickness=0)
canvas.pack(pady=20)
rounded_rect(canvas, 20, 20, 200, 200, radius=60, fill="#2a2f5a", outline="#2a2f5a")

# Nota principal
note_label = tk.Label(canvas, text="A", font=("Calibri", 48, "bold"), bg="#2a2f5a", fg="white")
canvas.create_window(110, 110, window=note_label)

# Accidental
accidental_label = tk.Label(canvas, text="#", font=("Calibri", 24, "bold"), bg="#2a2f5a", fg="white")
canvas.create_window(135, 85, window=accidental_label)

# SLIDER
slider_frame = tk.Frame(main_content, bg="#1c1f3b", width=300, height=40)
slider_frame.pack(pady=20)

slider_canvas = tk.Canvas(slider_frame, width=300, height=40, bg="#1c1f3b", highlightthickness=0)
slider_canvas.pack()

slider_canvas.create_line(20, 18, 280, 18, width=6, fill="#2a2f5a", capstyle="round")

handle_x = 150
handle_y = 18
handle_radius = 10
slider_handle = slider_canvas.create_oval(
    handle_x - handle_radius, handle_y - handle_radius,
    handle_x + handle_radius, handle_y + handle_radius,
    fill="#4d5699",
    outline="#4d5699"
)

# ETIQUETA DE FRECUENCIA
style = ttk.Style()
style.configure("Dark.TLabel", background="#1c1f3b", foreground="white")
frequency_label = ttk.Label(main_content, text="440 Hz", font=("Calibri", 18, "bold"), style="Dark.TLabel")
frequency_label.pack(pady=10)

window.mainloop()
