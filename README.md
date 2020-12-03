# Algorithm Illuminated Exercises

## Overview

This repository contains solutions to the programming projects accompanied with [Tim Roughgarden's](http://www.timroughgarden.org/) Algorithm Illuminated series. This is a great series that you definitely don't want to miss, for more details check here [Algorithm Illuminated](http://www.algorithmsilluminated.org/)

## Intention

These solutions are just for reviewing the algorithms mentioned in the corresponding video lectures. To make the implementation simple, the solutions here are more or less the naive implementation of algorithms described in the slides, so not surprisingly, some of them might not scale to large problem sizes. 


## Getting Started

To sanity check these solutions, first you need to download the testcases from [here](http://www.algorithmsilluminated.org/datasets/) and put them under ./algorithmsilluminated/tests/. After that try the following command:

```
cd ./algorithmsilluminated
python -m unittest -v
```

you can also run the solution file itself, sanity check is added in each of the main functions e.g.

```
cd ./algorithmsilluminated
./algorithm/bellbellman_ford.py
```

For more test cases, check here: [stanford-algs](https://github.com/beaunus/stanford-algs). (Note the **alg** method defined in each solution file is used for testing the cases there)


