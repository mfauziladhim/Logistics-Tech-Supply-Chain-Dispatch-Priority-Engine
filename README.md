# Logistics-Tech-Supply-Chain-Dispatch-Priority-Engine
Program Python berbasis Pandas dan NumPy untuk menentukan prioritas pengiriman paket secara otomatis berdasarkan sisa waktu dan nilai barang.

# 🚚 Supply Chain & Dispatch Priority Engine

A Python-based automated cargo prioritization and dispatch optimization system built with **Pandas** and **NumPy**. This engine calculates multi-criteria priority scores for logistics management, balancing time urgency, value density, and operational constraints.

---

## 📌 Project Overview

In modern logistics and e-commerce supply chains, inefficient dispatching leads to delayed high-value deliveries and increased operational costs. This project simulates a dynamic cargo dataset and applies vector calculations to dynamically score and rank packages, ensuring critical items are loaded onto first-tier transport units.

Key problems solved:
* Eliminates scale dominance between high-value monetary metrics and single-digit deadline hours.
* Implements multi-criteria decision analysis (MCDA) using dynamic weighting.
* Filters top-priority shipments efficiently using Pandas vectorization.

---

## 🛠️ Tech Stack & Key Concepts

* **Python 3.x**
* **Pandas**: DataFrame manipulation, index setting, and `.nlargest()` filtering.
* **NumPy**: Random dataset generation (`np.random.choice`), array range operations, and vector arithmetic.

---

## 📐 Scoring Methodology

The algorithm normalizes raw values to establish balanced priority scoring:

1. **Monetary Normalization**: Converts raw value (IDR) to millions (`nilai_juta`) to match numerical scale boundaries.
2. **Time Urgency Factor**: Calculated as $\frac{1}{\text{Deadline (Hours)}}$, ensuring shorter deadlines yield exponentially higher urgency scores.
3. **Value Density**: Calculated as $\frac{\text{Nilai Juta}}{\text{Berat (Kg)}}$ to prioritize high-value per weight ratio.
4. **Final Priority Index**:
   $$\text{Priority Score} = (40 \times \text{Urgency}) + (30 \times \text{Value Density}) + 30$$

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/username/supply-chain-priority-engine.git](https://github.com/username/supply-chain-priority-engine.git)
   
