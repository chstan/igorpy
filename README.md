Pygor is a package for loading binary IGOR files. It's forked from [chstan's igorpy](https://github.com/chstan/igorpy) which is forked from [igor](https://github.com/wking/igor). The main purpose of pygor is to facilitate the loading of pxt files for [arpes-lite](https://github.com/jgobbo/arpes-lite).

Installation
------------

pygor is most easily installed with pip: `pip install pygor`

you can also clone the repo and install with [uv](https://docs.astral.sh/uv/)

Usage
-----

Standard usage is straightforward:

```python
from pygor import load

byte_order = "<" # options are "<", "=", ">"
data = load(IGOR_FILE_NAME, initial_byte_order=byte_order)
```

