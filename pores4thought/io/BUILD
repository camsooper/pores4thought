load("@python_deps//:requirements.bzl", "requirement")

py_test(
    name = "read_image_test",
    srcs = ["read_image_test.py"],
    main = "read_image_test.py",
    deps = [
        requirement("numpy"),
        requirement("pillow"),
    ],
    data = [
        "@s3_test_files//:test_images"
    ],
    size = "small",
)