#  🎀  Decorator Pattern
## Introduction
The Decorator pattern is a structural design approach that enables the addition of new functionalities to objects by encapsulating them within special wrapper objects. These wrappers encompass the additional behaviors, allowing for dynamic enhancement of the object's capabilities.
## 🚨 The Problem
Consider a scenario where you are working on a text processing library. You have a basic text processor class that can perform fundamental operations like reading and writing text. Now, your users request additional functionalities, such as encryption and compression, to enhance the capabilities of the text processor.

Creating separate classes for each combination of these functionalities (e.g., EncryptedTextProcessor, CompressedTextProcessor) could lead to a proliferation of classes and increased complexity. Moreover, users might want to apply multiple functionalities to the text simultaneously.

```
                   +------------------------+
                   |   TextProcessor        |
                   |                        |
                   | - read()                |
                   | - write()               |
                   +------------------------+
                            /       \
                           /         \
                          /           \
 +------------------------+             +------------------------+
 |   EncryptionDecorator  |             | CompressionDecorator  |
 |                        |             |                        |
 | - read()               |             | - read()               |
 | - write()              |             | - write()              |
 | - encrypt()            |             | - compress()           |
 +------------------------+             +------------------------+
           |
           |
           v
+------------------------+
| EncryptedTextProcessor |
|                        |
| - read()               |
| - write()              |
| - encrypt()            |
+------------------------+

```
In this situation, the Decorator pattern can be employed. You can define decorator classes like EncryptionDecorator and CompressionDecorator, each responsible for adding a specific functionality. Users can then wrap their basic text processors with these decorators to combine functionalities dynamically. This approach facilitates the creation of various combinations without the need for an extensive class hierarchy.

The Decorator pattern allows you to extend the behavior of the text processor by stacking decorators in a flexible and reusable manner. Users can easily add or remove functionalities based on their requirements without modifying the core text processing classes.
## ✔️ The Solution
When dealing with the limitations of static inheritance, Aggregation or Composition provides more adaptable solutions. These alternatives involve one object referencing another, allowing for dynamic changes in behavior at runtime.

The Decorator pattern, or "Wrapper," illustrates this concept. A wrapper associates with a target object, sharing the same methods and delegating requests. The wrapper can modify results before or after passing requests to the target.

In the context of a text editor example, Decorators could enhance the basic text processing capabilities. Clients can stack decorators based on their requirements, creating a structured stack. The client interacts with the last decorator in the stack, which adheres to the same interface as the base text processor.

This approach extends to various functionalities, such as adding encryption, compression, or custom formatting options. Clients can decorate objects with custom decorators, maintaining a consistent interface.

## 🚧 Structural Elements
1. **Component**: The Component defines the shared interface for both the wrappers and the wrapped objects.
2. **Concrete Component**: The Concrete Component class represents the basic object that can be wrapped with additional functionalities.
3. **Base Decorator**: The Base Decorator class adheres to the component interface and maintains a reference to a wrapped object. It can be an abstract class or an interface.
4. **Concrete Decorator**: The Concrete Decorator class extends the base decorator, adding additional functionalities to the wrapped object.
5. **Client**: The Client class creates a decorated object by stacking various decorators on top of a base component.

## 📚🔨 Implementation Guide

1. **Model Representation:** 
Ensure your app's core model adopts a tree structure. Break it down into simple elements and containers. Remember, containers should be capable of holding both simple elements and other containers.
2. **Component Interface Declaration:**
Identify the methods common to both the core component and optional layers. Establish a component interface and declare these methods.
3. **Concrete Component Creation:**
Implement a concrete component class to define the fundamental behavior.
4. **Base Decorator Creation:**
Develop a base decorator class with a field for storing a reference to a wrapped object. The field should be declared with the component interface type, enabling the linking of both concrete components and decorators. The base decorator should delegate all work to the wrapped object.
5. **Concrete Decorator Creation:**
Derive concrete decorators by extending them from the base decorator. A concrete decorator should execute its behavior either before or after the call to the parent method, which consistently delegates to the wrapped object.
6**Client Code:**
Client code is responsible for creating decorators and arranging them according to the desired composition.

## 💡 Implementation Tips
Apply the Decorator pattern when you need to dynamically assign additional behaviors to objects without disrupting existing code.

Utilize the Decorator to organize your business logic into layers, creating a decorator for each layer and combining objects with various logic combinations at runtime. All these objects can be treated uniformly by client code, as they adhere to a common interface.

Employ the pattern when extending an object's behavior through inheritance is impractical or impossible.

In instances where a programming language restricts further extension of a class (e.g., using the "final" keyword), the Decorator pattern becomes valuable. In such cases, reusing existing behavior involves wrapping the class with a custom wrapper, applying the principles of the Decorator pattern.






