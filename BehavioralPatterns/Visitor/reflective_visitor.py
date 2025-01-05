#  Visitor Decorator and Implementation
def _qualname(obj):
    """
    Get the fully-qualified name of an object, including its module.
    This uniquely identifies the object's location in the code.

    Args:
        obj: The object to get the qualified name for.

    Returns:
        A string representing the fully qualified name (e.g., "module.ClassName").
    """
    return obj.__module__ + "." + obj.__qualname__


def _declaring_class(obj):
    """
    Get the name of the class that declared the object.
    This is useful for determining where a method is defined.

    Args:
        obj: The object (typically a method) to analyze.

    Returns:
        A string representing the name of the declaring class.
    """
    name = _qualname(obj)  # Get the fully qualified name
    print(name)
    return name[
        : name.rfind(".")
    ]  # Extract the class portion by truncating after the last '.'


# A global registry to store mappings between declaring classes, argument types, and visitor methods.
_methods = {}


def _visitor_impl(self, arg):
    """
    A general-purpose visitor implementation that dynamically resolves
    and invokes the correct visitor method based on the types of `self`
    and `arg`.

    Args:
        self: The visitor instance (e.g., ExpressionPrinter).
        arg: The element being visited (e.g., DoubleExpression or AdditionExpression).

    Returns:
        The result of invoking the appropriate visitor method.

    Raises:
        KeyError: If no matching visitor method is found for the given types.
    """
    # Lookup the appropriate visitor method based on the visitor's class and the argument's type.
    method = _methods[(_qualname(type(self)), type(arg))]
    # Call the resolved visitor method with the provided arguments.
    return method(self, arg)


def visitor(arg_type):
    """
    A decorator for registering visitor methods. This allows the dynamic
    association of a method with a specific argument type, enabling the
    Visitor design pattern.

    Args:
        arg_type: The type of element this visitor method should handle.

    Returns:
        A decorator function that registers the method and replaces it
        with the general `_visitor_impl`.
    """

    def decorator(fn):
        # Get the name of the class that declared the function
        declaring_class = _declaring_class(fn)
        # Register the method in the global `_methods` registry
        _methods[(declaring_class, arg_type)] = fn
        # Replace the decorated method with the general visitor implementation
        return _visitor_impl

    return decorator


# --------------------------------------------------------------------------
# Concret implementation of the visitor pattern
# File system elements


class FileSystemElement:
    """
    Base class for all file system elements.
    This class defines the interface for accepting visitors.
    """

    def accept(self, visitor):
        """
        Accept a visitor and allow it to process the current element.

        Args:
            visitor: The visitor object that processes this element.
        """
        visitor.visit(self)


class File(FileSystemElement):
    """
    Represents a single file in the file system.
    """

    def __init__(self, name, size, extension):
        """
        Initialize a File object with its name, size, and extension.

        Args:
            name (str): The name of the file.
            size (int): The size of the file in bytes.
            extension (str): The file's extension (e.g., '.txt', '.py').
        """
        self.name = name  # Name of the file
        self.size = size  # Size of the file in bytes
        self.extension = extension  # File extension


class Directory(FileSystemElement):
    """
    Represents a directory in the file system, which can contain files and/or other directories.
    """

    def __init__(self, name):
        """
        Initialize a Directory object with its name.

        Args:
            name (str): The name of the directory.
        """
        self.name = name  # Name of the directory
        self.children = []  # List to store child elements (files or subdirectories)

    def add(self, element):
        """
        Add a file or directory to this directory.

        Args:
            element (FileSystemElement): A file or subdirectory to add.
        """
        self.children.append(element)  # Add the element to the directory's children


# Visitor classes
class TreeGenerator:
    def __init__(self):
        self.result = []

    @visitor(File)
    def visit(self, file):
        self.result.append(f"- {file.name}")

    @visitor(Directory)
    def visit(self, directory):
        self.result.append(f"[{directory.name}]")
        for child in directory.children:
            child.accept(self)

    def __str__(self):
        return "\n".join(self.result)


class SizeCalculator:
    def __init__(self):
        self.total_size = 0

    @visitor(File)
    def visit(self, file):
        self.total_size += file.size

    @visitor(Directory)
    def visit(self, directory):
        for child in directory.children:
            child.accept(self)


class ExtensionFilter:
    def __init__(self, extension):
        self.extension = extension
        self.matched_files = []

    @visitor(File)
    def visit(self, file):
        if file.extension == self.extension:
            self.matched_files.append(file.name)

    @visitor(Directory)
    def visit(self, directory):
        for child in directory.children:
            child.accept(self)


if __name__ == "__main__":
    # Create a sample file system
    root = Directory("root")
    root.add(File("file1.txt", 100, ".txt"))
    root.add(File("file2.py", 200, ".py"))
    subdir = Directory("subdir")
    subdir.add(File("file3.txt", 150, ".txt"))
    subdir.add(File("file4.md", 50, ".md"))
    root.add(subdir)

    # 1. Generate tree structure
    print("File System Structure:")
    tree_generator = TreeGenerator()
    root.accept(tree_generator)
    print(tree_generator)

    # 2. Calculate total size
    print("\nTotal Size of All Files:")
    size_calculator = SizeCalculator()
    root.accept(size_calculator)
    print(f"Total Size: {size_calculator.total_size} bytes")

    # 3. Filter files by extension
    print("\nFiles with .txt Extension:")
    txt_filter = ExtensionFilter(".txt")
    root.accept(txt_filter)
    print("Matched Files:", txt_filter.matched_files)
