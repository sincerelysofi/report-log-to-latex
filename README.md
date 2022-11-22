Log time to LaTeX converter
===========================

This script converts a time log into LaTeX for inclusion in a report. This script is specifically written with the intention of use for the Machine Learning class at Vrije Universiteit Amsterdam.

A time log is a tab-delimited `timelog.tsv` file in the following format:

| Week | Day | Begin | End | Category | Task |
| --- | --- | --- | --- | --- | --- |
| The week number | The date in %d.%m format. | The start time of task in %H:%M format. | The end time of task, also in %H:%M format. | The type of task being performed (prep, code, theory, report). |  A description of the task.

Please also see `timelog_example.tsv` for an example.

Usage
-----
Place the .py file in the same directory as the `timelog.tsv` file and run. The output can be copied into your report.

If you use this for your report, please cite this github page!

Example output
--------------

```latex
\begin{tabular}{rll}
\toprule
 Week &                           Task & Time spent \\
\midrule
    1 &           started a to-do list &        24m \\
    2 &      wrote a literature review &       1h5m \\
    3 & built a support vector machine &      5h16m \\
    4 &                cleaned up code &       1h9m \\
    4 &                 updated report &       1h8m \\
\bottomrule
\end{tabular}

Total: 9h2m
```
