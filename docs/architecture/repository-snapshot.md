# Repository Snapshot

## Purpose

A Repository Snapshot establishes the stable boundary for one DocuMind analysis. It prevents derived results from silently mixing repository states.

## Responsibilities

A snapshot describes repository identity and revision when available, the Analysis Scope, admitted Source Artifacts, their repository-relative locations and relevant metadata, source content or durable content references, and collection limitations. Limitations include excluded material, unreadable artifacts, and unsupported artifact types.

A snapshot does not interpret source material, decide what is noteworthy, or create recommendations. Those responsibilities belong to Repository Knowledge and Findings.

## Boundary and Identity

The snapshot boundary must identify the repository state, selected paths, and collection policy that define what was observed. A changed revision, source content, or scope produces a different snapshot. Consumers must be able to distinguish material that is absent from material that was excluded, unreadable, or not collected.

## Relationship to Derived Results

Repository Knowledge is derived from one Repository Snapshot. Each Knowledge Item, Finding, and Evidence record retains provenance sufficient to identify that snapshot. Evidence only refers to Source Artifacts and Source Locations inside the declared snapshot.
