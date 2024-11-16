## Install numpy into conda environment

```bash
    conda install -p /Users/trathanl/pythons/venv numpy --update-deps
    pip install numpy # Alternative
```

## Adding custom package

- Add [**init**.py](./package/__init__.py) for the new package
- Add your module file, such as [maths.py](./package/maths.py)
- To import your package:

```python
    from package.maths import addition
```
