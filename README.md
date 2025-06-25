# Jacobi Method for 2D Laplace Equation – Pressure Field Simulation

This project implements the **Jacobi iterative method** in **Python** to solve the **2D Laplace equation**, simulating steady-state pressure distribution across a rectangular domain. This method is commonly used in **fluid mechanics**, **reservoir simulation**, and **potential flow analysis**.

---

## 🔍 Project Objective

To numerically solve the Laplace equation under fixed boundary conditions and simulate how pressure equilibrates in a fluid system using **discrete iteration** methods.

---

## ⚙️ Method Overview

- **Governing Equation**:  
  \[
  \frac{\partial^2 P}{\partial x^2} + \frac{\partial^2 P}{\partial y^2} = 0
  \]
  
- **Numerical Approach**:  
  The domain is discretized into a grid of \(100 \times 100\) cells. The pressure at each point is updated iteratively using the Jacobi scheme:

  \[
  P_{i,j}^{n+1} = \frac{1}{4}(P_{i+1,j}^n + P_{i-1,j}^n + P_{i,j+1}^n + P_{i,j-1}^n)
  \]

- **Boundary Conditions**:  
  - Fluid inlet: left vertical boundary (at `j = 0`) between `i = 35` to `65` set to 1.  
  - Fluid outlet: bottom horizontal boundary (at `i = 99`) from `j = 0` to `30` also set to 1.

---

## 📈 Visualization

**The simulation tracks pressure contour development every certain iterations using **Matplotlib**, until convergence is reached.**

- For 300 Iterations

  ![300 Iterations](https://github.com/Nassor-Salum/jacobi-method-laplace-2d/blob/main/Screenshot%202025-06-25%20235819.png)


---

## 🧠 Applications

- Reservoir engineering (fluid distribution)
- Groundwater seepage models
- Electrostatics / Heat conduction (steady-state)
- CFD and porous media flow

---

## 🧪 Tools Used

- **Python 3**
- **Matplotlib** for plotting
- **NumPy** (optional for performance optimization, not used in current code)

---
## Author
**Nassor Salum**
**Petroleum Engineering | Simulation & Modeling | Python Enthusiast**
