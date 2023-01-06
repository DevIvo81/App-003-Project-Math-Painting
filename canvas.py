import numpy as np
import os
from PIL import Image

os.system("cls")


class Canvas:
    def __init__(self, width=1280, height=768, color="black"):
        self.color = color
        self.width = width
        self.height = height

        # Create 3D numpy array of zeros,
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        # Change [0, 0, 0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, mode="RGB")
        img.save(imagepath)
