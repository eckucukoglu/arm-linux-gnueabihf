cmd_/home/arcelik/kernel-headers/include/linux/byteorder/.install := /bin/bash scripts/headers_install.sh /home/arcelik/kernel-headers/include/linux/byteorder /home/arcelik/1511/linux_kernel/sober-kernel/include/uapi/linux/byteorder big_endian.h little_endian.h; /bin/bash scripts/headers_install.sh /home/arcelik/kernel-headers/include/linux/byteorder /home/arcelik/1511/linux_kernel/sober-kernel/include/linux/byteorder ; /bin/bash scripts/headers_install.sh /home/arcelik/kernel-headers/include/linux/byteorder /home/arcelik/1511/linux_kernel/sober-kernel/include/generated/uapi/linux/byteorder ; for F in ; do echo "\#include <asm-generic/$$F>" > /home/arcelik/kernel-headers/include/linux/byteorder/$$F; done; touch /home/arcelik/kernel-headers/include/linux/byteorder/.install
