
# 🕊️ Command
## Introduction
The Command pattern is a behavioral design approach that converts a request into a self-contained object encapsulating all relevant information about the request. This conversion enables passing requests as method arguments, facilitating the postponement or queuing of request execution, and facilitating the implementation of undoable operations.

##  🚨 The Problem
Consider a scenario where you are developing a smart home automation system. Your system includes a control panel with buttons for different devices, such as lights, thermostats, and security cameras. Each button on the control panel represents a specific operation, like turning on/off a device or adjusting its settings.

Initially, you might create a versatile Button class to handle various types of buttons across the control panel. However, as your smart home system evolves, you encounter a similar challenge. Each button needs to perform distinct actions, and the code for handling button clicks becomes complex.

At first, you may resort to creating numerous subclasses for each type of button to encapsulate the specific behavior. Yet, this approach quickly proves problematic. The growing number of subclasses becomes unwieldy, and any modification to the base Button class risks affecting the functionality across these subclasses. Your code becomes tightly coupled, with changes in the business logic potentially disrupting the GUI code.

The challenge intensifies when certain operations, like activating a "Home" mode or adjusting temperature settings, need to be triggered from multiple sources. Users may initiate these actions using buttons on the control panel, voice commands, or through a mobile app. Duplicating the code for these operations in various classes or making one part of the system dependent on another becomes impractical and error-prone.

In this context, employing the Command pattern becomes essential. By transforming each operation into a command object, you can decouple the sender (e.g., buttons, voice commands) from the receiver (e.g., devices, system). This design pattern allows you to encapsulate requests, parameterize objects based on different actions, queue operations, and support undo functionality, providing a more flexible and maintainable solution for handling the diverse interactions within your smart home automation system.
## ✔️ The Solution
In addressing the complexities of our smart home automation system, the Command pattern emerges as a strategic solution, offering a structured approach to handling diverse user interactions and device operations. This pattern excels in promoting flexibility, maintainability, and decoupling within the system's design.

The smart home system encounters a challenge where various devices, each represented by a button on the control panel, necessitate distinct actions. Initially, a versatile Button class handles these operations, but the code becomes intricate and prone to issues as the system evolves. The Command pattern provides a systematic way to manage these interactions.

In this context, the Command pattern involves encapsulating each device operation as a command object. These command objects act as intermediaries between the user interface elements (such as buttons on the control panel) and the underlying business logic that controls the devices. Instead of directly triggering operations in the business logic layer, the GUI objects delegate this responsibility to command objects.

The benefits of employing the Command pattern become evident as it addresses the challenges faced in the smart home context:

**Decoupling:** The GUI objects no longer need detailed knowledge about the business logic objects or how operations are executed. They simply trigger the appropriate command, leaving the command to handle the intricacies of the request.

**Flexibility:** By ensuring that all command objects implement a common interface, the system becomes versatile. Different commands can be seamlessly interchanged without modifying the sender, allowing for dynamic changes in behavior at runtime.

**Maintainability:** With operations encapsulated in command objects, modifications or additions to functionalities become more manageable. Changes in business logic don't necessarily impact the GUI code, reducing the risk of unintended side effects.

**Undo and Redo:** The Command pattern lays the groundwork for implementing undoable operations. Each command object can store the necessary information to reverse its own operation, enabling a straightforward approach to undoing user actions.

**Scalability:** As the smart home system expands with new devices or features, the Command pattern facilitates the incorporation of new command objects without significant modifications to the existing codebase.## Structural Elements

## Example
Imagine you're at a busy car service center for routine maintenance on your vehicle. As you pull into the service bay, an attendant greets you and takes note of the services you require, such as an oil change, tire rotation, and brake inspection. Instead of immediately conveying this information to the mechanics, the attendant logs your service request on a digital system.

The service request acts as a command, analogous to the paper order in the restaurant scenario. It enters a queue, awaiting its turn for the mechanics to address it. The details of your service needs are encapsulated in the request, providing the mechanics with all the necessary information to start working on your vehicle efficiently. This approach avoids the mechanics having to interrupt the workflow to inquire about specific service details directly from you.

Once the request reaches the top of the queue, the mechanics retrieve it from the system. They review the services requested, ensuring they have a clear understanding of what needs to be done. With the information readily available, they proceed to perform the oil change, tire rotation, and brake inspection without having to seek additional clarification.

Finally, the completed services are documented, and the details of the maintenance work, along with any additional notes, are updated in the system. The digital record serves as a log, much like the order on the kitchen wall in the restaurant, ensuring a smooth and organized workflow at the service center.

In this scenario, the Command pattern streamlines the communication and execution of service requests, allowing for efficient handling of maintenance tasks without constant back-and-forth interactions between the vehicle owner and the mechanics. The service request, akin to a command, plays a pivotal role in orchestrating the various tasks required for the maintenance of the vehicle.
The structure includes:

1. **Sender**: The `Sender` class, also known as the invoker, holds the responsibility of initiating requests. To achieve this, the class maintains a field to store a reference to a command object. Instead of directly dispatching the request to the receiver, the sender activates the associated command. Importantly, the sender is not tasked with creating the command object; typically, it receives a pre-existing command from the client through the constructor.

2. **Command**: The `Command` interface typically defines a singular method dedicated to executing the command.

3. **Concrete commands**: Concrete Commands are responsible for implementing diverse types of requests. Instead of independently executing the work, a concrete command is designed to delegate the call to one of the business logic objects. However, for code simplicity, these classes can be consolidated.

4. **Receiver**: The Receiver class encapsulates specific business logic, and virtually any object has the potential to act as a receiver. In the context of commands, the primary role is to manage the details of how a request is conveyed to the receiver. Typically, commands focus on the process of passing the request, leaving the actual execution of the work to the receiver.


## 💡 Applicability
The Command pattern facilitates the transformation of a particular method call into an independent object. This transformation introduces various intriguing possibilities, such as passing commands as method arguments, storing them within other objects, dynamically switching linked commands at runtime, and more.

Consider an illustrative scenario: You're in the process of developing a graphical user interface (GUI) component, such as a context menu. In this context, you aim to empower users to configure menu items, allowing them to associate operations that will be triggered when an end user clicks on a specific item.
Apply the Command pattern when there is a need to queue operations, schedule their execution, or perform remote execution.

Similar to any other object, a command object can undergo serialization, transforming it into a string format that can be effortlessly stored in a file or database. Subsequently, the string representation can be reconstructed into the original command object, enabling delayed and scheduled execution. Moreover, this capability extends to queuing, logging, or transmitting commands over a network, providing a versatile range of functionalities beyond standard execution.
Adopt the Command pattern when the implementation of reversible operations, specifically undo and redo functionalities, is a requirement.

While various approaches exist for implementing undo/redo mechanisms, the Command pattern stands out as one of the most widely used. To enable the reversal of operations, maintaining a history of executed commands becomes crucial. This command history typically takes the form of a stack, preserving executed command objects and associated backups of the application's state.
