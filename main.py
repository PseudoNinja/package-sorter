from package_sorter import sort


def main():
    """
    Demonstrate the package sorting system with example packages.
    """
    print("=" * 60)
    print("THOUGHTFUL ROBOTIC AUTOMATION - PACKAGE SORTING SYSTEM")
    print("=" * 60)
    print()
    
    test_packages = [
        {"width": 10, "height": 10, "length": 10, "mass": 5, "name": "Small Standard Package"},
        {"width": 100, "height": 100, "length": 100, "mass": 10, "name": "Bulky by Volume"},
        {"width": 150, "height": 50, "length": 50, "mass": 10, "name": "Bulky by Dimension"},
        {"width": 50, "height": 50, "length": 50, "mass": 25, "name": "Heavy Package"},
        {"width": 100, "height": 100, "length": 100, "mass": 20, "name": "Both Bulky and Heavy"},
        {"width": 149, "height": 149, "length": 44, "mass": 19.9, "name": "Just Below Thresholds"},
        {"width": 200, "height": 200, "length": 200, "mass": 50, "name": "Extremely Large and Heavy"},
    ]
    
    print(f"{'Package Description':<35} {'Width':<8} {'Height':<8} {'Length':<8} {'Mass':<8} {'Volume':<15} {'Result':<10}")
    print("-" * 110)
    
    for pkg in test_packages:
        volume = pkg["width"] * pkg["height"] * pkg["length"]
        result = sort(pkg["width"], pkg["height"], pkg["length"], pkg["mass"])
        
        print(f"{pkg['name']:<35} {pkg['width']:<8.1f} {pkg['height']:<8.1f} {pkg['length']:<8.1f} {pkg['mass']:<8.1f} {volume:<15,.0f} {result:<10}")
    
    print()
    print("=" * 60)
    print("Classification Rules:")
    print("  • BULKY: Volume >= 1,000,000 cm³ OR any dimension >= 150 cm")
    print("  • HEAVY: Mass >= 20 kg")
    print("  • STANDARD: Neither bulky nor heavy")
    print("  • SPECIAL: Either bulky OR heavy (but not both)")
    print("  • REJECTED: Both bulky AND heavy")
    print("=" * 60)


if __name__ == "__main__":
    main()