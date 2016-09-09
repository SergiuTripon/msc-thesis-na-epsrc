## MSc Thesis - Network Analysis on EPSRC funding data

This is a thesis project completed as part of the COMPGW99 - MSc Thesis module (MSc Web Science and Big Data Analytics) at University College London.

It proposes the application of a novel approach in graph theory, to identify coherent clusters of topics and researchers within *Networks of Topics* and *Researchers* constructed using current (2010 to 2016) and historical (1990 to 2000, 2000 to 2010) data collected from [EPSRC](https://www.epsrc.ac.uk/). For more information, please refer to the **[main thesis report](https://github.com/SergiuTripon/msc-thesis-na-epsrc/blob/master/documents/thesis/pdf/15110029_sergiu_tripon_epsrc_network_analysis.pdf)**.

####Author

Sergiu Tripon, MSc Web Science and Big Data Analytics candidate

####Supervisor

Dr. Shi Zhou, Senior lecturer at University College London

---

* **[Main thesis report](https://github.com/SergiuTripon/msc-thesis-na-epsrc/blob/master/documents/thesis/pdf/15110029_sergiu_tripon_epsrc_network_analysis.pdf)**
* **[Supplementary material](https://github.com/SergiuTripon/msc-thesis-na-epsrc/blob/master/documents/supplementary-material/15110029_sergiu_tripon_supplementary_material.pdf)**
* **[Research Data Management Plan](https://github.com/SergiuTripon/msc-thesis-na-epsrc/blob/master/documents/research-data-management-plan/pdf/15110029_sergiu_tripon_research_data_management_plan.pdf)**
* **[Repository contents](#user-content-repository-contents)**
* **[Running the source code](#user-content-running-the-source-code)**

---

### Repository contents

* **algorithms/** - [Louvain community detection algorithm](https://bitbucket.org/taynaud/python-louvain) for [NetworkX](https://networkx.github.io/)
* **analysis/** - source code written for the analysis of the network, communities and sub-communities
* **data/** - various .gephi, .graphml, .png, .tsv and .txt files related to the networks and the visualisation of the networks
* **documents/** - main thesis report, supplementary material and research data management plan
* **experiments/** - experiments carried out to trial different network analysis packages
* **literature/** - research papers in PDF format representing the state-of-the-art of several different topics
* **network-maker** - source code written to collect the data and convert it into networks, data in the form of html files downloaded from the EPSRC Grants on the Web (GoW) service
* **wiki** - various .png, .psd, .pptx and .xlsx files used to add different media to the main thesis report and the GitHub wiki
* **requirements.txt** - pip .txt requirements file that consists of the project dependencies which can be installed by running ```bash pip install -r requirements.txt``` in a terminal window

---

### Running the source code

**Note: In order to run the source code, an virtual environment installation is required. The code is written in Python 3.5. The packages used in the project are listed in the _requirements.txt_ file and can be install using _pip_**.

Running the network analysis is achieved by running the *analysis.py* file with the desired parameters (**-n** requires network (topic or researcher), **-i** requires interpretation (grants, researchers or topics), **-d** requires data set (1990-2000, 2000-2010, 2010-2016)), following the steps below:

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
