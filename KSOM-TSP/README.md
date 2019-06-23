# KSOM-TSP
[![MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/kritiksoman/KSOM-TSP/blob/master/LICENSE)

Solving the Traveling Salesman Problem (TSP) using Kohonen self organizing map (KSOM).

## Overview
Uses the KSOM 1D topological ordering property to solve TSP. The data.csv contains coordinates for 29 cities.
The algorithm additionally deletes neurons that do not win and get updated more than 2 times in an iteration. 
It also starts with 1 neuron in the beginning and duplicates the winning neuron if it wins more than once. 

## Result Screenshots
![image1](https://github.com/kritiksoman/KSOM-TSP/blob/master/results/TSP_Result.png)

## Files
data.csv: Contains coordinates of the 29 cities. <br>
importfile.m: Loads the csv file. <br>
TSPSOM.m: Run the KSOM algorithm on the dataset and plots the optimal result.

## Reference
[1] Kohonen, Teuvo. Self-organizing maps. Vol. 30. Springer Science & Business Media, 2012. <br>
[2] http://www.math.uwaterloo.ca/tsp/world/countries.html#WI
