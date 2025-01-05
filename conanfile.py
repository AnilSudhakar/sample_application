import os

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.files import copy

class SimpleCPPConan(ConanFile):
    name = "sample_project"
    version = "0.0.1"
    description = "A sample project to test simple_cpp_project"
    url = "https://github.com/AnilSudhakar/simple_cpp_project.git"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"
    default_options = {"gtest/*:shared": False}

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("simple_cpp_project/1.0.0@official/release")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

