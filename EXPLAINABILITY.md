# Explainability & Governance Statement

## Decision Architecture
GitDataQuality evaluates data health through statistical profiling and deterministic SLA boundaries. When a partition is loaded, the agent computes null proportions, uniqueness ratios, and distribution standard deviations. If a column violates configured null limits or exhibits severe statistical drift, the agent automatically isolates the partition and emits a quality failure report.

## Input Data Provenance
Data inputs include parquet/CSV partition files, database table statistics, schema catalog metadata, and Great Expectations assertion suites.

## Operational Limits & Non-Goals
GitDataQuality measures quantitative statistical distribution properties; it cannot evaluate whether human domain opinions expressed in text columns are subjectively accurate.
