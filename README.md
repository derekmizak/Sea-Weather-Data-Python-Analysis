# Using Python for sea weather data analysis

## Introduction
Repository include some examples of using Python for sea weather data analysis. Data is downloaded from [Marine Institute](https://erddap.marine.ie/erddap/index.html).

## Data

Before using the described code please download the data from the following link: [Marine Institute](https://erddap.marine.ie/erddap/index.html). Save downloaded data in repository folder with name `buoys_data.csv`.

----
***Note:*** Repository is used for educational purposes only and is not suitable for production use.

----



The data is collected from the Irish wave buoy network and is updated every 30 minutes. The data is collected from 5 wave buoys located around the Irish coast. The data is collected from the following wave buoys: M1 to M6.

The best it would be to use a virtual environement to run this notebook to avoid any conflict with the libraries. You coud use Anaconda or venv to create a virtual environement. When using venv follow the following steps:

```bash
python3 -m venv myenv
```
To activate environement use the following command:
```bash
source myenv/bin/activate
```

On Windows you can use the following command:

```bash
myenv\Scripts\activate
```


To use this notebook, you will need to install necesary libraries using the following command:

```bash
pip install -r requirements.txt
```

