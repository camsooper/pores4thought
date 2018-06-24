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
   name = "hello_world_python_deps",
   requirements = "//pores4thought/hello_world/python:requirements.txt",
)

load("@hello_world_python_deps//:requirements.bzl", "pip_install")
pip_install()
