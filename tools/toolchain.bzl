def if_linux(if_true, if_false=None):
  if_false = if_false or []
  return select({
    "@//:is_x64_windows": if_false,
    "@//:is_x64_windows_msvc": if_false,
    "@//:is_darwin": if_false,
    "//conditions:default": if_true
  })

