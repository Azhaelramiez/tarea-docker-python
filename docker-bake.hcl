group "default" {
  targets = ["validate"]
}

target "validate" {
  dockerfile = "Dockerfile"
  context = "."
}