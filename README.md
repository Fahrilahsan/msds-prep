# msds-prep

MSDS pre-program study tracker. Journey starts May 11, 2026.

## About
This repo documents my technical preparation before starting the MS in Data Science 
program at Columbia University (August 2026). The goal is to close skill gaps in 
Python engineering, math foundations, and machine learning before classes begin.

## Progress

### ✅ Week 1 — Modern Python (May 12–17, 2026)
- Built a `User` and `PaidUser` class system with OOP, inheritance, `@property`, 
  type hints, and dunder methods (`__repr__`, `__str__`, `__len__`)
- Implemented `@timer` and `@cache` decorators from scratch
- Refactored a real-world market basket analysis notebook from a wellness company 
  dataset into a clean OOP module using classes, decorators, and type hints

## Repository Structure
msds-prep/
├── users.py                          # User & PaidUser class system
├── decorators.py                     # @timer and @cache decorators
├── projects/
│   └── market_basket/
│       ├── basket_analysis.py        # Market basket analysis OOP module
│       └── cohort_masked.csv         # Masked fitness class attendance data
└── README.md

## Roadmap
- **Phase 1** (May 12 – Jun 7): Modern Python, linear algebra, probability/stats, DSA basics
- **Phase 2** (Jun 8 – Jul 5): Andrew Ng ML Specialization, A/B testing, causal inference
- **Phase 3** (Jul 6 – Aug 2): Two-tower recommender system project
- **Phase 4** (Aug 3 – Aug 28): Deploy, resume rewrite, professor outreach