python_requirements(
    name = "prod-requirements",
    module_mapping = {
        "protobuf": [
            "google.protobuf",
            "google._upb",
        ],
        "setuptools": ["pkg_resources"],
    },
    resolve = "prod",
    source = "requirements_prod.txt",
)

python_requirements(
    name = "dev-requirements",
    module_mapping = {
        "protobuf": [
            "google.protobuf",
            "google._upb",
        ],
        "setuptools": ["pkg_resources"],
    },
    resolve = "dev",
    source = "requirements_dev.txt",
)