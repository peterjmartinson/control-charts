# Literary Control Charts
[Control charts](https://en.wikipedia.org/wiki/Control_chart) are typically used to evaluate the performance of some process over time.  However, they can also be effectively used to indicate changes of mood in a short story.

This project demonstrates the use of control charts in analyzing short stories, using as an example Washington Irving's _The Legend of Sleepy Hollow_.

The text of the story was lifted from [Project Gutenberg](https://www.gutenberg.org/ebooks/41).  The body of the story was initially processed manually using a simple text editor (Vim).  Then, the individual paragraphs were analyzed using Excel.  Finally, the control charts themselves were built using Python, Pandas, and Matplotlib.

The raw story can be found [here](https://github.com/peterjmartinson/control-charts/blob/dev/pipeline/Texts/SleepyHollow.txt).

The Excel breakdown can be found [here](https://github.com/peterjmartinson/control-charts/blob/dev/pipeline/Spreadsheets/SleepyHollowPData.xlsx).

The Jupyter notebook showing the creation of the actual control charts can be found [here](https://github.com/peterjmartinson/control-charts/blob/dev/pipeline/Notebooks/SleepyHollow_Analysis.ipynb).

A final PowerPoint presentation of the control chart can be found [here](https://github.com/peterjmartinson/control-charts/blob/dev/pipeline/Martinson_ControlCharts.pptx).

## Next Steps
I am writing a Python program to ingest raw text from Project Gutenberg, and do all the work my Excel file does above.  This will allow all analysis to be done inside the Jupyter notebook.

It's a work [in progress](https://github.com/peterjmartinson/control-charts/tree/dev/pipeline/Code), though!
