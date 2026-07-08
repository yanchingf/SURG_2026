
TO BE UPDATED (testcases in sdrg.py)

Two nodes, one in range, other out

x = [200, 400]
y = [200, 200]
r = [10, 300]

<details>
<summary>Log and FileID</summary>
Step 1 | Ω=(300, 1, 'Node')
    id=0 h=10 cluster=0 active=True
    id=1 h=300 cluster=1 active=True
Step 2 | Ω=(10, 0, 'Node')
    id=0 h=10 cluster=0 active=True
    id=1 h=300 cluster=1 active=False
Done at iteration 3

[Title](../src/tests/random-plots/20260703_030420)
</details>

Two nodes, mutually out of range

x = [200, 400]
y = [200, 200]
r = [10, 10]

<details>
<summary>Log and FileID</summary>
Step 1 | Ω=(10, 0, 'Node')
    id=0 h=10 cluster=0 active=True
    id=1 h=10 cluster=1 active=True
Step 2 | Ω=(10, 1, 'Node')
    id=0 h=10 cluster=0 active=False
    id=1 h=10 cluster=1 active=True
Done at iteration 3

[Title](../src/tests/random-plots/20260703_025829)
</details>

Two nodes, mutually in range

x = [200, 400]
y = [200, 200]
r = [300, 300]

<details>
<summary>Log and FileID</summary>
Step 1 | Ω=(200.0, (0, 1), 'Edge')
    id=0 h=300 cluster=0 active=True
    id=1 h=300 cluster=1 active=True
  Edge decimate: u=0 (cluster=0) v=1 (cluster=1)
  in_range check: True
  adj weight: 200.0
Step 2 | Ω=(400.0, 0, 'Node')
    id=0 h=400.0 cluster=0 active=True
    id=1 h=400.0 cluster=0 active=False
Done at iteration 3

[\[Title\](../src/tests/random-plots/20260703_025829)](../src/tests/random-plots/20260703_025942)
</details>

Three nodes, middle within range of the others (but new range does not extend to last node):

x = [200, 300, 400]
y = [200, 200, 200]
r = [150, 150, 150]

<details>
<summary>Log and FileID</summary>

Step 1 | Ω=(100.0, (0, 1), 'Edge')
    id=0 h=150 cluster=0 active=True
    id=1 h=150 cluster=1 active=True
    id=2 h=150 cluster=2 active=True
  Edge decimate: u=0 (cluster=0) v=1 (cluster=1)
  in_range check: True
  adj weight: 100.0
Step 2 | Ω=(200.0, 0, 'Node')
    id=0 h=200.0 cluster=0 active=True
    id=1 h=200.0 cluster=0 active=False
    id=2 h=150 cluster=2 active=True
Step 3 | Ω=(150, 2, 'Node')
    id=0 h=200.0 cluster=0 active=False
    id=1 h=200.0 cluster=0 active=False
    id=2 h=150 cluster=2 active=True
Done at iteration 4

[20260703_025404](../src/tests/random-plots/20260703_025404)
</details>

Three nodes, middle within range of the others (and new range does extend to last node):

x = [200, 300, 400]
y = [200, 200, 200]
r = [300, 300, 300]

<details>
<summary>Log and FileID</summary>

Step 1 | Ω=(200.0, (0, 2), 'Edge')
    id=0 h=300 cluster=0 active=True
    id=1 h=300 cluster=1 active=True
    id=2 h=300 cluster=2 active=True
  Edge decimate: u=0 (cluster=0) v=2 (cluster=2)
  in_range check: True
  adj weight: 200.0
Step 2 | Ω=(100.0, (0, 1), 'Edge')
    id=0 h=400.0 cluster=0 active=True
    id=1 h=300 cluster=1 active=True
    id=2 h=400.0 cluster=0 active=False
  Edge decimate: u=0 (cluster=0) v=1 (cluster=1)
  in_range check: True
  adj weight: 100.0
Step 3 | Ω=(600.0, 0, 'Node')
    id=0 h=600.0 cluster=0 active=True
    id=1 h=600.0 cluster=0 active=False
    id=2 h=400.0 cluster=0 active=False
Done at iteration 4

[Title](../src/tests/random-plots/20260703_025535)
</details>

Triangle, mutually in range

x = [100, 200, 150]
y = [100, 100, 186.6]
r = [110, 110, 110]

<details>
<summary>Log and FileID</summary>
Step 1 | Ω=(100.0, (0, 1), 'Edge')
    id=0 h=110 cluster=0 active=True
    id=1 h=110 cluster=1 active=True
    id=2 h=110 cluster=2 active=True
  Edge decimate: u=0 (cluster=0) v=1 (cluster=1)
  in_range check: True
  adj weight: 100.0
Step 2 | Ω=(99.99779997579945, (0, 2), 'Edge')
    id=0 h=120.0 cluster=0 active=True
    id=1 h=120.0 cluster=0 active=False
    id=2 h=110 cluster=2 active=True
  Edge decimate: u=0 (cluster=0) v=2 (cluster=2)
  in_range check: True
  adj weight: 99.99779997579945
Step 3 | Ω=(130.00220002420053, 0, 'Node')
    id=0 h=130.00220002420053 cluster=0 active=True
    id=1 h=120.0 cluster=0 active=False
    id=2 h=130.00220002420053 cluster=0 active=False
Done at iteration 4

[\[Title\](../src/tests/random-plots/20260703_025535)](../src/tests/random-plots/20260703_030049)
</details>

Grid, corner node largest, closest nodes in range but rest out of range

x = [100, 200, 300, 100, 200, 300, 100, 200, 300]
y = [100, 200, 300, 200, 100, 200, 300, 300, 100]
r = [300, 120, 10, 120, 120, 10, 10, 10, 10]

<details>
<summary>Log and FileID</summary>
Step 1 | Ω=(100.0, (0, 1), 'Edge')
    id=0 h=110 cluster=0 active=True
    id=1 h=110 cluster=1 active=True
    id=2 h=110 cluster=2 active=True
  Edge decimate: u=0 (cluster=0) v=1 (cluster=1)
  in_range check: True
  adj weight: 100.0
Step 2 | Ω=(99.99779997579945, (0, 2), 'Edge')
    id=0 h=120.0 cluster=0 active=True
    id=1 h=120.0 cluster=0 active=False
    id=2 h=110 cluster=2 active=True
  Edge decimate: u=0 (cluster=0) v=2 (cluster=2)
  in_range check: True
  adj weight: 99.99779997579945
Step 3 | Ω=(130.00220002420053, 0, 'Node')
    id=0 h=130.00220002420053 cluster=0 active=True
    id=1 h=120.0 cluster=0 active=False
    id=2 h=130.00220002420053 cluster=0 active=False
Done at iteration 4, plots saved to '/Users/sophie/Desktop/Kovacs/kovacs_lab/src/structures/../tests/random-plots/20260703_030049/'
(.venv) sophie@Sophies-Laptop-3 kovacs_lab % /Users/sophie/Desktop/Kovacs/kovacs_lab/.venv/bi
n/python /Users/sophie/Desktop/Kovacs/kovacs_lab/src/structures/sdrg.py
Step 1 | Ω=(100.0, (0, 3), 'Edge')
    id=0 h=300 cluster=0 active=True
    id=1 h=120 cluster=1 active=True
    id=2 h=10 cluster=2 active=True
    id=3 h=120 cluster=3 active=True
    id=4 h=120 cluster=4 active=True
    id=5 h=10 cluster=5 active=True
    id=6 h=10 cluster=6 active=True
    id=7 h=10 cluster=7 active=True
    id=8 h=10 cluster=8 active=True
  Edge decimate: u=0 (cluster=0) v=3 (cluster=3)
  in_range check: True
  adj weight: 100.0
Step 2 | Ω=(100.0, (0, 4), 'Edge')
    id=0 h=320.0 cluster=0 active=True
    id=1 h=120 cluster=1 active=True
    id=2 h=10 cluster=2 active=True
    id=3 h=320.0 cluster=0 active=False
    id=4 h=120 cluster=4 active=True
    id=5 h=10 cluster=5 active=True
    id=6 h=10 cluster=6 active=True
    id=7 h=10 cluster=7 active=True
    id=8 h=10 cluster=8 active=True
  Edge decimate: u=0 (cluster=0) v=4 (cluster=4)
  in_range check: True
  adj weight: 100.0
Step 3 | Ω=(340.0, 0, 'Node')
    id=0 h=340.0 cluster=0 active=True
    id=1 h=120 cluster=1 active=True
    id=2 h=10 cluster=2 active=True
    id=3 h=320.0 cluster=0 active=False
    id=4 h=340.0 cluster=0 active=False
    id=5 h=10 cluster=5 active=True
    id=6 h=10 cluster=6 active=True
    id=7 h=10 cluster=7 active=True
    id=8 h=10 cluster=8 active=True
Step 4 | Ω=(120, 1, 'Node')
    id=0 h=340.0 cluster=0 active=False
    id=1 h=120 cluster=1 active=True
    id=2 h=10 cluster=2 active=True
    id=3 h=320.0 cluster=0 active=False
    id=4 h=340.0 cluster=0 active=False
    id=5 h=10 cluster=5 active=True
    id=6 h=10 cluster=6 active=True
    id=7 h=10 cluster=7 active=True
    id=8 h=10 cluster=8 active=True
Step 5 | Ω=(10, 2, 'Node')
    id=0 h=340.0 cluster=0 active=False
    id=1 h=120 cluster=1 active=False
    id=2 h=10 cluster=2 active=True
    id=3 h=320.0 cluster=0 active=False
    id=4 h=340.0 cluster=0 active=False
    id=5 h=10 cluster=5 active=True
    id=6 h=10 cluster=6 active=True
    id=7 h=10 cluster=7 active=True
    id=8 h=10 cluster=8 active=True
Step 6 | Ω=(10, 5, 'Node')
    id=0 h=340.0 cluster=0 active=False
    id=1 h=120 cluster=1 active=False
    id=2 h=10 cluster=2 active=False
    id=3 h=320.0 cluster=0 active=False
    id=4 h=340.0 cluster=0 active=False
    id=5 h=10 cluster=5 active=True
    id=6 h=10 cluster=6 active=True
    id=7 h=10 cluster=7 active=True
    id=8 h=10 cluster=8 active=True
Step 7 | Ω=(10, 6, 'Node')
    id=0 h=340.0 cluster=0 active=False
    id=1 h=120 cluster=1 active=False
    id=2 h=10 cluster=2 active=False
    id=3 h=320.0 cluster=0 active=False
    id=4 h=340.0 cluster=0 active=False
    id=5 h=10 cluster=5 active=False
    id=6 h=10 cluster=6 active=True
    id=7 h=10 cluster=7 active=True
    id=8 h=10 cluster=8 active=True
Step 8 | Ω=(10, 7, 'Node')
    id=0 h=340.0 cluster=0 active=False
    id=1 h=120 cluster=1 active=False
    id=2 h=10 cluster=2 active=False
    id=3 h=320.0 cluster=0 active=False
    id=4 h=340.0 cluster=0 active=False
    id=5 h=10 cluster=5 active=False
    id=6 h=10 cluster=6 active=False
    id=7 h=10 cluster=7 active=True
    id=8 h=10 cluster=8 active=True
Step 9 | Ω=(10, 8, 'Node')
    id=0 h=340.0 cluster=0 active=False
    id=1 h=120 cluster=1 active=False
    id=2 h=10 cluster=2 active=False
    id=3 h=320.0 cluster=0 active=False
    id=4 h=340.0 cluster=0 active=False
    id=5 h=10 cluster=5 active=False
    id=6 h=10 cluster=6 active=False
    id=7 h=10 cluster=7 active=False
    id=8 h=10 cluster=8 active=True
Done at iteration 10

[Title](../src/tests/random-plots/20260703_030245)
</details>


Grid w/ middle node largest, radius grows to in_range for rest

x = [100, 200, 300, 100, 200, 300, 100, 200, 300]
y = [100, 200, 300, 200, 100, 200, 300, 300, 100]
r = [100, 300, 100, 100, 100, 100, 100, 100, 100]

<details>
<summary>Log and FileID</summary>
Step 1 | Ω=(100.0, (0, 3), 'Edge')
    id=0 h=100 cluster=0 active=True
    id=1 h=300 cluster=1 active=True
    id=2 h=100 cluster=2 active=True
    id=3 h=100 cluster=3 active=True
    id=4 h=100 cluster=4 active=True
    id=5 h=100 cluster=5 active=True
    id=6 h=100 cluster=6 active=True
    id=7 h=100 cluster=7 active=True
    id=8 h=100 cluster=8 active=True
  Edge decimate: u=0 (cluster=0) v=3 (cluster=3)
  in_range check: True
  adj weight: 100.0
Step 2 | Ω=(100.0, (0, 4), 'Edge')
    id=0 h=100.0 cluster=0 active=True
    id=1 h=300 cluster=1 active=True
    id=2 h=100 cluster=2 active=True
    id=3 h=100.0 cluster=0 active=False
    id=4 h=100 cluster=4 active=True
    id=5 h=100 cluster=5 active=True
    id=6 h=100 cluster=6 active=True
    id=7 h=100 cluster=7 active=True
    id=8 h=100 cluster=8 active=True
  Edge decimate: u=0 (cluster=0) v=4 (cluster=4)
  in_range check: True
  adj weight: 100.0
Step 3 | Ω=(100.0, (1, 5), 'Edge')
    id=0 h=100.0 cluster=0 active=True
    id=1 h=300 cluster=1 active=True
    id=2 h=100 cluster=2 active=True
    id=3 h=100.0 cluster=0 active=False
    id=4 h=100.0 cluster=0 active=False
    id=5 h=100 cluster=5 active=True
    id=6 h=100 cluster=6 active=True
    id=7 h=100 cluster=7 active=True
    id=8 h=100 cluster=8 active=True
  Edge decimate: u=1 (cluster=1) v=5 (cluster=5)
  in_range check: True
  adj weight: 100.0
Step 4 | Ω=(100.0, (1, 7), 'Edge')
    id=0 h=100.0 cluster=0 active=True
    id=1 h=300.0 cluster=1 active=True
    id=2 h=100 cluster=2 active=True
    id=3 h=100.0 cluster=0 active=False
    id=4 h=100.0 cluster=0 active=False
    id=5 h=300.0 cluster=1 active=False
    id=6 h=100 cluster=6 active=True
    id=7 h=100 cluster=7 active=True
    id=8 h=100 cluster=8 active=True
  Edge decimate: u=1 (cluster=1) v=7 (cluster=7)
  in_range check: True
  adj weight: 100.0
Step 5 | Ω=(300.0, 1, 'Node')
    id=0 h=100.0 cluster=0 active=True
    id=1 h=300.0 cluster=1 active=True
    id=2 h=100 cluster=2 active=True
    id=3 h=100.0 cluster=0 active=False
    id=4 h=100.0 cluster=0 active=False
    id=5 h=300.0 cluster=1 active=False
    id=6 h=100 cluster=6 active=True
    id=7 h=300.0 cluster=1 active=False
    id=8 h=100 cluster=8 active=True
Step 6 | Ω=(100.0, 0, 'Node')
    id=0 h=100.0 cluster=0 active=True
    id=1 h=300.0 cluster=1 active=False
    id=2 h=100 cluster=2 active=True
    id=3 h=100.0 cluster=0 active=False
    id=4 h=100.0 cluster=0 active=False
    id=5 h=300.0 cluster=1 active=False
    id=6 h=100 cluster=6 active=True
    id=7 h=300.0 cluster=1 active=False
    id=8 h=100 cluster=8 active=True
Step 7 | Ω=(100, 2, 'Node')
    id=0 h=100.0 cluster=0 active=False
    id=1 h=300.0 cluster=1 active=False
    id=2 h=100 cluster=2 active=True
    id=3 h=100.0 cluster=0 active=False
    id=4 h=100.0 cluster=0 active=False
    id=5 h=300.0 cluster=1 active=False
    id=6 h=100 cluster=6 active=True
    id=7 h=300.0 cluster=1 active=False
    id=8 h=100 cluster=8 active=True
Step 8 | Ω=(100, 6, 'Node')
    id=0 h=100.0 cluster=0 active=False
    id=1 h=300.0 cluster=1 active=False
    id=2 h=100 cluster=2 active=False
    id=3 h=100.0 cluster=0 active=False
    id=4 h=100.0 cluster=0 active=False
    id=5 h=300.0 cluster=1 active=False
    id=6 h=100 cluster=6 active=True
    id=7 h=300.0 cluster=1 active=False
    id=8 h=100 cluster=8 active=True
Step 9 | Ω=(100, 8, 'Node')
    id=0 h=100.0 cluster=0 active=False
    id=1 h=300.0 cluster=1 active=False
    id=2 h=100 cluster=2 active=False
    id=3 h=100.0 cluster=0 active=False
    id=4 h=100.0 cluster=0 active=False
    id=5 h=300.0 cluster=1 active=False
    id=6 h=100 cluster=6 active=False
    id=7 h=300.0 cluster=1 active=False
    id=8 h=100 cluster=8 active=True
Done at iteration 10

20260703_030539
</details>


