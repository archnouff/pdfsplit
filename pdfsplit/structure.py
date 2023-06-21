import json
from pathlib import Path
from typing import List, Tuple

import yaml

StructureIndices = List[Tuple[int, int, str]]


def get_structure(structure_file: Path) -> StructureIndices:
    with open(structure_file, 'r') as f:
        if structure_file.suffix == '.yaml' or structure_file.suffix == '.yml':
            config = yaml.safe_load(f)
        elif structure_file.suffix == '.json':
            config = json.load(f)
        else:
            raise ValueError(f'Unknown extension: {structure_file.suffix}')
    return [(split['first'] - 1, split['last'], split['name']) for split in config['splits']]


def split_pages_structure(n_pages: int) -> StructureIndices:
    return [(i, i + 1, f'{i:06}') for i in range(n_pages)]
