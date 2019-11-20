#!/usr/bin/env bash

MYVAR=${OUTFILE}.out
echo $MYVAR
MYERR=${OUTFILE}.err
echo $MYERR
./cmd1 < $INFILE | ./cmd3 > $MYVAR 2> $MYERR
