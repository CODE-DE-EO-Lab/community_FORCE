# FAQ

## How to install FORCE on CODE-DE

FORCE can be [compiled and installed](https://force-eo.readthedocs.io/en/latest/setup/install.html) from scratch in your virtual machine (VM).

The recommended way, however, is to simply use FORCE with Docker.
It is best to use a Linux VM.

1) [Install Docker](https://code-de.org/de/help/topic/faq/X5gxAxEAAB0ArF0T) in your virtual machine

2) download a Docker image using one of the following commands:

    ```
    docker pull davidfrantz/force
    docker pull davidfrantz/force:3.7.2
    docker pull davidfrantz/force:dev
    ```

    The first option is the latest official release.
    The second option refers to a specific version.
    The third option refers to the develop branch that includes the latest cutting-edge features.

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
  -v /codede/community/FORCE/C1/L2:/force \
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
  -v /codede/community/FORCE/C1/L2:/force \
  -w $PWD \
  -u $(id -u):$(id -g) \
  -t \
  --rm \
  davidfrantz/force'
```

After saving, logging out and in again, the alias is active and can be used like this (same command as the long commandline call above):

```
dforce force-higher-level $HOME/classification.prm
```
