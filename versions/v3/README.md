# OEIS A378495, FORMULA (revision #70): refutation and correction

**Authors:** Haobo Ma, Wenlin Zhang

We refute the adjacent-column Conjecture and prove the terminal-column Conjecture in the FORMULA section of Peter Kagey's OEIS entry A378495, revision #70 of October 17, 2026. For n>=5 the corrected adjacent difference is n!/[2(n-2)]=abs(A238474(n-3)); at n=4 it is 3. The literal conjecture fails at n=5, where its sides are 20 and 6. The earliest proof found of the row gcd, both differences and the index correction is Lien-Hung Su, DOI 10.5281/zenodo.23445724 v1 (October 18, 2026), Theorem 7.3, Proposition 7.4 and Remark 7.5; Ahaan Kallat gives a later independent proof in arXiv:2610.40342v1 (October 29, 2026), Theorem 4.1. This note gives a self-contained treatment of the differences and their boundary.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23903309](https://doi.org/10.5281/zenodo.23903309)
- Concept DOI: [https://doi.org/10.5281/zenodo.23903308](https://doi.org/10.5281/zenodo.23903308)
- License: CC-BY-4.0
- Version: 3
- Mathesis record: [oeis-a378495-difference-conjectures](https://mathesis-omega-research.apps.chrono-ai.fun/papers/oeis-a378495-difference-conjectures?version=3)

## How to cite

Haobo Ma, Wenlin Zhang (2026). OEIS A378495, FORMULA (revision #70): refutation and correction. Mathesis, version 3. https://doi.org/10.5281/zenodo.23903309

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/cdafeab0d44da2b6840cfc802535d2f94a146fad/D5/S3/Combinatorics/Derangements/AdjacentDifferenceRefutation.lean) | No public receipt |
| Lemma (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/cdafeab0d44da2b6840cfc802535d2f94a146fad/D5/S3/Combinatorics/Derangements/AdjacentDifferenceRefutation.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
