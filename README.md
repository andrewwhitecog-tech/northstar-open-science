# NorthStar Open-Science Monographs, Doctoral Dissertations & Simulation Bounds Verification Suite (2026)

[![Verify Simulation Bounds & Monographs](https://github.com/andrewwhitecog-tech/northstar-open-science/actions/workflows/ci.yml/badge.svg)](https://github.com/andrewwhitecog-tech/northstar-open-science/actions/workflows/ci.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0_%2F_MIT-emerald.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Live Research Portal](https://img.shields.io/badge/Web_Portal-northstarprime.net%2Fresearch%2F-blue)](https://northstarprime.net/research/)
[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/awhi4130/northstar-open-science-monographs-2026)
[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space_Portal-orange)](https://huggingface.co/spaces/awhi4130/northstar-open-science-portal)

Open-access repository containing **7 peer-review-ready scholarly monographs & doctoral dissertations** (`monographs/`) and the **executable 10-module Python verification suite** (`simulation_bounds_verifier.py` + `test_simulation_bounds.py` + JOSS `paper.md`/`paper.bib`).

---

## 1. Quickstart: Run the Simulation Bounds Verification Suite

```bash
pip install pytest
pytest test_simulation_bounds.py -v
python simulation_bounds_verifier.py
```

The verifier deterministically reproduces:
1. **Bostrom (2003) & Kipping (2020) Bayesian Model Averaging**: $P(\mathcal{M}_{\text{base}} \mid D_0) \approx 0.5022$ vs. $P(\mathcal{M}_{\text{sim}} \mid D_0) \approx 0.4978$.
2. **Ringel & Kovrizhin (2017) *Science Advances* Quantum Sign Problem**: $(2+1)\text{D}$ anomalous quantum Hall / gravitational anomaly lattice requires $\dim(\mathcal{H}) = 2^{500} \approx 3.27 \times 10^{150} > 10^{120}$ Bekenstein-Hawking universe bits.
3. **Planck-Scale Lattice Discretization Bounds**: Greisen-Zatsepin-Kuzmin (GZK) cosmic-ray threshold ($E > 5 \times 10^{19}\text{ eV}$) and *INTEGRAL* GRB 041219A vacuum birefringence ($\ell_{\text{grain}} < 10^{-48}\text{ m} \ll \ell_P$).
4. **Vazza (2025) Landauer-Bekenstein Thermodynamic Bounds vs. Edge & Brown (2026) Observer-Bounded Evaluation**: $1.625 \times 10^{41}\times$ complexity reduction and why retroactive macroscopic history reconstruction fails under quantum entanglement monogamy and classical Lyapunov chaos.
5. **Wolpert (2024–2025) & Miralles et al. (2025) Kleene/Rice Undecidability Bounds**.
6. **Natural Morphogenesis, Dissipative Allometry, Noether Symmetry, Laplace Resonance, F1F0-ATP Synthase ($\eta \ge 0.80$), and Feynman Stationary-Phase Counter-Analyses**.

---

## 2. Seven Open-Access Monographs & Preprint Packages (`monographs/`)

| # | Monograph / Dissertation | Preprint PDF | Scholar Page | Citeable Gist |
| :--- | :--- | :--- | :--- | :--- |
| **01** | **The Master Herbal Bible: 45-Species Kew POWO Taxonomic, Phytochemical & Lookalike Toxicology Compendium** | [Preprint PDF](monographs/01_master_herbal_bible_monograph/01_master_herbal_bible_monograph_PREPRINT_2026.pdf) | [Scholar Page](https://northstarprime.net/research/papers/01_master_herbal_bible_monograph/) | [GitHub Gist](https://gist.github.com/andrewwhitecog-tech/1cfc04c65386e5c3c80105145368e21a) |
| **02** | **Cascadia Bioregional Mycoflora, Caffeic-Acid Bioluminescence & 425°F Chitin Searing Thermodynamics** | [Preprint PDF](monographs/02_master_mycelium_monograph/02_master_mycelium_monograph_PREPRINT_2026.pdf) | [Scholar Page](https://northstarprime.net/research/papers/02_master_mycelium_monograph/) | [GitHub Gist](https://gist.github.com/andrewwhitecog-tech/b46db249b85b06465f6eb28434c25940) |
| **03** | **Helios, Hydros, Aer, and Terra: Unified 6-Book Food Systems Doctoral Dissertation** | [Preprint PDF](monographs/03_food_systems_doctoral_dissertation/03_food_systems_doctoral_dissertation_PREPRINT_2026.pdf) | [Scholar Page](https://northstarprime.net/research/papers/03_food_systems_doctoral_dissertation/) | [GitHub Gist](https://gist.github.com/andrewwhitecog-tech/8a357d88a130117e967f228b4d4401e2) |
| **04** | **Formal Physical, Information-Theoretic, and Computability Constraints on the Simulation Hypothesis** | [Preprint PDF](monographs/04_simulation_hypothesis_monograph/04_simulation_hypothesis_monograph_PREPRINT_2026.pdf) | [Scholar Page](https://northstarprime.net/research/papers/04_simulation_hypothesis_monograph/) | [GitHub Gist](https://gist.github.com/andrewwhitecog-tech/4fd5d5cd5dba17cf7a0b2ea61bad47ff) |
| **06** | **Invention Forge: 88-Package Parametric STEP CAD, KiCad & Theoretical Applied Physics Compendium** | [Preprint PDF](monographs/06_invention_forge_open_hardware_compendium/06_invention_forge_open_hardware_compendium_PREPRINT_2026.pdf) | [Scholar Page](https://northstarprime.net/research/papers/06_invention_forge_open_hardware_compendium/) | [GitHub Gist](https://gist.github.com/andrewwhitecog-tech/e24654837e2ecf4d0dad7346a53e925c) |
| **08** | **Comparative Anthropological History of World Religions & Predictive Game-Theoretic Historiography** | [Preprint PDF](monographs/08_comparative_religion_and_humanities_series/08_comparative_religion_and_humanities_series_PREPRINT_2026.pdf) | [Scholar Page](https://northstarprime.net/research/papers/08_comparative_religion_and_humanities_series/) | [GitHub Gist](https://gist.github.com/andrewwhitecog-tech/aefcace8d1ef38ecb1b0be176b26022f) |
| **09** | **The Definitive Book of Hyperbaric Chamber Therapy (14 UHMS Indications, Gas Laws & 50-Q ABMS Workbook)** | [Preprint PDF](monographs/09_hyperbaric_chamber_therapy_monograph/09_hyperbaric_chamber_therapy_monograph_PREPRINT_2026.pdf) | [Scholar Page](https://northstarprime.net/research/papers/09_hyperbaric_chamber_therapy_monograph/) | [GitHub Gist](https://gist.github.com/andrewwhitecog-tech/0d12c0ca9821014a907f4f220c9ed6fa) |

---

## 3. Zenodo & JOSS Integration

- **Zenodo Automatic DOI Minting**: Root `.zenodo.json` and `CITATION.cff` are pre-configured so toggling `andrewwhitecog-tech/northstar-open-science` in [Zenodo GitHub Settings](https://zenodo.org/account/settings/github/) automatically mints a permanent DataCite DOI (`10.5281/zenodo.*`).
- **Journal of Open Source Software (JOSS)**: Root `paper.md` and `paper.bib` conform to the JOSS submission specification (`https://joss.theoj.org/papers/new`).
