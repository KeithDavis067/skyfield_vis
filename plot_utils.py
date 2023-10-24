from datetime import datetime, timedelta
from dateutil import parser
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
from skyfield.api import load
from skyfield import almanac, units
from skyfield.elementslib import osculating_elements_of

try:
    from rich import print
except ImportError:
    pass

# import astropy.constants as const

kernel = load('de421.bsp')
ts = load.timescale()

BODY_NAMES = ["Sun", "Earth", "Moon", "Mercury", "Venus",
              "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

BODY_MARKERS = dict(zip(BODY_NAMES,
                        ["circle-dot", "circle-cross"] + 8 * ["circle"]))

BODY_COLORS = dict(zip(BODY_NAMES,
                   ["yellow",
                    "lightblue",
                    "grey",
                    "silver",
                    "darksalmon",
                    "red",
                    "green",
                    "purple",
                    "steelblue",
                    "slateblue"]))

BODY_STYLE_ELEMENTS = {}
for name in BODY_NAMES:
    BODY_STYLE_ELEMENTS[name] = {"symbol": BODY_MARKERS[name],
                                 "color": BODY_COLORS[name],
                                 "line": {"width": 2,
                                          "color": "grey"
                                          }
                                 }


def trace_style(name, x=[], y=[]):
    return {"name": name,
            "marker": BODY_STYLE_ELEMENTS[name],
            "line_thickness": 10
            }


def planet_path(name, t, vector):
    result = {"x": vector.at(t).ecliptic_xyz().au[0],
              "y": vector.at(t).ecliptic_xyz().au[1],
              "name": name,
              "marker": BODY_STYLE_ELEMENTS[name]
              }
    return result


def get_l_syn_period(t=None, kernel=kernel):
    """Return a nested dict of phases, their times and periods around `t`.

    Finds the moon phases using `kernel` within +/- 29.3 days of `t` or
    between the endpoints of `t` if `t` is iterable and returns a dict
    with the times of each phase and the synodic period between each
    phase.
    The dict structure is as so:

    {int:
        {"t": skyfield.timelib.Time,
         "p": np.array(dtype=datetime.timedelta}
    }
    """
    if t is None:
        t = ts.now()

    try:
        t1 = t[0]
        t2 = t[-1]
    except TypeError:
        t1 = t - 29.3
        t2 = t + 29.3

    t_phases, phases = almanac.find_discrete(
        t1, t2, almanac.moon_phases(kernel))
    syn = {}
    for phase in np.unique(phases):
        syn[phase] = {"t": t_phases[phases == phase]}

    # Create an array of timedeltas becuase skyfield doesn't do that.
    for phase in syn:
        if len(syn[phase]["t"]) > 1:
            syn[phase]["periods"] = np.array(
                [timedelta(days=dt) for dt in
                 (syn[phase]["t"][1:] - syn[phase]["t"][0:-1])
                 ]
            )

    return syn
