# 🚌 CAN Bus Logger & Visualizer in Python

**Simulate, log, and analyze CAN bus messages** using Python tools like `python-can`, `pandas`, and `matplotlib`. Built with clarity, precision, and extensibility in mind — this project showcases how embedded communication data can be structured, visualized, and understood with ease.

---

## 🚀 Features

- **Virtual CAN Bus Simulation** via `vcan0`
- **Message Transmission** with timestamped send logs
- **Real-Time Logging** of incoming CAN frames
- **CSV Export** for data archival and analysis
- **Bar Chart Visualization** for message distribution insights

---

## 📦 Technologies Used

| Layer            | Tools & Libraries               |
|------------------|----------------------------------|
| Interface        | `python-can` (virtual bus)      |
| Data Handling    | `pandas`, `datetime`            |
| Visualization    | `matplotlib`                    |
| Timing & Control | `time`, `sleep`, `recv` loop    |

---

## 📁 File Structure

```bash
├── can_logger.py       # Main script
├── can_log.csv         # Output log (generated on run)
├── README.md           # You're here!
```

---

## ▶️ Usage

Make sure `vcan0` is configured on your system (`modprobe vcan` + `ip link set vcan0 up`), then run:

```bash
python can_logger.py
```

- Messages will be **sent** with sample payloads.
- Incoming messages will be **recorded** for 15 seconds.
- A **CSV file** is created, followed by a **bar chart** showing message frequency by arbitration ID.

---

## 📊 Sample Output

```
Received: {
  'timestamp': '19:27:41.014',
  'arbitration_id': '0x124',
  'data': '55667788'
}
Message count per Arbitration ID:
0x124    5
0x125    3
0x123    7
```
---

## 🎯 Recruiter Insights

What this project reveals:

- 🔧 **Embedded & middleware know-how** — from bus simulation to message parsing  
- 🧠 **Data automation & analysis** — time-series logging, CSV export, and plotting  
- ✨ **Clarity-driven communication** — every line built with technical storytelling in mind  

If you’re hiring for Python-based embedded diagnostics, automotive middleware, or tooling development — this is a peek into how I build clean, modular, and scalable solutions.

---

## 🤝 Let's Connect

If you'd like to talk about embedded systems, Python tooling, or building technical content that educates and inspires — let's collaborate!

📬 [LinkedIn Profile](https://linkedin.com/in/ranganathachawan)  
💻 [More Projects](https://github.com/Ranganatha478)
