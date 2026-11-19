"""Static meeting fixtures used while the capture service is being designed.

This module deliberately contains plain dictionaries instead of a Django model.
It gives the meeting UI realistic data without pretending that a recording bot
or persistence layer exists yet.
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MEETING_MEDIA_URL = "/static/meetings/product-sync-sample.wav"

ONBOARDING_TRANSCRIPT = """[00:00] Maya (Product): Thanks everyone. Today we need to decide whether the
new-user checklist should be a single guided flow or a set of smaller prompts.

[00:18] Leo (Design): The test sessions strongly favoured the guided flow.
People understood the next step, but they missed the optional workspace invite.

[00:42] Priya (Engineering): We can ship the guided version without a schema
change. I would like the invite step to stay dismissible so it does not block
activation.

[01:05] Maya (Product): Agreed. The success metric is reaching the first project,
not collecting every profile field. Let us make the invite prompt secondary.

[01:22] Leo (Design): I will update the prototype with a visible skip action and
add an empty state for teams that have not invited anyone yet.

[01:38] Priya (Engineering): I will add events for checklist_started,
checklist_completed, and invite_prompt_skipped. That gives us a clean funnel.

[01:52] Maya (Product): Great. Priya owns the instrumentation, Leo owns the
prototype, and I will write the release note. We will review the funnel next
Thursday before enabling it for all workspaces."""

SUCCESS_TRANSCRIPT = """[00:00] Sam (Customer Success): Renewal risk is concentrated in three accounts
that have not invited a second teammate.
[00:31] Noor (Support): The common issue is that the invite control is hidden
after the first project is created.
[01:04] Sam (Customer Success): Let us add an in-product reminder and a weekly
digest for workspace owners. I will draft the customer list by Friday.
[01:42] Maya (Product): We will compare invite conversion before and after the
reminder and keep the experiment limited to ten workspaces."""

ROADMAP_TRANSCRIPT = """[00:00] Maya (Product): The candidates are audit history, bulk project import,
and custom roles.
[00:27] Priya (Engineering): Audit history has the clearest trust benefit and
the smallest integration risk.
[00:55] Leo (Design): Custom roles solve a real enterprise problem, but the
permission model needs more discovery first.
[01:24] Maya (Product): We will prioritise audit history for the next sprint,
then interview five admins about custom roles."""

DASHBOARD_TRANSCRIPT = """[00:00] Leo (Design): The dashboard is visually calm, but the status cards do
not tell an owner what action to take next.
[00:29] Maya (Product): Add one primary action to each card and move the full
project table below the fold.
[00:58] Priya (Engineering): I can reuse the existing project endpoints, so
this is a template change rather than a backend project.
[01:26] Leo (Design): I will bring the revised hierarchy to critique on Monday."""


MOCK_MEETINGS = [
    {
        "id": "meeting-004",
        "title": "Product sync: onboarding improvements",
        "date": "2026-09-24",
        "video_url": MEETING_MEDIA_URL,
        "raw_transcript": ONBOARDING_TRANSCRIPT,
    },
    {
        "id": "meeting-003",
        "title": "Customer success weekly review",
        "date": "2026-09-17",
        "video_url": MEETING_MEDIA_URL,
        "raw_transcript": SUCCESS_TRANSCRIPT,
    },
    {
        "id": "meeting-002",
        "title": "Q3 roadmap prioritisation",
        "date": "2026-09-10",
        "video_url": MEETING_MEDIA_URL,
        "raw_transcript": ROADMAP_TRANSCRIPT,
    },
    {
        "id": "meeting-001",
        "title": "Design critique: workspace dashboard",
        "date": "2026-09-03",
        "video_url": MEETING_MEDIA_URL,
        "raw_transcript": DASHBOARD_TRANSCRIPT,
    },
]

# Alias kept intentionally simple for views that want the seeded collection.
MEETINGS = MOCK_MEETINGS
