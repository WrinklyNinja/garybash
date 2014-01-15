garybash
========

An alternative port of the "Wrye Bash" for Fallout 3/NewVegas.

---

This branch holds all the files that are unique to Wrye Flash / Flash NV and that must be added to Bash as part of work to add support for FO3 and FNV to Bash. The directory structure used mimics that of the latest Bash `master` source, though the diff used to determine the changes used Bash commit 5d6ceae9b846aabb31b8ea4c51ce61ebac4a8f7f for comparison against the `master-newvegas-merge` branch. 

Where the latest Bash source is referenced, this refers to commit 9c20f9184f0b802051d5f60a9b65e7f25aa8661a at https://github.com/Utumno/wrye_bash_refactoring.git.

## Modified Files

Files that have been modified by Flash are present as diffs at this stage. These diffs will be edited to remove unnecessary changes. The changes to the files they reference in the Bash source since commit 5d6ceae9b846aabb31b8ea4c51ce61ebac4a8f7f will be traced, and the changes in the diffs then applied as appropriate to the latest Bash source.

## New Files

Files in this branch that are not diffs are not present in the Bash source at commit 5d6ceae9b846aabb31b8ea4c51ce61ebac4a8f7f, and are also not present in the latest Bash source.

The Bashed Lists documentation at `Mopy\Docs\Bashed Lists.md` needs to be integrated into the Bash docs, and is not intended to be kept in its current form.

The file at `Mopy\bash\game\fallout.py` needs to have its contents added to the currently-missing `fallout3.py` and `falloutnv.py` files.

## Missing files

The following files that are present in Flash but are not in this branch as either files or diffs yet. Once editing of them has finished, they will be added.

* `Mopy\bash\game\fallout3.py`
* `Mopy\bash\game\falloutnv.py`
* `Mopy\bash\basher.py`
* `Mopy\bash\bosh.py`
