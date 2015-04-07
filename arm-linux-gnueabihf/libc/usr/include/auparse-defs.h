/* auparse-defs.h --
 * Copyright 2006-07 Red Hat Inc., Durham, North Carolina.
 * All Rights Reserved.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Authors:
 *      Steve Grubb <sgrubb@redhat.com>
 */

#ifndef AUPARSE_DEFS_HEADER
#define AUPARSE_DEFS_HEADER

#include <time.h>

#ifdef __cplusplus
extern "C" {
#endif


/* Library type definitions */

/* This tells the library where the data source is located */
typedef enum { AUSOURCE_LOGS, AUSOURCE_FILE, AUSOURCE_FILE_ARRAY, 
	AUSOURCE_BUFFER, AUSOURCE_BUFFER_ARRAY,
	AUSOURCE_DESCRIPTOR, AUSOURCE_FILE_POINTER, AUSOURCE_FEED } ausource_t;

/* This used to define the types of searches that can be done.  It is not used
   any more. */
typedef enum {
	AUSEARCH_UNSET,
	AUSEARCH_EXISTS,
	AUSEARCH_EQUAL, AUSEARCH_NOT_EQUAL,
	AUSEARCH_TIME_LT, AUSEARCH_TIME_LE, AUSEARCH_TIME_GE, AUSEARCH_TIME_GT,
	AUSEARCH_TIME_EQ,
	AUSEARCH_INTERPRETED = 0x40000000
} ausearch_op_t;

/* This determines where to position the cursor when a search completes */
typedef enum { AUSEARCH_STOP_EVENT, AUSEARCH_STOP_RECORD,
	AUSEARCH_STOP_FIELD } austop_t;

/* This defines how search rule pieces are treated to decide when
 * to stop a search */
typedef enum { AUSEARCH_RULE_CLEAR, AUSEARCH_RULE_OR,
        AUSEARCH_RULE_AND, AUSEARCH_RULE_REGEX } ausearch_rule_t;


typedef struct
{
        time_t sec;             // Event seconds
        unsigned int milli;     // millisecond of the timestamp
        unsigned long serial;   // Serial number of the event
	const char *host;	// Machine's name
} au_event_t;


/* This indicates why the user supplied callback was invoked */
typedef enum {AUPARSE_CB_EVENT_READY} auparse_cb_event_t;

/* This determines the type of field at current cursor location */
enum {  AUPARSE_TYPE_UNCLASSIFIED,  AUPARSE_TYPE_UID, AUPARSE_TYPE_GID,
	AUPARSE_TYPE_SYSCALL, AUPARSE_TYPE_ARCH, AUPARSE_TYPE_EXIT,
	AUPARSE_TYPE_ESCAPED, AUPARSE_TYPE_PERM, AUPARSE_TYPE_MODE,
	AUPARSE_TYPE_SOCKADDR, AUPARSE_TYPE_FLAGS, AUPARSE_TYPE_PROMISC,
	AUPARSE_TYPE_CAPABILITY, AUPARSE_TYPE_SUCCESS, AUPARSE_TYPE_A0,
	AUPARSE_TYPE_A1, AUPARSE_TYPE_A2, AUPARSE_TYPE_SIGNAL, 
	AUPARSE_TYPE_LIST, AUPARSE_TYPE_TTY_DATA } auparse_type_t;

#ifdef __cplusplus
}
#endif
 
#endif

