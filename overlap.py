from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    # Implementa acá tu solución

    # Caso Base
    no_fit = (panel_width > roof_width and panel_width > roof_height) or (panel_height > roof_width and panel_height > roof_height)
    no_space = roof_width == 0 or roof_height == 0
    if no_fit or no_space:
        return 0

    # Paneles en dirección original
    original_direction_panels = (roof_height//panel_height) * (roof_width//panel_width)
    original_remaining_space = {}
    original_remaining_space["width"] = roof_width%panel_width
    original_remaining_space["height"] = roof_height%panel_height
    # Se calculan los paneles en la dirección original que caben en el espacio restante solo sí cabía alguino en el espacio original
    if (original_direction_panels != 0):
        original_extra_panels_1 = calculate_panels(panel_width, panel_height, original_remaining_space["width"], roof_height) + calculate_panels(panel_width, panel_height, roof_width - original_remaining_space["width"], original_remaining_space["height"])
        original_extra_panels_2 = calculate_panels(panel_width, panel_height, original_remaining_space["width"], roof_height - original_remaining_space["height"]) + calculate_panels(panel_width, panel_height, roof_width, original_remaining_space["height"])
        original_extra_panels = max([original_extra_panels_1, original_extra_panels_2])
        original_direction_panels += original_extra_panels

    # Paneles rotados
    other_direction_panels = (roof_height//panel_width) * (roof_width//panel_height)
    other_remaining_space = {}
    other_remaining_space["width"] = roof_width%panel_height
    other_remaining_space["height"] = roof_height%panel_width
    # Se calculan los paneles rotados que caben en el espacio restante solo sí cabía alguino en el espacio original
    if (other_direction_panels != 0):
        other_extra_panels_1 = calculate_panels(panel_width, panel_height, other_remaining_space["width"], roof_height) + calculate_panels(panel_width, panel_height, roof_width - other_remaining_space["width"], other_remaining_space["height"])
        other_extra_panels_2 = calculate_panels(panel_width, panel_height, other_remaining_space["width"], roof_height - other_remaining_space["height"]) + calculate_panels(panel_width, panel_height, roof_width, other_remaining_space["height"])
        other_extra_panels = max([other_extra_panels_1, other_extra_panels_2])
        other_direction_panels += other_extra_panels

    total = max([original_direction_panels, other_direction_panels])
    return total


def calculate_panels_overlap(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int,
                    overlap_width: int, overlap_height: int) -> int:
    
    panels = calculate_panels(panel_width, panel_height, roof_width, roof_height)
    
    extra_panels_1 = calculate_panels(panel_width, panel_height, roof_width - overlap_width, overlap_height) + calculate_panels(panel_width, panel_height, roof_width, roof_height - overlap_height)
    extra_panels_2 = calculate_panels(panel_width, panel_height, roof_width - overlap_width, roof_height) + calculate_panels(panel_width, panel_height, overlap_width, roof_height - overlap_height)
    extra = max([extra_panels_1, extra_panels_2])
    panels += extra

    return panels


def run_tests() -> None:
    with open('test_cases_overlap.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "overlap_w": test["overlapW"],
                "overlap_h": test["overlapH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels_overlap(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"],
            test["overlap_w"], test["overlap_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}",
              f"Overlap: {test['overlap_w']}x{test['overlap_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()