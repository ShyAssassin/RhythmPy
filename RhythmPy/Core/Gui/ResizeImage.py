from PIL import Image


def ResizeImage(Xsize, Ysize, image):
    """
    Used for resizing images for use in tkinter
    """
    image = Image.open(image)
    image.convert("LA")
    new_image = image.resize((Xsize, Ysize), Image.ANTIALIAS)
    # Resized_Image = ImageTk.PhotoImage(new_image)
    # _tkinter.TclError: image "2284364432192ResizeImage" doesn't exist
    # Resized_Image = ImageTk.PhotoImage(new_image)
    return new_image
