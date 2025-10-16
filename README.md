# digital_string_art
An interactive Python program that simulates a digital version of string art.   Users place "screws" on a digital board, and the program connects them with "strings", calculates the total string length, and estimates project cost.

---

## Project Description
This Python program creates a **digital version of string art** using the `turtle` graphics module.  
Users input the coordinates of screws, and the program:
- Draws **blue dots** for screws (nails),
- Connects them with **red lines** to simulate string patterns,
- Calculates the **total string length** using the distance formula,
- Estimates the **total material cost** (board + screws + string).

---

## Concepts Used
- **Turtle Graphics:** Drawing shapes and lines in a visual Python window.  
- **Loops:** Iterating through screw coordinates for drawing and distance calculation.  
- **User Input Handling:** Accepting dynamic coordinates from the user.  
- **Mathematical Computation:** Using the distance formula to find total string length.  
- **Variables & Arithmetic:** Accumulating totals for length and cost.  
- **`math` Module:** For square roots and distance calculations.  
- **Procedural Programming:** Step-by-step instructions combining logic and drawing.  

---

## How to Run
1. Make sure you have **Python 3** installed.  
2. Save the file as `string_art_assignment.py`.  
3. Open the file in **IDLE**, **VS Code**, or any Python IDE.  
4. Run the program.  
5. Enter:
   - The **total number of screws**,  
   - The **x** and **y** coordinates for each screw.  
6. Watch as:
   - The **blue nails** appear,  
   - The **red string pattern** connects them,  
   - The **total cost** appears in the turtle window,  
   - The **total string length** prints in the console.  
7. Click the turtle window to exit.

---

## 🧮 Material & Cost Formula
Total Cost = Board + (Number of Screws × Cost per Screw) + (String Length × Cost per Meter)
