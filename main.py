import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from filters import filters_dict

def load_image():
    global original_image, photo_image, filtered_image, blended_image
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg *.jpeg *.png *.bmp')])
    if file_path:
        original_image = Image.open(file_path).convert('RGB')
        photo_image = ImageTk.PhotoImage(original_image)
        image_label.config(image=photo_image)
        filtered_image = original_image.copy()
        blended_image = original_image.copy()
        apply_button.config(state=tk.NORMAL)
        save_button.config(state=tk.NORMAL)
        reset_button.config(state=tk.NORMAL)

def save_image():
    global blended_image
    if blended_image:
        file_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[('JPEG', '*.jpg'), ('PNG', '*.png'), ('BMP', '*.bmp')])
        if file_path:
            blended_image.save(file_path)
    else:
        messagebox.showwarning('Warning', 'No image to save.')

def apply_filter():
    global filtered_image, blended_image, photo_image
    filter_matrix = [[0 for _ in range(3)] for _ in range(3)]
    try:
        for i in range(3):
            for j in range(3):
                value = custom_entries[i][j].get()
                if value == '':
                    value = '0'
                filter_matrix[i][j] = float(value)
    except ValueError:
        messagebox.showerror('Error', 'Invalid filter values. Please enter numerical values.')
        return

    # Отображение сообщения "Обработка..."
    processing_label.config(text="Обработка...")
    root.update()

    filtered_image = apply_image_filter(original_image, filter_matrix)
    update_blended_image()
    photo_image = ImageTk.PhotoImage(blended_image)
    image_label.config(image=photo_image)

    # Скрытие сообщения "Обработка..."
    processing_label.config(text="")

def update_blended_image():
    global blended_image, photo_image
    alpha = float(blending_entry.get()) / 100.0
    blended_image = Image.blend(original_image, filtered_image, alpha=alpha)
    photo_image = ImageTk.PhotoImage(blended_image)
    image_label.config(image=photo_image)

def apply_image_filter(image, filter_matrix):
    width, height = image.size
    filtered_img = Image.new('RGB', (width, height))
    pixels = image.load()
    new_pixels = filtered_img.load()

    for x in range(width):
        for y in range(height):
            red, green, blue = 0, 0, 0
            for filter_x in range(-1, 2):
                for filter_y in range(-1, 2):
                    neighbor_x = x + filter_x
                    neighbor_y = y + filter_y
                    if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
                        r, g, b = pixels[neighbor_x, neighbor_y]
                    else:
                        r, g, b = 0, 0, 0
                    filter_value = filter_matrix[filter_x + 1][filter_y + 1]
                    red += r * filter_value
                    green += g * filter_value
                    blue += b * filter_value
            red = int(min(max(red, 0), 255))
            green = int(min(max(green, 0), 255))
            blue = int(min(max(blue, 0), 255))
            new_pixels[x, y] = (red, green, blue)
    return filtered_img

def reset_to_original():
    global photo_image, blended_image
    blended_image = original_image.copy()
    photo_image = ImageTk.PhotoImage(blended_image)
    image_label.config(image=photo_image)

def update_filter_matrix(event):
    selected_filter = filter_var.get()
    if selected_filter in filters_dict:
        filter_matrix = filters_dict[selected_filter]
        for i in range(3):
            for j in range(3):
                custom_entries[i][j].delete(0, tk.END)
                custom_entries[i][j].insert(0, str(filter_matrix[i][j]))

# Initialize variables
original_image = None
filtered_image = None
blended_image = None
photo_image = None

# Create main window
root = tk.Tk()
root.title('Image Filter Application')

# Top frame for Load and Save buttons
top_frame = ttk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X)

load_button = ttk.Button(top_frame, text='Load Image', command=load_image)
save_button = ttk.Button(top_frame, text='Save Image', command=save_image)
reset_button = ttk.Button(top_frame, text='Reset to Original', command=reset_to_original, state=tk.DISABLED)

load_button.pack(side=tk.LEFT, padx=5, pady=5)
save_button.pack(side=tk.LEFT, padx=5, pady=5)
reset_button.pack(side=tk.LEFT, padx=5, pady=5)

# Filter selection and matrix
filter_frame = ttk.Frame(root)
filter_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

filter_var = tk.StringVar()
filter_dropdown = ttk.Combobox(filter_frame, textvariable=filter_var, values=list(filters_dict.keys()))
filter_dropdown.bind("<<ComboboxSelected>>", update_filter_matrix)
filter_dropdown.pack(side=tk.LEFT, padx=5, pady=5)

# Custom filter matrix
matrix_frame = ttk.Frame(root)
matrix_frame.pack(side=tk.TOP, padx=10, pady=5)

custom_entries = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        custom_entries[i][j] = ttk.Entry(matrix_frame, width=5)
        custom_entries[i][j].grid(row=i, column=j, padx=5, pady=5)

# Blending entry
blending_frame = ttk.Frame(root)
blending_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

blending_label = ttk.Label(blending_frame, text="Blending (%):")
blending_label.pack(side=tk.LEFT)

blending_entry = ttk.Entry(blending_frame, width=5)
blending_entry.insert(0, "100")
blending_entry.pack(side=tk.LEFT, padx=5)

# Apply button
apply_button = ttk.Button(root, text='Apply Filter', command=apply_filter, state=tk.DISABLED)
apply_button.pack(side=tk.TOP, pady=10)

# Processing label
processing_label = ttk.Label(root, text="", foreground="red")
processing_label.pack(side=tk.TOP, pady=5)

# Image display area
image_label = ttk.Label(root)
image_label.pack(side=tk.TOP, padx=10, pady=10)

root.mainloop()