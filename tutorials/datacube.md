# **Analysis Ready Data (ARD) and the FORCE Data Cube Collection 1**

This tutorial describes the Analysis Ready Data provided in the [FORCE Data Cube Collection 1](https://code-de.org/de/portfolio/?id=78) on CODE-DE and EOLab.
Users can process the data with FORCE as introduced in the [following tutorial](DEADLINK).


# 1. Analysis Ready Data and Data cubes

The *FORCE Data Cube Collection 1* provides Analysis Ready Data *(ARD)*.

> According to the Committee on Earth Observation Satellites ([&rarr; CEOS](https://ceos.org/ard/)), ARD are *satellite data that have been processed to a minimum set of requirements and organized into a form that allows immediate analysis with a minimum of additional user effort and interoperability both through time and with other datasets.*

Since the reflectance measurements taken onboard the satellite, ARD have undergone a complex process, including radiometric calibration, georectification, the correction of atmospheric and topographic effects, cloud and cloud shadow detection and other acquisition quality-based criteria.
Finally, ARD are provided in a regular, non-overlapping grid system without any redundancy in a single coordinate system in the form of data cubes.
ARD are immediately usable for many applications without further processing.
Data cubes enable the interoperability and comparability of data, and facilitate data handling.
The original images are spatially reorganized in the regular tile grid with a common projection to ensure that further processing is not affected by incongruent scene footprints or inconsistencies in the extent of different datasets.
The data is also temporally organized, i.e. stored in a time-ordered manner.
This facilitates time series analysis within, but also across sensor systems and datasets.


# 2. Data in the FORCE Data Cube Collection 1 on CODE-DE / EOLab

## 2.1 Input Data

The FORCE Data Cube Collection 1 provides Analysis Ready Data (ARD) for Germany from 1984 to today, generated based on Level-1 Landsat and Sentinel-2 imagery (i.e. radiometrically calibrated and georectified).
Only Level-1 data that fulfilled the following criteria were processed to ARD:

- The estimated cloud cover, according to the ESA/USGS metadata, is lower than 70%
- The estimated cloud cover, according to the FORCE’s internal cloud masking, is lower than 90%
- Only Tier 1 image acquisitions from Landsat are included, which represent the highest available data quality

The FORCE Data Cube provides observations of the following sensor types:

- Landsat 4 Thematic Mapper (TM), Collection 2 ([technical facts](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-4?qt-science_support_page_related_con=0#qt-science_support_page_related_con))
- Landsat 5 Thematic Mapper (TM), Collection 2 ([technical facts](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-5?qt-science_support_page_related_con=0#qt-science_support_page_related_con))
- Landsat 7 Enhanced Thematic Mapper + (ETM+), Collection 2 ([technical facts](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-7?qt-science_support_page_related_con=0#qt-science_support_page_related_con))
- Landsat 8 Operational Land Imager (OLI), Collection 2 ([technical facts](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-8?qt-science_support_page_related_con=0#qt-science_support_page_related_con))
- Landsat 9, Operational Land Imager 2 (OLI-2), Collection 2 ([technical facts](https://www.usgs.gov/landsat-missions/landsat-9?qt-science_support_page_related_con=0#qt-science_support_page_related_con))
- Sentinel-2A MultiSpectral Instrument (MSI, [technical facts](https://sentinel.esa.int/web/sentinel/missions/sentinel-2))
- Sentinel-2B MultiSpectral Instrument (MSI, [technical facts](https://sentinel.esa.int/web/sentinel/missions/sentinel-2))

While Landsat TM/ETM+/OLI data is available at a spatial resolution of 30x30 m per pixel, the resolution of Sentinel-2 A/B imagery is 10x10 m per pixel.


## 2.2 Pre-Processing and Analysis Ready Data

Level-1 data from all sensors provided in the FORCE Data Cube Collection 1 are pre-processed to ARD according to a standardized workflow (Figure 1).
 
IMAGE

*Figure 1: FORCE ARD Processing System Workflow (source: Frantz et al.
2019, modified).*

This article explains the components of this workflow and the parameters used for pre-processing data in the FORCE Data Cube Collection 1.

___

### Cloud and cloud shadow detection and masking

Data in the FORCE Data Cube Collection 1 have undergone a cloud and cloud shadow detection and masking procedure.
As optical sensors cannot “see through clouds”, this is necessary to avoid spectral artefacts that do not reveal information about the land surface.

In the FORCE Data Cube Collection 1, pixels detected as opaque clouds are represented as no data (confident cloud category in table 1).

Cloud detection was performed by an Fmask algorithm ([Zhu & Woodcock 2012](https://doi.org/10.1016/j.rse.2011.10.028)), modified by recent improvements ([Frantz et al. 2015](https://doi.org/10.1109/LGRS.2015.2390673), [Zhu et al. 2015](https://doi.org/10.1016/j.rse.2014.12.014)).

For Sentinel-2, a Cloud Displacement Index was implemented to compensate missing thermal information (such as available in Landsat) employing parallax effects ([Frantz et al. 2018](https://doi.org/10.1016/j.rse.2018.04.046)).

Parallax effects make use of slightly different image acquisition angles in spectrally adjacent near infrared bands that have an effect on cloud positioning, and are invisible on land surface features (*Figure 2*).
 The FORCE cloud detection was rigorously assessed in the Cloud Masking Intercomparison eXercise (CMIX, [Skakun et al. 2022](https://doi.org/10.1016/j.rse.2022.112990)).

IMAGE

*Figure 2: Parallax effects for cloud detection in Sentinel-2 imagery*

After cloud and cloud shadow detection, a buffer mask of 300 m was applied around clouds (90 m around cloud shadow) in order to make sure that hazy transition zones between clouded and non-clouded areas not detected as clouds do not contaminate the image chip.

Cloud masking information can be found in the [QAI output file](link to following section; Data Output).

___

### Radiometric correction

ARD in the FORCE Data Cube Collection 1 have been atmospherically corrected ([Frantz et al. 2016](https://doi.org/10.1109/TGRS.2016.2530856)).
Atmospheric correction converts top-of-atmosphere reflectance to bottom-of-atmosphere reflectance (or surface reflectance).
This was achieved through radiative transfer modelling using multiple scattering assumptions and image-based estimation of atmospheric parameters, e.g.
aerosol optical depth, as well as water vapor for Sentinel-2.
Auxiliary information on water vapor was used to correct Landsat data ([Frantz et al. 2019](https://doi.org/10.3390/rs11030257)).

The 1 arc-second Copernicus Digital Elevation Model was used to adjust path lengths in the atmospheric correction.
FORCE’s atmospheric correction functionalities are described in [Frantz et al. 2016](https://doi.org/10.1109/TGRS.2016.2530856) and have been globally validated in the Atmospheric Correction Inter-comparison eXercise (ACIX, [Doxani et al.
2018](https://doi.org/10.3390/rs10020352)) as well in ACIX II (Doxani et al., in preparation).

The ARD were also corrected for other radiometric phenomena like adjacency, bidirectional reflectance distribution function (BRDF), and topographic effects.
Adjacency effect correction aims to reduce the background contamination with radiation that does not originate from the observed target.
BRDF correction aims to normalize the reflectance to a standardized view and sun angle.
Topographic correction aims at removing illumination effects that are introduced by different solar angles in combination with sloped terrain.
For the latter, an enhanced C-correction (see [Buchner et al. 2020](https://doi.org/10.1016/j.rse.2020.111967)) with the 1 arc-second Copernicus DEM was used.


### Co-registration

ARD from Sentinel-2 A/B image acquisitions in the FORCE Data Cube Collection 1 have been co-registered with Landsat data.
Co-registration is required for all Sentinel-2 A/B data acquired before the use of the Sentinel-2 Global Reference Image (GRI, Dechoz et al.
2015).
These data are affected by a geolocation uncertainty of up to 12m, which corresponds to more than one Sentinel-2 pixel.
In the FORCE Data Cube Collection 1, those effects were reduced by increasing Sentinel-2 geometric accuracy with a series of Landsat base images ([Rufin et al.
2021](https://doi.org/10.1109/LGRS.2020.2982245)).
Figure 3 illustrates the difference of co-registered and original imagery.

IMAGE

Figure 3: Animation of original and co-registered Sentinel-2 images on Crete
Please find more information about how and why to co-register Sentinel-2 data with Landsat data in the [FORCE Co-Registration tutorial](https://force-eo.readthedocs.io/en/latest/howto/coreg.html).

____

### Resolution Merge

For Sentinel-2A/B imagery, pre-processing included a resolution merge of the bands that are only available at 20x20 m resolution (red edge bands, broad near-infrared band, and short-wave infrared bands).
In order to enable further analysis of ARD data with consistent spatial resolution, information at 20x20 m resolution was increased to a resolution of 10x10m using the ImproPhe data fusion approach ([Frantz et al.
2016b](https://doi.org/10.1109/TGRS.2016.2537929)).

____

### Auxiliary Data

A digital elevation model *(DEM)* mosaic covering the complete study area and a precompiled water vapor database *(WVDB)* are used for topographic and atmospheric correction of the Level-1 data.

The DEM is used for enhanced cloud shadow detection, atmospheric correction, and to perform the topographic correction.
In the cloud shadow detection, the DEM is primarily used to distinguish cloud shadows from water and topographic shadows.
In the atmospheric correction, the DEM is used to scale the optical depths with altitude.
In the FORCE Data Cube Collection 1, the Copernicus DEM is used for these purposes.

During atmospheric correction, the effect of water vapor absorption can only be corrected if the amount of water vapor in the atmosphere is known.
Sentinel-2A/B data includes a water vapor channel to directly estimate water vapor content.
In contrast, Landsat sensors do not have such information on board, which is why an external dataset is required.
The FORCE Data Cube Collection 1 uses a *MODIS*-based water vapor database providing daily water vapor estimates for the WRS-2 tiles that Landsat Level-1 data is provided in for download.
Please find a detailed description of the water vapor database of the FORCE Data Cube in [Frantz et al. (2019)](https://doi.org/10.3390/rs11030257).


## 2.3 The FORCE Data Cube Collection 1

The FORCE Data Cube Collection 1 makes use of the data cube concept.
This means that during ARD generation, Level-1 Landsat and Sentinel-2 data are reorganized from WRS-2 and MGRS scene tiles to a common coordinate system and in regular, non-overlapping tiles by splitting the data into image chips.
Redundancy is prevented by aggregation of same-day/same-sensor data on output, i.e., redundant Level 1 data are not carried to Level 2.
Figure xxx displays the key elements of the data cube and grid structure as used in the FORCE Data Cube Collection 1.

Figure xxx: The data cube concept in FORCE
The grid is the regular spatial subdivision of the land surface in the target coordinate system.
The grid origin is the location, where the tile numbering starts with zero.
Tile numbers increase toward the South and East.
The origin of the FORCE Data Cube Collection 1 is at -25° longitude and 60° latitude.
This makes the tiles with the X-identifier X0052 the most western tiles in Germany.
The tile is one entity of the grid, i.e.a grid cell with a unique tile identifier, e.g.
X0069_Y0043.
The tile is stationary, i.e.it always covers the same extent on the land surface, e.g.
X0069_Y0043 holds a part of the Berlin metropolitan area.
The tile size is 30x30 km in the FORCE Data Cube Collection 1.
Each Level-1 image is partitioned into several chips, i.e.any original image is intersected with the grid and then tiled into chips.
Chips are grouped in datasets, which group data according to acquisition date and sensor.
The data cube groups all datasets within a tile in a time-ordered manner.
The FORCE Data Cube Collection 1 provides data from 1984 to today.
The data cube may contain data from several sensors and different resolutions, such as Landsat 30x30 m or Sentinel-2 10x10 m resolution.
The FORCE Data Cube Collection 1 grid uses the ETRS89-extended / LAEA Europe (EPSG: 3035) projection.
The Grid provides Landsat and Sentinel-2 data coverage for all tiles that intersect with German state territory (Figure xxx).



Figure xxx: screenshot Germany with grid, including tile identifiers.
Spatial extent: lower left 4016030/2654920, upper right 4706030/3584920 (in m).
The FORCE Data Cube Collection 1 grid can be downloaded as a geopackage file here.
The data cube is accompanied by a data cube definition file Data Cube-definition.prj.
This file is key for all FORCE further processing of ARD.
Each higher-level module will save a copy of this file in the corresponding output directory, which must not be modified or removed in order to preserve FORCE functionalities.
It contains the data cube projection in well-known text (WKT), the grid origin as longitude and latitude, the grid origin as x-coordinate and y-coordinate in projection units (meter for the FORCE Data Cube Collection 1), the tile size in meters, and the block size in meters (required for higher-level analysis routines, see Tutorial T13).
The Data Cube definition file of the FORCE Data Cube Collection 1 looks like this:

```
PROJCS["ETRS89 / LAEA Europe",GEOGCS["ETRS89",DATUM["European_Terrestrial_Reference_System_1989",SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],AUTHORITY["EPSG","6258"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4258"]],PROJECTION["Lambert_Azimuthal_Equal_Area"],PARAMETER["latitude_of_center",52],PARAMETER["longitude_of_center",10],PARAMETER["false_easting",4321000],PARAMETER["false_northing",3210000],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AUTHORITY["EPSG","3035"]]
-25.000000
60.000000
2456026.363042
4574919.607965
30000.000000
3000.000000
```

### Output format and naming conventions

ARD in the FORCE Data Cube Collection 1 are structured according to their tile identifier.
FORCE has a standardized naming convention for all ARD output files.
Please see the documentation for further details.
The files can be accessed as follows:
X00xx_Y00yy/YYYYMMDD_LEVEL2_SENSOR_*.tif
Here, X00xx_Y00yy describes the tile identifier, for example X0069_Y0043 for a part of the Berlin metropolitan area.

All file names are characterized by a leading date, indicating the year, month and day of the respective image acquisition, for example 20210627 for the 27th of June 2021.

LEVEL2 is a standard filename component of all FORCE-generated ARD.

All file names contain a sensor identifier (LND04, LND05, LND07, LND08 for the Landsat sensors, and SEN2A, SEN2B for Sentinel-2 sensors).
* is a 3-digit placeholder for the product type generated along with ARD pre-processing (see following paragraph).
FORCE Data Cube Collection 1 output files are provided as compressed geotiff files with internal block structure.

### FORCE Data Cube Collection 1 product types

#### Bottom-of-atmosphere (BOA)

Bottom-of-Atmosphere (BOA) reflectance is the standard ARD product in the FORCE Data Cube Collection 1.
BOA represents multi-band reflectance values of the respective sensor.
All bands are provided at the same spatial resolution (10x10 m for Sentinel-2, 30x30 m for Landsat).
Values are scaled with 10000 (i.e.100% reflectance = 10000), the no data value is -9999.
Negative reflectance values are possible due to the nature of the atmospheric correction.
The files do not include bands intended for atmospheric characterization (e.g.
thermal.
ultra-blue, water vapor or cirrus bands).
Landsat ARD contain six bands (blue, green, red, near infrared, short-wave infrared 1 and 2), and Sentinel-2 ARD contain ten bands (Landsat bands plus three red edge bands, and the broad near infrared band).
Please see the FORCE documentation for sensor-specific band tables.

#### Quality Assurance Information (QAI)

The Quality Assurance Information (QAI) contains all per-pixel quality information generated by FORCE.
FORCE provides a description of the quality of each pixel in the form of quality bits.
The bits represent combinations of surface, atmospheric, and processing-related conditions.
FORCE uses a 16-bit file format, which is why 16 quality bits can be stored in the QAI fi.e.Bit No.
Parameter name
Bit comb.
Integer
State

0
Valid data
0
0
valid

1
1
no data

1–2
Cloud state
00
0
clear

01
1
less confident cloud (i.e., buffered cloud)

10
2
confident, opaque cloud

11
3
cirrus

3
Cloud shadow flag
0
0
no

1
1
yes

4
Snow flag
0
0
no

1
1
yes

5
Water flag
0
0
no

1
1
yes

6–7
Aerosol state
00
0
estimated (best quality)

01
1
interpolated (mid quality)

10
2
high (aerosol optical depth > 0.6, use with caution)

11
3
fill (global fallback, low quality)

8
Subzero flag
0
0
no

1
1
yes (use with caution)

9
Saturation flag
0
0
no

1
1
yes (use with caution)

10
High sun zenith flag
0
0
no

1
1
yes (sun elevation < 15°, use with caution)

11–12
Illumination state
00
0
good (incidence angle < 55°, best quality for top.
correction)

01
1
medium (incidence angle 55°–80°, good quality for top.
correction)

10
2
poor (incidence angle > 80°, low quality for top.
correction)

11
3
shadow (incidence angle > 90°, no top.
correction applied)

13
Slope flag
0
0
no (cosine correction applied)

1
1
yes (enhanced C-correction applied)

14
Water vapor flag
0
0
measured (best quality, only Sentinel-2)

1
1
fill (scene average, only Sentinel-2)

15
Empty
0
0
TBD


The QAI file enables the user to assess the overall usefulness of a given pixel for a particular application.
For example, the following quality bit sequence represents a valid, cloud- and cloud shadow-free, snow-free observation over land, well-illuminated, but with a slope > 2° based on the topographic correction procedure.
Bit:
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0


Flag:
0
0
1
0
0
0
0
0
0
0
0
0
0
0
0
0





Check out this documentation  for further information about single quality bit conditions, and this tutorial, which explains what quality bits are, how quality bits are implemented in FORCE, how to visualize them, and how to deal with them in further analysis.

#### Cloud / Cloud shadow /Snow distance (DST)

The Cloud / cloud shadow / snow distance (DST) product gives the distance to the next opaque cloud, buffered cloud, cirrus cloud, cloud shadow or snow.
The unit is meters, and nodata value is -9999.
This product can be used in FORCE for further analysis to generate Best Available Pixel (BAP) composites.
Note that this is not the actual cloud mask, which can rather be found in the QAI product!

#### Haze Optimized Transformation (HOT)

The Haze Optimized Transformation (HOT) product contains the HOT index, which is computed on Level-1 Top-of-atmosphere reflectance.
The HOT is useful to avoid hazy and residual cloud contamination.
The scale is 10000, and nodata value is -9999.
This product can be used in FORCE for further analysis to generate Best Available Pixel (BAP) composites.

#### Overview (OVV)

The overview file is the only one that comes as a .jpg file without geolocation information.
The overview file is a small thumbnail of the actual image chip that allows a quick preview without loading the multi-band image chip (Figure xxx).
The detected clouds and cloud shadows are colored in pink and cyan.
Cirrus clouds are drawn in red, snow in yellow, subzero reflectance in teal, and saturated reflectance in brown.

Figure xxx: Overview (OVV) image 20210627_LEVEL2_SEN2A_OVV.jpg

#### View zenith (VZN)

The View zenith (VZN) product contains the view zenith (the average view zenith for Sentinel-2, and an approximated view zenith for Landsat).
The scale is 100, and nodata value is -9999.
This product can be used in FORCE for further analysis to generate Best Available Pixel (BAP) composites.

# Further Reading

FORCE Documentation: https://force-eo.readthedocs.io/en/latest/index.html
FORCE Tutorials: https://force-eo.readthedocs.io/en/latest/howto/index.html
FORCE Publications: https://force-eo.readthedocs.io/en/latest/refs.html#refs
Standard reference: Frantz, D.
(2019): FORCE – Landsat + Sentinel-2 Analysis Ready Data and beyond: Remote Sensing 11, 1124.
Doi: http://doi.org/10.3390/rs11091124
FORCE Code: https://github.com/davidfrantz/force
FORCE on ResearchGate: https://www.researchgate.net/project/FORCE-Framework-for-Operational-Radiometric-Correction-for-Environmental-monitoring

# How to use Analysis Ready Data in the FORCE Data Cube Collection 1?

ARD provided by the FORCE Data Cube Collection 1 can be further processed and analyzed by CODE-DE users using FORCE processing functionalities.
Please use this tutorial [here: Link to Tutorial T13] as a starting point and the FORCE documentation for a more detailed description.


# References

Buchner, J.; Yin, H.; Frantz, D.; Kümmerle, T.; Askerov, E.; Bakuradze, T.; Bleyhl, B.; Elizbarashvili, N.; Komarova, A.; Lewínska, K.
E.; Rizayeva, A.; Sayadyan, H.; Tan, B.; Tepanosyan, G.; Zazanashvili, N.; Radeloff, V.
C.
Land-cover change in the Caucasus Mountains since 1987 based on the topographic correction of multi-temporal Landsat composites, Remote Sens.
Environ.
2020, 248, 111967
Dechoz, C.; Poulain, V.; Massera, S.; Languille, F.; Greslou, D.; de Lussy, F.; Gaudel, A.; L’Helguen, C.; Picard, C.; Trémas, T.
Sentinel 2 global reference image, Proceedings Volume 9643, Image and Signal Processing for Remote Sensing XXI 2015
Doxani, G.; Vermote, E.; Roger, J.-C.; Gascon, F.; Adriaensen, S.; Frantz, D.; Hagolle, O.; Hollstein, A.; Kirches, G.; Li, F.; et al.
Atmospheric Correction Inter-Comparison Exerci.e.Remote Sens.
2018, 10, 352.
Frantz, D.; Röder, A.; Udelhoven, T.; Schmidt, M.
Enhancing the Detectability of Clouds and Their Shadows in Multitemporal Dryland Landsat Imagery: Extending Fmask.
IEEE Geosci.
Remote Sens.
Lett.
2015, 12, 1242–1246.
Frantz, D.; Stellmes, M.; Röder, A.; Udelhoven, T; Mader, S.; Hill, J.
Improving the Spatial Resolution of Land Surface Phenology by Fusing Medium- and Coarse-Resolution Inputs, IEEE Transactions on Geoscience and Remote Sensing, 2016, 54, 7, 4153 – 4164			
Frantz, D.; Haß, E.; Uhl, A.; Stoffels, J.; Hill, J.
Improvement of the Fmask algorithm for Sentinel-2 images: Separating clouds from bright surfaces based on parallax effects.
Remote Sens.
Environ.
2018, 215, 471–481.
Frantz, D.; Stellmes, M.; Hostert, P.
A Global MODIS Water Vapor Database for the Operational Atmospheric Correction of Historic and Recent Landsat Imagery, Remote Sens.
2019, 11(3), 257
Frantz, D.
FORCE—Landsat + Sentinel-2 Analysis Ready Data and Beyond, Remote Sens.
2019, 11(9), 1124
Rufin, P.; Frantz, D.; Yan, L.; Hostert, P.
Operational Coregistration of the Sentinel-2A/B Image Archive Using Multitemporal Landsat Spectral Averages, IEEE Geoscience and Remote Sensing Letters, 2020, 18, 4, 712 - 716
Zhu, Z.; Woodcock, C.E.
Object-Based Cloud and Cloud Shadow Detection in Landsat Imagery.
Remote Sens.
Environ.
2012, 118, 83–94.
Zhu, Z.; Wang, S.; Woodcock, C.E.
Improvement and Expansion of the Fmask Algorithm: Cloud, Cloud Shadow, and Snow Detection for Landsats 4–7, 8, and Sentinel 2 Images.
Remote Sens.
Environ.
2015, 159, 269–277.
