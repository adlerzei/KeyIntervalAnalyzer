# KeyIntervalAnalyzer

This class can be used to analyze the length of the intervals between two successive Bluetooth packets. The purpose of this class is the validation, that each recorded interval can be assigned to a multiple of 15ms, which is the sniff interval duration of the Apple Magic Keyboard.

The class generates a boxplot over the recorded data. 

## Dependencies

To run this program, you need to install the following Python libraries:

  * [argparse](https://pypi.org/project/argparse/)
  * [matplotlib](https://pypi.org/project/matplotlib/)
  * [tikzplotlib](https://pypi.org/project/tikzplotlib/)
  
### Installation

These packages can be installed by using your favorite packet manager. For instance, if you use [pip](https://pip.pypa.io/en/stable/), just run the following command:

```
pip install argparse matplotlib tikzplotlib
```

## Usage

In the following, sample instructions are given to execute the relevant parts of the script. The complete script is contained in the following class:
 
 * **IntervalChecker (interval_checker.py)**

The class reads a text file, that contains all recorded latencies between two successive Bluetooth packets. The script is located in the ```./csv/``` folder. In this file, each latency is stored in a separate line. To record such a file, the BluetoothKeySniffer can be used.
 
To run a script that executes the respective methods of the class, just execute the following command in a terminal:

```
sudo python interval_checker.py
```
