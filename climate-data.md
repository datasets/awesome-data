
# Climate open data

Everyone can have access to climate data, however many people were not able to access the data due to various reasons: failing register on the website, 
formulating and sending request to get the right data they need.
Here we write precise 

We use several sources for open data on temperature:
1. reanalysis data from GES DISC MERRA from https://disc.gsfc.nasa.gov/
2. observational data: example data available for downloading after login http://data.ceda.ac.uk/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.0.0.0/60km/  and downloadable data link url = 'http://dap.ceda.ac.uk/thredds/fileServer/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.0.0.0/60km/tas/mon/v20181126/tas_hadukgrid_uk_60km_mon_188401-188412.nc' and https://services.ceda.ac.uk/cedasite/myceda/user/ 

# How to download the data 
1. Create account and log in to https://www.ceda.ac.uk/ 
2. Depending on the variables and time-scale of the data you want to download setup request, for example, 2010 taxmax (temperature): http://dap.ceda.ac.uk/thredds/fileServer/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.0.0.0/60km/tas/mon/v20181126/tas_hadukgrid_uk_60km_mon_201001-201012.nc



# Climate variables  
Examples of climate variables:
    surface_air_temperature 

    surface_layer_height 

    surface_pressure 

    surface_specific_humidity 

    surface_wind_speed

# Code for parcing data 

For parcing data one needs to install ´xarray´ python package.
The code for parcing the data is uploaded to the folder https://github.com/Liyubov/climate_open_data/blob/master/parse_hadukgrid.py 

You can also open and look into the climate data using command line via:
*ncdump -t tasmax_hadukgrid_uk_60km_mon_188601-188612.nc*
