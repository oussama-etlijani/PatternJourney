from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent: str = "") -> str:
        pass


class File(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name

    def display(self, indent: str = "") -> str:
        return f"{indent}File: {self.name}\n"


class Directory(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        self.children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        self.children.remove(component)

    def display(self, indent: str = "") -> str:
        result = f"{indent}Directory: {self.name}\n"
        for child in self.children:
            result += child.display(indent + "  ")
        return result


if __name__ == "__main__":
    # Creating leaf objects (Files)
    file1 = File("Document1.txt")
    file2 = File("Image.jpg")
    file3 = File("Spreadsheet.xlsx")

    # Creating composite object (Directory)
    root_directory = Directory("Root")

    # Adding leaf objects to the composite
    root_directory.add(file1)
    root_directory.add(file2)

    # Creating a subdirectory
    subdirectory = Directory("Subfolder")
    subdirectory.add(file3)

    # Adding the subdirectory to the root directory
    root_directory.add(subdirectory)

    # Displaying the entire file system structure
    print("File System Structure:")
    print(root_directory.display())
