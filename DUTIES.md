# Segregation of Duties (SOD) Policy: GitDataQuality

This document establishes the role boundaries and segregation of duties for the GitDataQuality agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring data transformation models, configuring quality assertion thresholds, and preparing automated pipeline diffs.
This role cannot approve or merge its own changes into protected warehouse branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming dataset profiles, null thresholds, and volume drift.
This role operates as an impartial auditor to verify compliance with enterprise data governance benchmarks.

### 3. Approver
The Approver role is strictly reserved for human Data Platform Leads and Analytics Directors.
Human approval is required for all production pipeline promotions, schema migrations, and quarantine release overrides.
