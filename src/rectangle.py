def calculate_rectangle_area(length, width):
    """Oblicza pole prostokąta."""
    if length <= 0 or width <= 0:
        raise ValueError("Długość i szerokość muszą być dodatnie.")
    return length * width

if __name__ == "__main__":
    try:
        length = float(input("Podaj długość prostokąta: "))
        width = float(input("Podaj szerokość prostokąta: "))
        area = calculate_rectangle_area(length, width)
        print(f"Pole prostokąta wynosi: {area}")
    except ValueError as e:
        print(f"Błąd: {e}")