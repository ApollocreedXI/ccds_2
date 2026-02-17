# ccds_2 documentation!

## Description

This is a major assignment deliverable with the purpose to provide training on cloud service storage access, data science project templating, and version controlling.

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://ccds-project/data/`.
* `make sync_data_down` will use `aws s3 sync` to recursively sync files from `s3://ccds-project/data/` to `data/`.


