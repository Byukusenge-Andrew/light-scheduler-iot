# Light Scheduler

A web-based IoT dashboard to schedule a light using WebSocket and MQTT, with simulated light control.

## Overview
This project simulates an IoT system where a user schedules a light's ON/OFF times via a browser interface. The schedule is sent to a WebSocket server, forwarded to an MQTT broker, and processed by a Python subscriber that simulates light control (no Arduino required).

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (websockets, paho-mqtt)
- **MQTT**: Mosquitto (mosquitto_pub, mosquitto_sub)

## Setup Instructions
1. **Prerequisites**:
   - Install Python 3, Mosquitto broker, and required Python packages:
     ```bash
     pip install websockets paho-mqtt