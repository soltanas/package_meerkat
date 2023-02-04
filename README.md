# package_meerkat

package_meerkat is a Python library for visualising and discovering insights in packages.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_meerkat.

```bash
pip install package_meerkat
```

## Usage

```python
import package_meerkat
import pandas as pd

graph = package_meerkat.look_in(pd)

package_meerkat.visualize(graph)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
