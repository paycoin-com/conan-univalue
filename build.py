import sys
import os

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(channel="testing")
    #
    # if sys.platform == "linux":
    #     # cross-compile windows from linux... easier
    #     builder.add(settings={"os":"Windows", "arch": "x86_64", "build_type": "Debug"},
    #                 options={}, env_vars={}, build_requires={})
    #
    #     builder.add(settings={"os":"Windows", "arch": "x86_64", "build_type": "Release"},
    #                 options={}, env_vars={}, build_requires={})
    #
    #     builder.add(settings={"os":"Windows", "arch": "x86", "build_type": "Debug"},
    #                 options={}, env_vars={}, build_requires={})
    #
    #     builder.add(settings={"os":"Windows", "arch": "x86", "build_type": "Release"},
    #                 options={}, env_vars={}, build_requires={})
    #
    # # debug/release 54 bit build
    # builder.add(settings={"arch": "x86_64", "build_type": "Debug"},
    #             options={}, env_vars={}, build_requires={})

    builder.add(settings={"os":"Android", "os.api_level": 21, "arch": "armv7", "build_type": "Release",
                          "compiler": "clang", "compiler.version" : "9", "compiler.libcxx": "libc++",},
                options={}, env_vars={}, build_requires={"*": ["android_ndk_installer/r21d@bincrafters/stable"]})

    builder.add(settings={"os":"Android", "os.api_level": 24, "arch": "armv7", "build_type": "Release",
                          "compiler": "clang", "compiler.version" : "9", "compiler.libcxx": "libc++",},
                options={}, env_vars={}, build_requires={"*": ["android_ndk_installer/r21d@bincrafters/stable"]})

    # builder.add(settings={"os":"Android", "os.api_level": 24, "arch": "armv7", "build_type": "Release"},
    #             options={}, env_vars={}, build_requires={})

    # builder.add(settings={"arch": "x86_64", "build_type": "Release"},
    #             options={}, env_vars={}, build_requires={})
    #
    # builder.add(settings={"arch": "armv7", "build_type": "Release"},
    #             options={}, env_vars={}, build_requires={})

    builder.run()
