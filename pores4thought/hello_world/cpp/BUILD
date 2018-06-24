load("//tools:toolchain.bzl", "if_linux")

package(default_visibility = ["//visibility:public"])

cc_test(
    name = "test",
    size = "small",
    srcs = glob(["*.cc"]),
    linkopts = if_linux(["-lpthread"]),
)
