from pathlib import Path

import click
from pikepdf import Pdf


@click.command()
@click.argument('input-front-pdf', type=Path)
@click.argument('input-back-pdf', type=Path)
@click.argument('output-pdf', type=Path)
def main(
        input_front_pdf: Path,
        input_back_pdf: Path,
        output_pdf: Path,
):
    with Pdf.open(input_front_pdf) as front_pdf:
        with Pdf.open(input_back_pdf) as back_pdf:
            n_pages = len(back_pdf.pages)
            assert(n_pages == (len(front_pdf.pages)))
            new_pdf = Pdf.new()
            for i in range(n_pages):
                new_pdf.pages.append(front_pdf.pages[i])
                new_pdf.pages.append(back_pdf.pages[n_pages - i - 1])
            new_pdf.save(output_pdf)


if __name__ == '__main__':
    main()
