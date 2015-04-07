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
- binutils version: 2.24.
 
# Extensions

 Package | Dependencies
--- | ---
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

 Package | Dependencies
--- | ---
ssl-dev | ssl1.0.0, zlib1g-dev
ssl1.0.0 | debconf, zlib1g
zlib1g-dev | zlib1g
debconf | perl-base
perl-base | dpkg

 Package | Dependencies
--- | ---
pcre3-dev | pcre3, pcrecpp0
pcre3 | -
pcrecpp0 | pcre3, stdc++6
stdc++6 | -

 Package | Dependencies
--- | ---
ustr-dev | ustr-1.0-1
ustr-1.0-1 | -

 Package | Dependencies
--- | ---
audit-dev | audit0
audit0 | -

 Package | Dependencies
--- | ---
bz2-dev | bz2-1.0
bz2-1.0 | *

 Package | Dependencies
--- | ---
flex | debconf, dpkg, m4
debconf | *
dpkg | *
m4 | -
