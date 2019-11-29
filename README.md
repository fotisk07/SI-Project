# SI-Project

## Introduction
A radio remote controlled robot that maps the space around it.

## Exemples

 ```python map.py --d 100 100 --p 50 50``` \
 <img src="https://github.com/fotisk07/SI-Project/blob/master/Mapping/Examples/dim%3D(100%2C%20100)_pos%3D(50%2C%2050)/Real_Map.png" width="425"/> <img src="https://github.com/fotisk07/SI-Project/blob/master/Mapping/Examples/dim%3D(100%2C%20100)_pos%3D(50%2C%2050)/Produced_map.png" width="425"/>
 
```python map.py --d 18 34 --p 8 8 ```\
<img src="https://github.com/fotisk07/SI-Project/blob/master/Mapping/Examples/dim%3D(18%2C%2034)_pos%3D(8%2C%208)/Real_Map.png" width="425"/> <img src="https://github.com/fotisk07/SI-Project/blob/master/Mapping/Examples/dim%3D(18%2C%2034)_pos%3D(8%2C%208)/Produced_map.png" width="425"/>
 
 ```python map.py --d 30 20 --p 5 5 --n```\
 <img src="https://github.com/fotisk07/SI-Project/blob/master/Mapping/Examples/dim%3D(20%2C%2030)_pos%3D(5%2C%205)/Real_Map.png" width="425"/> <img src="https://github.com/fotisk07/SI-Project/blob/master/Mapping/Examples/dim%3D(20%2C%2030)_pos%3D(5%2C%205)/Produced_map.png" width="425"/>

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

## Usage

The program runs using [Simulate](https://github.com/fotisk07/SI-Project/blob/master/Mapping/Simulate.py) which relies on the use of LiMap and LiSim for the simulation
* Basic Usage ```python simulate.py ```  
Runs the Mapping procedure for one round
  - Plot and save the graphs(loss,real map, produced map, confusion matrix) ath the default dir  
  with ```python simulate.py -g```
  - Add noise with ```python simulate.py -n```
  - Animate it with ```python simulate.py --ani```
  - Specify dimensions with ```python simulate.py -d 10 10  ```
  - Specifiy position with ```python simulate.py -p 5 5 ```
  - Save stats for nerds with ```python simulate.py -stats```
  - Change saving directory to "dim,pos"
* Example of advanced usage:  
```
python simulate.py -d 50 50 -p 10 10 -n -ani -stats -g
```
The first picture is the above command executed
   
## Contributing

Please read [CONTRIBUTING](https://github.com/fotisk07/SI-Project/blob/master/CONTRIBUTING.md) for the process for submitting pull requests.

## Secuirity

Shout out to [Mateo](https://github.com/CeType) for making sure that our project has a sound secuirity policy. You will find  
all the necesserary details [here](https://github.com/fotisk07/SI-Project/blob/master/SECURITY.md)

## Authors

* **Alexander Flammant** - *Initial work*
* **Theodore Halley** - *Initial work*
* **Fotios Kapotos** - *Initial work*
* **Mateo Rivera** - *Initial work*

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/fotisk07/SI-Project/blob/master/LICENSE) file for details
