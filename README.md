garybash
========

An alternative port of the "Wrye Bash" for Fallout 3/NewVegas.

---

This branch holds all the files that are unique to Wrye Flash / Flash NV and that must be added to Bash as part of work to add support for FO3 and FNV to Bash. The directory structure used mimics that of the latest Bash `master` source, though the diff used to determine the changes used Bash commit 5d6ceae9b846aabb31b8ea4c51ce61ebac4a8f7f for comparison against the `master-newvegas-merge` branch. 

## Modified Files

Files that have been modified by Flash are present as diffs at this stage. Currently the following file diffs are missing while their files are still being edited.

* `Mopy\bash\basher.py`
* `Mopy\bash\bosh.py`

None of the modified files have yet been processed to remove any unnecessary modifications.

## WIP New Files

Apart from these files, the content of this branch is ready for integration into the Bash repository.

* `Mopy\Docs\Bashed Lists.html`
* `Mopy\Docs\Bashed Lists.txt`
* `Mopy\Docs\Wrye Flash (FNV).txt`
* `Mopy\Docs\Wrye Flash (FO3).txt`
* `Mopy\bash\l10n\Japanese (FNV-specific).txt`
* `Mopy\bash\l10n\Japanese.txt`

The docs need to have any relevant info extracted and rewritten for inclusion into the Bash docs, and the Japanese translation files need to be combined and turned into gettext translation files.

## Missing files

The following files that are present in Flash but are not in this branch as either files or diffs yet. Once editing of them has finished, they will be added.

* `Mopy\bash\game\fallout3.py`
* `Mopy\bash\game\falloutnv.py`
