cmd_/home/arcelik/kernel-headers/include/linux/usb/.install := /bin/bash scripts/headers_install.sh /home/arcelik/kernel-headers/include/linux/usb /home/arcelik/1511/linux_kernel/sober-kernel/include/uapi/linux/usb audio.h cdc-wdm.h cdc.h ch11.h ch9.h functionfs.h g_printer.h gadgetfs.h midi.h tmc.h video.h; /bin/bash scripts/headers_install.sh /home/arcelik/kernel-headers/include/linux/usb /home/arcelik/1511/linux_kernel/sober-kernel/include/linux/usb ; /bin/bash scripts/headers_install.sh /home/arcelik/kernel-headers/include/linux/usb /home/arcelik/1511/linux_kernel/sober-kernel/include/generated/uapi/linux/usb ; for F in ; do echo "\#include <asm-generic/$$F>" > /home/arcelik/kernel-headers/include/linux/usb/$$F; done; touch /home/arcelik/kernel-headers/include/linux/usb/.install
