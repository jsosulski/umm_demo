# UMM

Code to run UMM for different BCI ERP datasets.

## Disclaimer

To be able to **run** these scripts, you need to request access to the core UMM code from [this page](https://todo.todo).
Note that a patent application for BCI applications using UMM has been submitted.
For non-commercial purposes you are free to use the UMM algorithm.

**JAN COMMENT: SOMEONE WITH LEGAL KNOWLEDGE SHOULD PROBABLY REWORD/REWRITE THE ABOVE**

## Setup

:warning: If you want to actually run the example notebook, you need to replace the file `umm_demo/classification/umm.py` with the version you can download above.

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

Now you can open the examples notebook and you should be able to run it.
