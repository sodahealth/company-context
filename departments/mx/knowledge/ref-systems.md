---
title: "MX Systems and Access"
summary: "Systems, tools, and access groups used by the Member Experience and Merchants & Payments teams"
topics: [access, systems, tools, mx, payments, member-experience]
systems: [FIS, Galileo, Brex, SharePoint, Auth0]
people: [Jared Dauman, John Michael King, Julie Fleischer, Nidhi Nayyar]
content_type: "reference"
departments: [mx]
roles: [all]
classification: "internal"
last_verified: "2026-04-10"
review_cycle_days: 90
authorship: "agent-autonomous"
---

# MX Systems and Access

This document describes the systems, tools, and access groups used by the Member Experience and Merchants & Payments teams.

## Team Members

### Merchants & Payments

| Name | Title | Reports To |
|------|-------|-----------|
| Jared Dauman | CPO / Head of Operations | Robby Knight (CEO) |
| John Michael King | Sr. Director, Merchants & Payments | Jared Dauman |
| Gary Stein | Senior Manager | John Michael King |
| Jay Verkay | Associate Director | John Michael King |
| Matthew Mague | Sr. Manager | John Michael King |
| Samyuktha Balaji | Manager | John Michael King |
| Shang Wang | Associate Director | John Michael King |
| Kylie Cashin | Analyst | Shang Wang |

### Member Experience

| Name | Title | Reports To |
|------|-------|-----------|
| Julie Fleischer | CXO | Casey Bartolucci (CCO) |
| Nidhi Nayyar | Senior Manager, Member Experience | Ariane Grazian |
| Ann Grafelman | Visual Designer | Nidhi Nayyar |
| Jill Blacketer | Contract Designer | Sarah Rumfelt |

## Standard Access (All MX Members)

All MX team members are assigned the `department-mx` Entra group.

## Key Systems — Merchants & Payments

### FIS (Payment Processing)

- **What it does**: Core payment processing platform. Handles transaction authorization, clearing, and settlement for Evermore's prepaid Mastercard benefit cards.
- **Who uses it**: M&P team (primarily John Michael King's org)
- **Integration**: Engineering squad Banana Dance builds and maintains the FIS integration code

### Galileo (Card Operations)

- **What it does**: Card issuing and management platform. Handles card activation, balance inquiries, card status management, and account operations.
- **Who uses it**: M&P team
- **Integration**: Engineering squad Banana Dance maintains the Galileo integration
- **Note**: Jared reviews Galileo account data as part of financial/contract management

### Settlement and Reconciliation Systems

- **What it does**: Processes for reconciling transactions between FIS, Galileo, merchants, and Evermore's funding accounts. Includes SIF (Standard Interchange Format) accuracy tracking and item-level restriction enforcement.
- **Who uses it**: M&P team -- Gary Stein, Jay Verkay, Matthew Mague, Shang Wang, Kylie Cashin
- **Key data**: Weekly Transaction & SIF Accuracy Report (reviewed on Confluence)

### Brex (Corporate Card / Expenses)

- **What it does**: Corporate card and expense management platform. Jared Dauman's most-used application (42 sign-ins in 90d, 33 active days).
- **Who uses it**: Jared Dauman (heavy usage), other team members for expense reporting
- **Note**: Brex as the #1 app for the CPO signals heavy financial operations activity

### Auth0 (Evermore API — Production)

- **What it does**: Authentication for the Evermore API. M&P team accesses production environments for payment operations.
- **Who uses it**: Jared Dauman (weekly), M&P team members as needed

## Key Systems — Member Experience

### &more Brand Assets and Design Tools

- **What it does**: The &more brand is Evermore's member-facing identity. MX manages brand guidelines, visual assets, and design templates for card carriers, catalogs, in-store signage, and digital content.
- **Who uses it**: Julie Fleischer, Nidhi Nayyar, Ann Grafelman, Jill Blacketer
- **Tools**: Figma (design review), Adobe Creative Suite (design production)

### Materials Production (Aproove, ABCorp)

- **What it does**: Production pipeline for printed member materials -- card carriers, welcome kits, benefit catalogs. Aproove manages the approval workflow; ABCorp handles print fulfillment.
- **Who uses it**: Nidhi Nayyar (primary), coordinated with Sarah Rumfelt (Office of CEO)

## Shared Systems

### SharePoint

- **What it does**: Document management and collaboration. Heavy usage across both sub-functions for SOW documents, RFP materials, merchant catalogs, financial models, and operational documents.
- **Who uses it**: Entire MX department -- Jared Dauman is a heavy user (72 combined sign-ins in 90d across SharePoint Online and Web Client)

### Confluence

- **What it does**: Internal knowledge base. Jared Dauman is the company's most prolific Confluence user (2,661 pages all-time, 252 contributed in 90d). Used for EBT go-live coordination, transaction reports, company policies, and operational documentation.
- **Who uses it**: Entire MX department, with Jared as the primary contributor

### Smartsheet

- **What it does**: Project management and tracking. Jared's PM tool of choice (20 combined sign-ins in 90d).
- **Who uses it**: Jared Dauman (primary), M&P team for project tracking

## Cross-Department Collaboration

| Department | Collaboration Area |
|-----------|-------------------|
| Product Engineering (Banana Dance squad) | FIS and Galileo integration code, payment technology |
| Product (Shilpa Mohanty) | Payments product roadmap, reimbursement, braided funding |
| Product (Courtney Louie, Peter Barkey-Bircann) | Member experience features -- OX portal, IVR, SMS |
| HPS (Ariane Grazian's team) | Sponsor implementations requiring payment setup and member materials |
| New Markets (Sarah Hagan) | EBT/SNAP expansion -- M&P owns the payments platform side |
| Growth (Alex Kochanik) | Retailer partnerships, in-store media, CPG brand deals |
| Finance (Zach Newcomb) | Settlement reconciliation, invoicing, material cost tracking |
| Office of CEO (Sarah Rumfelt) | Materials production coordination, Aproove projects |
