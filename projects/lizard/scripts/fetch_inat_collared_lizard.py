import json
import time
from pathlib import Path

import pandas as pd
import requests

BASE_OBS_URL = "https://api.inaturalist.org/v1/observations" #inat base api url
BASE_PLACE_URL = "https://api.inaturalist.org/v1/places" #inat url for identifying locations (places)

RAW_DIR = Path("data/raw") #raw data path
PROC_DIR = Path("data/processed") #processed data path
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROC_DIR.mkdir(parents=True, exist_ok=True)



# Step 1: Look up Oklahoma place_id dynamically ___

def get_place_id(place_name="Oklahoma"):
    url = "https://api.inaturalist.org/v1/places/autocomplete"
    params = {
        "q": place_name,
        "per_page": 10,
        "order_by": "area"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    results = response.json().get("results", [])

    if not results:
        raise ValueError(f"No place found for query: {place_name}")

    # Prefer a state-level match
    for place in results:
        if place.get("admin_level") == 10:
            print(f"Matched place: {place.get('display_name', place.get('name'))} (id={place['id']})")
            return place["id"]

    # fallback: first result
    place = results[0]
    print(f"Using fallback place: {place['display_name']} (id={place['id']})")
    return place["id"]


# Step 2: Fetch observations --------------------

def fetch_all_observations(place_id):
    all_results = []
    page = 1

    while True:
        params = {
            "taxon_name": "Crotaphytus collaris",
            "place_id": place_id,
            "per_page": 200,#large num to reduce calls
            "page": page,
            "order_by": "observed_on",
            "order": "asc"
        }

        response = requests.get(BASE_OBS_URL, params=params, timeout=30)
        response.raise_for_status()
        payload = response.json()

        results = payload.get("results", [])
        if not results:
            break

        all_results.extend(results)
        print(f"Fetched page {page} with {len(results)} records")

        if len(results) < params["per_page"]:
            break

        page += 1
        time.sleep(1)

    return all_results



# Step 3: Save raw JSON ------------------------

def save_raw_json(results):
    outpath = RAW_DIR / "inat_collared_lizard_oklahoma_raw.json"
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Saved raw JSON to {outpath}")


# Step 4: Flatten into Pandas DataFrame  ----------------

def flatten_results(results):
    rows = []

    for obs in results:
        taxon = obs.get("taxon") or {}
        geojson = obs.get("geojson") or {}
        coords = geojson.get("coordinates")

        longitude = None
        latitude = None
        if isinstance(coords, list) and len(coords) == 2:
            longitude, latitude = coords

        rows.append({
            "id": obs.get("id"),
            "observed_on": obs.get("observed_on"),
            "quality_grade": obs.get("quality_grade"),
            "scientific_name": taxon.get("name"),
            "common_name": taxon.get("preferred_common_name"),
            "latitude": latitude,
            "longitude": longitude,
            "positional_accuracy": obs.get("positional_accuracy"),
            "geoprivacy": obs.get("geoprivacy"),
            "captive": obs.get("captive"),
            "user": (obs.get("user") or {}).get("login"),
            "uri": obs.get("uri"),
        })

    return pd.DataFrame(rows)


# Step 5: Run functions (Find place → Pull data → Save raw → Clean → Save processed)-------------------------

def main():
    print("Looking up Oklahoma place_id...")
    place_id = get_place_id("Oklahoma")

    print("Fetching observations...")
    results = fetch_all_observations(place_id)

    print(f"Total observations fetched: {len(results)}")

    save_raw_json(results)

    df = flatten_results(results)

    out_csv = PROC_DIR / "inat_collared_lizard_oklahoma.csv"
    df.to_csv(out_csv, index=False)

    print(f"Saved processed CSV to {out_csv}")
    print(df.head())


if __name__ == "__main__": # if this file is run directly execute the main fxn (that runs all functions in the correct order)
    main()