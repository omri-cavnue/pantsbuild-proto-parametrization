# Description
This repository contains a sample of protobuf parametrization failure with Pantsbuild

## Reproduce
1. First run: `pants export-codegen ::`
2. Next, run `pants export --resolve=prod` and activate the virtual environment
3. Now, run `pants test ::`. This should return a successful test run
4. To reproduce the failure, comment the first `protobuf_sources` target under `messages/proto/BUILD` and uncomment the second `protobuf_sources` such that the `protobuf_sources` target has a parametrized resolve field with both dev and prod set.
5. Now, run `pants test ::` and you should see an error similar to:
```
stderr:
definitions/third_party/bq/v1/bq_field.proto: File not found.
definitions/third_party/bq/v1/bq_table.proto: File not found.
definitions/messages/human/v1/person.proto: File not found.
definitions/messages/animal/v1/dog.proto:5:1: Import "definitions/third_party/bq/v1/bq_field.proto" was not found or had errors.
definitions/messages/animal/v1/dog.proto:6:1: Import "definitions/third_party/bq/v1/bq_table.proto" was not found or had errors.
definitions/messages/animal/v1/dog.proto:7:1: Import "definitions/messages/human/v1/person.proto" was not found or had errors.
definitions/messages/animal/v1/dog.proto:25:12: "human.v1.Person" is not defined.
```