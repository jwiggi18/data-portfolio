# Life Sciences PhD Careers Project — Data Documentation

## Data Organization

- `raw/`: Original downloaded data files and documentation
- `processed/`: Cleaned datasets used for analysis
- `docs/`: Codebooks, questionnaires, and technical documentation

# Data Sources

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


The ECDS has no API therefore the following data tables were dowloaded directly from the ecds [website]() in .xlsx format anhttps://ncses.nsf.gov/surveys/early-career-doctorates/2017d saved in data/raw/ecdcs/:
- employment_setting.xlsx
- position_type.xlsx
- sex_ethnicity.xlsx

The raw data were cleaned scripts/clean_ecdcs_data.py. 

The following subsets of the full spreadsheets were produced and stored in data/processed/ecdcs/. 

position_type.xlsx subsets
- position_all_biology.xlsx = Three rows from the raw spreadsheet that contain biology PhDs
    - position_bio_ag_life: "Agricultural and environmental life sciences"
    - position_ag_life: "Agricultural and environmental life sciences"
    - postion_bio_biomed: "Biological and biomedical sciences"
-
-
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



