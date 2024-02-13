# 🧍‍♂️  Singelton Design Pattern

## Introduction

The Singleton design pattern is a way to create a class that can only have one instance, and it offers a universal way to access that singular instance.

## 🚨 The Problem
The Singleton pattern addresses two issues simultaneously, although this goes against the Single Responsibility Principle:

Firstly, it ensures that a class can only have one instance. This is usually important for controlling access to shared resources like a database or a file. Imagine you create an object and then decide to make another; instead of getting a new one, you receive the original object you created. Achieving this is not possible through a regular constructor, as constructors are designed to always create a new object.

Secondly, the Singleton pattern offers a universal access point to this unique instance. It acts similarly to a global variable, allowing you to access the object from anywhere in your code. Unlike a global variable, however, a Singleton instance is protected from being overwritten, which enhances the safety of your application.

The pattern's popularity has led some to label any class that addresses even one of these issues as a "singleton." It's advantageous to centralize the solution for both issues in one class, especially if the rest of your application is already dependent on it.
## ✔️ The Solution
Every Singleton implementation generally follows these two essential steps:

1. Restrict the default constructor to private access, which prevents the creation of new instances of the Singleton class using the 'new' operator.

2. Implement a static method that serves as a substitute for the constructor. Internally, this method invokes the private constructor to create a unique instance and stores it in a static field. Any subsequent calls to this static method will return the pre-existing instance.

If your code can access the Singleton class, you can call its static method. Doing so will consistently return the same unique instance.
## 🚧 Structural Elements
The Singleton class includes a static method called 'getInstance,' which always returns the identical instance of the class it belongs to.

The constructor of the Singleton class should be inaccessible to external code. The 'getInstance' method should be the exclusive means for obtaining the Singleton object.

## Example
The operating system (OS) running on a computer can also exemplify the Singleton pattern. A computer typically runs a single instance of an operating system at any given time. Even if there are different processes and applications running simultaneously, they all interact with that one instance of the OS. The term "Operating System" in this context serves as a global point of access, allowing various software components to interact with system resources through a single, unique entity. Just like in a Singleton, this ensures that there's a coordinated, singular point for managing these resources.

## Implementation Guide
1. Introduce a private static field in the class to hold the unique singleton instance.

2. Create a public static method that serves as the means to obtain the singleton instance.

3. Within this static method, utilize "lazy initialization" to generate a new object only during its first invocation and store it in the static field. All following calls to this method should return this pre-existing instance.

4. Set the class constructor to private access. This allows only the class's static method to invoke the constructor, preventing other objects from doing so.

4. In the client code, replace all instances where the singleton's constructor is directly called with calls to the class's public static method for instance retrieval.
