# Life Sciences PhD Careers Project — Data Documentation

## Overview

This project analyzes early career outcomes for life sciences PhD recipients, with a focus on employment sector and job activities (e.g., teaching vs research).

The goal is to understand how closely doctoral training aligns with actual career outcomes.

## Research Questions

- What jobs do life sciences PhDs hold within 10 years of graduation?
- What proportion of PhDs are in teaching-focused roles?
- How do actual career outcomes compare to initial post-graduation plans?

## Data Sources

### 1. Early Career Doctorates Survey (ECDS)

Source: National Science Foundation, National Center for Science and Engineering Statistics

Early Career Doctorates Survey (ECDS) [website](https://ncses.nsf.gov/surveys/early-career-doctorates/2017)

Purpose:
- Primary dataset for analyzing job activities (teaching, research, management)
- Focuses on individuals within 10 years of earning a PhD

Use in this project:
- Identify proportion of PhDs in teaching vs research roles
- Analyze alignment between training and job responsibilities

Citation: 
National Center for Science and Engineering Statistics (NCSES). 2021. Early Career Doctorates: 2017. NSF 21-323. Alexandria, VA: National Science Foundation. Available at https://ncses.nsf.gov/pubs/nsf21323/.
---

### 2. Survey of Doctorate Recipients (SDR)

Source: National Science Foundation, National Center for Science and Engineering Statistics

Purpose:
- Longitudinal data on PhD career outcomes

Use in this project:
- Estimate employment sector distribution (academia, industry, government)
- Provide broader context for career trajectories

---

### 3. Survey of Earned Doctorates (SED)

Source: National Science Foundation, National Center for Science and Engineering Statistics

Purpose:
- Captures post-graduation plans at time of degree completion

Use in this project:
- Compare expected vs actual career outcomes

## Data Organization

- `raw/`: Original downloaded data files and documentation
- `processed/`: Cleaned datasets used for analysis
- `docs/`: Codebooks, questionnaires, and technical documentation

## Workflow

1. Download and store raw data in `raw/`
2. Clean and recode variables using scripts in `scripts/`
3. Save processed datasets in `processed/`
4. Generate figures in `outputs/figures/`
5. Display results in Quarto project pages

## Dependencies
- pandas
- openpyxl (required for reading Excel files)

## Notes and Limitations

- Job activity categories require interpretation and are self-reported (e.g., defining "teaching-heavy")
- SED captures intended outcomes, not actual employment
- Differences in survey design across datasets may affect comparability