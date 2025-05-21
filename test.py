def cm_to_imet(cm: float) -> (int, int):
    """
    Convert a height in centimeters to feet and inches.
    Returns a tuple (feet, inches).
    """
    # Convert cm to total inches
    total_inches = cm / 2.54
    
    # Calculate whole feet
    feet = int(total_inches // 12)
    
    # Calculate remaining inches (rounded)
    inches = int(round(total_inches - (feet * 12)))
    
    return feet, inches

def format_height_imperial(cm: float) -> str:
    """
    Given a height in cm, return a formatted string like "6′ 3″".
    """
    feet, inches = cm_to_imet(cm)
    return f"{feet}′ {inches}″"

# Example usage:
heights_cm = [191.0, 178.0, 180.0]
for cm in heights_cm:
    print(f"{cm} cm → {format_height_imperial(cm)}")
