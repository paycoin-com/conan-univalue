from conans import ConanFile, CMake, tools


class UnivalueConan(ConanFile):
    name = "univalue"
    version = "1.0.6"
    license = "MIT"
    channel = "testing"
    author = "Paycoin <hello@paycoin.com>"
    url = "https://github.com/paycoin-com/univalue.git"
    description = "High performance RAII C++ JSON library and universal value object class"
    topics = ("bitcoin", "json")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    build_policy = "missing"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/paycoin-com/univalue.git", "master")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*", dst="include", src="univalue/include")
        self.copy("*.h", dst="include", src="univalue")
        self.copy("*univalue.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["univalue"]
