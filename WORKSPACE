git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "8b5d0683a7d878b28fffe464779c8a53659fc645",
)

new_git_repository(
    name = "googletest",
    build_file = "third_party/gtest.BUILD",
    remote = "https://github.com/google/googletest",
    tag = "release-1.8.0",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories")

pip_repositories()

load("@io_bazel_rules_python//python:pip.bzl", "pip_import")
pip_import(
   name = "python_deps",
   requirements = "//third_party:requirements.txt",
)

load("@python_deps//:requirements.bzl", "pip_install")
pip_install()

new_http_archive(
    name = "s3_test_files",
    url = "https://s3.amazonaws.com/pores4thought/test_data.zip",
    build_file_content =
"""
filegroup(
  name = "test_images",
  srcs = ["ThreePhase_dseg.tif", "ThreePhase.tif"],
  visibility = ["//visibility:public"],
)
""",
    type = "zip"
)
