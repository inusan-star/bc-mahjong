# bc-mahjong

## Environment Setup

### 1. Create and Activate Conda Environment

Use the provided `environment.yml` to create and activate the environment. This will install Python 3.9, project dependencies, and necessary tools.

```bash
conda env create -f environment.yml
conda activate bc-mahjong
```

### 2. Install mjx-convert

Clone the specific branch and install the `mjx-convert` tool for log conversion. This version is a fork of the [mjx-convert](https://github.com/mjx-project/mjx-convert).

```bash
git clone -b mahjong-imitator --single-branch https://github.com/inusan-star/mjx-convert.git
cd mjx-convert
make install
pip install .
cd ..
```

## Data Preparation

### 1. Place Mjlog Files

Download Tenhou `.mjlog` files (e.g., from [Tenhou Log](https://tenhou.net/sc/raw/)) and place them into the `data/mjlogs/` directory. The `data/mjlog_list.json` file contains the list of log identifiers used in this paper.

```bash
mkdir -p data/mjlogs
# Place Tenhou .mjlog files (e.g., from [Tenhou Log](https://tenhou.net/sc/raw/)) in this directory
```

### 2. Convert Mjlogs to JSON

Convert the `.mjlog` files to JSON format using the `mjx-convert` tool. The converted JSON files will be generated in the `data/json_logs/` directory.

```bash
python src/data/convert_mjlog.py
```
