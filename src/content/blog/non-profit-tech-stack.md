# A Practical Tech Stack for a Neighborhood Non-Profit

I recently became treasurer of the [Stuyvesant Park Neighborhood Association](https://spnanyc.org), a long-running community organization in NYC. We run on an annual budget of about $100k with an endowment of about $150k, but our tools had not kept up with the organization.

This post covers the stack we implemented, why we chose each tool, and the order I would recommend for other small non-profits.

## The Stack (in Implementation Order)

1. **Website hosting**: Squarespace (~$150/year, basic plan)
2. **Email + identity**: Google Workspace for Nonprofits (free tier)
3. **Cards + AP + treasury**: Ramp (free plan)
4. **Accounting**: QuickBooks Online via TechSoup (~$80/year)

The order matters. Set up your website and domain email first, then configure payments/cards, then connect accounting. Your card/AP platform often determines which accounting integrations are practical.

## 1) Website Hosting: Simplify and Consolidate

We moved from a legacy WordPress setup (InMotion Hosting + GoDaddy) to Squarespace.

Why we switched:
- Our old WordPress install had plugin conflicts and ongoing maintenance risk.
- Squarespace cut annual hosting cost materially (from roughly $600/year to roughly $150/year).
- It was easier to find contractors who can maintain Squarespace without ongoing custom development.
- We could consolidate domain and website under one vendor, which reduced operational overhead.

Permission model we use:
- `Admin` account: domain, billing, and high-risk settings.
- `Designer` account: content and layout updates.

This split lets board officers retain control while giving freelancers limited access.

## 2) Email Hosting: Create a Stable Operating Identity

Google Workspace for Nonprofits was the clear choice for us: free, reliable, and familiar for most volunteers.

What we implemented:
- Kept personal email flexibility for board members (no forced migration on day one).
- Created a shared `admin` identity for vendor logins and account recovery.
- Created groups:
  - `info@...` as the public inbound contact.
  - `board@...` as an internal distribution list.

Big practical win: no more fragile CC chains across many personal addresses.

## 3) Corporate Cards and AP: Replace Paper Checks

When I took over, payments were managed through handwritten checks and a physical check register. It worked, but it was slow and error-prone.

We adopted Ramp to modernize spending and approvals:
- Corporate cards + AP workflows in one system.
- No monthly fee on the basic plan.
- Yield on operating cash plus card rewards improved treasury efficiency.
- Faster approvals and cleaner audit trail than paper checks.

Governance setup:
- Four officers as administrators/approvers.
- Each department receives a shared "Fund" with a monthly spending cap.
- Staff and volunteers receive role-appropriate cards and limits.

Adoption was fast once people realized they no longer had to manage lost checks and reimbursement delays.

## 4) Accounting: Keep It Standard

We chose QuickBooks Online (QBO), primarily because:
- It is widely used and easy to hand off to accountants/bookkeepers.
- Non-profit pricing via TechSoup is very affordable.
- It integrates with our payments workflow.

What has worked:
- Monthly budget and P&L reporting by segment.
- Better visibility than spreadsheet-only processes.

Limitations we still feel:
- UI can be slow and reporting customization is inconsistent.
- Some useful report automations are oddly unavailable.
- 1099 e-filing pricing is high relative to newer alternatives.

## What Changed Operationally

After these four moves, finance operations became much easier:
- Fewer vendors and fewer credentials to manage.
- Faster payment cycles and clearer approvals.
- Better board reporting with less manual work.
- Less key-person risk because access and process are documented.

For a small non-profit, “boring and reliable” is usually better than “custom and clever.”


