#ifndef USTR_H
#define USTR_H 1

#ifndef USTR_DEBUG
#define USTR_DEBUG 0
#endif

#if USTR_DEBUG
# include "ustr-conf-debug.h"
#else
# include "ustr-conf.h"
#endif

#include "ustr-main.h"
#include "ustr-b.h"
#include "ustr-cmp.h"
#include "ustr-fmt.h"
#include "ustr-io.h"
#include "ustr-ins.h"
#include "ustr-parse.h"
#include "ustr-pool.h"
#include "ustr-set.h"
#include "ustr-srch.h"
#include "ustr-utf8.h"
#include "ustr-spn.h"
#include "ustr-sub.h"
#include "ustr-replace.h"
#include "ustr-split.h"
#include "ustr-sc.h"

#endif
