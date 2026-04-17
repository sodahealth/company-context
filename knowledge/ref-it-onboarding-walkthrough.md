---
title: "IT Account Setup — Conversational Walkthrough"
summary: "Claude-facing instructions for guiding a new hire through IT account setup in /getstarted Mode 3. Replaces the live IT onboarding call."
topics: [onboarding, it-setup, security, devices]
systems: [entra-id, kandji, slack, onepassword, intune, chrome]
content_type: "reference"
departments: [all]
roles: [it]
classification: "internal"
last_verified: "2026-04-17"
review_cycle_days: 180
---

# IT Account Setup — Conversational Walkthrough

> **For Claude:** This document is your guide for walking a new hire through IT setup
> in `/getstarted` Mode 3. Follow the five phases below in order. Each phase has:
> what to say, what to watch for, how to handle problems, and when to move on.
>
> The experience should feel like a patient colleague sitting next to them — not a
> checklist. One thing at a time. Wait for confirmation before moving on. Be warm.
>
> Total time: about 20-30 minutes depending on pace.

---

## How to Begin

After the company introduction (Mode 3, Step 6), transition into setup:

> "Now that you've seen the platform and gotten oriented to the company — let's make
> sure everything on your laptop is ready to go. I'll walk you through it step by step.
> There's no rush. We'll go one thing at a time and I'll wait for you at each step."

Then proceed through the five phases below.

---

## Phase 1 — "Let's Confirm You're Signed In" (~8 min)

### 1a. Laptop Login

Ask:
> "First — did you log into your Mac already using the temporary credentials IT sent you?
> Your username is your `first.last` name matching your work email."

- **If yes:** Great, move to 1b.
- **If no / "I got a new Mac but haven't logged in yet":**
  > "No problem. Log in now using the temporary password IT sent to your Outlook before
  > your start date. Your username is `first.last` — for example, `carey.willson`.
  > Let me know once you're in."

- **If Outlook hasn't finished installing yet:**
  > "Outlook may still be installing in the background — that's normal and takes about
  > 10 minutes from first login. In the meantime, you can reach your email at
  > myapps.microsoft.com in any browser. Does your inbox look right?"

### 1b. Microsoft Authenticator

> "During your first login, your Mac should have prompted you to set up Microsoft
> Authenticator on your phone. This is how you'll approve sign-ins going forward —
> instead of a password, your phone taps to confirm it's you. Did you get through
> that step?"

- **If yes:** Good. "Is the Soda Health tile showing in your Authenticator app?"
  - Yes → ✅ move to 1c.
  - No → walk through setup below.
- **If no / skipped:**
  > "Let's do it now — it only takes two minutes, and without it you'll get locked out
  > of everything eventually."

  Walk them through:
  1. "Download Microsoft Authenticator from the App Store or Google Play on your phone."
  2. "Open it, tap 'Add account', then tap 'Work or school account'."
  3. "Enter your `@sodahealth.com` email and follow the prompts."
  4. "When it asks how to verify — choose 'Push notifications'. You'll get a tap-to-approve
     prompt instead of typing codes. Much easier."
  5. "Let me know when the Soda Health tile appears in the app."

- **If push notifications aren't working:**
  > "No worries — use the 6-digit code method for now. Open the app, tap the Soda Health
  > tile, and use the code it shows to approve sign-ins. We can revisit the push setup
  > after."

### 1c. macOS Quick Tips

> "One quick thing before we move on: if you're coming from Windows, macOS works
> slightly differently. The one shortcut you'll use constantly is Command+Shift+5 —
> that lets you take a screenshot or record your screen. Useful for showing IT an error."

Ask: "Are you pretty comfortable with Mac, or is this your first time?"
- If first time: mention the Apple Mac user guide exists online if they want it later.
- Either way: move on.

---

## Phase 2 — "Your Password Vault (Start Now, Finish Later)" (~5 min)

> "Next up: 1Password. This is Evermore's password manager — it keeps all your login
> credentials in one place so you only need to remember one master password. More
> importantly, it generates unique passwords for each site. Reusing passwords is the
> number-one way accounts get compromised."

**Important:** Start this now and then *park it* — a second email arrives 5-15 minutes
later. You'll come back to finish it in Phase 4.

> "Let's kick off the setup now, because there's a second email that takes a few minutes
> to arrive. While we wait, we'll keep going with other things."

Walk them through:

1. "Open Outlook and look for an invite from 1Password. If it's not in your inbox,
   check Spam or Junk."
   - **If missing:** "It may still be in transit. Let's come back in a few minutes.
     Keep an eye out for it while we do the next steps."

2. "Click the link in the email — it opens in your browser. Follow the setup steps."

3. **Secret Key — this is important:**
   > "At some point it will show you a PDF with your Secret Key. Save that PDF somewhere
   > safe — not just your desktop. Think of it like a backup key to your vault. If you
   > lose it, recovery is a pain. Where are you thinking of saving it?"
   
   (Wherever they say is fine. Just get them to save it before moving on.)

4. "You'll need a second email to finish — that usually arrives in 5-15 minutes.
   Let's keep going while we wait."

✅ **Park Phase 2 and move to Phase 3.**

---

## Phase 3 — "Browser, Apps, and Device" (~10 min)

*Run this while waiting for the 1Password second email.*

### 3a. Chrome Sign-In

> "Let's set up Chrome. Open it and sign in with your `@sodahealth.com` email — this
> creates a work Chrome profile that keeps your bookmarks and extensions separate from
> any personal browsing. It'll also sync across devices if you have Chrome elsewhere."

Walk them through:
1. Open Chrome → click the profile icon → "Sign in to Chrome" → enter work email
2. "Once you're signed in, set Chrome as your default browser: open System Settings,
   go to Desktop & Dock, and at the bottom you'll see 'Default web browser'. Switch it
   to Google Chrome."

Ask: "Are you signed into Chrome with your work account now?"

### 3b. Zoom Quick Settings

> "Quick one — open Zoom, go to Settings, then Video. Turn off 'Center Stage' — it
> auto-pans the camera and is distracting on calls. Then go to Background & Effects
> and turn on 'Blur my background'. That's the company standard for video calls."

Ask: "Got those turned off and on?"

### 3c. Kandji / Iru (Device Management)

> "You'll see an app on your Mac called Iru — that's our device management tool.
> It keeps your laptop secure and up to date automatically."

Key things to tell them:
- **Red dot = updates waiting.** "When you see a red dot on Iru, install the updates.
  Don't ignore them."
- **It will force updates eventually.** "If you skip updates too long, Iru will install
  them automatically — it won't wait for a convenient moment. Better to do it on
  your own terms."
- **App library.** "Iru also has a library of IT-approved apps you can install yourself.
  If you need something, check there first."
- **Admin requests.** "Occasionally an app update will pop up asking for admin
  permission. Before you click Allow, make sure it's something you recognize."

Ask: "Can you see Iru on your desktop or in your Applications folder?"
- If not visible: "It may still be installing — Kandji runs in the background after
  first login. It should appear within about 15 minutes. Keep an eye out for it."

### 3d. SSO Portal and App Access

> "Evermore uses Single Sign-On — SSO — which means you sign in once and it unlocks
> all your apps. The way most people think of it: you use your Evermore email to log
> into everything, instead of making separate usernames and passwords."

> "Your home base is myapps.microsoft.com — open that in Chrome and log in with
> your work email. Every app we use shows up there as a tile."

Walk them through checking access:
1. "Click the Atlassian tile. That's Confluence (our wiki) and Jira (project tracking).
   Does it let you in?"
   - Yes → ✅
   - No → "That one might be provisioning — it can take a few hours from your start date.
     I'll note it as something to check on."

2. "You should already have Outlook and Teams working from your laptop setup. Those are fine."

3. "Click Smartsheet — that's our project management tool. Does it open?"
   - Yes → ✅
   - No → Note for follow-up.

> "If anything is missing, let me know at the end and I'll flag it for IT."

---

## Phase 4 — "Finish 1Password + Slack" (~8 min)

### 4a. Complete 1Password

> "Let's check if that second 1Password email came through."

- **If yes:** 
  > "Great — use that email along with your username, your Secret Key from the PDF,
  > and the password you just set to finish signing in. Let me know when you're into
  > your vault."

  Then:
  1. "Now let's get the desktop app. Press Command+Space to open Spotlight, type
     '1Password', and open it."
  2. "Sign in with your username, Secret Key, and password."
  3. "It'll ask you to set up an authenticator for 1Password itself — follow those
     prompts on your phone. This is a second layer of security just for your vault."
  4. "Once you're in, you'll see an Employee vault — that's where company-shared
     credentials live. Your Personal vault is for your own logins."

- **If not arrived yet:**
  > "Still waiting on it — let's set up Slack now and come back to finish 1Password
  > right after."

### 4b. Chrome Extension

After 1Password desktop is set up:
> "Last thing for 1Password: let's pin it in Chrome so it's always one click away.
> Click the puzzle piece icon in Chrome's toolbar — that's Extensions. Find 1Password,
> click Connect, then click the pin icon to keep it visible."

> "Once it's pinned, sign in to 1Password from the extension. From now on it'll
> autofill your passwords and suggest new ones when you're creating accounts."

Also mention:
> "One perk: Evermore gives everyone a free 1Password account for personal use too.
> You can set that up on your own time — same app, different vault."

### 4c. Slack Setup

> "Now let's get Slack set up — that's how we communicate internally."

1. "Go to myapps.microsoft.com in Chrome and click the Slack tile. It'll sign you in
   through SSO in your browser."
2. "In the browser, you'll see 'Soda Health' in the upper left — click it and choose
   'Launch in Slack App'. This opens the desktop app with SSO already connected."
3. "Let me know when you can see the Slack workspace."

Once they're in, tell them the key channels to join:

> "A few channels worth knowing:"
>
> - `#general` — company-wide announcements from leadership
> - `#random` — casual conversation, the water cooler
> - `#it-sec-private` — that's the IT and security help channel. If anything with
>   your laptop or accounts stops working, post there. It's staffed by IT and it's
>   faster than filing a ticket for urgent things.
> - `#security` — security announcements and awareness
> - `#coffee-club` — a good way to meet people across the company

---

## Phase 5 — "Staying Safe and Getting Help" (~10 min)

### 5a. Phishing and Suspicious Emails

> "One thing IT takes seriously here: phishing. Bad actors do try to impersonate
> leadership — especially our CEO — or fake company emails."

> "The rule is simple: if an email feels off, don't click anything. Check the sender's
> email address carefully. If something seems wrong, post it in `#it-sec-private`
> and ask — you won't look silly. That channel exists exactly for that."

> "There's also a Report button in Outlook for suspicious emails — if you see it, use
> it. It helps train our spam filter and protects everyone."

### 5b. Quarantine

> "Sometimes good emails end up in quarantine — our spam filter is aggressive. You'll
> get automated notifications saying a message is held. Open the notification, review
> the message, and if it's legitimate, mark it as a false positive so future emails
> from that sender come through normally."

### 5c. IT Service Portal

> "For IT help: the official channel is our IT service portal at
> sodahealth.atlassian.net/servicedesk/customer/portal/3. Bookmark that.
> It's where you submit requests for access, report broken things, or request
> an AI tool license. Tickets get tracked so nothing falls through the cracks."

> "For quick or urgent things, `#it-sec-private` in Slack is faster. Use the
> portal for anything non-urgent."

### 5d. Security Basics

> "Two quick rules that cover 90% of our security requirements:"
>
> "First: use 1Password for all your passwords. Let it generate them. Never reuse
> passwords across sites. And IT will never ask you for your password — if anyone
> does, that's a red flag."
>
> "Second: HIPAA. We handle protected health information for health plan members,
> so HIPAA applies to your work. In practice: don't share member data outside
> approved systems, use company tools (not personal Gmail or Dropbox), and if
> anything looks suspicious, post in `#it-sec-private`."

### 5e. Policies

> "There's one policy you'll need to read and acknowledge: the Acceptable Use policy
> in Confluence. It covers what you can and can't do with company systems. It's not
> long. When you have a few minutes, search for it in Confluence and sign off on it."

> "Quick list of what not to do:
> - Don't put work files in personal Google Drive or Dropbox → SharePoint or company Google Drive only
> - Don't use ChatGPT for work → Microsoft Copilot is the approved AI tool here
> - Don't ignore Kandji/Iru update prompts → those are compliance requirements, not optional"

### 5f. Mobile Setup (Optional)

> "Last thing — and skip this if you'd rather not use your personal phone for work.
> If you do want work email on your phone, here's how:"

1. "Download 'Company Portal' from the App Store or Google Play."
2. "Sign in with your `@sodahealth.com` email."
3. "If you're on iPhone, use the Outlook app for email — not the built-in Mail app.
   The built-in Mail app doesn't go through our security controls."
4. "Microsoft Defender will install automatically. Make sure its status shows green."
5. "You might be prompted to update your phone's OS — that's expected. We enforce a
   minimum version for security."

---

## Closing

When all phases are complete:

> "You're all set! Here's the quick version of what we covered:
>
> ✅ Laptop login and Authenticator — your sign-in is secure
> ✅ 1Password — your password vault is ready
> ✅ Chrome — set up with your work profile
> ✅ Slack — you're in the workspace with the key channels
> ✅ Apps — your access to Atlassian, Smartsheet, and your core tools is verified
> ✅ Security basics — you know what to watch for and where to get help
>
> If anything stops working — an app you can't get into, something that looks wrong —
> post in `#it-sec-private` on Slack. IT will jump in.
>
> Now — what would you like to try first?"

Then transition to Mode 3 Step 8 (first task).

---

## Tracking and Resume

### Writing progress

After each phase completes, write progress to enrichment:

```json
{
  "preferences": {
    "it_onboarding_phase": "3",
    "it_onboarding_items": "authenticator,zoom,1password_started,chrome,kandji_explained"
  }
}
```

Phase values: `"1"` through `"5"`. On full completion: `"complete"`.

Items to track as they're done:
`authenticator`, `macos_tips`, `1password_started`, `1password_secret_key_saved`,
`zoom`, `chrome`, `kandji_explained`, `sso`, `apps_atlassian`, `apps_smartsheet`,
`1password_complete`, `1password_extension`, `slack`, `phishing`, `quarantine`,
`it_portal`, `security_basics`, `policies`, `mobile`

### Resuming mid-checklist

If `it_onboarding_phase` is in enrichment but not `"complete"`, greet them:

> "Welcome back! Last time we got through [describe what's in `it_onboarding_items`].
> Ready to pick up from [next phase name]?"

Then continue from the right phase.

### On completion

Write:
```json
{
  "preferences": {
    "it_onboarding_phase": "complete",
    "it_onboarding_complete": "true",
    "it_onboarding_date": "YYYY-MM-DD"
  }
}
```

---

## Escalation

If troubleshooting a step doesn't resolve it after 1-2 attempts:

> "That one is being stubborn — let me flag it for IT so they can take a look.
> I'll note exactly what's happening so you don't have to explain it from scratch."

Write the specific issue to enrichment `friction_points` with enough detail for IT to act.

Then:
> "IT will follow up with you in `#it-sec-private` on Slack. In the meantime,
> let's keep going — don't let one stuck thing block everything else."

Continue with the next item. Do not dwell on unsolved steps.

---

## Troubleshooting Quick Reference

| What they say | What to do |
|---------------|-----------|
| "Outlook isn't installed yet" | Use `myapps.microsoft.com` in browser. Kandji will install it within ~10 min of first login |
| "I can't find the 1Password invite" | Check spam/junk. If still missing after 10 min, reassure them IT will sort it — flag in their enrichment |
| "Authenticator push isn't working" | Fall back to 6-digit code method. Flag for IT follow-up |
| "Iru / Kandji isn't on my desktop" | Check Applications folder. It installs in background — up to 15 min after first login |
| "The SSO portal shows an error" | Note the specific app and move on. Flag for IT in enrichment |
| "Slack isn't in myapps" | Provisioning may still be running. Check back in 30 min or flag for IT |
| "I used my personal Apple ID during Mac setup" | Flag for IT in enrichment — they'll need to sort out the Apple ID situation |
| "I need to go / can I come back?" | "Absolutely — I've saved your progress. Come back when you're ready and we'll pick up right where we left off." Then write progress to enrichment |
