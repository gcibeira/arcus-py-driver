# Arcus Py Driver

Arcus Py Driver is a Python USB driver designed to facilitate communication with Arcus DMX-J-SA-17 stepper motors.

## Overview

The Arcus Py Driver offers seamless USB communication with the motor driver, enabling the transmission of ASCII commands for precise motor control. A comprehensive list of available commands can be found in the [motor manual] (https://www.arcus-technology.com/support/downloads/download-info/dmx-j-sa-17-manual/)

### Features

- **PerformaxUSB**: A native USB driver developed using the PyUSB library. This component was meticulously crafted through reverse engineering, leveraging USBPcap and Wireshark for insights. Relevant captures are provided within this repository.

- **PerformaxDll**: A wrapper for the manufacturer-provided DLLs, accessible on the official website. Leveraging ctypes, this component interfaces with the DLLs, albeit with exclusive compatibility for Windows systems.

## Getting Started

### Dependencies

- Python >= 3
- PyUSB

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/gcibeira/arcus-py-driver.git
   ```

2. Install the PyUSB library:
   ```
   pip install pyusb
   ```

### Usage

1. Execute the provided example file:
   ```bash
   python example.py
   ```

   This example establishes communication with any motor connected to the USB port. It presents a prompt for sending commands to the motor. Experiment with the following commands to begin:
   
   - `EO=1`: Power ON the motor.
   - `HSPD=2400`: Set the speed to 2400.
   - `J+`: Move the motor forward.

## Author

Gerardo D. Cibeira - 2023

## Version History

- 0.2
  - Implementation of the PerformaxDevice class to manage multiple device instances.
  
- 0.1
  - Initial Release

## License

This project is licensed under the MIT License. Refer to the LICENSE.md file for more details.

## External Resources

- [Arcus NEMA 17 Integrated USB Stepper Basic](https://www.arcus-technology.com/products/integrated-stepper-motors/nema-17-integrated-usb-stepper-basic/)