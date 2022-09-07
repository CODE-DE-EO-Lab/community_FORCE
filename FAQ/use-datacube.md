# FAQ

## How to use the FORCE datacube collection 1 on CODE-DE

1) start a Virtual Machine

2) mount the dataset

## How to analyze the data with FORCE

1) install and set up [FORCE with Docker](https://github.com/CODE-DE-Cloud/community_FORCE/tree/main/FAQ/install.md)

2) Generate an empty parameter file, e.g. for Time Series Analysis (TSA):

```
dforce force-parameter tsa.prm TSA
```

3) Modify the parameter file to your needs using the text editor of your choice (vi, nano, ...)

4) Run the process:

```
dforce force-higher-level tsa.prm
```


## Note

> Tutorials that demonstrate the usage of the Higher Level Processing System of FORCE are available [here](https://force-eo.readthedocs.io/en/latest/howto/index.html).

> Knowledge-based articles that (1) describe the [FORCE data cube collection 1](link to portfolio) in depth, and (2) demonstrate the usage of FORCE on the CODE-DE platform were prepared and will be soon available on CODE-DE/EOLab websites.
> These are accompanied by examples [paremeter files](https://github.com/CODE-DE-Cloud/community_FORCE).
