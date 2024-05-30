# 🚪 Proxy Pattern

## Introduction

The Proxy design pattern is a structural pattern that allows you to provide a substitute or placeholder for another
object. This proxy manages access to the original object, enabling actions to be taken either before or after the
request reaches the original object.

## 🚨 The Problem

Suppose you are developing graphic user interface application, which needs to display images from a remote server.
Loading these images can be slow, and you don't want your application to become unresponsive while waiting for the
images to load. Moreover, you might not need all images immediately; they should only be loaded when they are needed (
e.g., when they come into view).

## ✔️ The Solution

We could use the Proxy pattern to create a virtual proxy for the images. The virtual proxy will act as a placeholder for
the actual images and will only load them when necessary.

## 🚧 Structural Elements

**Service Element:** defines the methods that the Service offers. The proxy must implement this interface to effectively
masquerade as a service object.
**Service:** defines the real object that the proxy represents.
**Proxy:** maintains a reference to the service object and controls access to it.
**Client:** interacts with the proxy to access the service object.

## 📚🔨 Implementation Guide

1. Define the Service Interface: Create an interface that both the RealService and Proxy will implement. This ensures
   that the proxy can be used in place of the real service object.
2. Implement the Real Service: Create a class that implements the Service interface. This class will contain the actual
   functionality that the proxy will provide access to.
3. Implement the Proxy: Create a class that implements the Service interface. This class will maintain a reference to
   the
   RealService object and control access to it. The proxy can add additional functionality, such as logging, caching, or
   security checks, before delegating the request to the real service object.
4. Implement Proxy Methods: Implement the methods in the Proxy class. These methods should delegate the request to the
   real service object, performing any additional functionality before or after the request is made.
5. Use the Proxy: In the client code, create an instance of the Proxy class and use it to access the service object. The
   client should interact with the proxy as if it were the real service object, allowing the proxy to manage access to
   the real service object.

## 💡 Implementation Tips

The Proxy pattern is helpful when you need to control access to an object, add a layer of security, manage resource
consumption, or handle additional functionality such as logging or caching without altering the original object's code.
Some scenarios where the Proxy pattern is beneficial include:

**Lazy Initialization in a photo viewer application:** loading high-resolution images can be time-consuming. A virtual
proxy can be used to load images on demand (only when they are viewed) rather than loading all images upfront. This
reduces initial load time and memory consumption.

**Accessing remote services in a distributed system:** a proxy can be used to manage network connections, handle
security concerns, and cache responses to reduce latency. This approach Encapsulates the details of network
communication, providing a local object that handles remote method calls seamlessly.

**Result caching in web application:** where some data fetched from a database or external API can be cached to improve
performance. A caching proxy can store the results of expensive operations and return the cached results for subsequent
requests. This reduces the load on the database or external API and improves response time for repeated requests.