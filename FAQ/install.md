# FAQ

## How to install FORCE on CODE-DE

FORCE can be [compiled and installed](https://force-eo.readthedocs.io/en/latest/setup/install.html) from scratch in your virtual machine (VM).

The recommended way, however, is to simply use FORCE with Docker.
It is best to use a Linux VM.

1) [Install Docker](https://code-de.org/de/help/?topic=faq&id=67471868) in your virtual machine

2) download a Docker image using one of the following commands:

    ```
    docker pull davidfrantz/force
    docker pull davidfrantz/force:3.7.2
    docker pull davidfrantz/force:dev
    ```

    The first option is the latest official release.
    The second option refers to a specific version.
    The third option refers to the develop branch that includes the latest cutting-edge features.
    See [here](https://hub.docker.com/repository/docker/davidfrantz/force) for available tags and versions.

3) Check if this works:

    ```
    docker run \
      davidfrantz/force force -v
    ```


## Post-Installation steps

Now, you are basically good to go.
There are some things to consider when using Docker, though.
The Docker container is isolated from your VM, thus FORCE will not be able to see any files that exist on CODE-DE.

The following command makes following directories accesible from within the Docker container:

- your home directory,
- the general CODE-DE data repository,
- the [FORCE datacube](**link to portfolio**) using the short mount directory ``/force``, and 
- your current working directory

It also makes sure that data is created with your current user name.

```
docker run \
  -v $HOME:$HOME \
  -v /codede:/codede \
  -v /force/FORCE/C1/L2/ard:/force \
  -w $PWD \
  -u $(id -u):$(id -g) \
  -t \
  --rm \
  davidfrantz/force \
  force-higher-level $HOME/classification.prm
```

> As this long commandline is tedious to type into the console every time, it is recommended to put an alias to the file ``$HOME/.profile``:

```
alias dforce=' \
  docker run \
  -v $HOME:$HOME \
  -v /codede:/codede \
  -v /force/FORCE/C1/L2/ard:/force \
  -w $PWD \
  -u $(id -u):$(id -g) \
  -t \
  --rm \
  davidfrantz/force'
```

After saving, logging out and in again, the alias is active and can be used like this:

The data are then available under ``/force`` from within the Docker container:

```
dforce ls /force | head
```
```
CITEME_0x20.txt  X0054_Y0037  X0059_Y0063  X0065_Y0052  X0071_Y0063
CITEME_0xc0.txt  X0054_Y0038  X0059_Y0064  X0065_Y0053  X0071_Y0064
CITEME_0xf1.txt  X0054_Y0039  X0059_Y0065  X0065_Y0054  X0071_Y0065
X0044_Y0052      X0054_Y0040  X0059_Y0066  X0065_Y0055  X0071_Y0066
X0044_Y0053      X0054_Y0041  X0060_Y0026  X0065_Y0056  X0072_Y0031
X0045_Y0050      X0054_Y0042  X0060_Y0027  X0065_Y0057  X0072_Y0032
X0045_Y0051      X0054_Y0043  X0060_Y0028  X0065_Y0058  X0072_Y0033
X0045_Y0052      X0054_Y0044  X0060_Y0029  X0065_Y0059  X0072_Y0034
X0045_Y0053      X0054_Y0045  X0060_Y0030  X0065_Y0060  X0072_Y0035
X0046_Y0047      X0054_Y0046  X0060_Y0031  X0065_Y0061  X0072_Y0036
```

This here is the same call as before (same command as the long commandline call above):

```
dforce force-higher-level $HOME/classification.prm
```

