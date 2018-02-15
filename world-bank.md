---
title: World Bank Data
description: An overview of the World Bank data holdings
---

The World Bank has a wide array of high quality data and much of it is [open data][[]. It includes over 15 major databases with more than 2000 indicators.

[open data]: https://opendefinition.org/

## Data

There are a variety of different databases.

One of the major open ones are the World Development Indicators which provide a variety of important indicators ranging from GDP and population to CO2 emissions and literacy in a standardized cross country form.

## API

The World Bank has a data API. You can use this to access a variety of data including the world developemn

You can get data in CSV, JSON and XML (default).

Per indicator:

```bash
https://api.worldbank.org/indicator/GC.DOD.TOTL.GD.ZS?format=csv

# for some reason json format just yields metadata
https://api.worldbank.org/indicator/GC.DOD.TOTL.GD.ZS?format=json
```

More elaborate queries documented in http://blogs.worldbank.org/opendata/first-steps-in-integrating-open-data:

```
http://api.worldbank.org/en/countries/KE;XF;XM/indicators/EN.ATM.CO2E.PC?date=1961:2011&format=csv

```
http://api.worldbank.org/en/countries/KE;XF;XM/indicators/EN.ATM.CO2E.PC?date=1961:2011&format=json
```

## License: OPEN (mostly)

Currently no easy way to automatedly obtain that listing though.

As of April 20th 2010 data is now open (subject to some reservations for specific datasets). See this [blog post](http://blog.okfn.org/2010/04/20/world-bank-opens-up-development-data/).

### License Details

[Terms of use summary](http://data.worldbank.org/summary-terms-of-use) state:

> You are free to copy, distribute, adapt, display or include the data in other products for commercial and noncommercial purposes at no cost subject to certain limitations summarized below.
> 
> You must include attribution for the data you use in the manner indicated in the metadata included with the data.
> 
> You must not claim or imply that The World Bank endorses your use of the data by or use The World Bank’s logo(s) or trademark(s) in conjunction with such use.
>
> Other parties may have ownership interests in some of the materials contained on The World Bank Web site. For example, we maintain a list of some specific data within the Datasets that you may not redistribute or reuse without first contacting the original content provider, as well as information regarding how to contact the original content provider. Before incorporating any data in other products, please check the list: Terms of use: Restricted Data
>
> The World Bank makes no warranties with respect to the data and you agree The World Bank shall not be liable to you in connection with your use of the data.

