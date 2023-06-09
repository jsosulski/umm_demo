# UMM

Code to run UMM for BCI ERP datasets.

## Disclaimer

Please note, that a patent is pending for UMM.
We want to encourage the pickup of UMM by a wide audience for non-commercial / academic purposes, but would like to keep track of potential commercial use of UMM.
Thus to obtain the file, please drop an email to Jan or Michael with an indication, if you intend to use the software for non-commercial / academic or for commercial purposes.

## Setup

:warning: If you want to actually run the example notebook, you need to replace the file `umm_demo/classification/umm.py` with the version you obtained from above.

Create and activate a virtual environment using:

```bash
python3 -m venv venv
source venv/bin/activate
```

Then install the necessary requirements:
```bash
pip install -r requirements.txt
pip install -e .
```

If you have a system jupyter notebook installation, you need to register the virtual environment as a notebook kernel:

```bash
ipython kernel install --name "umm-venv" --user
```

Now you can open the examples notebook and you should be able to run it:

```bash
jupyter notebook examples/
```


# Frequently asked questions

### It says I am missing some umm.py file?

You need to download the file in an extra step, as indicated at the top of this readme.

### It says some "zip" file is not a zip?

Unfortunately the dataset host sometimes stops transmission early and you are left with a corrup .zip file.
To fix this go to the `~/mne_data/` directory, and either delete everything (not recommended) or find the "zip file" impostor and delete it.

