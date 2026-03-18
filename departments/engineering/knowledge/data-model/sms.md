---
title: "Data Model: SMS"
summary: "Schema reference for the sms database -- SMS session state, inbound/outbound message history, and threaded conversations"
topics: [data-model, sms, messaging, sessions, twilio]
systems: [Harmony, Cloud SQL, PostgreSQL, Twilio]
people: []
content_type: reference
departments: [engineering]
roles: [all]
classification: internal
last_verified: "2026-03-18"
review_cycle_days: 90
---

# Data Model: sms

**Database:** sms
**Migrations:** 5
**Tables:** 3

The sms database manages SMS session state and message history.

---

## Tables

### sms_session
| Column | Type | Notes |
|--------|------|-------|
| id | bytea (XID) | |
| harmony_number | varchar | Harmony's SMS number |
| member_number | varchar | Member's phone |
| an_level | varchar | Account number level |
| member_id | bytea FK -> sponsor.member | Cross-DB logical reference |
| inherited_session_id | bytea FK -> sms_session | Session inheritance (threading) |
| thread_type / thread_state | varchar | Conversation management |
| expires_at | timestamp | Session expiration |

### sms_inbound
| Column | Type | Notes |
|--------|------|-------|
| session_id | bytea FK -> sms_session | |
| sms_identifier | varchar | External message ID |
| message_text | text | |
| received_at | timestamp | |

### sms_outbound
| Column | Type | Notes |
|--------|------|-------|
| session_id | bytea FK -> sms_session | |
| sms_identifier | varchar | External message ID |
| message_text | text | |
| sent_at | timestamp | |

---

## Key Patterns

1. **Session inheritance** -- Sessions can inherit from previous sessions for threaded conversations
2. **Directional tables** -- Separate inbound/outbound for clarity
3. **Soft expiration** -- expires_at without deletion
4. **Cross-DB reference** -- member_id references sponsor.member (logical FK, not enforced)
