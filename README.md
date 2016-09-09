## MSc Thesis - Network Analysis on EPSRC funding data

This is the thesis I completed as part of the COMPGW99 - MSc Thesis module (MSc Web Science and Big Data Analytics) which I undertook at UCL.

* **[Repository contents](#user-content-repository-contents)**
* **[Running the source code](#user-content-running-the-source-code)**

---

### Repository contents

* **algorithms/** - 
* **analysis/** - 
* **data/** - 
* **documents/** - 
* **experiment/s** -
* **literature/** - 
* **network-maker** - 
* **wiki** - 
* **requirements.txt** - 

---

### Running the source code

```bash
# activate virtual environment
$ source venv/bin/activate

# navigate to analysis source folder
$ cd msc-thesis-na-epsrc/analysis/src/

# analyse topic (grants as edges, 2010-2016)
$ python analysis.py -n topic -i grants -d 2010-2016
# analyse topic (grants as edges, 2000-2010)
$ python analysis.py -n topic -i grants -d 2000-2010
# analyse topic (grants as edges, 1990-2000)
$ python analysis.py -n topic -i grants -d 1990-2000

# analyse topic (researchers as edges, 2010-2016)
$ python analysis.py -n topic -i researchers -d 2010-2016
# analyse topic (researchers as edges, 2000-2010)
$ python analysis.py -n topic -i researchers -d 2000-2010
# analyse topic (researchers as edges, 1990-2000)
$ python analysis.py -n topic -i researchers -d 1990-2000

# analyse researcher (grants as edges, 2010-2016)
$ python analysis.py -n topic -i grants -d 2010-2016
# analyse researcher (researchers as edges, 2000-2010)
$ python analysis.py -n topic -i grants -d 2000-2010
# analyse researcher (researchers as edges, 1990-2000)
$ python analysis.py -n topic -i grants -d 1990-2000

# analyse researcher (topics as edges, 2010-2016)
$ python analysis.py -n topic -i topics -d 2010-2016
# analyse researcher (topics as edges, 2000-2010)
$ python analysis.py -n topic -i topics -d 2000-2010
# analyse researcher (topics as edges, 1990-2000)
$ python analysis.py -n topic -i topics -d 1990-2000
```
