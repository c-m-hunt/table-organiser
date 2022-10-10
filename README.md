# Table planner

Allocates groups of people to tables.

Was planning to do something more complicated that meant you could put groups to not sit togther etc but this suited my needs in the end.

## Setup

In the root of the repo, create a `data` directory. Add `groups.csv` and `tables.csv`

### `tables.csv`
CSV file with columns: 
* ID - an integer ID for the table. Probably not really required. Abitrary.
* Capacity - an integer value for the number of people on the table
* Active - 0 or 1 - value to asily switch the table on and off

Example:
```
0,11,1
1,13,1
2,12,1
3,12,1
```

### `groups.csv`
CSV with columns:
* Group name
* Number in group - an integer with the size of the group
* Vegetarians - an integer for tne number of vegetarians in the gorup

Example:
```
Group 1,10,3
Group 2,4,2
Group 3,5,1
```

## Running
```
python3 main.py
```
This will return some basic information:
```
Table setup:
10 seats: 11
11 seats: 1
12 seats: 7
----------------------------
Remaining seats: 205
Required seats: 202
----------------------------
Remaining seats: 3
Filled seats: 202
----------------------------
```
It will also output a file in `data` directory callect `output.csv` which will detail which groups have been allocated to which tables
