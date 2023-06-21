from pathlib import Path
from typing import Optional

import click
from pikepdf import Pdf

from ..structure import get_structure, split_pages_structure


@click.command()
@click.argument('input-pdf', type=Path)
@click.argument('output_directory', type=Path)
@click.option('--output-prefix', '-p', type=str, default='')
@click.option('--structure-file', '-s', type=Path, default=None)
def main(
        input_pdf: Path,
        output_directory: Path,
        output_prefix: str,
        structure_file: Optional[Path]
):
    with Pdf.open(input_pdf) as pdf:
        if structure_file is not None:
            structure = get_structure(structure_file)
        else:
            structure = split_pages_structure(len(pdf.pages))
        output_directory.mkdir(parents=True, exist_ok=True)

        for start_idx, end_idx, pdf_name in structure:
            new_pdf = Pdf.new()
            for i in range(start_idx, end_idx):
                new_pdf.pages.append(pdf.pages[i])
            new_pdf.save(output_directory / f'{output_prefix}{pdf_name}.pdf')


if __name__ == '__main__':
    main()
