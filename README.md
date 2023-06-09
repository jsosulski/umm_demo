# UMM

Code to run UMM for BCI ERP datasets.

## Important Disclaimer

The source code for the core algorithm of Unsupervised Mean-difference Maximization (UMM) is protected by copyright of the Radboud University, the Netherlands, 2023, and a patent is pending for UMM-based applications. The authors encourage the use of this code for non-commercial, not-for-profit and academic purposes. However, the source code may only be copied, published, or used for other purposes under a license that is to be obtained from Radboud University.

To obtain the code (umm.py), please send an email with the subject _umm.py request_ to either Jan or Michael that states your name, affiliation and the information, if you intend to use the software either for non-commercial / academic purposes or for commercial purposes.

Michael: ![Screenshot_2023_06_09](https://github.com/jsosulski/umm_demo/assets/8556638/7370abdf-9452-4727-a223-c70adfc1f6ce)

Jan: ![Screenshot_20230609_061736](https://github.com/jsosulski/umm_demo/assets/2545339/7aa2393d-ffe6-4799-a05d-d57bf6894093)


## Setup

:warning: If you want to re-run the example notebook, you need to replace the mockup file `umm_demo/classification/umm.py` with the version of umm.py that you have obtained following the above description.

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

Unfortunately the dataset host sometimes stops transmission early and you are left with a corrupt .zip file.
To fix this go to the `~/mne_data/` directory, and either delete everything (not recommended) or find the unfinished "zip file" impostor and delete it.

