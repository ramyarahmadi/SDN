# SDN
Implementing various scenarios in SDN network
# Custom SDN Linear Topology with Mininet

This repository contains a Python implementation of a custom Software-Defined Networking (SDN) topology using the **Mininet** emulation framework. 

## 📌 Topology Overview
The topology consists of a linear structure with the following components:
*   **3 Switches** connected in a line (s1-s2-s3).
*   **2 Client Hosts** (h1 and h2) connected to s1 and s2 respectively.
*   **1 Dedicated Server** (h3) connected to s3.
*   **Centralized Controller** managing the switches.
  <img width="899" height="514" alt="image" src="https://github.com/user-attachments/assets/573e74f5-b746-4bda-9576-d10c5382d59f" />


The design allows for testing network performance (bandwidth and delay) between clients and the server across multiple hops.

## 🚀 Features
- **Configurable Bandwidth:** Separate bandwidth settings for hosts, servers, and inter-switch links.
- **Dynamic Delay:** Simulated propagation delay (default: 5ms) on all links.
- **CPU Limitation:** Ability to limit host CPU usage for realistic performance testing.
- **Automatic Cleanup:** Includes error handling to automatically clean up Mininet on failure (`mn -c`).

## 🛠 Prerequisites
You need to have Mininet installed on your Linux environment (Ubuntu recommended).
```bash
sudo apt-get install mininet



<img width="899" height="514" alt="image" src="https://github.com/user-attachments/assets/38481f91-1f30-4d9d-99a2-7b2c9cb3fc09" />
