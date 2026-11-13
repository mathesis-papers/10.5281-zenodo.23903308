# A378495 difference note: reproduction

The main source is `note.tex`; it has an inline bibliography and no external
figures or TeX inputs. Build it with **Tectonic 0.17.0**:

```sh
tectonic --untrusted note.tex
```

Alternatively, run `pdflatex -interaction=nonstopmode -halt-on-error note.tex`
twice. No BibTeX pass is required because the bibliography is inline.
Use a standard TeX installation providing geometry, amsmath, amssymb, amsthm,
booktabs, fontenc, lmodern and hyperref. First-use Tectonic may download its
standard TeX bundle. No shell escape, credentials or external data are needed.

Run the included independent checks with Python 3.10 or later:

```sh
python3 verify.py
```

The script enumerates every permutation for sizes 1 through 9 and independently
computes columns by the last-label cycle recurrence through size 80. It checks
the long-cycle identity, both corrected differences, every tested failure of
the literal adjacent formula, the n=4 boundary, and row gcds for sizes 3 through
80. It writes `checks.json`; successful output says `all assertions passed`.
The finite checks are not proofs for unbounded n. The note proves the two
difference formulas and cites the full row-gcd theorem of Lien-Hung Su,
DOI 10.5281/zenodo.23445724 v1, Theorem 7.3, with Ahaan Kallat's later
independent proof in arXiv:2610.40342v1, Theorem 4.1(b) and Theorem 5.1 with r=1.

## Verification sources

The pinned Lean files contain the corresponding declarations:

https://github.com/the-omega-institute/trureturing/blob/cdafeab0d44da2b6840cfc802535d2f94a146fad/D5/S3/Combinatorics/Derangements/AdjacentDifferenceRefutation.lean

https://github.com/the-omega-institute/trureturing/blob/cdafeab0d44da2b6840cfc802535d2f94a146fad/D5/S3/Combinatorics/Derangements/TerminalDifference.lean

`AdjacentDifferenceRefutation.result` in `AdjacentDifferenceRefutation.lean`
expresses the negation of the literal universal formula, with witness n=5.
`TerminalDifference.result` in `TerminalDifference.lean` expresses the
terminal formula for all n>=5, with rational subtraction. Both are in the
namespace `D5.S3.Combinatorics.Derangements`.
The corrected adjacent formula and long-cycle identity have written proofs in
the note. The full row-gcd equality is the cited theorem of Su. The checks in
`verify.py` have the finite ranges listed above.

## Sources and reuse

The original posing source is Peter Kagey's OEIS A378495, internal revision #70
(October 17, 2026), COMMENTS and FORMULA. A238474 has offset 0. The earliest
proof found of the row gcd, both differences and the index correction is
Su's October 18, 2026 preprint, Theorem 7.3, Proposition 7.4 and Remark 7.5:
https://doi.org/10.5281/zenodo.23445724
Kallat's October 29, 2026 preprint gives a later independent proof and cites
Su in Section 1.5:
https://arxiv.org/abs/2610.40342v1
This note provides a self-contained treatment of the differences and their boundary.

The displayed zero first column of A378495 is retained as a convention;
literal avoidance of 1-cycles among derangements would instead give D_n.
This distinction affects none of the difference statements or the row gcd.

Creators, in order: Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang
(National University of Singapore; ChronoAI Pte Ltd, Singapore).
License: Creative Commons Attribution 4.0 International, `cc-by-4.0`.
https://creativecommons.org/licenses/by/4.0/

The archive contains the complete LaTeX source, metadata, exact-check program,
and finite-check certificate.
