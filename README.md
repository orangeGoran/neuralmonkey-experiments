Neural monkey - doing some expirements with neural machine translations. want to make own api which will provide translations from one to another languge.
## Usage

```bash
neuralmonkey-train <EXPERIMENT_INI>
neuralmonkey-run <EXPERIMENT_INI> <DATASETS_INI>
neuralmonkey-server <EXPERIMENT_INI> [OPTION] ...
neuralmonkey-logbook --logdir <EXPERIMENTS_DIR> [OPTION] ...
```

## Installation
http://neural-monkey.readthedocs.io/en/latest/

## Package Overview

- `bin`: Directory with neuralmonkey executables

- `examples`: Example configuration files for ready-made experiments

- `lib`: Third party software

- `neuralmonkey`: Python package files

- `scripts`: Directory with tools that may come in handy. Note dependencies for
   these tools may not be listed in the project requirements.

- `tests`: Test files

## License

The software is distributed under the [BSD
License](https://opensource.org/licenses/BSD-3-Clause).
```bib
@article{NeuralMonkey:2017,
    author = {Jind{\v{r}}ich Helcl and Jind{\v{r}}ich Libovick{\'{y}}},
    title = {{Neural Monkey: An Open-source Tool for Sequence Learning}},
    journal = {The Prague Bulletin of Mathematical Linguistics},
    year = {2017},
    address = {Prague, Czech Republic},
    number = {107},
    pages = {5--17},
    issn = {0032-6585},
    doi = {10.1515/pralin-2017-0001},
    url = {http://ufal.mff.cuni.cz/pbml/107/art-helcl-libovicky.pdf}
}
```
