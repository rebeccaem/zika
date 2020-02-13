# zika

This code includes models for the reduced and enriched Zika models.
The parameters of the discrepancy model are calibrated using QUESO.

Dependencies: QUESO, Eigen

My Makefile is included for reference.

The steps to run the code are as follows:
rm -r outputData (if already exists)
 ./bin/zika_ip inputs/mhInput.inp

To plot the time series results:
cd postprocessing
./post_proc.sh
python3 compute-percents.py
python3 percent-time-series.py

You can also run 
./bin/gen_data
to test the forward model alone.
