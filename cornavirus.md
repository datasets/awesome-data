---
title: Novel Coronavirus 2020
description: Data and analysis on the Coronavirus Pandemic
keywords: Coronavirus, Covid-19
date: 2020-03-21
modified: 2020-03-21
image: 
---

Qu: What are the key figures of Covid-19 worldwise, such as:
- total number of people infected,
- total number of people recovered,
- and total number of people that died.

An: Novel Coronavirus 2019 time series case data for confirmed, recovered and deaths - https://datahub.io/core/covid-19

---

## README

The [Severe acute respiratory syndrome Coronavirus 2](https://en.wikipedia.org/wiki/Severe_acute_respiratory_syndrome_coronavirus_2) (SARS-CoV-2) has had a worldwide effect. The World Health Organization (WHO) on March 11 declared COVID-19 ([Coronavirus disease 2019](https://en.wikipedia.org/wiki/Coronavirus_disease_2019)) a pandemic, pointing to the over 118,000 cases of the coronavirus illness in over 110 countries and territories around the world at the time. 

This dataset provides time series data tracking the number of people affected by COVID-19 worldwide, including:

- confirmed tested cases of Coronavirus infection
- how many have reportedly died while sick with Coronavirus
- the number of people who have reportedly recovered from it

## Data

The [Johns Hopkins University Center for Systems Science and Engineering](https://systems.jhu.edu/) (CSSE) has been doing a great public service from an early point by sharing data on the epidemic on the [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19) repository.

This Data Package is currently updated daily from there. 

## Preparation

We have normalized data a bit - unpivoted and transfered dates to be more machine readable.

This repository uses [dataflows](https://github.com/datahq/dataflows) to process and normalize the data. Install `dataflows`, so you can run the update with:

```
python process.py
```

## Data

CSSE currently list the following upstream datasources:

- World Health Organization (WHO): https://www.who.int/
- DXY.cn. Pneumonia. 2020. http://3g.dxy.cn/newh5/view/pneumonia.
- BNO News: https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/
- National Health Commission of the People’s Republic of China (NHC):
- http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml
- China CDC (CCDC): http://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm
- Hong Kong Department of Health: https://www.chp.gov.hk/en/features/102465.html
- Macau Government: https://www.ssm.gov.mo/portal/
- Taiwan CDC: https://sites.google.com/cdc.gov.tw/2019ncov/taiwan?authuser=0
- US CDC: https://www.cdc.gov/coronavirus/2019-ncov/index.html
- Government of Canada: https://www.canada.ca/en/public-health/services/diseases/coronavirus.html
- Australia Government Department of Health: https://www.health.gov.au/news/coronavirus-update-at-a-glance
- European Centre for Disease Prevention and Control (ECDC): https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases
- Ministry of Health Singapore (MOH): https://www.moh.gov.sg/covid-19
- Italy Ministry of Health: http://www.salute.gov.it/nuovocoronavirus

We will endeavour to provide more detail on how regularly and by which technical means the data is updated. Additional background is available in the [CSSE blog](https://systems.jhu.edu/research/public-health/ncov/), and in the [Lancet paper](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30120-1/fulltext) ([DOI](https://doi.org/10.1016/S1473-3099(20)30120-1)), which includes this figure:

![](https://i.imgur.com/X32lUEU.png)

## License

The data comes from public sources and was primarily collated via John Hopkins University on GitHub. We have used that data and processed it further, and are releasing the results under the Public Domain Dedication and License.

We are also explicitly licensing any contribution of ours under that license.




