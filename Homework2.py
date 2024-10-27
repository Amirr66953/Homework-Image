from PIL import Image
import sys

def zoom_image(input_image_path, zoom_factor):
    with Image.open(input_image_path) as img:
        new_width = int(img.width * zoom_factor)
        new_height = int(img.height * zoom_factor)

        zoomed_img = img.resize((new_width, new_height), Image.LANCZOS)

        output_image_path = f"zoomed_{zoom_factor}x_{input_image_path.split('/')[-1]}"
        zoomed_img.save(output_image_path)
        
        print(f"Zoomed image saved as: {output_image_path}")

if __name__ == "__main__":
    try:
        input_image_path = input("Enter the path of the image: ")
        zoom_factor = float(input("Enter the zoom factor (e.g., 1.5 for 150%): "))

        if zoom_factor <= 0:
            print("Zoom factor must be greater than 0.")
            sys.exit(1)

        zoom_image(input_image_path, zoom_factor)

    except FileNotFoundError:
        print("The specified image file was not found. Please check the path and try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the zoom factor.")