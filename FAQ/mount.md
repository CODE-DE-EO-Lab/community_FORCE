# How to mount the FORCE community collection as an NFS share

In order to improve performance in accessing the FORCE community collection, 
a dedicated NFS server has been launched within the Cloud and is now available for all virtual machines. 
If you want to access it, your virtual machine needs to be connected to the dlr-access-net network interface.

## How to mount FORCE NFS share

### General information

The FORCE NFS server is accessible within the Cloud under *nfs.force.code-de.org* or under the corresponding IP address: *10.210.48.205*

The following directories are available on the NFS FORCE server:

```
Export list for nfs.force.code-de.org:
/exports/FORCE-C1-L2 (everyone)
```

### How to

To mount the FORCE collection as an NFS share, create a new directory, for example:

```
sudo mkdir /force
```

Mount the shared directory with one of the following commands:

```
sudo mount 10.210.48.205:/exports/FORCE-C1-L2 /force
sudo mount nfs.force.code-de.org:/exports/FORCE-C1-L2 /force
```

To automatically mount an NFS share when your Linux system boots, add a line to the ``/etc/fstab`` file. 
The ``/etc/fstab`` file contains a list of entries that define where, how and what filesystems will be mounted during the system startup.

Edit ``/etc/fstab`` with your favorite editor and add the following entry:

```
nfs.force.code-de.org:/exports/FORCE-C1-L2 /force nfs defaults 0 0
```

From now on, the shared catalogue will automatically be mounted in the specified directory.

