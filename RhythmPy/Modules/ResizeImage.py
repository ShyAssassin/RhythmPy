from PIL import Image

# used for resizing images for tkinter
def ResizeImage(Xsize, Ysize, image):
    image = Image.open(image)
    image.convert("LA")
    new_image = image.resize((Xsize, Ysize), Image.ANTIALIAS)
    # cant use this here
    # _tkinter.TclError: image "2284364432192ResizeImage" doesn't exist
    # Resized_Image = ImageTk.PhotoImage(new_image)
    return new_image
