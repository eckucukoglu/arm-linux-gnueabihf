#ifndef USTR_CONF_H
#define USTR_CONF_H 1

/* this is the custom version for the library itself, for everyone else
 * ustr-import generates one depending on the options. */

/* The default is now to link against libc. */
#ifndef USTR_CONF_INCLUDE_CODEONLY_HEADERS
#define USTR_CONF_INCLUDE_CODEONLY_HEADERS 0
#endif

/* We can't: if defined(__GLIBC__) && (!defined(_GNU_SOURCE) || !_GNU_SOURCE)
 *  because by the time we've included a libc header it's too late. */ 
#ifndef _GNU_SOURCE
#define _GNU_SOURCE 1
#endif

/* maybe move memmem / memrchr here? */

#if ! USTR_CONF_INCLUDE_CODEONLY_HEADERS
/* If you aren't just using the headers, these should match the .c's */

# define USTR_CONF_HAVE_64bit_SIZE_MAX     0
# define USTR_CONF_HAVE_RETARDED_VSNPRINTF 0
# define USTR_CONF_HAVE_STDINT_H 1
# define USTR_CONF_HAVE_DYNAMIC_CONF 1

# define USTR_CONF_USE_DYNAMIC_CONF  USTR_CONF_HAVE_DYNAMIC_CONF

# define USTR_CONF_REF_BYTES   1
# define USTR_CONF_EXACT_BYTES 0
# define USTR_CONF_USE_SIZE    0

# define USTR_CONF_USE_ASSERT   1
# define USTR_CONF_USE_EOS_MARK 1

#else
/* Same defaults, but can be altered at will. */
/* Note that you really shouldn't alter the _HAVE_* ones, but whatever */

# ifndef USTR_CONF_HAVE_64bit_SIZE_MAX
# define USTR_CONF_HAVE_64bit_SIZE_MAX     0
# endif
# ifndef USTR_CONF_HAVE_RETARDED_VSNPRINTF
# define USTR_CONF_HAVE_RETARDED_VSNPRINTF 0
# endif
# ifndef USTR_CONF_HAVE_STDINT_H
# define USTR_CONF_HAVE_STDINT_H 1
# endif
# ifndef USTR_CONF_HAVE_DYNAMIC_CONF
# define USTR_CONF_HAVE_DYNAMIC_CONF 1
# endif

/* no USE_DYNAMIC_CONF ... use default in ustr-main.h */

# ifndef USTR_CONF_REF_BYTES
# define USTR_CONF_REF_BYTES   1
# endif
# ifndef USTR_CONF_EXACT_BYTES
# define USTR_CONF_EXACT_BYTES 0
# endif
# ifndef USTR_CONF_USE_SIZE
# define USTR_CONF_USE_SIZE    0
# endif

# ifndef USTR_CONF_USE_ASSERT
# define USTR_CONF_USE_ASSERT   1
# endif
# ifndef USTR_CONF_USE_EOS_MARK
# define USTR_CONF_USE_EOS_MARK 1
# endif

#endif

#endif
