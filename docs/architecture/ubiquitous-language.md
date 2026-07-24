# Ubiquitous Language

This vocabulary is shared by product, engineering, and future analyzers.

## Terms

**Repository** is the versioned source collection being analyzed.

**Repository Snapshot** is the bounded, point-in-time representation of repository material admitted to one analysis. It is the source of record for all derived results.

**Source Artifact** is an item in a snapshot, including a file, directory, symbolic link, or repository metadata record.

**Source Location** is a precise address in a Source Artifact. It can identify the entire artifact or a stable portion of it.

**Repository Knowledge** is structured understanding derived from a Repository Snapshot. It describes facts and relationships, not generated prose or recommendations.

**Knowledge Item** is one addressable fact, classification, or relationship in Repository Knowledge.

**Relationship** is a directed, meaningful connection between Knowledge Items or Source Artifacts, such as containment, declaration, reference, dependency, or configuration.

**Finding** is an interpretable conclusion about Repository Knowledge for a stated analysis purpose.

**Evidence** is verifiable support for a Knowledge Item or Finding. It refers to one or more Source Locations in the Repository Snapshot.

**Analyzer** is a capability that derives Repository Knowledge, Findings, or both for a specific purpose. README generation is a future consumer, not a definition, of the model.

**Analysis Scope** is the declared snapshot boundary, including admitted material, exclusions, and the intended analysis purpose.

**Provenance** records where a model element originated and which snapshot it belongs to.

## Required Distinctions

- A Repository Snapshot is input material; Repository Knowledge is derived.
- A Knowledge Item states what is present or related; a Finding explains why that knowledge matters for a purpose.
- Evidence supports a claim; it is not the claim itself.
- The model must remain independent of AI providers and analysis techniques.
