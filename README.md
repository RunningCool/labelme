<img src="https://github.com/wkentaro/labelme/blob/master/labelme/icons/icon.png?raw=true" align="right" />

labelme-ng: Images Correspondence Annotation Tool with Python
==========================================

Labelme-ng is a fork from [wkentaro/labelme](https://github.com/wkentaro/labelme), supplying correspondence annotation feature for pairs of images. It is written in Python and uses Qt for its graphical interface.


Requirements
------------

- Ubuntu / macOS / Windows
- Python2 / Python3
- [PyQt4 / PyQt5](http://www.riverbankcomputing.co.uk/software/pyqt/intro)


Installation
------------

There are options:

- Platform agonistic installation: Anaconda, Docker
- Platform specific installation: Ubuntu, macOS

**Anaconda**

You need install [Anaconda](https://www.continuum.io/downloads), then run below:

```bash
conda create --name=labelme python=2.7
source activate labelme
conda install pyqt
pip install labelme
```

**Docker**

You need install [docker](https://www.docker.com), then run below:

```bash
wget https://raw.githubusercontent.com/wkentaro/labelme/master/scripts/labelme_on_docker
chmod u+x labelme_on_docker

# Maybe you need http://sourabhbajaj.com/blog/2017/02/07/gui-applications-docker-mac/ on macOS
./labelme_on_docker static/apc2016_obj3.jpg -O static/apc2016_obj3.json
```

**Ubuntu**

```bash
sudo apt-get install python-qt4 pyqt4-dev-tools
sudo pip install labelme
```

**macOS**

```bash
brew install qt qt4 || brew install pyqt  # qt4 is deprecated
pip install labelme
```


Usage
-----

**Annotation**

Run `labelme --help` for detail.

```bash
labelme  # Open GUI
```
The line annotations are saved in *.json* file, while the correspondence for two views are saved in *.crd* file. 



Acknowledgement
---------------

Labelme-ng is a fork from [wkentaro/labelme](https://github.com/wkentaro/labelme), supplying correspondence annotation feature for pairs of images. The repo of [wkentaro/labelme](https://github.com/wkentaro/labelme) is a fork of [mpitid/pylabelme](https://github.com/mpitid/pylabelme), whose development has already stopped.
