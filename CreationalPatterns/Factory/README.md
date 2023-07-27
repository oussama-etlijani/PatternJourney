# Factory Method Design Pattern

## Introduction

The Factory Method is a creational design pattern that is often used to provide a level of abstraction to the process of object creation. Instead of calling the constructors directly to create objects, this pattern suggests that we use a special factory method to create them.

## 🚨 The Problem

Imagine you're building an online food delivery application. The initial version of your app can only cater to pizza deliveries, hence the majority of your code resides inside the PizzaDelivery class.

As time progresses, your app gains significant traction. Every day, you receive numerous requests from sushi restaurants, burger joints, and vegan eateries, all wanting to be incorporated into your app. This is indeed a positive development, isn't it? But what about the code? As it stands, most of your code is tightly coupled to the PizzaDelivery class. Adding other food deliveries, like SushiDelivery or BurgerDelivery, into the app would necessitate modifications to the entire codebase. Furthermore, if you later decide to include another type of food delivery into your app, you'll probably have to make all these modifications again.

Consequently, you would end up with highly complex code, filled with conditional statements that alter the app's functionality depending on the class of food delivery objects.
## ✔️ The Solution

The Factory Method pattern recommends that you replace direct object construction calls (using the new operator) with calls to a specific factory method. Don't worry: the objects are still being created using the new operator, but now it's being invoked from within the factory method. Objects returned by a factory method are often termed as products.

At first glance, this modification may appear redundant: we've simply relocated the constructor call from one section of the program to another. However, bear in mind that now you can override the factory method in a subclass and change the type of products being created by the method.

There's a minor limitation, though: subclasses may return different types of products only if these products share a common base class or interface. Also, the factory method in the base class should declare its return type as this interface. 

For instance, the PizzaDelivery, SushiDelivery, and BurgerDelivery classes should all implement the FoodDelivery interface, which stipulates a method called deliver. Each class implements this method differently: PizzaDelivery delivers pizza, SushiDelivery delivers sushi, and BurgerDelivery delivers burgers. The factory method in the PizzaRestaurant class returns PizzaDelivery objects, whereas the factory method in the SushiRestaurant class returns SushiDelivery objects, and so on.

The code that utilizes the factory method (frequently referred to as the client code) doesn't perceive a difference between the actual products returned by various subclasses. The client treats all the products as abstract FoodDelivery. The client understands that all food delivery objects are expected to have the deliver method, but the specific implementation isn't critical to the client.
## 🚧 Structural Elements

- **Product**: The product declares the common interface for objects that the factory method creates.
- **Concrete Products**: These are various implementations of the product interface.
- **Creator**: This class declares the factory method that returns new product objects. Its main function is not to create products, but it houses some core business logic related to products. The factory method assists in decoupling this logic from the concrete product classes.
- **Concrete Creators**: These classes override the base factory method so it returns a different type of product.

## Example

An example of the Factory Method pattern could be seen in the creation of cross-platform database connections in a web application. The Factory Method can be used to establish these connections without coupling the client code to the concrete database classes. This way, the base class uses different database connections to interact with the data without having to rewrite the logic for each different type of database, by declaring a factory method to create connections, for instance. Therefore, it can later create a subclass that returns MySQL connections from the factory method.

The Factory Method design pattern offers a practical way to decouple the client code from concrete classes, consequently making your code more modular, adaptable, and easier to maintain. For example, if you later decide to change your database from MySQL to PostgreSQL, you can simply create a new factory method that produces PostgreSQL connections without changing the client code that uses these connections.
