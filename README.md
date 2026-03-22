# 🔢 Bisection Method (Python)

---

## 🎬 Demo Animation

---

## 📌 Overview

The **Bisection Method** is a numerical algorithm used to find the root of a function by repeatedly dividing an interval and selecting the subinterval where the sign changes.

---

## ⚙️ Features

✨ Dynamic function input
📊 Step-by-step iterations
🎯 Accurate root approximation
🧠 Clean & beginner-friendly code
⚡ Fast convergence

---

## 🧠 Algorithm

```text
1. Choose a and b such that f(a) * f(b) < 0
2. Compute midpoint: c = (a + b) / 2
3. If f(c) == 0 → root found
4. If f(a)*f(c) < 0 → root in [a, c]
5. Else → root in [c, b]
6. Repeat until tolerance is met
```

---

## ▶️ How to Run

```bash
python first_method.py
```

---

## 🧪 Example

### Input:

```bash
x**3 - x - 2
1
2
```

### Output:

```text
Counter 0: a = 1.0000, b = 2.0000, c = 1.5000
...
Root found: 1.5215
```

---

## 📸 Real Output

---

## 📥 Input Rules

✅ Correct:

```python
x**2 - 4
math.cos(x) - x
math.exp(x) - 3*x
```

❌ Wrong:

```python
x^2
```

---

## ⚠️ Notes

* Function must change sign in interval
* Works only for continuous functions
* Uses `eval()` → avoid unsafe input

---

## 🚀 Future Improvements

* 📈 Add graph visualization (Matplotlib)
* 🖥 Build GUI version
* ⚡ Add Newton & Secant methods

---


## 👨‍💻 Author

**Yousef Lotfy**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
