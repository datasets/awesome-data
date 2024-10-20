---
title: Coronavirus Data and Resources
description: A collection of the most important, relevant datasets on Coronavirus (COVID-19) outbreak.
keywords: coronavirus, covid-19, health, epidemic
date: 2020-03-25
modified: 2020-03-25
image: climate-change.png
---

Coronavirus disease 2019 (COVID-19) time series listing confirmed cases, reported deaths and reported recoveries. Data is disaggregated by by country (and sometimes subregion). Coronavirus disease (COVID-19) is caused by the [Severe acute respiratory syndrome Coronavirus 2 (SARS-CoV-2)][sars2] and has had a worldwide effect. On March 11 2020, the World Health Organization (WHO) declared it a pandemic, pointing to the over 118,000 cases of the coronavirus illness in over 110 countries and territories around the world at the time.

[covid]: https://en.wikipedia.org/wiki/Coronavirus_disease_2019
[sars2]: https://en.wikipedia.org/wiki/Severe_acute_respiratory_syndrome_coronavirus_2

## Cases, Deaths and Recoveries

Primary Dataset: https://datahub.io/core/covid-19

This dataset includes time series data tracking the number of people affected by COVID-19 worldwide, including:

* confirmed tested cases of Coronavirus infection
* how many have reportedly died while sick with Coronavirus
* the number of people who have reportedly recovered from it

Data is in CSV format and updated daily. It is sourced from [this upstream repository](https://github.com/CSSEGISandData/COVID-19) maintained by the amazing team at [Johns Hopkins University Center for Systems Science and Engineering](https://systems.jhu.edu/) (CSSE) who have been doing a great public service from an early point by collating data from around the world.

Data is cleaned and normalized, for example tidying dates and consolidating several files into normalized time series. There is also metadata such as column descriptions.

### Sources

The upstream dataset currently lists the following upstream datasources:

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
- ECDC dataset https://www.ecdc.europa.eu/en/coronavirus
- Metadata on publications about coronavirus https://github.com/nties/COVID19-open-research-dataset 
- Open data resources for fighting COVID https://arxiv.org/abs/2004.06111v1

Additional background is available in the [CSSE blog](https://systems.jhu.edu/research/public-health/ncov/), and in the [Lancet paper](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30120-1/fulltext) ([DOI](https://doi.org/10.1016/S1473-3099(20)30120-1)), which includes this figure:

![](https://i.imgur.com/X32lUEU.png)

## Cases By Country

For now see https://datahub.io/core/covid-19 as that includes aggregate figures by country. For additional sources (verified and crowd-sourced) https://github.com/open-covid-19/data


### US

Data sources: COVID Tracking Project in USA https://covidtracking.com/  
New York Times data from https://github.com/nytimes/covid-19-data 


Data information: 
COVID Tracking Project in USA provides the information from state/district/territory public health authorities—or, occasionally, from trusted news reporting, official press conferences, or (very occasionally) tweets or Facebook updates from state public health authorities or governors.
Data from New York Times is State-Level Data

State-level data can be found in the states.csv file. (Raw CSV file here.)

date,state,fips,cases,deaths
2020-01-21,Washington,53,1,0

### Italy

Data source: https://github.com/pcm-dpc/COVID-19


Data information:
In order to inform citizens and make available the data collected, useful only for communication and information purposes, the Civil Protection Department has developed an interactive geographical dashboard that can be reached at http://arcg.is/C1unv (desktop version) and http://arcg.is/081a51 (mobile version) and makes available, under license CC-BY-4.0, the following information updated daily at 6:30 p.m. (following the press conference of the Head of Department):

    National trend
    Json data
    Provinces data
    Regions data
    Summary sheets
    Areas
    Notes

### United Kingdom

Data source: https://github.com/tomwhite/covid-19-uk-data


Data information: 
The following CSV files are available:

    data/covid-19-cases-uk.csv: daily counts of confirmed cases for (upper tier) local authorities in England, health boards in Scotland and Wales, and local government district for Northern Ireland.
        Note that prior to 18 March 2020 Wales data was broken down by local authority, not heath board, and prior to 27 March 2020 there were no breakdowns by area for Northern Ireland.
    data/covid-19-totals-uk.csv: daily counts of tests, confirmed cases, deaths for the whole of the UK
    data/covid-19-totals-england.csv: daily counts of tests, confirmed cases, deaths for England
    data/covid-19-totals-northern-ireland.csv: daily counts of tests, confirmed cases, deaths for Northern Ireland
    data/covid-19-totals-scotland.csv: daily counts of tests, confirmed cases, deaths for Scotland
    data/covid-19-totals-wales.csv: daily counts of tests, confirmed cases, deaths for Wales
    data/covid-19-indicators-uk.csv: daily counts of tests, confirmed cases, deaths for the whole of the UK and individual countries in the UK (England, Scotland, Wales, Northern Ireland). This is a tidy-data version of covid-19-totals-*.csv combined into one file.

### France

Data source: https://github.com/cedricguadalupe/FRANCE-COVID-19


Data information: 
Data is updated daily according to the main sources of information: 
Agence Regionale de Sante;    Santé Publique France : https://www.santepubliquefrance.fr/;   Geodes: https://geodes.santepubliquefrance.fr/#c=indicator&view=map2

The github repository wih data contains three main files with confirmed cases, number of death and number of recovered people.

    france_coronavirus_time_series-confirmed.csv
	france_coronavirus_time_series-deaths.csv 	
	france_coronavirus_time_series-recovered.csv

## Models
There are various types of models in epidemiology, which are used for prediction of prevalence (total number of infected) or the duration of an epidemic spreading processes. One of the most commonly used types is compartmental models, where population is divided into compartments of people with the same properties, e.g. people who are susceptible to virus, who are recovered etc.
There are three main types of compartmental models in epidemiology based on which many other models can be built upon: 
    Susceptible-Infected (SI), where each person can be just in two states, either susceptible (S) or infected (I); 
     Susceptible-Infected-Recovered (SIS), where each person can be in one of two states, susceptible (S) or infected (I), but then can become susceptible again;
     Susceptible-Infected-Recovered (SIR), where each person can be  in one of three states, susceptible (S), infected (I) or recovered (R).
     

In **SIR model** one can study the number of people in each of three compartments: susceptible, infected and recovered, denoted by variable S, I and R correspondingly. SIR system can be  expressed by the set of ordinary differential equations proposed by [O. Kermack and Anderson Gray McKendrick](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology). 

The simulations of SIR model are shown in the python script [here](https://github.com/Liyubov/heterogeneous-dynamics-on-networks/blob/master/code_network_heterogen_models/spreading_SIR.py).

The main take-away message from the SIR model simulations is that we observe so-called peak of epidemic, when the number of infected people reaches its maximum. This moment of when size of epidemic outbreak is maximal depends on SIR model parameters: probability of epidemic transmission and recovery from the disease. 

Another model, which has been proven to be much more realistic for some epidemics spreading models is **SEIR model** [1]. 
The main idea of this model is that for many important infections there is a significant incubation period during which individuals have been infected but are not yet infectious themselves. During this period the individual is in a special state E (exposed), additional state to three states of parts of population in SIR model. 

The SEIR model studies number of people between four states: susceptible (S), exposed (E), infected (I), and resistant (R) , each being the number of people in those groups. There are several model parameters, which partially control how fast people move from being susceptible to exposed, from exposed to infected, and from infected to resistant. This model can have additional parameters; one is the background mortality, which is unaffected by disease-state, while the other is vaccination. The vaccination moves people from the susceptible to resistant directly, without becoming exposed or infected.
The SEIR model is the most widely used tool for predicting epidemics and acting to suppress them. In 2020, the model was further refined by Richard Neuer [3].


## References:
1. [Maslov et al. "Window of Opportunity for Mitigation to Prevent Overflow of ICU capacity in Chicago by COVID-19"](https://arxiv.org/abs/2003.09564)
2. [Pastor-Satoras et al. "Epidemic processes in complex networks"](https://arxiv.org/abs/1408.2701)
3. [COVID model by Neuer](https://neherlab.org/covid19/)
4. [O. Kermack and Anderson Gray McKendrick](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology)
5. Simulations of SIR and SEIR models [here](https://github.com/Liyubov/heterogeneous-dynamics-on-networks/blob/master/code_network_heterogen_models/spreading_SIR.py)
