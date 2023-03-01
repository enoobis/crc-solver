# crc-solver

Color Resistor Code Solver is a simple application that calculates the resistance value of a resistor based on its color bands. The user can enter the colors of the first three bands and the multiplier band, and the application will display the resistance value in ohms.

![image](https://user-images.githubusercontent.com/62465404/222076095-583b6bde-6231-4150-9c35-2e8b09237c92.png)

## Installation

To install the required packages, run the following command:
```
pip install tkinter
```
## Usage

To run the application, execute the following command:
```
python main.py
```

The application will display a window with four input fields for the color bands and a button to calculate the resistance value. Enter the color codes for the first three bands and the multiplier band, and then click the "Calculate" button to display the resistance value.

## Color Codes

The following color codes are supported:

Color | Code
------|-----
Black | 0
Brown | 1
Red | 2
Orange | 3
Yellow | 4
Green | 5
Blue | 6
Purple | 7
Gray | 8
White | 9
Gold | -1
Silver | -2

## Tolerance Values

The following tolerance values are supported:

Color | Tolerance
------|----------
Brown | 1%
Red | 2%
Green | 0.5%
Blue | 0.25%
Purple | 0.1%
Gray | 0.05%
Gold | 5%
Silver | 10%

## License

This project is licensed under the MIT License
