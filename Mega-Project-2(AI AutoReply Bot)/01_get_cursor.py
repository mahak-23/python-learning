"""
Cursor Position Detector 

Usage: Run this script and move your mouse to get coordinates
"""

import pyautogui

print("🖱️  Mouse Coordinate Detector")
print("=" * 40)
print("Move your mouse around to see coordinates")
print("Press Ctrl+C to stop")
print("=" * 40)

while True:
    try:
        a = pyautogui.position()
        print(f"Position: {a}")
        # Example coordinates:
        # Chrome icon: 1639, 1412
        # Chat selection area: 1003, 237 to 2187, 1258
        # Message box: 1026, 244 to 1131, 1321
    except KeyboardInterrupt:
        print("\n✅ Coordinate detection stopped")
        break
