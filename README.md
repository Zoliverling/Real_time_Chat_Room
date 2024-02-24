# Real-time Chat Application

## Introduction

This project involves the development of a real-time chat application that enables users to communicate in a single chat or group chat environment.
The application is built using Python and utilizes socket programming for network communication and Tkinter for the graphical user interface. 

Key components of the project include:

__ChatClient__: Manages the client-side operations, allowing users to send and receive messages in real-time.

__ChatServer__: Handles the server-side operations, managing multiple client connections and facilitating message broadcasting.

__SingleChatClient and SingleChatServer__: Specialized modules for one-on-one communication, ensuring private chat sessions.

__ServerStarter and ClientStarter__: Initializer modules that set up the server and client, respectively, and allow users to select the desired chat mode.

## Chat Client

This module uses Python's Tkinter package for the graphical user interface, allowing users to send and receive messages in real-time. 
It employs socket programming for network communication with the chat server and threading to handle asynchronous message updates.

## Chat Server

This module utilizes socket programming to manage connections and communication between multiple clients. 
It uses threading to handle each client connection in parallel, ensuring efficient message broadcasting and client management.

## SingleChatClient and SingleChatServer

This module combines the functionalities of SingleChatClient and SingleChatServer to provide a seamless one-on-one chat experience. 
It uses Python's Tkinter package for the graphical user interface and socket programming for network communication between two clients. 
The module ensures a private and secure chat environment, managing connections, message forwarding, and disconnections efficiently.

## ServerStarter and ClientStarter

This module merges the functionalities of ServerStarter and ClientStarter, providing a unified entry point for the chat application. 
It utilizes Tkinter for the initial graphical interface where users can select the chat mode (single or group chat). 
Based on the selection, it sets up the appropriate chat server and launches the corresponding chat client interface, using socket programming to establish the necessary connections.


