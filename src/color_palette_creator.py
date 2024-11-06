import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from collections import Counter
import colorsys
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import sv_ttk
import os


def resize_image(image, width=600):
    aspect_ratio = float(image.shape[1]) / float(image.shape[0])
    height = int(width / aspect_ratio)
    return cv2.resize(image, (width, height))


def extract_dominant_colors(image, k=10):
    # Reshape image to be a list of pixels
    pixels = image.reshape((-1, 3))

    # Apply KMeans clustering to find dominant colors
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_
    labels = kmeans.labels_

    # Filter out colors that are mostly black or white
    filtered_colors = []
    for color in colors:
        if not (np.mean(color) < 30 or np.mean(color) > 225):
            filtered_colors.append(color)

    # Count each label frequency and keep only those in filtered colors
    counts = Counter(labels)
    sorted_colors = []
    for i in counts.keys():
        if any(np.array_equal(colors[i], fc) for fc in filtered_colors):
            sorted_colors.append(colors[i])

    return sorted_colors, labels

def group_bottom_colors(image, num_colors=10):
  # Reshape the image to pixels
    pixels = image.reshape((-1, 3))

    # Apply KMeans clustering to find bottom colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_

    # Filter out colors that are mostly black or white
    filtered_colors = []
    for color in colors:
        if not (np.mean(color) < 30 or np.mean(color) > 225):
            filtered_colors.append(color)

    return filtered_colors


def adjust_brightness(color, factor):
    return np.clip(color * factor, 0, 255)


def adjust_hue(color, angle):
    r, g, b = color / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    
    # Adjust the hue value
    h = (h + angle / 360.0) % 1
    
    # Convert back to RGB
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return np.array([r, g, b]) * 255


def plot_color_palette(colors, output_file='color_palette.png'):
    num_colors = len(colors)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis('off')

    color_height = 1.0 / num_colors

    # Plot the colors
    for i, color in enumerate(colors[::-1]):
        rect = Rectangle((0, 1 - (i + 1) * color_height), 1, color_height, facecolor=color / 255.0)
        ax.add_patch(rect)

    plt.savefig(output_file, bbox_inches='tight')
    plt.close(fig)


def plot_brightness_shifts(colors, output_file='brightness_shifts.png', brightness_factors=[0.5, 0.75, 1.25, 1.5]):
    num_colors = len(colors)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis('off')

    color_width = 1.0 / len(brightness_factors)
    color_height = 1.0 / num_colors

    # Plot brightness shifts
    for i, color in enumerate(colors[::-1]):
        for col, brightness in enumerate(brightness_factors):
            adjusted_color = adjust_brightness(color, brightness)
            rect = Rectangle(
                (col * color_width, 1 - (i + 1) * color_height),
                color_width,
                color_height,
                facecolor=adjusted_color / 255.0
            )
            ax.add_patch(rect)

    plt.savefig(output_file, bbox_inches='tight')
    plt.close(fig)

def plot_hue_shifts(colors, output_file='hue_shifts.png', hue_shifts=[0, 10, 20, 30]):
    num_colors = len(colors)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis('off')

    color_width = 1.0 / len(hue_shifts)
    color_height = 1.0 / num_colors

    # Plot hue shifts
    for i, color in enumerate(colors[::-1]):
        for col, hue_shift in enumerate(hue_shifts):
            adjusted_color = adjust_hue(color, hue_shift)
            rect = Rectangle(
                (col * color_width, 1 - (i + 1) * color_height),
                color_width,
                color_height,
                facecolor=adjusted_color / 255.0
            )
            ax.add_patch(rect)

    plt.savefig(output_file, bbox_inches='tight')
    plt.close(fig)


def combine_color_palettes(output_file='combined_palette.png', *input_files):
    images = [plt.imread(file) for file in input_files]
    resized_images = [cv2.resize(image, (1000, 1000)) for image in images]

    combined_image = np.vstack(resized_images)

    plt.imsave(output_file, combined_image)


def save_color_images(image, colors, labels, output_folder='color_samples', threshold_factor=0.1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create masks for each color and save the corresponding images
    for i, color in enumerate(colors):
        # Calculate dynamic color distance threshold based on color variation in the image
        mean_color_distance = np.mean([np.linalg.norm(pixel - color) for pixel in image.reshape(-1, 3)])
        threshold = threshold_factor * mean_color_distance

        # Calculate color distance to find approximate matches
        color_diff = np.linalg.norm(image - color, axis=-1)
        mask = color_diff < threshold
        extracted_image = np.zeros_like(image)
        extracted_image[mask] = image[mask]
        output_path = os.path.join(output_folder, f'color_sample_{i+1}.png')
        plt.imsave(output_path, extracted_image)

def save_top_color_samples(image, top_colors, labels, output_folder='color_samples_top_colors'):
    save_color_images(image, top_colors, labels, output_folder=output_folder)

def save_family_color_samples(image, family_colors, labels, output_folder='color_samples_family_colors'):
    save_color_images(image, family_colors, labels, output_folder=output_folder)



def create_color_palette():
    # Create a GUI window for selecting parameters
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: (root.quit(), root.destroy(), exit()))
    root.title("Color Palette Parameters")
    root.geometry("500x500")  # Hard set window size  # Adjusted window size to ensure visibility
    sv_ttk.set_theme("dark")

    # Variables to hold user input
    k_var = tk.IntVar(value=10)
    family_colors_var = tk.IntVar(value=10)
    brightness_var = tk.StringVar(value="0.5/0.75/1.25/1.5")
    hue_var = tk.StringVar(value="0/10/20/30")
    image_path = tk.StringVar(value="")
    output_folder = tk.StringVar(value="No folder selected")
    save_samples_var = tk.BooleanVar(value=False)

    # Function to handle image selection
    def select_image():
        path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if path:
            image_path.set(path)
            update_submit_button_state()

    # Function to handle output folder selection
    def select_output_folder():
        folder = filedialog.askdirectory(title="Select an Output Folder")
        if folder:
            output_folder.set(folder)
            update_submit_button_state()

    # Function to handle submission of parameters
    def update_submit_button_state():
      if image_path.get() != "" and output_folder.get() != "No folder selected":
          submit_button.config(state='normal', text='Submit ❤️')
          select_image_button.config(text="Image Selected")
          select_folder_button.config(text="Folder Selected")
      else:
          submit_button.config(state='disabled', text='Submit 💔')
          if image_path.get() == "":
              select_image_button.config(text="Select Image")
          else: 
              select_image_button.config(text="Image Selected")
          if output_folder.get() == "No folder selected":
              select_folder_button.config(text="Select Folder")
          else:
              select_folder_button.config(text="Folder Selected")

    def submit_parameters():
        try:
            # Validate inputs
            k = k_var.get()
            num_family_colors = family_colors_var.get()
            brightness_factors = [float(b) for b in brightness_var.get().split("/")]
            hue_shifts = [float(h) for h in hue_var.get().split("/")]

            if k <= 0 or num_family_colors <= 0:
                raise ValueError("Number of colors must be positive.")
            if not all(0.0 < bf <= 5.0 for bf in brightness_factors):
                raise ValueError("Brightness factors must be between 0 and 5.")
            if not all(0 <= hs < 360 for hs in hue_shifts):
                raise ValueError("Hue shifts must be between 0 and 360 degrees.")

            root.quit()
            root.destroy()
        except ValueError as e:
            tk.messagebox.showerror("Input Error", str(e))

    # Create labeled frames for different sections
    file_handling_frame = ttk.Labelframe(root, text="File Handling", padding=(10, 5), width=490)
    file_handling_frame.place(x=5, y=10, width=490)

    color_palette_frame = ttk.Labelframe(root, text="Color Palette Preparation", padding=(10, 5), width=490)
    color_palette_frame.place(x=5, y=160, width=490)

    factors_frame = ttk.Labelframe(root, text="Factors and Options", padding=(10, 5), width=490)
    factors_frame.place(x=5, y=310, width=490)

    ttk.Label(file_handling_frame, text="Select Input Image:").grid(row=0, column=0, sticky='w', padx=10, pady=5)
    select_image_button = ttk.Button(file_handling_frame, text="Select Image", command=select_image)
    select_image_button.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    

    ttk.Label(file_handling_frame, text="Select Output Folder:").grid(row=1, column=0, sticky='w', padx=10, pady=5)
    select_folder_button = ttk.Button(file_handling_frame, text="Select Folder", command=select_output_folder)
    select_folder_button.grid(row=1, column=1, padx=5, pady=5, sticky='w')

    ttk.Label(color_palette_frame, text="Number of Dominant Colors (Top Colors):").grid(row=0, column=0, sticky='w', padx=10, pady=5)
    k_entry_var = tk.IntVar(value=10)
    k_entry = ttk.Entry(color_palette_frame, textvariable=k_entry_var)
    k_entry.grid(row=0, column=2, padx=5, pady=5)
    k_entry_var.trace_add('write', lambda *args: k_slider.set(k_entry_var.get()))
    k_slider = ttk.Scale(color_palette_frame, variable=k_var, from_=1, to=100, orient='horizontal', command=lambda val: k_entry_var.set(int(float(val))))
    k_slider.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(color_palette_frame, text="Number of Family Colors:").grid(row=1, column=0, sticky='w', padx=10, pady=5)
    family_colors_entry_var = tk.IntVar(value=10)
    family_colors_entry = ttk.Entry(color_palette_frame, textvariable=family_colors_entry_var)
    family_colors_entry.grid(row=1, column=2, padx=5, pady=5)
    family_colors_entry_var.trace_add('write', lambda *args: family_colors_slider.set(family_colors_entry_var.get()))
    family_colors_slider = ttk.Scale(color_palette_frame, variable=family_colors_var, from_=1, to=100, orient='horizontal', command=lambda val: family_colors_entry_var.set(int(float(val))))
    family_colors_slider.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(factors_frame, text="Brightness Factors:").grid(row=0, column=0, sticky='w', padx=10, pady=5)
    ttk.Entry(factors_frame, textvariable=brightness_var).grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(factors_frame, text="Hue Shifts:").grid(row=1, column=0, sticky='w', padx=10, pady=5)
    ttk.Entry(factors_frame, textvariable=hue_var).grid(row=1, column=1, padx=5, pady=5)


    ttk.Checkbutton(file_handling_frame, text="Save color sample images", variable=save_samples_var).grid(row=2, column=0, columnspan=3, sticky='w', padx=10, pady=5)

    # Submit button
    submit_button = ttk.Button(root, text="Submit 💔", command=submit_parameters, state='disabled', width=40)
    submit_button.place(x=50, y=450, width=400)

    root.mainloop()

    # Get the user-provided parameters
    k = k_var.get()
    num_family_colors = family_colors_var.get()
    brightness_factors = [float(b) for b in brightness_var.get().split("/")]
    hue_shifts = [float(h) for h in hue_var.get().split("/")]
    save_samples = save_samples_var.get()

    # Output the chosen parameters to console
    print(f"Number of Dominant Colors: {k}")
    print(f"Number of Family Colors: {num_family_colors}")
    print(f"Brightness Factors: {brightness_factors}")
    print(f"Hue Shifts: {hue_shifts}")
    print(f"Save Color Samples: {save_samples}")

    # Load and resize the image
    if not image_path.get():
        print("No image file selected. Exiting.")
        return

    image = cv2.imread(image_path.get())
    if image is None:
        print("Error: Could not load image. Please check the file path and try again.")
        exit()
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = resize_image(image)

    # Extract top dominant colors
    top_colors, labels = extract_dominant_colors(image, k=k)

    # Group bottom colors
    family_colors = group_bottom_colors(image, num_colors=num_family_colors)

    # Set output folder path
    if not output_folder.get():
        print("No output folder selected. Using current directory.")
        output_folder_path = "./"
    else:
        output_folder_path = output_folder.get() + "/"

    # Create a color palette for the top colors
    plot_color_palette(top_colors, output_file=output_folder_path + 'top_color_palette.png')
    # Create brightness and hue shifts for top colors
    plot_brightness_shifts(top_colors, output_file=output_folder_path + 'top_brightness_shifts.png', brightness_factors=brightness_factors)
    plot_hue_shifts(top_colors, output_file=output_folder_path + 'top_hue_shifts.png', hue_shifts=hue_shifts)

    # Create a color palette for family colors
    plot_color_palette(family_colors, output_file=output_folder_path + 'family_color_palette.png')
    # Create brightness and hue shifts for family colors
    plot_brightness_shifts(family_colors, output_file=output_folder_path + 'family_brightness_shifts.png', brightness_factors=brightness_factors)
    plot_hue_shifts(family_colors, output_file=output_folder_path + 'family_hue_shifts.png', hue_shifts=hue_shifts)

    # Combine all three files into one
    combine_color_palettes(output_folder_path + 'combined_color_palettes.png',
                           output_folder_path + 'top_color_palette.png',
                           output_folder_path + 'top_brightness_shifts.png',
                           output_folder_path + 'top_hue_shifts.png',
                           output_folder_path + 'family_color_palette.png',
                           output_folder_path + 'family_brightness_shifts.png',
                           output_folder_path + 'family_hue_shifts.png')

    # Save individual color images showing original regions if enabled
    if save_samples:
        save_top_color_samples(image, top_colors, labels, output_folder=output_folder_path + 'top_color_samples')
        save_family_color_samples(image, family_colors, labels, output_folder=output_folder_path + 'family_color_samples')

    print("Color palettes and combined palette created successfully.")

# Required installations:
# pip3 install opencv-python
# pip3 install numpy
# pip3 install scikit-learn
# pip3 install matplotlib

# Example usage
create_color_palette()
