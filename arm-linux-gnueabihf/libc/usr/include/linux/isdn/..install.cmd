cmd_/home/arcelik/kernel-headers/include/linux/isdn/.install := /bin/bash scripts/headers_install.sh /home/arcelik/kernel-headers/include/linux/isdn /home/arcelik/1511/linux_kernel/sober-kernel/include/uapi/linux/isdn capicmd.h; /bin/bash scripts/headers_install.sh /home/arcelik/kernel-headers/include/linux/isdn /home/arcelik/1511/linux_kernel/sober-kernel/include/linux/isdn ; /bin/bash scripts/headers_install.sh /home/arcelik/kernel-headers/include/linux/isdn /home/arcelik/1511/linux_kernel/sober-kernel/include/generated/uapi/linux/isdn ; for F in ; do echo "\#include <asm-generic/$$F>" > /home/arcelik/kernel-headers/include/linux/isdn/$$F; done; touch /home/arcelik/kernel-headers/include/linux/isdn/.install