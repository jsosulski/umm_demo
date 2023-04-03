try:
    from . import visual_speller
except ImportError:
    print(
        "Could not import visual speller code. If you want to run examples please install 'neuro' extras."
    )
    pass
