# Interval Checker
#
# Copyright (C) 2020  Christian Zei
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import csv
import argparse
from datetime import datetime
import matplotlib.pyplot as plt
from tikzplotlib import save as tikz_save

class IntervalChecker:
    def __init__(self):
        self.timings = []
        self.timing_dates = []
        self.deltas = []
        self.processed_timings = []

    def read_csv(self, path):
        with open(path, mode='r') as infile:
            reader = csv.reader(infile, delimiter=";")
            self.timings = list(str(rows[0]) for rows in reader)

    def convert_timings(self):
        for timing in self.timings:
            if timing == "0:00:00":
                continue
            timing_date = datetime.strptime(timing, "%H:%M:%S.%f")
            if timing_date.microsecond < 1000:
                continue
            self.timing_dates.append(timing_date)

    def analyze(self):
        for timing_date in self.timing_dates:
            delta = timing_date.microsecond % 15000
            inverse_delta = 15000 - delta

            if delta < inverse_delta:
                correct_delta = delta
            else:
                correct_delta = -1 * inverse_delta

            self.deltas.append(correct_delta)

    def analyze2(self):
        total_time = 0
        for timing_date in self.timing_dates:
            total_time += timing_date.microsecond
            delta = total_time % 15000
            inverse_delta = 15000 - delta
            if delta < inverse_delta:
                correct_delta = delta
            else:
                correct_delta = -1 * inverse_delta

            self.deltas.append(correct_delta)

    def plot(self):
        for delta in self.deltas:
            if delta > 1000:
                print(delta)
        plt.style.use("seaborn-whitegrid")

        plt.boxplot(self.deltas, vert=False)
        plt.xscale('symlog', linthreshx=10)
        tikz_save(
            "fig/interval_delta.tex",
            axis_height='\\figH',
            axis_width='\\figW',
            extra_axis_parameters=["tick label style={font=\\footnotesize}",
                                   "xtick={-5000,-1000,-100,-10,0,10,100,1000,5000}",
                                   "xticklabels={-5,-1,-0.1,-0.01,0,0.01,0.1,1,5}",
                                   "xlabel = {ms}",
                                   "scaled x ticks = false",
                                   "x tick label style={/pgf/number format/fixed, /pgf/number "
                                   "format/1000 sep = \\thinspace}"]
        )
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Bluetooth timings if they fit into 15ms timing interval of "
                                                 "Apple Magic Keyboard's sniff interval")
    parser.add_argument("--name", "-n", nargs=1, help="CSV file name prefix.", required=True)
    args = parser.parse_args()

    checker = IntervalChecker()
    checker.read_csv("csv/" + args.name[0] + ".csv")
    checker.convert_timings()
    checker.analyze()
    checker.plot()
