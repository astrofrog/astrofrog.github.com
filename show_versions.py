import sys
import platform

try:
    print(platform.python_version())
except:
    print("Could not determine Python version")

try:
    print(platform.platform())
except:
    print("Could not determine platform")

try:
    import numpy
except ImportError:
    print("Numpy not installed")
else:
    try:
        print(numpy.__version__)
    except:
        print("Could not determine Numpy version")

try:
    import scipy
except ImportError:
    print("Scipy not installed")
else:
    try:
        print(scipy.__version__)
    except:
        print("Could not determine Scipy version")

try:
    import matplotlib
except ImportError:
    print("Matplotlib not installed")
else:
    try:
        print(matplotlib.__version__)
    except:
        print("Could not determine Matplotlib version")

try:
    import IPython
except ImportError:
    print("IPython not installed")
else:
    try:
        print(IPython.__version__)
    except:
        print("Could not determine IPython version")
