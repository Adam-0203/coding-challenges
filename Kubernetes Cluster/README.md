# Kubernetes Cluster Simulator

A C++ object-oriented simulation of a Kubernetes-like cluster management system. This project models the core concepts of container orchestration, including clusters, nodes (servers), pods, and containers, demonstrating resource allocation, scheduling, and lifecycle management.

## 📖 Overview

This application provides a simplified simulation of how a Kubernetes cluster operates. It defines a hierarchy of resources (Containers, Pods, Servers) and manages their deployment onto a cluster of nodes. The project is a practical demonstration of advanced C++ features and software design patterns.

## 🏗️ Architecture & Class Hierarchy

The project is built around a core inheritance hierarchy rooted in the `Resource` class:


### Key Components:

*   **`Resource`:** The abstract base class defining the common interface (`start()`, `stop()`, `getMetrics()`) for all compute resources.
*   **`Container`:** Represents a single software container (e.g., Docker). It has a unique ID, a container image, and CPU/memory requirements.
*   **`Pod`:** A group of one or more tightly coupled containers that are scheduled together on the same node. Pods are the smallest deployable units in the simulation.
*   **`Server`:** Represents a physical or virtual machine (Node) in the cluster. It manages its available CPU and memory and can have resources allocated to it.
*   **`KubernetesCluster`:** The main orchestrator. It contains a collection of `Server` (nodes) and scheduled `Pod` objects. It handles the scheduling logic for deploying pods.

## ⚙️ Core Functionality

*   **Resource Management:** Tracks CPU and memory allocation for all components.
*   **Scheduling:** The cluster uses a simple **bin-packing** algorithm to schedule pods onto nodes with sufficient available resources.
*   **Lifecycle Management:** Provides methods to start/stop resources and deploy/remove pods and containers.
*   **Metrics & Monitoring:** Each class implements a `getMetrics()` method to report its current state, allowing for easy visualization of the cluster's health.

## 🚀 Features

- **Object-Oriented Design:** Heavy use of inheritance, polymorphism, and encapsulation.
- **Smart Pointers:** Utilizes `std::unique_ptr` and `std::shared_ptr` for automatic and safe memory management.
- **STL Containers:** Employs `std::vector`, `std::unordered_map`, and `std::string` for efficient data handling.
- **Operator Overloading:** Implements `operator<<` for easy printing of object states.
- **Modularity:** Code is separated into logical headers and implementation files for clarity and maintainability.

## 🛠️ Build Instructions

### Prerequisites
- A C++ compiler supporting C++11 or later (e.g., `g++`, `clang++`)

### Compilation
Compile all the `.cpp` files together.

```bash
# Using g++
g++ -std=c++17 *.cpp -o kubernetes_simulator

# Using clang++
clang++ -std=c++17 *.cpp -o kubernetes_simulator
