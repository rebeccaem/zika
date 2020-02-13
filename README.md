# zika

This code includes models for the reduced and enriched Zika models.
The parameters of the discrepancy model are calibrated using QUESO.

Dependencies: QUESO (https://github.com/libqueso/queso), Eigen

My Makefile is included for reference.

The steps to run the code are as follows:
```
rm -r outputData
./bin/zika_ip inputs/mhInput.inp
```
Remove or move existing 'outputData' directory. This directory is created during the inverse problem. 
'mhInput.inp' is an input file for QUESO.

To plot the time series results:
```
cd postprocessing
./post_proc.sh
python3 compute-percents.py
python3 percent-time-series.py
```

You can also run 
```
./bin/gen_data
```
to test the forward model alone.

Can ignore 'americo' and 'data' directories.
