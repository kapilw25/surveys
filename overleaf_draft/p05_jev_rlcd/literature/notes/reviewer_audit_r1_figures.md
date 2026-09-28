# Reviewer audit of figures 1 to 11 (P05)

## Round 2 (re-verification after the fix pass)

Inputs checked: the new renders `deliverables/fig1_p05-1.png` to `fig11_p05-1.png`, re-rendered at 400 to 500 dpi for zooms. They are now acmart acmsmall, 395 pt wide. Also checked: `figures/*.tex`, the generators (`build/p05_common.py`, `gallery.py`, `gen_corpus.py`, `gen_taxonomy.py`, `gen_phaseA.py`, `gen_fig11.py`, `gen_jev_market.py`) and the data (`literature/corpus.tsv`, `s4_families.tsv`, `gallery_licences.tsv`, `merge_report.md`, `harvest/h*.tsv`, `notes/prior_surveys.md`, `build/phaseA_meta.json`, `notes/jev_decision_index_2026-09-27.json`, `refs.bib`, `corpus.bib`, `build/all.bbl`, `build/panels_*.tsv`).

The following numbers were re-derived and match the data:

| Figure | Numbers checked |
|---|---|
| fig2 | 108 of 408 listed; S4 = 79; 34 shown (T1 8, T2 6, T3 8, T4 8, T5 4); theory 5 |
| fig3 | 39 surveys; 33 of them from 2024 onward; TYP has 1 partial (A9 Lin) |
| fig4 | Searches 69 + 67 + 66 + 64 + 86 + 77 + 1 = 430; 22 duplicates; 11 matched; 408 included; 79 core; 329 landscape. Surveys 32 + 17 - 10 = 39. Hub 268 - 76 - 4 = 188. Board 68 systems |
| fig5 | 408; 79; 5 stages; 39; 460 bib entries; stage bars 35 / 34 / 63 / 126 / 79 / 5 / 66 |
| fig6 | Every bar, including access 221 / 126 / 49 / 12 |
| fig7 | 75 of 79 (95%); 38 of 258; every series point |
| fig11 | The three open systems with the highest skill are Surogate Rune (0.1196), Decider chat (0.0471) and AutoJev-27B (0.0178); Jev has skill 57.91 and ECE 0.074; the board has 67 non-hosted systems, 51 with open weights and 16 code only |

I opened two licences on arXiv, 2406.12673 and 2604.23333; both are CC BY 4.0.

### Status of the 38 round-1 findings

| # | artefact | round-1 finding (short) | status | evidence now |
|---|---|---|---|---|
| 1 | fig2 | Leaf text about 4 pt | NO LONGER APPLICABLE | You chose to keep fig2 at one page. For the record, the leaf line pitch is now about 9 px at 200 dpi, i.e. about 2.7 pt text |
| 2 | fig1 | The "Inside training" row was mostly X works, chosen alphabetically | FIXED | The row is now S4 only: Guo 2026 (T1), Yang 2026 (T3), Gao 2026 (T4), Wang 2026b (T5). The caption states the rule |
| 3 | fig1, fig8, fig9 | Centre-crop discarded 35-65% of each source | FIXED | `--fit` letterboxes every tile; whole figures are visible (400 dpi crop of the fig8 S4 row) |
| 4 | fig8, fig9 | S4 panels were old | FIXED | fig8 S4 panels are all from 2026; fig9 S4 panels are Steyvers 2025, Tan 2026, Zhang 2025 and Yaldiz 2026 |
| 5 | fig8, fig9 | S1 missing from fig8; S2 thin in fig9 | FIXED | Every stage has 2 to 4 panels in both figures |
| 6 | fig1, fig8, fig9 | False "vector, full resolution" sentence | FIXED | Removed from all three captions |
| 7 | fig1, fig8, fig9 | No licence recorded per panel | FIXED | Every panel is `reusable=yes`, CC BY 4.0, in `gallery_licences.tsv`; there is a licence column in Table 7; two licences checked on arXiv |
| 8 | fig1 | The top-row title did not fit its panels | FIXED | The row is retitled "read-off, post-hoc maps, prompts, extra inference (S0 to S3)", with one panel per stage (S0 Gottesman, S1 Luo, S2 Kumar, S3 Cohen) |
| 9 | fig2, fig4, fig7 | Theory works counted inside S4 | FIXED | A separate stage, TH, holds 5 works; the core is 79 in fig2, fig4, fig5 and fig7 |
| 10 | fig2 | T families assigned by regex | FIXED | `s4_families.tsv` assigns each of the 84 works by hand, with a reason. hager2025 is now T1; park2025 and ma2026 are T2 |
| 11 | several | Stage colours differed between figures | FIXED | One palette, `p05_common.SCOLOR`, used by fig2, fig5, fig7, fig8, fig9 and fig10 (a residual in fig1 is new finding N7) |
| 12 | several | Stage names and X grouping differed | FIXED | One name table, `SNAME`; fig1 no longer shows X; fig4 places X in the landscape (a residual in fig10 is N9) |
| 13 | fig3 | Bare surnames with no citation | NOT FIXED (now minor) | Each label now links to arXiv or the DOI, but the printed label is still a bare surname with no year or Table 1 id. "Zhang" appears in two lanes and "Li" in two forms |
| 14 | fig3 | Caption overclaims on TYP and "most" | FIXED | "33 of the 39 ... (1 partial: Lin 2026)"; both re-derived |
| 15 | fig3 | Off-axis lanes; "tier" | FIXED | Lanes C and E dropped (39 surveys); lanes are now "topic group" |
| 16 | fig4 | Build vocabulary in PRISMA | FIXED | "harvester", "adversarial audits" and "keys" are gone; the figure now says "citation searching" and "matched to references already cited" |
| 17 | fig4 | No sources, dates or search strings | NOT FIXED (now minor) | The figure is now "adapted from PRISMA 2020" and screening is marked "not recorded". But the main column still says only "7 web searches", with no engine, date or query, while the side box does date the Hub search |
| 18 | fig4 | "Jev" undefined | FIXED | The caption now says "Jev is a hosted typed-decision model (Table A1)" (the link is new finding N5) |
| 19 | fig4, fig2 | Corpus year conflicts with bib year | NOT FIXED (now minor) | fig2 still prints "Rewarding Doubt ... [Bani-Harouni et al. 2026a]" (arXiv 2503.02623, first version 2025) and "Leng ... [Leng et al. 2025]" (2410.09724). corpus.tsv says 2025 and 2024, and fig6/fig7 count them under those years |
| 20 | fig6 | "harvester" sentence | FIXED | Relabelled "not reported"; "harvester" is gone (the new meaning of the label is N11) |
| 21 | fig6 | Metric panel misleading | NO LONGER APPLICABLE | Panel (d) now shows access (221 / 126 / 49 / 12, re-derived) |
| 22 | fig10 | S4 wording and callout contradicted the core | FIXED | "S4 a calibration term enters the training loss or reward"; the callout now covers parsing and enforcement only |
| 23 | fig11 | Data-like dots; "vendor evaluations" | FIXED | Panels (a) and (d) are measured from the board JSON; the typed dots and the vendor phrase are gone (scope is new finding N4) |
| 24 | fig3, fig10, fig11 | Wrong page geometry | FIXED | acmart acmsmall at 395 pt; fig3 and fig11 fit; fig10 is only 1.59 pt overfull |
| 25 | fig2 | "other" families | FIXED | The 14 S0 works are now "empirical studies of read-off calibration" (titles checked: all empirical); S1's "other" is split into three named families |
| 26 | fig9 | Kalai tile credit | NO LONGER APPLICABLE | The tile is no longer in fig9 |
| 27 | fig2 | "evenly spaced in time"; shading sentence | FIXED | Now "evenly spaced over the family's works in year order"; the shading sentence is removed |
| 28 | fig2 | Family names differed | FIXED | One `TNAME` in `p05_common` (a residual in novelty_gap.md is N13) |
| 29 | fig3 | Labels and dots ambiguous | NOT FIXED (minor) | 500 dpi crop of lane A: the Xie leader line strikes through "Shorinwa"; the S. Li, Huang and Beigi dots overlap; Ulmer's dot overlaps Z. Xia's hollow mark; M. Zhang's hollow mark overlaps G. Liu's dot |
| 30 | fig1, fig8, fig9 | Truncated or duplicate labels | NOT FIXED (now major; see N2) | Truncation is fixed. But the a/b suffixes are computed inside the gallery, not taken from the paper's citations, so 12 panel labels disagree with the paper's citation labels |
| 31 | fig8 | Non-calibration methods under a calibration title | FIXED | Retitled "How confidence is produced and used"; PICARD removed |
| 32 | fig5 | Process sentence; typed count; redundancy | FIXED | Sentence removed; stage count computed (`nst`); "verified" dropped (the 460 count is N10) |
| 33 | fig6 | 2026 partial year not flagged | FIXED | "2026*" with "(*2026 is partial)" |
| 34 | fig7 | Defensive sentence; solid 2026 segment | FIXED | Sentence removed; the 2025 to 2026* segment is dashed |
| 35 | fig4 | Box and caption disagree; hyphenation | NOT FIXED (minor) | The box says "7 web searches, one per stage (two for S3)", but S0 and S1 share one search (h1: "S0 and S1 69"), so there are 6 stage searches plus 1. Words still break: "nor-malised", "ex-cluded" |
| 36 | fig11 | "decision ECE" undefined; axis mismatch | FIXED | Defined in the caption; the axis reads "probability on the chosen option" |
| 37 | fig1 | Rhetorical title | FIXED | Now declarative |
| 38 | fig10, fig11 | Internal notes in the source | FIXED | "P3 analogue" is gone; fig11 is auto-generated |

Summary: 27 FIXED, 7 NOT FIXED (1 of them now major), 4 NO LONGER APPLICABLE.

### New defects found in round 2

| artefact | check | what the reader sees | evidence | severity | fix |
|---|---|---|---|---|---|
| fig1, fig8, fig9 | R7 | Panel labels contradict the paper's citation labels. The fig1/fig8 panel "Wang 2026b" is the Process Supervision paper, which the paper cites as Wang et al. 2026d; "Wang et al. 2026b" in the reference list is the conformal paper, shown in fig9 as "Wang 2026a". The fig8 panel "Wang 2025b" (SLOT) is cited as 2025c, and the paper's 2025b is the one fig9 calls "Wang 2025a" | `gallery.label_names()` assigns suffixes only among gallery rows. Compared with `build/all.bbl`, 12 panel instances disagree: Yang 2026 (2026b), Wang 2026b (2026d), Wang 2025b (2025c), Aggarwal 2023 (2023b), Liu 2023 (2023a), Yang 2024 (2024b), Wang 2025a (2025b), Wang 2026a (2026b), Li 2025 (2025f), Zhang 2025 (2025c) | major | Take each label from the .bbl (natbib `\citeauthor`/`\citeyear`, or parse `\bibitem[...]`), so the label equals the in-text citation |
| fig8, fig9 | R4, R6 | The caption states "newest first, one per method family (one per training family T1 to T5 at S4), at most 4 per stage". Six of the 12 stage rows repeat a family | fig8 S1: Luo 2026 and Ulmer 2024a (both learned calibrators). fig8 X: Taubenfeld and Aggarwal (both adaptive compute). fig9 S0: Stengel-Eskin and Ahuja (both empirical). fig9 S1: Luo 2026, Ulmer 2024a and Dhuliawala (all three learned calibrators). fig9 S2: Marashian and Wang 2025a (both verbalised numeric). fig9 S4: T1 twice, T3 twice, and no T2, T4 or T5. `rule_order()` is a round-robin that repeats families once each family has one panel | major | State the real rule ("families taken in turn, largest first, newest within a family"), or cap at one per family and leave the cells empty. Say in fig9 which T families have no reusable results figure |
| fig1, fig8, fig9 | R10 | The whole-figure tiles are thumbnails whose text cannot be read in print | Cell width is 3.36 cm. For example, Yang 2026 (a source 1455 px wide at 200 dpi, i.e. 7.3 in) is reduced 0.18 times, so its 7-8 pt labels print at about 1.3 pt. Also unreadable: Guo 2026, Doula 2025, Luo 2026 (fig8); Sanz-Guerrero, Tan 2026, Yaldiz 2026, Fanconi 2025 (fig9) | major | Let wide source figures span two cells, or use 2 to 3 columns (fewer panels per row). Keep only panels whose key labels print at 5 pt or more |
| fig11 | R12, R11, R4 | Both measured panels come from one leaderboard for one product family: Jev plus 67 Jev-style systems (names such as AutoJev and Jev-Style), with Jev drawn as a bold starred point. "Skill" is not defined, and the caption gives no provenance or limits | The JSON source is `multimodalart-jev-decision-index.static.hf.space`, "Decision Index 0.2.1", generated 2026-09-27, 32 calibration benchmarks, 1-in-6 sample of requests, not peer reviewed | major | Give the board's source, date, sampling and benchmark set in the caption, and define skill. Draw Jev like the other systems. Otherwise move (a) and (d) to the appendix beside Table A2 and keep (a) to (d) schematic in the main text |
| fig10, fig4 | R11 | A vendor homepage is linked from two captions: "Jev (TypeSafe AI)" linking to typesafe.ai. fig10 frames the survey's decision loop as that product's interface | `\href{https://typesafe.ai/}{Jev}` in the fig10 caption (fig_decision_loop.tex) and in gen_corpus.fig4 | minor | Refer to Tables A1/A2 without a vendor link, e.g. "hosted and open typed-decision models (Tables A1, A2) expose this interface" |
| fig1 | R1, R4 | The caption says "the other families have no reusable figure that passed the visual check, or exceed four panels". "Passed the visual check" describes the authors' curation, and the clause is garbled: only T2 is missing | fig_hero_collage.tex caption. No T2 panel exists in either gallery | minor | "T2 (reward-model calibration) has no figure under a reuse licence" |
| fig1 | R7 | The top band spans S0 to S3 but is drawn in S1's blue | `gallery.compile_()`: `{A:SCOLOR["S1"]}` | minor | Use a neutral colour for the S0 to S3 group band |
| fig1, fig8 | R10 | The Gao 2026 and Wang 2026b tiles carry a stray horizontal rule above the figure (captured from the source page) | 400 dpi crop of the fig8 S4 row, top of tiles 3 and 4 | minor | Trim the extraction box below the rule, or mark the tiles keep-trim and re-crop |
| fig10 | R7 | The stage tags "S1 post-hoc", "S2 prompt" and "S3 repeated or set-valued inference" differ from the shared names ("S1 post-hoc map", "S2 prompt elicitation", "S3 extra inference") | fig_decision_loop.tex is hand-written and does not use `SNAME` | minor | Use the SNAME short forms on the tags |
| fig5 | R3 | "460 references in total" counts every bib entry, forced in by `\nocite{*}`. That includes the 10 surveys fig4 excludes as off-axis | refs.bib phaseA block: "49 prior surveys" (still includes C/E, e.g. xiao2023survey on non-autoregressive generation); `build_all.py` adds `\nocite{*}` | minor | Count the references the paper actually cites, or drop the 10 off-axis entries from refs.bib |
| fig6 | R4 | "'not reported' marks a value the paper does not state" asserts something about 5 works (contract) and 12 works (access). In round 1 the same code meant "could not be determined" | corpus.tsv `?` values were not re-checked (no field_overrides for them) | minor | Re-check the 17 works, or label the value "not determinable" |
| fig2, fig4, fig5 | R4 | Core = 79 includes park2025know and ma2026distributional, whose `trained=partial` means "a separate estimator is trained" (Table legend). fig4 defines core as a calibration term in "the model's own training loss or reward" | corpus.tsv: the only 2 S4 rows with trained is not yes. `p05_common.LEGEND` defines "partial" | minor | Either state in fig4/Table 2 that T2 includes calibrating the reward model, or re-mark the two rows |
| novelty_gap.md (vs fig2) | R7 | The family names in the novelty claim no longer match the figures: "supervised confidence targets", "proper-scoring-rule RL", "action-targeted rewards", "process- and meaning-level confidence rewards" | Compare `p05_common.TNAME`: "T1 supervised calibration objectives", "T3 calibration rewards on stated confidence", "T4 abstention and refusal training" | minor | Update novelty_gap.md to the TNAME wording |
| fig1, fig8, fig9 (source) | R11 | Stale inputs would ship with the source: 45 old `tile_*.jpg` sit beside the PNGs the figures use | figures/img: hero_collage has 20 files for 8 panels; method_gallery 35 for 20; results_gallery 42 for 24 | minor | Delete the unused JPEGs in the gallery build |
| fig11 | R10 | Tick labels and legend text are at `\tiny` (5 pt on a 10 pt body) | 18 `\tiny` nodes in fig_future_protocol.tex | minor | Use `\scriptsize` (7 pt) |

### Per-artefact state

| artefact | state | open items |
|---|---|---|
| fig1 | FIX | N2, N3, N6, N7, N8 |
| fig2 | FIX | #19, N12 |
| fig3 | FIX | #13, #29 |
| fig4 | FIX | #17, #19, #35, N5, N12 |
| fig5 | FIX | N10, N12 |
| fig6 | FIX | N11 |
| fig7 | CLEAN | Every number re-derived; one palette and shared names; 2026 dashed and flagged; theory exclusion stated; no process or chat text; fits the page |
| fig8 | FIX | N1, N2, N3, N8 |
| fig9 | FIX | N1, N2, N3 |
| fig10 | FIX | N5, N9 |
| fig11 | FIX | N4, N15 |

(Ids of the new findings, by row of the new-defects table: row 1 = N2 citation labels, row 2 = N1 selection rule, then rows 3 to 15 = N3 thumbnails, N4 leaderboard scope, N5 vendor link, N6 hero caption, N7 band colour, N8 stray rule, N9 fig10 tags, N10 460 references, N11 "not reported", N12 trained=partial, N13 novelty_gap names, N14 stale JPEGs, N15 tiny fonts.)

11 artefacts, 1 CLEAN, 10 FIX

REVIEWER VERDICT: FIX

## Round 3 (re-verification after the second fix pass)

Inputs checked: the new renders `deliverables/fig*_p05-1.png`, re-rendered at 500 dpi to zoom into fig3 and fig11. Also checked: the current `figures/*.tex`, `build/gallery.py`, `gen_corpus.py`, `gen_taxonomy.py`, `gen_phaseA.py`, `gen_fig11.py` and `p05_common.py`, and the data in `literature/corpus.tsv`, `s4_families.tsv`, `field_overrides.tsv`, `notes/jev_decision_index_2026-09-27.json`, `notes/jev_hf_models.md`, `build/all.bbl` and `build/panels_*.tsv`. The acmsmall text block was measured with acmart itself: `\textheight` = 574.0 pt and `\textwidth` = 395.8 pt.

The following numbers were re-derived and match the data:

| Figure | Numbers checked |
|---|---|
| fig2 | 108 of 408; S4 = 79; 34 shown; theory 5 |
| fig3 | 39 surveys; 33 from 2024 onward; 1 partial |
| fig4 | 430 / 22 / 11 / 408 / 79 / 329; 32 + 17 - 10 = 39; 268 - 76 - 4 = 188; 68 systems |
| fig5 | 450 = 460 bib entries - 10 off-axis surveys. None of the 10 is cited in any figure or table; 449 of the remaining 450 are cited in figures or tables |
| fig6 | Contract 166 / 79 / 95 / 41 / 22 / 5, after the new overrides for singh2026structured and others; access 221 / 126 / 49 / 12 |
| fig7 | 75 of 79 (95%); 38 of 258 |
| fig11 | 38 panel benchmarks, 32 calibration benchmarks, 1-in-6 sample, Decision Index 0.2.1, generated 2026-09-27. "Chance-normalised" skill is confirmed in `jev_hf_models.md`, line 27 |

Gallery labels: all 40 panel labels in fig1, fig8 and fig9 now equal the `\bibitem` labels in `build/all.bbl` (0 mismatches).

### Status of the items open after round 2

| item | status | evidence now |
|---|---|---|
| #13 fig3 bare surnames | FIXED | Labels read "surname year" (e.g. "Xia 2025" vs "Xia 2026", "M. Zhang 2026") and each links to the survey |
| #17 fig4 sources and dates | FIXED | "7 web searches run on 2026-09-26 (queries not recorded)". How that date is computed is new finding R3-6 |
| #19 corpus vs bib year | FIXED | The fig2 caption now says citations show the publication year, which can differ from the first-version year counted in Figures 6 and 7 |
| #29 fig3 overlaps | FIXED | Leader lines are drawn under the label fills, so no line strikes through a label, and every label is centred on its own mark (500 dpi crop of lane A). Coincident dots remain but each has its own label |
| #30 / N2 gallery labels vs citations | FIXED | 0 of 40 labels differ from all.bbl (e.g. "Yang et al. 2026b", "Wang et al. 2025c", "Wang et al. 2026b" for wang2026conformal) |
| #35 fig4 box vs caption; hyphenation | FIXED | "one per stage (two for S3)" removed; `\hyphenpenalty=10000`; no broken words in the render |
| N1 selection rule | FIXED | Every stage row in fig8 and fig9 now has distinct families (checked against corpus `group` and `tfam`), with at most 3 per stage, as the caption says. A residual is new finding R3-7 |
| N3 unreadable thumbnails | NOT FIXED (major) | fig8/fig9 tiles are 4.51 cm wide, but wide sources still shrink about 0.25 times. Doula 2025 (1455 px source) and Yang 2026b, Guo 2026 and Gao 2026 in fig8, and Stengel-Eskin 2022, Luo 2026, Luo 2025, Marashian 2026, Ferrer 2026, Tan 2026 and Soiffer 2025 in fig9, print their labels at about 1.5 to 2 pt. fig1 keeps 4 columns at 3.36 cm (about 0.18 times: Doula, Yang, Guo, Tan are unreadable) |
| N4 fig11 leaderboard scope | FIXED | The caption gives source, release, single snapshot, not peer reviewed, sampling, benchmark counts and the definition of skill, all checked against the JSON and jev_hf_models.md. Jev is a hollow diamond the same size as the other marks |
| N5 vendor link | FIXED | No `\href` to typesafe.ai in fig4 or fig10; fig10 names "TypeSafe AI" once, as the source of Jev |
| N6 hero caption curation wording | FIXED | "passed the visual check" is gone from fig1. (The fig1 caption now contradicts its panels: new finding R3-4) |
| N7 hero band colour | FIXED | The S0 to S3 band is a neutral grey |
| N8 stray page rules | FIXED | The fig1 and fig8 Gao 2026 tiles are clean; Wang 2026b is no longer in a gallery |
| N9 fig10 tags | FIXED | "S0 read-off", "S1 post-hoc map", "S2 prompt elicitation", "S3 extra inference (repeated or set-valued)"; p(option given state) is restored |
| N10 460 references | FIXED | "450 references in the bibliography", consistent with the bib minus the 10 uncited off-axis surveys |
| N11 "not reported" | FIXED | Tick labels and caption read "not determinable ... could not be determined from the paper" |
| N12 trained=partial in core | FIXED | The T2 definition (`p05_common.TDEF`) now says its works are marked Trained = partial when the policy is not retrained; TH rows are Trained = no |
| N13 novelty_gap family names | FIXED | novelty_gap.md T1 to T5 now match TNAME |
| N14 stale tiles | NOT FIXED (minor) | The JPEGs are gone, but 12 unused PNGs remain: method_gallery has 20 files for 16 panels, results_gallery 24 for 16 |
| N15 fig11 `\tiny` | FIXED | No `\tiny` in fig_future_protocol.tex. The larger legend now overflows: new finding R3-3 |

### New defects found in round 3

| artefact | check | what the reader sees | evidence | severity | fix |
|---|---|---|---|---|---|
| fig8, fig9 | R10 | Each gallery is taller than the page, so it cannot be placed in the paper; LaTeX will report "Float too large" and the bottom will be cut off | Each deliverable page is 820.7 pt tall. The acmsmall `\textheight` is 574.0 pt (measured with acmart), and even the paper is only 722.7 pt tall. The 3-column change made the grid 6 rows of 4.5 cm tiles | block | Split each gallery in two (S0 to S2 and S3 to X), or go back to 4 columns with 2-column-wide cells only for wide sources. Keep each float at 574 pt or less, including the caption |
| fig2 | R10 | The taxonomy float is taller than the text block. This is about fit, not text size (your one-page decision is kept) | The deliverable page is 604.3 pt against a 574.0 pt `\textheight`: the forest is scaled to `0.9\textheight` (516.6 pt) and the longer caption adds about 88 pt | major | Scale to about `0.84\textheight`, or shorten the caption, so that the figure plus caption fits in 574 pt |
| fig11 | R10 | The legend of panel (a) runs about 1.3 cm into panel (b), printing over (b)'s risk axis and dashed baseline ("...(ECE 0.120)", "...(ECE 0.047)") | 500 dpi crop around the (a)/(b) boundary. The legend nodes are anchored at 0.57 W with `\scriptsize` text and the long system names | major | Put the legend below panel (a), or in two lines with short names (e.g. "Surogate Rune", "Decider chat"), and check that nothing crosses x = W |
| fig1 | R4 | The caption says "one per training family for S4 (T1, T3, T4; T2, T5 not shown)", but the S4 row has 4 panels and two are T3: Yang et al. 2026b and Tan et al. 2026 | panels_hero_collage.tsv; corpus `tfam`: yang2026scaling = T3, tan2026on = T3 | minor | Drop the second T3 panel (3 panels, or add T5 wang2026process, which is CC BY), or reword the caption |
| fig8, fig9 | R6 | The S4 rows omit families without saying so: fig8 shows T3, T1 and T4 (no T2 or T5); fig9 shows T3 and T1 (no T2, T4 or T5). fig1's caption names its missing families, but these captions do not. For T5, a reusable figure exists (wang2026process, CC BY), so it was cut by the cap of 3, not by availability | panels_method_gallery.tsv and panels_results_gallery.tsv; gallery_licences.tsv | minor | Add "S4 shows T1, T3 and T4 (T2 has no reusable figure; T5 omitted by the cap of 3)" and the equivalent for fig9 |
| fig4 | R3 | The search date "2026-09-26" is not a recorded date. It is the modification time of the harvest files, so it changes whenever a file is re-saved | `gen_corpus.fig4`: `os.path.getmtime` of literature/harvest/h*.tsv. h5_s4training.bib was modified 2026-09-27 01:30 (the .tsv was not, so the printed date has not yet moved) | minor | Record the search dates in a data file (e.g. a `searched` column or merge_report.md) and print that value |
| fig11 | R7 | The `\Description` (alt text) says "Jev marked by a star", but the render shows a hollow diamond. The "Jev" label in (d) sits between the diamond and a code-only grey dot at skill of about 56, so it could label either | fig_future_protocol.tex, line 163; render of panel (d) | minor | Update the Description; attach the label with a short leader line to the diamond |

### Per-artefact state

| artefact | state | reason |
|---|---|---|
| fig1 | FIX | N3 (4 columns at 3.36 cm), R3-4 |
| fig2 | FIX | R3-2 (604 pt float in a 574 pt text block) |
| fig3 | CLEAN | Numbers re-derived; labels carry surname, year and link; no line crosses a label; fits (397 pt); caption claims match Table 1 data |
| fig4 | FIX | R3-6 |
| fig5 | CLEAN | Every card and bar re-derived; 450 checked; shared palette and names; no process text; fits |
| fig6 | CLEAN | Every bar re-derived (contract 79/22 after the overrides); "not determinable" defined; 2026 flagged; fits |
| fig7 | CLEAN | 75/79 and 38/258 re-derived; dashed 2026; theory exclusion stated; fits |
| fig8 | FIX | R3-1 (block), N3, R3-7, N14 |
| fig9 | FIX | R3-1 (block), N3, R3-7, N14 |
| fig10 | CLEAN | Shared tag names; no clipping (the only overfull box in all.log is in tab_future_metrics); S4 wording matches the core rule; no vendor link; fits (322 pt) |
| fig11 | FIX | R3-3, R3-5 |

Round-3 counts: of the 21 items open after round 2, 19 are FIXED and 2 are NOT FIXED (N3 major, N14 minor). There are 7 new defects: 1 block, 2 major, 4 minor.

11 artefacts, 5 CLEAN, 6 FIX

REVIEWER VERDICT: FIX

## Round 4 (re-verification after the third fix pass)

Inputs checked: the new renders (all rebuilt at 01:57 to 01:58), with the page heights measured by `pdfinfo` against the acmsmall `\textheight` of 574.0 pt (measured with acmart in round 3). I zoomed into fig6(b) and fig11(a) and (d) at 200 to 300 dpi. Also checked: `figures/*.tex`, `build/panels_*.tsv`, `build/gallery_verdicts.tsv`, `literature/gallery_licences.tsv`, `literature/harvest/search_log.tsv`, `literature/corpus.tsv` and `build/all.bbl`.

Numbers re-derived: the fig4 landscape box gives 324 = S0 35 + S1 34 + S2 63 + S3 126 + X 66, plus 5 theory works = 329, and the 5 theory works are in Table 3 (`tab_compare_s4.tex`) and not in Table 8. fig6(b) is 166 / 79 / 95 / 41 / 22 / 5. All 39 gallery labels (7 in the hero, 16 in fig8, 16 in fig9) equal their `all.bbl` labels (0 mismatches). Every hero and gallery tile file is used (7 of 7, 16 of 16, 16 of 16).

### Status of the items open after round 3

| item | status | evidence now |
|---|---|---|
| R3-1 fig8/fig9 taller than the page | NOT FIXED (block) | `pdfinfo`: fig8 and fig9 are still 395.3 x **690.4 pt** against a 574.0 pt `\textheight`, 116 pt over (the whole acmsmall page is 722.7 pt). The 4-column grid with 3 panels per stage still has 6 stage bands of tiles plus a 7-line caption |
| R3-2 fig2 taller than the text block | FIXED | `\resizebox{!}{0.84\textheight}`; page 570.0 pt, within 574.0 pt |
| R3-3 fig11 legend overflow | FIXED | 300 dpi crop: the short names ("Surogate Rune", "Decider chat") keep the legend inside panel (a); it ends about 2 mm past (a)'s arrow tip and about 1 cm short of (b)'s axis. No curve crosses a legend line |
| R3-4 hero one-per-family | FIXED | The S4 row is Yang et al. 2026b (T3), Guo et al. 2026 (T1) and Gao et al. 2026 (T4), matching "T1, T3, T4; T2, T5 not shown". All hero panels come from Figure 8, as the caption now says |
| R3-5 fig11 alt text; Jev label | FIXED | The Description says "hollow diamond"; the "Jev" label has a leader line ending at the diamond |
| R3-6 fig4 search date | FIXED | The dates come from `literature/harvest/search_log.tsv` (7 streams, each 2026-09-26, "queries not recorded"), and the generator asserts that every stream is logged. `getmtime` is no longer used |
| R3-7 omitted S4 families unnamed | FIXED | fig8: "At S4, T5 had a figure but was cut by the cap of 3. T2 has no reusable figure that passed the check" (true: wang2026process was kept and is CC BY; leng2024taming is not reusable). fig9: "T2, T4, T5 have no reusable figure that passed the check" (true: `gallery_verdicts.tsv` has no kept, reusable results tile for T2, T4 or T5) |
| N3 unreadable thumbnails | NOT FIXED (major) | fig1, fig8 and fig9 tiles are all back to 3.363 cm (4-column cells), smaller than round 3's 4.51 cm. Wide sources (e.g. Doula 2025, Yang 2026b, Guo 2026, Gao 2026, Stengel-Eskin 2022, Luo 2025/2026, Ferrer 2026, Tan 2026, Soiffer 2025) print their labels at about 1.3 to 1.5 pt. You asked for a comparison with round 2: round 2 also used 3.363 cm tiles, so **no tile is worse than in round 2**, but every tile is smaller than in round 3. The coordinator calls this a known trade-off, but no user decision records it, so it stays open |
| N14 stale tiles | FIXED | The folders are cleared before each compile: hero 7 files, 7 used; method 16, 16 used; results 16, 16 used |

### New defects found in round 4

| artefact | check | what the reader sees | evidence | severity | fix |
|---|---|---|---|---|---|
| fig6 | R7 | Panel (b) labels the category "typed", while the value everywhere else is "typed-decision": the Table 3/5/8 legend defines "typed-decision (a probability per declared option)", and the fig4/fig3 text says "typed-decision model" and "typed decision outputs" | 200 dpi crop of fig6(b); `p05_common.LEGEND`; `gen_corpus.fig6` order list still uses "typed-decision" as the data key | minor | Label the bar "typed-decision" (rotate or wrap the tick), or define "typed" in the caption as the typed-decision contract of Table 2 |

No other new defects: fig2, fig3, fig4, fig5, fig7, fig10 and fig11 were re-read against every check.
- fig10's act/abstain/escalate boxes no longer touch, and all tags use the shared names.
- fig11 (d)'s legend and the Jev leader stay clear of the data.
- fig4's landscape sum and table references are correct.

### Per-artefact state

| artefact | state | reason |
|---|---|---|
| fig1 | FIX | N3 (hero tiles 3.36 cm; Doula, Yang, Guo, Gao labels about 1.3 pt) |
| fig2 | CLEAN | Fits (570 pt); counts re-derived; year note present; leaf text size waived by your decision |
| fig3 | CLEAN | Unchanged since round 3 (caption and render re-read) |
| fig4 | CLEAN | Logged search dates; 324 + 5 = 329 re-derived; tables correctly referenced; no process vocabulary; fits |
| fig5 | CLEAN | Unchanged since round 3 (450, cards and bars re-read) |
| fig6 | FIX | New minor R7 ("typed" vs "typed-decision") |
| fig7 | CLEAN | Unchanged since round 3 (75/79, 38/258 re-read) |
| fig8 | FIX | R3-1 (block, 690 pt float), N3 |
| fig9 | FIX | R3-1 (block, 690 pt float), N3 |
| fig10 | CLEAN | Boxes separated, shared tag names, fits (317 pt) |
| fig11 | CLEAN | Legend inside (a), Jev leader line, Description matches, provenance and skill defined, fits (426 pt) |

Round-4 counts: of the 9 items open after round 3, 7 are FIXED and 2 are NOT FIXED (R3-1 block, N3 major). There is 1 new minor defect.

11 artefacts, 7 CLEAN, 4 FIX

REVIEWER VERDICT: FIX

## Round 5 (re-verification after the fourth fix pass)

Inputs checked: the renders rebuilt at 02:12, with page heights from `pdfinfo` against the acmsmall `\textheight` of 574.0 pt. I zoomed into the fig9 label rows at 400 dpi and into fig2 (S4 and theory branches) and fig5 at 200 dpi. Also checked: `figures/*.tex`, `tables/tab_panel_provenance.tex` (the Table 7 caption), `build/p05_common.py`, `build/panels_*.tsv`, `literature/gallery_licences.tsv` and `build/all.bbl`.

Re-verified:
- **Galleries:** 39 panels. All are CC BY 4.0 (`reusable=yes`), and all 39 labels equal their `all.bbl` labels. Every tile file is used (7/7, 16/16, 16/16).
- **fig4:** "Outside the core: 329 = 324 (S0 35 + S1 34 + S2 63 + S3 126 + X 66) + 5 theory works"; the caption says the theory works are listed with the core in Table 3 but not counted in it (they are in `tab_compare_s4.tex`).
- **fig6:** unchanged counts 166 / 79 / 95 / 41 / 22 / 5.

### Status of the items open after round 4

| item | status | evidence now |
|---|---|---|
| R3-1 fig8/fig9 taller than the text block | FIXED | `pdfinfo`: fig8 and fig9 are each 395.3 x 572.8 pt, within the 574.0 pt `\textheight` (1.2 pt spare). The captions are two lines and point to Table 7, whose caption now carries the selection rule and the per-figure S4 family notes |
| N3 unreadable thumbnails | NO LONGER APPLICABLE | You chose "Shrink to fit one page" and accepted tile legibility at 5 columns (2.676 cm tiles); not re-raised |
| R4 fig6 "typed" vs "typed-decision" | FIXED | The fig6 caption defines "typed: a probability per declared option; score: one stated number", matching the Table 2 / legend definitions |

### Checks of the other changes

| change | verdict |
|---|---|
| fig4 "Outside the core" box | Correct: 324 + 5 = 329 re-derived; table references correct |
| fig10 "ordinal scale"; equal action boxes | Correct in the render: act, abstain and escalate have equal height and no longer touch; the caption lists "a choice among labels, an ordinal scale or yes/no", matching the box |
| fig8/fig9 captions | "Each panel shows a whole figure of the cited paper, reproduced under its CC BY licence" is true for all 32 gallery panels (licence file). The pointer to Table 7 for the rule satisfies R6 |

### New defects found in round 5

| artefact | check | what the reader sees | evidence | severity | fix |
|---|---|---|---|---|---|
| fig9 | R10 | In the S0 row, the first label "Stengel-Eskin and Van Durme 2022" runs into the second column and prints over "Liu et al. 2023a". It reads "Stengel-Eskin and Van DurmLi 2022al. 2023a", so neither citation can be read | 400 dpi crop of the fig9 S0 label row (y about 470 to 610 px). The label is wider than the 2.676 cm tile pitch at 5 columns; before round 5 the cell was wide enough | major | Wrap long labels to two lines (or abbreviate to the natbib short form "Stengel-Eskin and Van Durme 2022" on two lines). Check that no label is wider than the cell |
| fig2, fig5 | R10, R5 | The "Theory and analysis" colour is now almost the same as S4's, so the theory group looks like part of the core. The text says it is not counted in the core | `p05_common.SCOLOR`: TH 9C6B8E vs S4 B279A2 gives CIELAB delta E of 7.5 for the full fills in fig5 (round 4's D4B0C8 gave 22.0). For fig2's 40% tints delta E is 3.0, barely above the just-noticeable 2.3. See the 200 dpi crops of the fig2 S4/theory branches and the fig5 bars | minor | Choose a TH colour clearly distinct from S4 (delta E > 15 against every stage colour), e.g. a neutral grey-brown, or a hatched fill for TH |

No other new defects. fig1, fig3, fig4, fig6, fig7, fig8, fig10 and fig11 were re-read against every check.
- **Labels:** fig8's longest labels ("Khanmohammadi et al. 2025", "Gottesman and Geva 2024") stay clear of their neighbours.
- **Fit:** all floats fit within 574 pt (the largest are fig2 at 570.0 pt and fig8/fig9 at 572.8 pt).
- **Build log:** the only overfull box in `all.log` (2.3 pt) is in a table, not a figure.

### Per-artefact state

| artefact | state | reason |
|---|---|---|
| fig1 | CLEAN | Rule-conformant panels (S0 to S3 one each; S4 T1, T3, T4), labels equal the citations, CC BY, fits (260 pt); tile legibility accepted by your decision |
| fig2 | FIX | R5-2 (TH fill nearly the same as S4) |
| fig3 | CLEAN | Unchanged; re-read |
| fig4 | CLEAN | Box and caption correct and re-derived |
| fig5 | FIX | R5-2 (TH bar nearly the same colour as the S4 bar) |
| fig6 | CLEAN | "typed" and "score" defined; counts re-derived |
| fig7 | CLEAN | Unchanged; re-read |
| fig8 | CLEAN | 572.8 pt fits; labels clear; caption true |
| fig9 | FIX | R5-1 (overprinted S0 labels) |
| fig10 | CLEAN | Equal action boxes, "ordinal scale" consistent with the caption |
| fig11 | CLEAN | Unchanged since round 4; re-read |

Round-5 counts: the 3 items open after round 4 are closed (2 FIXED, 1 NO LONGER APPLICABLE by your decision). There are 2 new defects (1 major, 1 minor).

11 artefacts, 8 CLEAN, 3 FIX

REVIEWER VERDICT: FIX

## Round 6 (re-verification after the fifth fix pass)

Inputs checked: the renders rebuilt at 02:25 and page heights from `pdfinfo`. I cropped every label row of fig8 and fig9 at 400 dpi (6 rows each, stacked) and cropped the fig2 theory branch at 200 dpi; fig1, fig5, fig10 and fig11 were viewed at full resolution. Also checked: `build/p05_common.py` (`SCOLOR`, `st<S>txt`), `figures/*.tex` (16 `\adjustbox` label wrappers in each gallery and 7 in the hero) and `tables/tab_definitions.tex`. Colour distances are CIELAB ΔE; text contrast follows the WCAG ratio.

### Status of the round-5 items

| item | status | evidence now |
|---|---|---|
| R5-1 fig9 overprinted S0 labels | FIXED | At 400 dpi, "Stengel-Eskin and Van Durme 2022" is scaled to its 2.676 cm cell and ends before "Liu et al. 2023a" begins. None of the other 30 gallery labels in fig8 and fig9 crosses a neighbour. The widest, "Khanmohammadi et al. 2025", "Gottesman and Geva 2024" and "Sanz-Guerrero et al. 2026", stay inside their cells |
| R5-2 TH vs S4 colour | FIXED | stTH is 8C6D1F. ΔE against S4 is 64.2 for full fills (fig5) and 26.2 for 40% tints (fig2); against every other stage it is at least 44.2 full and at least 15.9 tinted (smallest: S2 orange). The fig2 theory branch and the fig5 bar are visibly ochre |

### Checks of the other changes

| change | verdict |
|---|---|
| `st<S>txt` = `!70!black` for coloured text and white-on-fill tags | Contrast ratios (white on the darkened fill, or darkened text on white) are S0 6.1, S1 7.8, S2 4.9, S3 5.8, S4 6.2, TH 8.2 and X 6.5, all at least 4.5 (WCAG AA). Before the change, white on the plain S2 orange was 2.6. Seen in the fig10 tags and caption, the fig11 target labels and the gallery bands |
| Galleries at 572.8 pt | Confirmed: fig8 = fig9 = 572.795 pt, within 574.0 pt |
| fig10 actions: answer / abstain or defer / escalate | The render and the caption agree. There is a residual about meaning: new finding R6-1 |

### New defects found in round 6

| artefact | check | what the reader sees | evidence | severity | fix |
|---|---|---|---|---|---|
| fig10 | R5 | "Defer" (mid band) and "escalate" (low band) are now separate actions, but the figure no longer says where escalation goes, so the two read as synonyms. In the learning-to-defer literature, deferring is handing the case to an expert, i.e. escalating. Round 2's box said "escalate: larger model or human"; the current box shows only $p<\tau_{\mathrm{lo}}$ | fig_decision_loop.tex lines 20-21. Table 2 (tab_definitions.tex lines 18, 22) lists defer and escalate as distinct actions without defining how they differ | minor | Put the target back in the escalate box ("to a larger model or a human"), and give defer its meaning (e.g. "abstain or ask for more input"), or merge defer into escalate |

No other new defects. fig1 to fig9 and fig11 were re-read against every check.
- **Labels and fit:** hero labels are wrapped to their 3.36 cm cells; every float fits within 574 pt (fig2 570.0, fig8/fig9 572.8, the rest smaller).
- **Colours:** the darkened gallery bands keep each stage's hue, so they match the other figures.
- **fig11:** the "Jev" label and its leader line stay clear of the grey code-only dots.
- **Build log:** the only overfull box in `all.log` (2.3 pt) is in a table.

### Per-artefact state

| artefact | state | reason |
|---|---|---|
| fig1 | CLEAN | Rule-conformant panels, labels wrapped to their cells and equal to the citations, darkened bands readable, fits |
| fig2 | CLEAN | TH distinct (ΔE 26.2 tinted); fits (570 pt); counts re-derived in earlier rounds and unchanged |
| fig3 | CLEAN | Unchanged; re-read |
| fig4 | CLEAN | Unchanged since round 5; re-read |
| fig5 | CLEAN | TH bar ochre (ΔE 64.2 vs S4); counts unchanged |
| fig6 | CLEAN | Unchanged since round 5; re-read |
| fig7 | CLEAN | Unchanged; re-read |
| fig8 | CLEAN | 572.8 pt; all 16 labels clear at 400 dpi |
| fig9 | CLEAN | 572.8 pt; all 16 labels clear at 400 dpi |
| fig10 | FIX | R6-1 (defer vs escalate undefined) |
| fig11 | CLEAN | Darkened target labels legible; leader and legend clear |

Round-6 counts: both round-5 items are FIXED. There is 1 new minor defect.

11 artefacts, 10 CLEAN, 1 FIX

REVIEWER VERDICT: FIX
