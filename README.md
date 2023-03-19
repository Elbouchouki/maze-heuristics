## PathFinding Algorithms

# grids :
  - autogenerate 
  - './exemples/normal.png'
  - './exemples/small.png'
  - './exemples/large.png'
  - './exemples/25x25.png'
  - './exemples/40x40.png'
  - './exemples/50x50.png'
  - './exemples/100x100.png'


#### BreadthFirstSearch
  
```python
python3 Main.py -g autogenerate -a breadthFirstSearch True
```

#### DepthFirstSearch

```python
python3 Main.py -g autogenerate -a depthFirstSearch True
```

#### DepthFirstSearch

```python
python3 Main.py -g autogenerate -a dijkstra True
```


#### BestFirstSearch

- bestFirstSearch euclidienne :

```python
python3 Main.py -g autogenerate -a bestFirstSearch -d euclidienne True
```

- bestFirstSearch manhattan :

```python
python3 Main.py -g autogenerate -a bestFirstSearch -d manhattan True
```

- bestFirstSearch tchebychev :

```python
python3 Main.py -g autogenerate -a bestFirstSearch -d tchebychev True
```

- bestFirstSearch minkowski :
  
```python
python3 Main.py -g autogenerate -a bestFirstSearch -d minkowski True
```

- Compare All bestFirstSearch distances :

```python
python3 Main.py -g autogenerate -c true -t bestFirstSearch
```


#### Astar

- astar euclidienne :

```python
python3 Main.py -g autogenerate -a astar -d euclidienne True
```

- astar manhattan :

```python
python3 Main.py -g autogenerate -a astar -d manhattan True
```

- astar tchebychev :

```python
python3 Main.py -g autogenerate -a astar -d tchebychev True
```

- astar minkowski :

```python
python3 Main.py -g autogenerate -a astar -d minkowski True
```

- Compare All astar distances :

```python
python3 Main.py -g autogenerate -c true -t astar
```

# Compare Everything

```python
python3 Main.py -g autogenerate -c true 
```