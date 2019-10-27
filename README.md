# SI-Project

## Introduction
A radio remote controlled robot that maps the space around it.

## Exemples

 ```python map.py --dim 100 100 --pos 50 50``` \
 <img src="https://github.com/fotisk07/SI-Project/blob/master/Mapping/Examples/dim%3D(100%2C%20100)_pos%3D(50%2C%2050)/Real_Map.png" width="425"/> <img src="https://github.com/fotisk07/SI-Project/blob/master/Mapping/Examples/dim%3D(100%2C%20100)_pos%3D(50%2C%2050)/Produced_map.png" width="425"/>
 

 


## Usage

* Using LiSim
  * Initializing a Lidar Object
  ```lidar = sim.Lidar() ```
  * Using the functions of the Lidar Object
  ``` lidar.simulate()```
* Running the mapping software, for example
```python map.py --dim 10 10 --pos 5 5``` (to be implented)



## Prerequisites

The Code is written in Python 3.6.5 . If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip.

To install pip run in the command Line
```
python -m ensurepip -- default-pip
```
to upgrade it
```
python -m pip install -- upgrade pip setuptools wheel
```
to upgrade Python
```
pip install python -- upgrade
```
You have to install several dependencies to get the project up and running. To do so just type
```
pip install requirements.txt
```
This will install all necessery packages

## Contributing

Please read [CONTRIBUTING](https://github.com/fotisk07/Fourier-Transform/blob/master/CONTRIBUTING) for the process for submitting pull requests.

## Authors

* **Alexander Flammant** - *Initial work*
* **Fotios Kapotos** - *Initial work*
* **Mateo Rivera** - *Initial work*

This project is licensed under the MIT License - see the [LICENSE.md]https://github.com/fotisk07/SI-Project/blob/master/LICENSE) file for details
