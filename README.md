This toolchain is extended version of Linaro Toolchain 2014.09.
Please see README.toolchain for further information.
###############################################################

# arm-linux-gnueabihf

- This package can be installed in any location.  Consider using the
included `bin/arm-linux-gnueabihf-pkg-config` to make finding libraries 
and dependencies easier.

- The system root contains the basic header files and libraries to link
your programs against.

- The sysroot is `arm-linux-gnueabihf/libc`.

- gcc version: 4.9.2,
- glibc version: 2.19,
- binutils version: 2.24,
- gdb version: 7.6.1
- binutils version: 2.24,
 
# extensions

 Package | Dependencies
--- | --- | ---
readline6-dev | dpkg, readline6, tinfo-dev
dpkg | bz2-1.0, lzma5, selinux1, tar, zlibg1g
readline6 | readline-common, tinfo5
tinfo-dev | tinfo5
tinfo5 | -
readline-common | dpkg
bz2-1.0 | -
lzma5 | -
selinux1 | -
tar | -
zlibg1g | -


