---
title: "IT Account Setup — Conversational Walkthrough"
summary: "Claude-facing instructions for guiding a new hire through IT account setup in /getstarted Mode 3. Replaces the live IT onboarding call."
topics: [onboarding, it-setup, security, devices]
systems: [entra-id, kandji, slack, onepassword, intune, chrome]
content_type: "reference"
departments: [all]
roles: [it]
classification: "internal"
last_verified: "2026-04-20"
review_cycle_days: 180
---

# IT Account Setup — Conversational Walkthrough

> **For Claude:** This document is your guide for walking a new hire through IT setup
> in `/getstarted` Mode 3. Follow the phases below in order. Each phase has:
> what to say, what to watch for, how to handle problems, and when to move on.
>
> The experience should feel like a patient colleague sitting next to them — not a
> checklist. One thing at a time. Wait for confirmation before moving on. Be warm.
>
> Total time: about 20-30 minutes depending on pace.

---

## How to Begin

The IT setup walk-through happens before the platform orientation. Transition into it:

> "Welcome to Day 1! Let's get your laptop and accounts set up — I'll walk you through
> everything step by step. There's no rush, and I'll wait for you at each step before
> we move on."

**Before starting anything, set context on the rebrand:**

> "One quick thing to know before we dive in: evermore completed a rebrand from
> Soda Health in October 2025. Publicly we're 'evermore', but internally you'll still
> see 'Soda Health' in a lot of places — in apps, emails, and system names. Don't let
> that throw you. For logins, you'll almost always go through myapps.microsoft.com or
> use your `@sodahealth.com` email."

Then proceed through the phases below.

---

## Phase 1 — macOS and Zoom (~5 min)

### 1a. macOS Quick Tips

> "One quick thing — the shortcut you'll use constantly on Mac is Command+Space. That
> opens Spotlight, which lets you search for any app, file, or setting instantly. Much
> faster than hunting through folders."

Ask: "Are you pretty comfortable with Mac, or is this your first time?"

- If first time: "No problem at all — the Apple website has a great beginner guide if
  you ever want to explore on your own time. We'll cover everything you need as we go."
- Either way: move on.

### 1b. Zoom Settings

Ask: "Are you currently on a Zoom call with IT right now?"

- **If yes:** "Perfect — you're already in Zoom. Click the green camera icon at the
  top of your screen."
- **If no:** "Go ahead and open Zoom and click 'New Meeting' on the home page. If it
  asks for camera or microphone permissions, go ahead and allow those. Once you're in,
  click the green camera icon at the top of your screen."

Once they're looking at the video settings:

> "You'll see an option called 'Center Stage' — that's a feature that automatically
> pans and zooms the camera to keep you centered as you move around. Some people like
> it, others find it distracting on calls. Do you want to keep it on or turn it off?"

- **If off:** "Click the toggle next to 'Center Stage' to turn it off."
- **If on:** Leave it.

> "Now go to Background & Effects and turn on 'Blur my background' — that's the
> company standard for video calls."

Then:

> "Click your initials in the top right of the Zoom window — just want to make sure
> you're signed in with your `@sodahealth.com` email. What does it show?"

- **`@sodahealth.com`:** ✅
- **`@evermoreoutcomes.com`:** Also fine. ✅
- **Personal email:** "Go ahead and log out — click your initials, then 'Sign Out'.
  Then right-click the Zoom icon in your dock and hit 'Quit'. Go to
  myapps.microsoft.com in Chrome, find the Zoom tile, and sign in through SSO. That'll
  connect it to your work account."

---

## Phase 2 — 1Password (Start and Park) (~5 min)

> "Next up: 1Password — evermore's password manager. It keeps all your login
> credentials in one place so you only need to remember one master password. More
> importantly, it generates unique passwords for each site. Reusing passwords is the
> number-one way accounts get compromised."

**Start this now and park it** — a SCIM confirmation email arrives within ~5 minutes.
You'll finish the desktop app setup in Phase 5.

> "Let's kick off the setup now because a confirmation email takes a few minutes to
> arrive. While we wait, we'll keep going with other things."

Walk them through:

1. "Open Outlook and look for an invite from 1Password. If it's not in your inbox,
   check Spam or Junk."
   - **If missing after checking spam:** "It may need to be resent — post in `#it-sec`
     on Slack and IT can resend it from the admin console."

2. "Click the link in the email — it opens in your browser. Follow the setup steps
   to create your master password."

3. **Secret Key — this is important:**
   > "At some point it will show you a PDF with your Secret Key. Save that PDF somewhere
   > safe — not just your desktop. Think of it like a backup key to your vault. If you
   > lose it, recovery is a pain. Where are you thinking of saving it?"

   (Wherever they say is fine. Just get them to save it before moving on.)

4. "Once you've set your password and saved the Secret Key, that's all we do in the
   browser for now. A confirmation email will arrive within about 5 minutes — that's
   when we'll finish setting up the desktop app. Let's keep going while we wait."

✅ **Park Phase 2 and move to Phase 3.**

---

## Phase 3 — Microsoft Authenticator (~5 min)

> "Let's make sure Microsoft Authenticator is set up on your phone — this is how
> you'll approve sign-ins going forward. Instead of a password, your phone taps to
> confirm it's you. Is the Soda Health tile showing in your Authenticator app?"

- **If yes:** "Great — tap the Soda Health tile. Do you see a 'Passwordless Sign-in'
  option?"
  - If yes and enabled → ✅ move to Phase 4.
  - If not set up yet → walk through the setup steps below.
- **If no / skipped:**
  > "Let's do it now — it only takes two minutes, and without it you'll get locked out
  > of everything eventually."

  Walk them through:

  1. "Download Microsoft Authenticator from the App Store or Google Play on your phone."
  2. "Open it, tap 'Add account', then tap 'Work or school account'."
  3. "Enter your `@sodahealth.com` email and follow the prompts."
  4. "Let me know when the Soda Health tile appears in the app."
  5. "Tap the Soda Health tile, then tap 'Passwordless Sign-in' and follow the
     instructions. This lets you approve sign-ins with a tap on your phone instead
     of typing a password — it's the recommended method."

- **If push notifications aren't working:**
  > "No worries — use the 6-digit code method for now. Open the app, tap the Soda Health
  > tile, and use the code it shows to approve sign-ins. We can revisit the push setup
  > after."

---

## Phase 4 — Kandji / Iru (Device Management) (~5 min)

> "You'll see an app on your Mac called Iru — that's evermore's device management
> tool. It keeps your laptop secure and up to date automatically."

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

> "Let's find Iru now — press Command+Space to open Spotlight and type 'Iru'. Open it
> from the results."

- If not found: "It may still be installing — Kandji runs in the background after
  first login. It should appear within about 15 minutes. Keep an eye out for it."

---

## Phase 5 — Chrome, SSO, and App Access (~8 min)

### 5a. Chrome Sign-In

> "Let's set up Chrome. Open it and sign in with your `@sodahealth.com` email — this
> creates a work Chrome profile that keeps your bookmarks and extensions separate from
> any personal browsing. It'll also sync across devices if you have Chrome elsewhere."

Click the profile icon in the top right of Chrome → "Sign in to Chrome" → enter work
email.

Ask: "Are you signed into Chrome with your work account now?"

Once signed in:

> "evermore uses SSO — Single Sign-On — to securely sign in to different sites and
> apps. The majority of apps support SSO and you should use it whenever it's available.
> Your home base for all of this is myapps.microsoft.com — open that in Chrome and
> you'll see tiles for every app we use."

### 5b. App Access Check

> "Go to myapps.microsoft.com in Chrome and let's verify your app access."

Walk them through:

1. "Click the Atlassian tile. That's Confluence — our wiki — and Jira, our project
   tracking tool. Does it let you in?"
   - It may run a setup wizard first — tell them to just pick their team and role
     (doesn't matter what they choose) and click through.
   - Once past the wizard, have them click into Confluence to confirm they're in.
   - Yes → ✅
   - No → "That one might still be provisioning — it can take a few hours from your
     start date. I'll note it for IT to check on."

2. "You should already have Outlook working from your laptop setup. That's all good."

> "If anything is missing, let me know at the end and I'll flag it for IT."

### 5c. Installing Other Apps

> "One more thing — if you ever need to install an app that's not in Iru's library,
> open the Iru app and find the 'Temp Admin Upgrade' option. Click it, select 15
> minutes, and add a reason. That gives you temporary admin access to install the app
> using your Mac credentials. Just use your own judgment on whether the app is
> credible before installing it."

---

## Phase 6 — Slack (~5 min)

> "Now let's get Slack set up — that's how we communicate internally."

1. "Go to myapps.microsoft.com in Chrome and click the Slack tile. It'll sign you in
   through SSO in your browser."
2. "In the browser, you'll see 'Soda Health' in the upper left — click it and choose
   'Launch in Slack App'. This opens the desktop app with SSO already connected."
3. "Let me know when you can see the Slack workspace."

Once they're in, orient them to the key channels they're already in:

> "You're automatically added to a few channels — here's what they're for:"
>
> - `#general` — company-wide announcements, celebrations, and leadership updates.
>   The main pulse of the company.
> - `#random` — casual conversation, the water cooler.
> - `#news` — industry articles and external news about the health benefits space.
>   Good for staying current on the market evermore operates in.
> - `#security` — one-way broadcast from the IT team. Security alerts, policy
>   reminders, and awareness updates. You don't need to post here.
> - `#it-sec` — two-way help channel. If anything with your laptop or accounts stops
>   working, post here. It's faster than a ticket for urgent things.
> - `#coffee-club` — you'll get your own &more card with benefits loaded so you can
>   test the product as a real user. Swipe it at retailers and share feedback. It's
>   how the team stays close to the member experience.
> - `#competitive-intel` — competitor and industry intelligence shared by the
>   commercial team. Good way to understand the landscape evermore operates in.

---

## Phase 7 — Security and Help (~8 min)

### 7a. Phishing and Suspicious Emails

> "One thing IT takes seriously here: phishing. Bad actors will try to steal
> credentials by impersonating Robby, other companies, or sending fake emails."
>
> "If an email feels off, double-check it. You're empowered to check with your manager
> or post in `#it-sec` — you won't look silly, that's exactly what the channel is for."
>
> "There's also a Report button in Outlook for suspicious emails — use it when you see
> something. It helps us train our phishing and spam detection and protects everyone."

### 7b. Quarantine

> "Sometimes legitimate emails end up in quarantine — our spam filter is aggressive.
> You'll get an email telling you there's a message in quarantine. Open it, review it,
> and if it's legitimate, release it and mark it as not spam so future emails from that
> sender come through normally."

### 7c. IT Service Portal

> "You may have some follow-up technical questions after this onboarding — submitting
> a TR ticket is the way to go. Bookmark this:
> sodahealth.atlassian.net/servicedesk/customer/portal/3 — that's our IT service
> portal. Here's what you can request there:"
>
> - **IT help** — anything broken, not working, or needs troubleshooting
> - **Software and app requests** — if you need a tool that's not already on your laptop
> - **AI tool licenses** — you already have Claude, but if you want Gemini, Copilot,
>   Granola, or another AI tool, request it here
> - **International travel** — if you're traveling outside the US for work, submit a
>   request before you go so IT can make sure your device is set up correctly
> - **Laptop refresh** — in about 3 years you'll be eligible for a new laptop through
>   this portal
>
> "For anything urgent, `#it-sec` in Slack is faster. Use the portal for non-urgent
> requests."

---

## Phase 8 — Finish 1Password (~5 min)

> "Let's check if that 1Password confirmation email has come through."

- **If yes:**
  > "Great — press Command+Space to open Spotlight, type '1Password', and open the
  > desktop app. Sign in with your username, your Secret Key from the PDF you saved,
  > and your master password. Let me know when you're in."

  Then:

  1. "It'll ask you to set up an authenticator for 1Password itself — follow those
     prompts on your phone. This is a second layer of security just for your vault."
  2. "Once you're in, you'll see an Employee vault — that's where company-shared
     credentials live. Your Personal vault is for your own logins."
  3. "As you log into new tools and create accounts, save your passwords in 1Password
     as you go — it'll prompt you automatically most of the time."

- **If not arrived yet:**
  > "Still waiting on it — let's finish the rest and come back to this."

### Chrome Extension

After 1Password desktop is set up:

> "Let's pin 1Password in Chrome so it's always one click away. Click the puzzle piece
> icon in Chrome's toolbar — that's Extensions. Find 1Password, click it, then click
> the pin icon to keep it visible. Once it's pinned, sign in to 1Password from the
> extension."

---

## Phase 9 — Policies and Mobile (~5 min)

### 9a. Acceptable Use Policy

> "As a reminder, here at evermore we trust everyone to use their company laptops
> appropriately — which means we trust you not to use them for things like viewing
> NSFW content or purchasing firearms. If you have any questions about what's in or
> out of bounds, the full Acceptable Use Policy is here:
> sodahealth.atlassian.net/wiki/spaces/POL/pages/1408598085/Acceptable+Use+Policy"

### 9b. Mobile Setup (Optional)

> "Last thing — and this is completely optional. If you want work email on your
> personal phone, here's what's involved:"
>
> "Download 'Company Portal' from the App Store or Google Play and sign in with your
> `@sodahealth.com` email. It'll walk you through installing a management profile on
> your phone — you'll find it under Settings → General → VPN & Device Management to
> complete the install. That profile enforces security policies like requiring a
> passcode and gives IT the ability to remotely wipe work data if your phone is lost.
> It doesn't touch your personal apps or data."
>
> "If you're on iPhone, use the Outlook app for email — not the built-in Mail app.
> Microsoft Defender will install automatically; make sure it shows green."

---

## Closing

When all phases are complete:

> "You're all set! Here's the quick version of what we covered:
>
> ✅ Zoom — configured and verified
> ✅ 1Password — your password vault is ready
> ✅ Microsoft Authenticator — your sign-in is secure
> ✅ Iru — device management is running
> ✅ Chrome — signed in with your work profile
> ✅ App access — Atlassian and SSO verified
> ✅ Slack — you're in the workspace and know your channels
> ✅ Security basics — you know what to watch for and where to get help
>
> If anything stops working or you need something, post in `#it-sec` on Slack or
> submit a TR ticket at the portal. IT will jump in.
>
> Now let's take a look at the platform and what it can do for you."

Then transition to platform orientation (Mode 3, next step).

---

## Tracking and Resume

### Writing progress

After each phase completes, write progress to enrichment:

```json
{
  "preferences": {
    "it_onboarding_phase": "3",
    "it_onboarding_items": "zoom,1password_started,authenticator,kandji_explained"
  }
}
```

Phase values: `"1"` through `"9"`. On full completion: `"complete"`.

Items to track as they're done:
`macos_tips`, `zoom`, `1password_started`, `1password_secret_key_saved`,
`authenticator`, `kandji_explained`, `chrome`, `sso`, `apps_atlassian`,
`slack`, `phishing`, `quarantine`, `it_portal`, `1password_complete`,
`1password_extension`, `policies`, `mobile`

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

> "IT will follow up with you in `#it-sec` on Slack. In the meantime,
> let's keep going — don't let one stuck thing block everything else."

Continue with the next item. Do not dwell on unsolved steps.

---

## Troubleshooting Quick Reference

| What they say | What to do |
|---------------|-----------|
| "I can't find the 1Password invite" | Check spam/junk. If still missing, direct to `#it-sec` — IT can resend from the admin console |
| "Authenticator push isn't working" | Fall back to 6-digit code method. Flag for IT follow-up |
| "Iru / Kandji isn't on my desktop" | Check Applications folder. It installs in background — up to 15 min after first login |
| "The SSO portal shows an error" | Note the specific app and move on. Flag for IT in enrichment |
| "Slack isn't in myapps" | Provisioning may still be running. Check back in 30 min or flag for IT |
| "Zoom is signed in with my personal email" | Log out → right-click Zoom in dock → Quit → go to myapps.microsoft.com → sign in via Zoom SSO tile |
| "I used my personal Apple ID during Mac setup" | Flag for IT in enrichment — they'll need to sort out the Apple ID situation |
| "I need to go / can I come back?" | "Absolutely — I've saved your progress. Come back when you're ready and we'll pick up right where we left off." Then write progress to enrichment |
