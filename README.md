Neual machine translation based on Neural Monkey for Bachelor dissertation. Accessible at: waiting_for_server
## Usage

```bash
bin/neuralmonkey-train exp-nm-mt/translation.ini
bin/neuralmonkey-run exp-nm-mt/translation.ini exp-nm-mt/translation_run.ini
bin/neuralmonkey-server --configuration exp-nm-mt/translation.ini
```
## Installation
```bash
python3 -m venv nm
source nm/bin/activate
git clone https://github.com/ufal/neuralmonkey
cd neuralmonkey
pip3 install numpy 
pip install --upgrade -r requirements-gpu.txt
```

## Getting corpuses

Accessible at: http://opus.nlpl.eu/<br>
Used column: alg (row item: en-sl)<br>
CORPUSES URLS:<br>
ANG: http://opus.nlpl.eu/download/OpenSubtitles2018/en-sl/c.clean.en.gz<br>
SLO: http://opus.nlpl.eu/download/OpenSubtitles2018/en-sl/c.clean.sl.gz<br>

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
