## tmp-cleaner
Small file cleaning tool.
Search and delete files with specified extensions.

### How to use

clean ```.``` directory
```bash
python tmp_cleaner.py
```

or clean ```dir1, dir2, dir3``` directories
```bash
python tmp_cleaner.py dir1 dir2 dir3
```


### Default extensions
Edit this line - create your own list to avoid typing extensions every time you use the script.
```python
default_extensions = ['*.o', '*.obj', '*.class', '*.out']   # EXTENSIONS LIST
```
