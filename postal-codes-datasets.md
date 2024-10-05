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

```yml
schema:
  fields:
    - name: country_code
      title: Country Code
      description: ISO 3166-1 alpha-2 code for the country.
      type: string
    - name: postal_code
      title: Postal Code
      description: Postal code for the location.
      type: string
    - name: place_name
      title: Place Name
      description: Name of the city, town, or place.
      type: string
    - name: admin_name1
      title: Administrative Name 1
      description: Primary administrative division (e.g., state, region).
      type: string
    - name: admin_code1
      title: Administrative Code 1
      description: Code for the primary administrative division.
      type: string
    - name: admin_name2
      title: Administrative Name 2
      description: Secondary administrative division (e.g., county, district).
      type: string
    - name: admin_code2
      title: Administrative Code 2
      description: Code for the secondary administrative division.
      type: string
    - name: admin_name3
      title: Administrative Name 3
      description: Tertiary administrative division (e.g., municipality, borough).
      type: string
    - name: admin_code3
      title: Administrative Code 3
      description: Code for the tertiary administrative division.
      type: string
    - name: latitude
      title: Latitude
      description: Latitude coordinate of the place.
      type: number
    - name: longitude
      title: Longitude
      description: Longitude coordinate of the place.
      type: number
    - name: accuracy
      title: Accuracy
      description: Accuracy level of the latitude and longitude coordinates.
      type: integer
    - name: alternativeCityName
      title: Alternative City Name
      description: Alternative name(s) for the city or place.
      type: string
```

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
