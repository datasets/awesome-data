---
title: Postal Codes Datasets
description: Comprehensive collection of postal codes datasets from around the world.
keywords: postal codes, postal code datasets, geolocation data, zip codes, worldwide postal codes
date: 2024-10-01
modified: 2024-10-01
---

## Overview

Postal codes are essential for various applications like mail delivery, location-based services, demographic studies, and geographic analysis. This collection brings together datasets of postal codes from different regions worldwide to support diverse use cases in both public and private sectors.

## Metadata and data samples

This schema specifies each column's name, title, description, and type, following a format compatible with the W3C's tabular data standard.

| Name                 | Title                    | Description                                                | Type    |
|----------------------|--------------------------|------------------------------------------------------------|---------|
| country_code         | Country Code             | ISO 3166-1 alpha-2 code for the country.                   | string  |
| postal_code          | Postal Code              | Postal code for the location.                              | string  |
| place_name           | Place Name               | Name of the city, town, or place.                          | string  |
| admin_name1          | Administrative Name 1    | Primary administrative division (e.g., state, region).     | string  |
| admin_code1          | Administrative Code 1    | Code for the primary administrative division.              | string  |
| admin_name2          | Administrative Name 2    | Secondary administrative division (e.g., county, district).| string  |
| admin_code2          | Administrative Code 2    | Code for the secondary administrative division.            | string  |
| admin_name3          | Administrative Name 3    | Tertiary administrative division (e.g., municipality, borough).| string  |
| admin_code3          | Administrative Code 3    | Code for the tertiary administrative division.             | string  |
| latitude             | Latitude                 | Latitude coordinate of the place.                          | number  |
| longitude            | Longitude                | Longitude coordinate of the place.                         | number  |
| accuracy             | Accuracy                 | Accuracy level of the latitude and longitude coordinates.  | integer |
| alternativeCityName  | Alternative City Name    | Alternative name(s) for the city or place.                 | string  |

### Sample data France

<FlatUiTable
  data={{
    "url": "https://postal.datahub.io/fr.csv"
  }}
/>

## Version control and storage

We store the data in the S3 API compatible object storage which allows our users to leverage popular libraries and SDKs designed for AWS S3. For example, you can easily integrate the data into your application using boto3 for Python. There are many other alternatives for other programming languages.

Using object storage we can organize data by the date when it was gathered. While always keeping the “latest” version available with a persistent prefix, we provide the ability to look through historical versions of the data. Below is a reflection of directory (prefix) structure in our blob storage:

```bash
/postal-codes/
│
├── US/
│   ├── latest/
│   │   └── 0.csv
│   ├── 2024-10-01/
│   │   └── 0.csv
│   ├── 2024-09-01/
│   │   └── 0.csv
│   └── ...
│
├── CA/
│   ├── latest/
│   │   └── 0.csv
│   ├── 2024-10-01/
│   │   └── 0.csv
│   ├── 2024-09-01/
│   │   └── 0.csv
│   └── ...
│
├── GB/
│   ├── latest/
│   │   └── 0.csv
│   ├── 2024-10-01/
│   │   └── 0.csv
│   ├── 2024-09-01/
│   │   └── 0.csv
│   └── ...
│
└── ...
```

In this structure:

- The bucket name is `postal-codes/`.
- Each country has its own two-letter country code directory (e.g., `US/`, `CA/`, `GB/`).
- Inside each country directory, there is:
  - A `latest/` folder containing the most up-to-date CSV file named `0.csv`.
  - Date-named directories (`YYYY-MM-DD` format) that contain CSV files for postal codes data as it existed on those specific dates.
  - Note that files are named by index for simplicity when writing a script, i.e., the first file is always `0.csv` and if there are more than a single file per country, users can expect it to be called `1.csv` and so on.

## Policy

* Country, regional, state or city level postal codes datasets depending on administrative divisions in the given country/region.
* Updated **monthly** to include new changes in postal code allocations.

## State of the World

* On a global level, open datasets for postal codes are available, but the granularity and coverage can vary. For some countries, postal code datasets include detailed location data such as state/region details, city information and so on.
* On a local level, many countries maintain official postal code datasets that are regularly updated to reflect new allocations, discontinuations, and changes in geographical boundaries.

Parameters

* Postal code
* Administrative division (city, region etc.) 
* Additional metadata can be provided in a separate dataset.

## Sources

* Global sources for standard publicly available datasets.
* Country-specific sources. Please, inquire for more details.
