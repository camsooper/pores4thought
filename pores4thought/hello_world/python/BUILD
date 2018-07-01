load("@python_deps//:requirements.bzl", "requirement")

py_test(
    name = "hello_world",
    srcs = ["hello_world.py"],
    main = "hello_world.py",
    deps = [
        requirement("numpy"),
    ],
    size = "small",
)