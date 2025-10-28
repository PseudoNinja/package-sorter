# Thoughtful Robotic Automation - Package Sorting System

A package sorting system for robotic automation that classifies packages into different stacks based on their dimensions and mass.

## Overview

This application helps robotic arms dispatch packages to the correct stack by analyzing their volume and mass. Packages are classified as **STANDARD**, **SPECIAL**, or **REJECTED** according to specific business rules.

## Classification Rules

### Package Categories

-   **BULKY Package**: A package is bulky if:

    -   Its volume (Width × Height × Length) is greater than or equal to **1,000,000 cm³**, OR
    -   Any single dimension is greater than or equal to **150 cm**

-   **HEAVY Package**: A package is heavy if:
    -   Its mass is greater than or equal to **20 kg**

### Dispatch Stacks

Based on the package categories, packages are sorted into three stacks:

| Stack        | Description                         | Criteria                             |
| ------------ | ----------------------------------- | ------------------------------------ |
| **STANDARD** | Packages handled normally           | Neither bulky nor heavy              |
| **SPECIAL**  | Packages requiring special handling | Either bulky OR heavy (but not both) |
| **REJECTED** | Packages that cannot be processed   | Both bulky AND heavy                 |

## Installation

### Prerequisites

-   Python 3.11 or higher

### Setup

1. Clone or download this project
2. No additional dependencies required - uses Python standard library only

## Usage

### Basic Usage

Import the `sort` function and pass package dimensions and mass:

```python
from package_sorter import sort

# Sort a package: 100cm × 100cm × 100cm, weighing 15kg
result = sort(width=100, height=100, length=100, mass=15)
print(result)  # Output: "SPECIAL" (bulky by volume, not heavy)

# Sort a heavy package: 50cm × 50cm × 50cm, weighing 25kg
result = sort(width=50, height=50, length=50, mass=25)
print(result)  # Output: "SPECIAL" (heavy, not bulky)

# Sort a rejected package: 150cm × 100cm × 100cm, weighing 20kg
result = sort(width=150, height=100, length=100, mass=20)
print(result)  # Output: "REJECTED" (both bulky and heavy)

# Sort a standard package: 50cm × 50cm × 50cm, weighing 10kg
result = sort(width=50, height=50, length=50, mass=10)
print(result)  # Output: "STANDARD" (neither bulky nor heavy)
```

### Function Signature

```python
def sort(width, height, length, mass):
    """
    Dispatch packages to the correct stack based on volume and mass.

    Args:
        width (float): Width in centimeters
        height (float): Height in centimeters
        length (float): Length in centimeters
        mass (float): Mass in kilograms

    Returns:
        str: Stack name - "STANDARD", "SPECIAL", or "REJECTED"
    """
```

### Running the Demo

To see the sorting system in action with example packages:

```bash
python main.py
```

This will display a table showing various packages and their classifications:

```
============================================================
THOUGHTFUL ROBOTIC AUTOMATION - PACKAGE SORTING SYSTEM
============================================================

Package Description                 Width    Height   Length   Mass     Volume          Result
--------------------------------------------------------------------------------------------------------------
Small Standard Package              10.0     10.0     10.0     5.0      1,000           STANDARD
Bulky by Volume                     100.0    100.0    100.0    10.0     1,000,000       SPECIAL
Bulky by Dimension                  150.0    50.0     50.0     10.0     375,000         SPECIAL
Heavy Package                       50.0     50.0     50.0     25.0     125,000         SPECIAL
Both Bulky and Heavy                100.0    100.0    100.0    20.0     1,000,000       REJECTED
Just Below Thresholds               149.0    149.0    44.0     19.9     976,844         STANDARD
Extremely Large and Heavy           200.0    200.0    200.0    50.0     8,000,000       REJECTED
```

### Running Tests

To verify the sorting logic works correctly:

```bash
python test_package_sorter.py
```

All 15 tests should pass, covering:

-   Standard packages
-   Bulky packages (by volume and dimension)
-   Heavy packages
-   Rejected packages
-   Edge cases and boundary conditions

Expected output:

```
test_bulky_by_height_dimension ... ok
test_bulky_by_length_dimension ... ok
test_bulky_by_volume ... ok
test_bulky_by_width_dimension ... ok
test_heavy_package ... ok
test_rejected_bulky_and_heavy_by_dimension ... ok
test_rejected_bulky_and_heavy_by_volume ... ok
test_standard_package ... ok
... (and more)

----------------------------------------------------------------------
Ran 15 tests in 0.003s

OK
```

## Examples

### Example 1: Standard Package

```python
from package_sorter import sort

# Small box: 30cm × 30cm × 30cm, 5kg
result = sort(30, 30, 30, 5)
print(result)  # "STANDARD"
```

### Example 2: Bulky Package (by Volume)

```python
from package_sorter import sort

# Large volume: 100cm × 100cm × 100cm = 1,000,000 cm³, 15kg
result = sort(100, 100, 100, 15)
print(result)  # "SPECIAL"
```

### Example 3: Bulky Package (by Dimension)

```python
from package_sorter import sort

# Long package: 200cm × 50cm × 50cm, 10kg
result = sort(200, 50, 50, 10)
print(result)  # "SPECIAL"
```

### Example 4: Heavy Package

```python
from package_sorter import sort

# Dense package: 40cm × 40cm × 40cm, 30kg
result = sort(40, 40, 40, 30)
print(result)  # "SPECIAL"
```

### Example 5: Rejected Package

```python
from package_sorter import sort

# Both bulky and heavy: 150cm × 150cm × 150cm, 50kg
result = sort(150, 150, 150, 50)
print(result)  # "REJECTED"
```

### Example 6: Processing Multiple Packages

```python
from package_sorter import sort

packages = [
    {"width": 100, "height": 50, "length": 50, "mass": 10},
    {"width": 40, "height": 40, "length": 40, "mass": 25},
    {"width": 200, "height": 100, "length": 100, "mass": 30},
]

for i, pkg in enumerate(packages, 1):
    result = sort(pkg["width"], pkg["height"], pkg["length"], pkg["mass"])
    print(f"Package {i}: {result}")

# Output:
# Package 1: STANDARD
# Package 2: SPECIAL
# Package 3: REJECTED
```

## Project Structure

```
.
├── package_sorter.py       # Core sorting function
├── test_package_sorter.py  # Unit tests (15 test cases)
├── main.py                 # Demo application
├── README.md               # This file
├── replit.md               # Project documentation
└── .gitignore              # Python ignore patterns
```

## Integration Example

### Integrating with a Robotic System

```python
from package_sorter import sort

class RoboticArm:
    def __init__(self):
        self.standard_stack = []
        self.special_stack = []
        self.rejected_stack = []

    def process_package(self, width, height, length, mass, package_id):
        """Process a package and dispatch to appropriate stack"""
        classification = sort(width, height, length, mass)

        if classification == "STANDARD":
            self.standard_stack.append(package_id)
            print(f"Package {package_id} → Standard Stack")
        elif classification == "SPECIAL":
            self.special_stack.append(package_id)
            print(f"Package {package_id} → Special Handling")
        elif classification == "REJECTED":
            self.rejected_stack.append(package_id)
            print(f"Package {package_id} → Rejected")

        return classification

# Usage
robot = RoboticArm()
robot.process_package(50, 50, 50, 10, "PKG-001")  # → Standard Stack
robot.process_package(150, 60, 60, 15, "PKG-002")  # → Special Handling
robot.process_package(160, 100, 100, 25, "PKG-003")  # → Rejected
```

## Testing

The test suite includes comprehensive coverage:

-   ✓ Standard packages (normal size and mass)
-   ✓ Packages at threshold boundaries
-   ✓ Bulky packages by volume (≥ 1,000,000 cm³)
-   ✓ Bulky packages by dimension (width/height/length ≥ 150 cm)
-   ✓ Heavy packages (≥ 20 kg)
-   ✓ Rejected packages (bulky AND heavy)
-   ✓ Edge cases (very small, very large, etc.)

## License

This project is provided as-is for Thoughtful's robotic automation factory.

## Support

For questions or issues, please refer to the project documentation or contact your system administrator.
