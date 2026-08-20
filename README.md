# Mini SOC Log Analyzer — Python Security Event Engine

A modular, lightweight log parsing and analysis engine designed to evaluate authentication events, detect suspicious behaviors (e.g., brute-force patterns), and generate actionable security reports from raw logs.

This project focuses on **clean code practices, modular architecture, and fundamental Python mechanics** (data structures, custom parsing, and exception handling) without relying on third-party analytical frameworks.

---

## 🚀 Project Status

**Fase 0 Completed / Active Refactoring**  
Current focus:
* Refactoring analysis logic into composable modules.
* Expanding interactive query options (User, IP, and Status filters).
* Implementing automated security alert thresholds.

> *This project represents a lightweight security analysis foundation built using pure Python.*

---

## 🎯 Goal

Traditional SOC scripting often relies on monolithic, hardcoded loops that break easily when log formats vary or scale up.  
This engine explores a structured approach:
* **Logs as Structured Entities:** Raw strings are parsed into immutable event models (tuples/dictionaries).
* **Decoupled Data Pipeline:** File ingestion is isolated from analytical functions.
* **Declarative Aggregation:** Reusable query and summary functions evaluate security events independently.

The objective is to analyze login activity, identify high-risk IPs, and highlight compromised accounts with a clear separation of concerns.

---

## 🧠 Core Concepts

### Event Pipeline Architecture

An event goes through a predictable transformation flow from raw text to security insight:

```text
Raw Log Line
 └── Parsing & Validation (`recepcion_datos.py`)
      └── Event Dictionary
           ├── Filtering & Searching (`buscar_*`)
           └── Security Metric Aggregation (`resumen()`)
