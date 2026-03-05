# ARP Protocol Analysis – Ethernet and Address Resolution

## 1. Introduction

The Address Resolution Protocol (ARP) is used in local networks to map IP addresses to MAC addresses. While the Network layer uses IP addresses for logical addressing, the Data Link layer requires MAC addresses for actual frame delivery within a LAN.

ARP acts as a bridge between these two layers.

## 2. Objective

The goal of this lab is to:

1. Understand how ARP resolves IP addresses to MAC addresses.
2. Analyze ARP request and reply messages.
3. Study how Ethernet frames carry ARP packets.
4. Explain the interaction between Network and Data Link layers.

## 3. Theoretical Background

When a host wants to send an IP packet to another device in the same local network:

1. It checks its ARP cache to see if it already knows the MAC address.
2. If not, it sends an ARP request (broadcast).
3. The device with the matching IP responds with an ARP reply (unicast).
4. The sender stores the mapping in its ARP table.

ARP Request characteristics:
- Destination MAC: ff:ff:ff:ff:ff:ff (broadcast)
- Contains sender IP, sender MAC
- Contains target IP
- Target MAC initially unknown

ARP Reply characteristics:
- Sent as unicast
- Contains the correct MAC address for the requested IP

## 4. ARP Packet Structure

An ARP packet contains:

- Hardware type (Ethernet = 1)
- Protocol type (IPv4 = 0x0800)
- Hardware size (6 bytes for MAC)
- Protocol size (4 bytes for IPv4)
- Opcode (1 = request, 2 = reply)
- Sender MAC address
- Sender IP address
- Target MAC address
- Target IP address

ARP is encapsulated inside an Ethernet frame with EtherType 0x0806.

## 5. Practical Experiment

To observe ARP in action:

1. I opened Wireshark.
2. I started capturing traffic on your active network interface.
3. I cleared my ARP cache:
   - Windows: arp -d *
4. I pinged my local router
5. I stopped the capture.
6. Filter by typing:
   arp

I observed:

- An ARP Request (broadcast)
- An ARP Reply (unicast)

## 6. Analysis

Why is ARP request broadcast?

Because the sender does not know which device owns the target IP address. Broadcasting ensures that all devices in the local network receive the request.

Why is ARP reply unicast?

Because the responding device knows exactly who requested the information.

What layer does ARP belong to?

ARP operates conceptually between the Network and Data Link layers, but in the OSI model it is typically considered part of the Data Link layer because it works with MAC addresses and Ethernet frames.

## 7. ARP Table

Devices store resolved mappings in an ARP cache.

Example entry:

IP address        MAC address
192.168.1.1       aa:bb:cc:dd:ee:ff

This avoids sending ARP requests for every packet.


## 8. Security Considerations – ARP Spoofing

ARP has no authentication mechanism.

This allows attacks such as ARP spoofing (or ARP poisoning), where an attacker sends fake ARP replies to associate their MAC address with another device’s IP.

This can enable:
- Man-in-the-middle attacks
- Traffic interception
- Session hijacking

This weakness shows that ARP prioritizes simplicity over security.

## 9. Reflection

ARP demonstrates how different network layers interact in practice. While IP handles logical addressing, actual communication within a LAN depends entirely on MAC addresses.

The broadcast nature of ARP requests also highlights how local networks rely on shared media behavior.

Although ARP is simple and efficient, its lack of authentication makes it vulnerable to attacks, showing that protocol design involves trade-offs between performance and security.