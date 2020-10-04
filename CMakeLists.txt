cmake_minimum_required(VERSION 3.8)
enable_language(C)
enable_language(CXX)


include(ExternalProject)

ExternalProject_Add(
        univalue_ex
        PREFIX ${CMAKE_CURRENT_BINARY_DIR}
        GIT_REPOSITORY "https://github.com/paycoin-com/univalue.git"
        GIT_SHALLOW TRUE
        #CONFIGURE_COMMAND ./autogen.sh COMMAND ./configure --enable-module-ecdh --enable-experimental --prefix=${CMAKE_CURRENT_BINARY_DIR}
        BUILD_IN_SOURCE 1
        )

ExternalProject_Get_Property(univalue_ex install_dir)

add_library(univalue STATIC IMPORTED GLOBAL)

add_dependencies(univalue univalue_ex)

file(MAKE_DIRECTORY ${install_dir}/include)

set_target_properties(univalue PROPERTIES IMPORTED_LOCATION ${install_dir}/lib/${CMAKE_STATIC_LIBRARY_PREFIX}univalue${CMAKE_STATIC_LIBRARY_SUFFIX})

set_target_properties(univalue PROPERTIES INTERFACE_INCLUDE_DIRECTORIES ${install_dir}/include)

export(PACKAGE univalue)
