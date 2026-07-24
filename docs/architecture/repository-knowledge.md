# Repository Knowledge

## Purpose

Repository Knowledge is DocuMind's reusable semantic understanding of a Repository Snapshot. It separates repository facts and relationships from the presentation or analysis purpose that consumes them.

## Responsibilities

Repository Knowledge represents discovered repository elements, meaningful classifications, directed relationships, provenance, completeness limits, and links from material claims to supporting Evidence. It provides a factual substrate that multiple analyzers can reuse, including future README generation.

## Boundaries

Repository Knowledge is not a copy of repository files, a generated document, or a recommendation. It does not prescribe changes or rank issues; those are interpretive concerns expressed as Findings.

Knowledge may be incomplete because its snapshot is incomplete or a fact cannot be established. The model must preserve that limit rather than turning absence of support into an unsupported negative claim.

## Relationships

Each Knowledge Item has provenance to its Repository Snapshot. Knowledge Items may be connected by explicit Relationships and supported by one or more Evidence records. Findings reference Knowledge Items for a stated purpose; one Knowledge Item can support several Findings.

The model remains provider-agnostic. Relationships are first-class information, and claims are traceable to evidence within the snapshot.
