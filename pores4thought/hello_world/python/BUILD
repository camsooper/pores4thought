load("@hello_world_python_deps//:requirements.bzl", "requirement")

py_test(
    name = "test",
    srcs = ["test.py"],
    main = "test.py",
    deps = [
        requirement("numpy"),
        requirement("ImageHash"),
        requirement("click"),
        requirement("protobuf"),
    ],
    size = "small",
)
