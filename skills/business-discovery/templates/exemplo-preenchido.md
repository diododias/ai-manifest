# Requirements — Waiting list for full month

> Completed example (fictitious demand) to serve as a reference ("north star")
> to the output format. It's not a real backlog feature.

- **Epic:** Capacity · **Status:** 🟡 under discovery
- **Updated:** 2026-06-13 · **Agendas:** [2026-06-13]
- **Participants:** Luiz, PM

## Context & objective
Today, when the month's capacity runs out, the customer doesn't buy and disappears without leaving
trail. Objective: capture interest (waitlist) and notify when a vacancy opens
(cancellation or reconciliation). Successful target on SC-1.

## Glossary / domain
- **SaleMonth** *(exists)* — month of sale, capacity in minutes.
- **Vacancy** — minutes released due to cancellation or reconciliation (RN-30).
- **WaitlistEntry** *(new)* — (customer_email, variant_id, sale_month_id).
  Uniqueness: the triple is unique (RN-W2).

## User stories & scenarios
- **US-1** *(Priority: P1)* As a customer, with the month running out, I want to enter the
  list with email address to be notified when a vacancy opens.
  - *Independent test:* open an exhausted month, sign up for an email, see the persisted entry.
  - **Scenarios:**
    1. **Given** a month with 20 min free and the Elaborated variant (180 min),
       **When** the customer opens the variant page, **Then** they see the button
       "Join list" instead of "Buy".
    2. **Given** a customer already subscribed to (email, variant, month), **When** he
       register again, **Then** the system does not create a 2nd line and responds as success.
    3. *(exception)* **Given** an email in an invalid format, **When** the customer
       sends, **Then** the registration is rejected with a validation message.

- **US-2** *(Priority: P2)* As a subscriber, I want to receive an email with a link to
  checkout when a compatible vacancy opens.
  - **Scenarios:**
    1. **Given** a queue with 3 registered in a variant, **When** a vacancy opens with
       minutes ≥ work_minutes, **So** only the 1st in line (FIFO) receives an email with a link.
    2. **Given** that the 1st in line received the email, **When** the confirmation window passes
       reservation ⟨X h — DA-1⟩ without checkout, **Then** the place moves to the next in line.
    3. *(exception)* **Given** open space and empty queue, **When** the system
       processes, **Then** nothing is sent and the spot remains available for normal purchase.

- **US-3** *(Priority: P3)* As an artisan (admin), I want to see the list by month to
  size future capacity.
  - **Scenarios:**
    1. **Given** a month with subscribers, **When** the admin opens the month panel,
       **Then** see the list (email, variant, date) in order of registration.

## Business rules
- **RN-W1** *(state)* **While** `available_minutes < work_minutes` for
  variant, the system should display "Join list" instead of "Buy".
  *Ex: month with 20 minutes free, Elaborado asks for 180 → shows waitlist.*
  *(checks: US-1 scenario 1)*
- **RN-W2** *(unwanted)* **If** there is already a registration in (email, variant, month),
  **then** the system should not create a 2nd entry and should respond as success.
  *Ex: 2nd send the same → 1 line, successful response.* *(checks: US-1 scenario 2)*
- **RN-W3** *(event)* **When** `minutos_liberados ≥ work_minutes`, the system
  must notify the 1st registrant in line in FIFO order. *Ex: queue [A,B,C] → email
  only for A.* *(checks: US-2 scenario 1)*
- **RN-W4** *(event)* **When** reservation window ⟨X h — DA-1⟩ expires without
  checkout, the system must release the space to the next person in line. *(checks: US-2 scenario 2)*
- **RN-W5** *(event)* **When** the sales month ends, the system must expire
  registrations open ⟨or roll over to next month? —DA-2⟩.

## Flows
**Happy:** month runs out → customer joins the list → admin cancels an order →
system detects vacancy → FIFO email → customer closes checkout in the window.
**Exceptions / edge cases:** vacancy opens and queue is empty; registered already bought another
variant; invalid/bounce email; two simultaneous cancellations freeing up space
for the same 1st in line (competition — confirm treatment).

## Success criteria (measurable)
- **SC-1** ⟨30%?⟩ of those registered for a vacancy convert to checkout within the window
  reservation. *(target to be confirmed — DA-4)*
- **SC-2** Reset the months exhausted without capturing interest (today 100% disappears without a trace).

## Out of scope
Advance billing · priority paid · in-app push.

## Open questions
- **DA-1** Email booking window = how many hours? *(owner: PM · next agenda)*
- **DA-2** Registration expires at the end of the month or rolls over to the next one? *(owner: PM)*
- **DA-3** Notifies by exact variant or any that fits in the minutes? *(owner: PM/Tech)*
- **DA-4** Conversion target (SC-1) = how much? *(owner: PM)*

## ⚠️ Gaps detected in transcription
- "the way we did it on the reservation" → what TTL? I took over 30 min
  (current ReservationGroup) — **confirm**.
- "send the same email as the confirmation email" → template not defined here;
  Reference Milestone 1D's transactional email deliverable.
- US-2 scenario 2 without "So" closed for those who missed the window: return to the end of the
  queue or leave? — **confirm** (becomes DA if persists).
- SC-1 without number (conversion target) → DA-4.

## Changelog by schedule
- **2026-06-13** — creation. New: US-1..3 (with Given/When/Then scenarios),
  RN-W1..W5 (structured), SC-1..2, WaitlistEntry glossary. Pending issues: DA-1..4.
  Assumption to be confirmed: vacancy TTL = 30 min.
