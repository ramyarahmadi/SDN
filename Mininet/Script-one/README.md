🌐 Custom Mininet Topology Script
📖 Overview

This script implements a custom network topology using the Mininet network emulator. The goal is to simulate a configurable network environment where multiple hosts communicate through a chain of switches while allowing control over bandwidth, delay, and CPU resources.

The topology dynamically creates N hosts and N switches. Each host is connected to its own switch, and all switches are connected sequentially to form a linear network path. In this design, the last host acts as a server, while the remaining hosts behave as clients.

This setup is useful for network experiments, bandwidth testing, congestion analysis, and protocol evaluation.
🏗️ Topology Structure

For example, when n_host = 3, the network will be created as follows:

                                                                    
h1 ── s1 ── s2 ── s3 ── h3
        │
        h2

Where:

    h1, h2 → client hosts
    h3 → server host
    s1, s2, s3 → switches connected in a chain

Each host communicates through the switch network to reach the server.
⚙️ Key Features

✨ Dynamic topology generation based on the number of hosts

✨ Custom bandwidth control for different types of links

✨ Network delay simulation

✨ CPU limitation support for hosts

✨ Automatic connectivity testing

✨ Interactive Mininet CLI for experimentation
🧩 Configurable Parameters

The SampleTopo class allows several parameters to customize the network:

    n_host → Total number of hosts in the topology
    bw_host → Bandwidth of client host–switch links
    bw_server → Bandwidth of the server–switch link
    bw_net → Bandwidth of switch–switch links
    delay → Link delay applied to all connections
    cpu → CPU limit assigned to the server host
    maxq → Optional maximum queue size for links

These parameters allow researchers to simulate different network conditions.
🚀 Running the Script

The script initializes the topology inside the main() function:

#code
topo = SampleTopo(3)
net = Mininet(topo=topo, link=TCLink)

Steps performed during execution:

    The custom topology is created.
    Mininet starts the virtual network.
    A connectivity test (pingAll) verifies communication between hosts.
    The Mininet CLI opens for interactive experimentation.

🧪 Testing the Network

Inside the Mininet CLI, you can run several useful commands:

                                                                    
nodes
net
h1 ping h3
iperf h1 h3

These commands allow you to inspect the topology, test connectivity, and measure bandwidth between hosts.
🧹 Automatic Cleanup

If the script encounters an error, it automatically executes:

                                                                    
sudo mn -c

This command cleans any leftover Mininet processes, ensuring the environment remains ready for future simulations.
🎯 Use Cases

This topology can be used for:

    Network performance experiments
    Bandwidth and congestion analysis
    Client–server communication testing
    Protocol evaluation in controlled environments
    Educational demonstrations of software-defined networking concepts

✅ This script provides a simple yet flexible Mininet topology suitable for networking labs, research experiments, and simulation-based learning.
