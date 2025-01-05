cmake_minimum_required(VERSION "3.22")

project(sample_project LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS ON)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR}/build/Release/generators)

find_package(simple_cpp_project REQUIRED)

add_executable(sample_app 
    src/main.cpp
    )

# This is necessary to find the header files and libraries installed by the package
target_include_directories(sample_app
    PRIVATE
        ${simple_cpp_project_INCLUDE_DIRS}
    )

target_link_directories(sample_app
    PRIVATE
        ${simple_cpp_project_INCLUDE_DIRS}/../lib
    )

target_compile_features(sample_app 
    PRIVATE
        cxx_std_17
    )
set_target_properties(sample_app 
    PROPERTIES
        CXX_EXTENSIONS OFF
        CMAKE_CXX_STANDARD_REQUIRED ON
    )
target_link_libraries(sample_app 
    PRIVATE
        logger
    )
