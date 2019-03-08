from conans import ConanFile, CMake
class Pkg(ConanFile):
    name = "TestC"
    version = "1.0.1"
    settings = "os", "compiler", "arch", "build_type"
    requires = "plibsys/0.0.4@saprykin/stable --build missing"
    generators = "cmake"
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*.h", src="src", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["helloC"]
