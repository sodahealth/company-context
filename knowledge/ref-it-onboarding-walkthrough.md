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

Then proceed through the five phases below.

---

## Phase 1 — "Let's Confirm You're Signed In" (~5 min)

### 1a. Microsoft Authenticator

> "Let's make sure Microsoft Authenticator is set up on your phone — this is how
> you'll approve sign-ins going forward. Instead of a password, your phone taps to
> confirm it's you. Is the Soda Health tile showing in your Authenticator app?"

- **If yes:** "Great — tap the Soda Health tile. Do you see a 'Passwordless Sign-in'
  option?"
  - If yes and enabled → ✅ move to 1b.
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

### 1b. macOS Quick Tips

> "One quick thing — the shortcut you'll use constantly on Mac is Command+Space. That
> opens Spotlight, which lets you search for any app, file, or setting instantly. Much
> faster than hunting through folders."

Ask: "Are you pretty comfortable with Mac, or is this your first time?"

- If first time: "No problem at all — Macs are pretty intuitive once you get the hang
  of it. The Apple website has a great beginner guide if you ever want to explore on
  your own time. We'll cover everything you need as we go."
- Either way: move on.

---

## Phase 2 — "Your Password Vault (Start Now, Finish Later)" (~5 min)

> "Next up: 1Password. This is evermore's password manager — it keeps all your login
> credentials in one place so you only need to remember one master password. More
> importantly, it generates unique passwords for each site. Reusing passwords is the
> number-one way accounts get compromised."

**Important:** Start this now and then *park it* — a SCIM confirmation email arrives
within 5 minutes. You'll come back to finish on the desktop app in Phase 4.

> "Let's kick off the setup now, because there's a confirmation email that takes a few
> minutes to arrive. While we wait, we'll keep going with other things."

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

## Phase 3 — "Browser, Apps, and Device" (~10 min)

*Run this while waiting for the 1Password confirmation email.*

### 3a. Chrome Sign-In

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

### 3b. Zoom

> "Let's get Zoom configured. Open Zoom and click 'New Meeting' on the home page.
> If it asks for camera or microphone permissions, go ahead and allow those."

Once they're in a meeting:

> "Click the green camera icon at the top of your screen. You'll see an option called
> 'Center Stage' — that's a feature that automatically pans and zooms the camera to
> keep you centered as you move around. Some people like it, others find it distracting
> on calls. Do you want to keep it on or turn it off?"

- **If off:** "Click the toggle next to 'Center Stage' to turn it off."
- **If on:** Leave it.

Then:

> "Now click your initials in the top right of the Zoom window — just want to make sure
> you're signed in with your `@sodahealth.com` email. What does it show?"

- **`@sodahealth.com`:** ✅
- **`@evermoreoutcomes.com`:** Also fine. ✅
- **Personal email:** "Go ahead and log out — click your initials, then 'Sign Out'.
  Then right-click the Zoom icon in your dock and hit 'Quit'. Go to
  myapps.microsoft.com in Chrome, find the Zoom tile, and sign in through SSO. That'll
  connect it to your work account."

### 3c. Kandji / Iru (Device Management)

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
- **Installing from the web.** "If you want to install something from the web that's
  not in Iru's library, make sure it's a credible app, then use the temporary admin
  upgrade option in Jira to get elevated permissions, and use your Mac credentials to
  complete the install."
- **Admin requests.** "Occasionally an app update will pop up asking for admin
  permission. Before you click Allow, make sure it's something you recognize."

Ask: "Can you see Iru on your desktop or in your Applications folder?"

- If not visible: "It may still be installing — Kandji runs in the background after
  first login. It should appear within about 15 minutes. Keep an eye out for it."

### 3d. App Access Check

> "Go to myapps.microsoft.com in Chrome and let's verify your app access."

Walk them through checking access:

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

---

## Phase 4 — "Finish 1Password + Slack" (~8 min)

### 4a. Complete 1Password

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
  > "Still waiting on it — let's set up Slack now and come back to finish 1Password
  > right after."

### 4b. Chrome Extension

After 1Password desktop is set up:

> "Last thing for 1Password: let's pin it in Chrome so it's always one click away.
> Click the puzzle piece icon in Chrome's toolbar — that's Extensions. Find 1Password,
> click it, then click the pin icon to keep it visible. Once it's pinned, sign in to
> 1Password from the extension."

### 4c. Slack Setup

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
> - `#security` — security announcements and awareness from the IT team.
> - `#it-sec` — IT and security help. If anything with your laptop or accounts stops
>   working, post there. It's faster than a ticket for urgent things.
> - `#coffee-club` — you'll get your own &more card with benefits loaded so you can
>   test the product as a real user. Swipe it at retailers and share feedback. It's
>   how the team stays close to the member experience.
> - `#competitive-intel` — competitor and industry intelligence shared by the
>   commercial team. Good way to understand the landscape evermore operates in.

---

## Phase 5 — "Staying Safe and Getting Help" (~10 min)

### 5a. Phishing and Suspicious Emails

> "One thing IT takes seriously here: phishing. Bad actors do try to impersonate
> leadership — especially our CEO — or send fake company emails."
>
> "The rule is simple: if an email feels off, don't click anything. Check the sender's
> email address carefully. If something seems wrong, post it in `#it-sec` on Slack and
> ask — you won't look silly. That channel exists exactly for that."
>
> "There's also a Report button in Outlook for suspicious emails — use it when you see
> something. It helps train the spam filter and protects everyone."

### 5b. Quarantine

> "Sometimes legitimate emails end up in quarantine — our spam filter is aggressive.
> You'll get automated notifications when a message is held. Open the notification,
> review it, and if it's legitimate, release it and mark it as not spam so future
> emails from that sender come through normally."

### 5c. IT Service Portal

> "You may have some follow-up technical questions after this onboarding — to get IT
> assistance, submitting a TR ticket is the way to go. Bookmark this:
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
> anything looks suspicious, post in `#it-sec`."

### 5e. Policies

> "As a reminder, here at evermore we trust everyone to use their company laptops
> appropriately — which means we trust you not to use them for things like viewing
> NSFW content or purchasing firearms. If you have any questions about what's in or
> out of bounds, the full Acceptable Use Policy is here:
> sodahealth.atlassian.net/wiki/spaces/POL/pages/1408598085/Acceptable+Use+Policy"

### 5f. Mobile Setup (Optional)

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
> ✅ Microsoft Authenticator — your sign-in is secure
> ✅ 1Password — your password vault is ready
> ✅ Chrome — set up with your work profile
> ✅ Zoom — configured and verified
> ✅ Iru — device management is running
> ✅ App access — Atlassian and SSO verified
> ✅ Slack — you're in the workspace and know your channels
> ✅ Security basics — you know what to watch for and where to get help
>
> If anything stops working or you need something, post in `#it-sec` on Slack or
> submit a ticket at the portal. IT will jump in.
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
    "it_onboarding_items": "authenticator,zoom,1password_started,chrome,kandji_explained"
  }
}
```

Phase values: `"1"` through `"5"`. On full completion: `"complete"`.

Items to track as they're done:
`authenticator`, `macos_tips`, `1password_started`, `1password_secret_key_saved`,
`zoom`, `chrome`, `kandji_explained`, `sso`, `apps_atlassian`,
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
