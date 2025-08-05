# ai_test

This repository contains a simple script for running multiple fetchers to retrieve reference data. The `fetch.py` script reads a YAML configuration file and uses various fetchers to query sources like Semantic Scholar, Crossref, Scopus, and Web of Science.

## Usage

Run the script with Python 3.x:

```
python fetch.py


```


The script expects a configuration file at `config/reference_queries.yaml` containing the search queries. Each entry in the YAML file should specify a `name`, a `key`, and a set of `search_terms` corresponding to the fetchers you want to run.

## Requirements

Install dependencies using:
```
pip install -r requirements.txt
```

The `requirements.txt` file lists the Python packages needed to run the scripts (e.g., PyYAML).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Additional Scripts

The repository also includes a simple script for counting letters in a word. Run it as follows:

```
python count_letters.py
```

This script will prompt you to enter a word and then display the number of letters.
