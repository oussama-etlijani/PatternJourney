from abc import ABC, abstractmethod


# Abstract base class defining the interface for Image
class Image(ABC):
    @abstractmethod
    def display(self):
        pass


# The real object that we want to proxy. It performs the actual image loading and displaying.
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()  # Load the image from disk upon initialization

    def load_image_from_disk(self):
        print(f"Loading image from {self.filename}")  # Simulate loading image from disk

    def display(self):
        print(f"Displaying {self.filename}")  # Simulate displaying the image


# The proxy class, which controls access to the RealImage object
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None  # RealImage is not created until it is needed

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(
                self.filename
            )  # Lazy initialization of RealImage
        self.real_image.display()  # Delegate the display method to the RealImage


if __name__ == "__main__":
    image1 = ProxyImage("photo1.jpg")
    image2 = ProxyImage("photo2.jpg")

    # Images will be loaded only when display is called for the first time
    image1.display()  # Loads and displays photo1.jpg
    image2.display()  # Loads and displays photo2.jpg
    image1.display()  # Only displays photo1.jpg, without loading again
