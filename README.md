# adatools

`adatools` is a Python package with software tools in addition to the [roboticstoolbox](https://github.com/petercorke/robotics-toolbox-python) which we use in ADA526.

## Installation

To install `adatools` follow these steps:

1. Decide where you want to keep the toolbox. This can be anywhere on your computer. For example, you can make a new folder in Documents, or you can put it into your working directory for ADA526.

>>Open a termninal window, an `cd` into this directory. 
>>   ```shell
>>   cd path/to/your/directory
>>   ```

2. Clone the repository:

   ```shell
   git clone https://github.com/frdedynamics/adatools.git
   ```

3. Navigate to the `adatools` directory in which the `setup.py` file is located:

   ```shell
   cd adatools
   ```

4. Install the package:

   ```shell
   pip install .
   ```

Now the package should be available for import in Python on your system.


## Usage

Once `adatools` is installed, you can import it in your Python scripts:

```python
import adatools
```

## Examples

You can find example scripts in the `examples` directory of this repository. These examples demonstrate how to use the functionalities of the `adatools` package.


## Updating
When there are updates to the `adatools` package, you can update your local copy by navigating to the `adatools` directory (where the `setup.py` file is located)
```shell
cd path/to/your/directory/adatools
```
 and pulling the latest version from the repository:
```shell
git pull origin master
```
Then, you can upgrade the package installation:
```shell
pip install --upgrade .
```

## Uninstalling
To uninstall the package, navigate to the `adatools` directory (where the `setup.py` file is located)
```shell
cd path/to/your/directory/adatools
```
and uninstall the package:
```shell
pip uninstall adatools
```
