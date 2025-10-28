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
    volume = width * height * length
    
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"