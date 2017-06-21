# Parallel Computation of Randomized Tukey HSD test with gxp3

# Example

## Input

`data/sample/matrix`

```
0.7 0.5 0.0
0.3 0.1 0.0
0.2 0.0 0.2
0.6 0.2 0.1
0.4 0.4 0.3
0.4 0.3 0.3
0.0 0.0 0.1
0.7 0.5 0.2
0.1 0.3 0.4
0.3 0.3 0.4
```

`data/sample/systems`

```
X
Y
Z
```

## Run

```
gxpc make -j 50 MATRIX=data/sample/matrix SYSL=data/sample/systems NTRIAL=5000 -- -a cpu_factor=0.25 -a state_dir=${HOME}/public_html/gxpstatus/randtukeyhsd
```

## Output

```
X Y 0.07500000000000001 0.2652
X Z 0.0999999999999999 0.1082
Y Z 0.024999999999999883 0.8842
```
