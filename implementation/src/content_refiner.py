from __future__ import annotations

from pathlib import Path

REPLACEMENTS = {
    "Draft notes for: Overview.": "This page is designed to help small service businesses compare CRM options without wasting time on generic software lists.",
    "Draft notes for: Who this is for.": "It is for owners and operators who need quoting, scheduling, invoicing, customer follow-up, and basic pipeline visibility in one place.",
    "Draft notes for: Key considerations.": "The most important factors are field-service fit, ease of use, quoting and dispatch features, pricing clarity, and how well the tool scales with the team.",
    "Draft notes for: Top picks.": "The strongest candidates combine scheduling, customer history, estimates, invoicing, and reliable workflows for small service teams.",
    "Draft notes for: Comparison table.": "A comparison table should highlight best fit, strengths, weaknesses, and pricing posture for each tool.",
    "Draft notes for: How to choose.": "Choose based on company size, dispatch complexity, budget tolerance, and whether you need a field-service-first tool or a broader CRM.",
    "Draft notes for: Final recommendation.": "For most small service businesses, a field-service-first CRM is usually a better starting point than a generic CRM.",
    "Draft notes for: Why this niche needs a CRM.": "Service businesses lose time and revenue when customer communication, quoting, scheduling, and invoicing are scattered across spreadsheets and chat apps.",
    "Draft notes for: Top options.": "The best options are usually the products already optimized for dispatch, field teams, repeat jobs, and customer lifecycle visibility.",
    "Draft notes for: Implementation tips.": "A small team should start with job intake, quoting, and customer tracking first, then layer in automation and reporting after adoption.",
    "Draft notes for: Recommendation.": "The best choice depends on whether the business values simplicity, deeper operations control, or broader marketing automation.",
    "Draft notes for: Quick verdict.": "This comparison should quickly tell the reader which product fits smaller teams versus more complex service operations.",
    "Draft notes for: Feature comparison.": "The comparison should focus on scheduling, dispatching, invoicing, communication, and reporting rather than generic CRM checklists.",
    "Draft notes for: Pricing.": "Pricing should be evaluated by real fit, not headline cost alone, because operational mismatch can be more expensive than software fees.",
    "Draft notes for: Best fit by scenario.": "Different tools win depending on business size, service complexity, and how central field operations are to daily workflow.",
    "Draft notes for: Why people look for alternatives.": "Users usually look for alternatives when cost, complexity, or missing workflow features start to slow the team down.",
    "Draft notes for: Best alternatives.": "Alternatives should be grouped by best fit, budget sensitivity, and operational complexity.",
    "Draft notes for: How to switch.": "Switching is easiest when customer records, active jobs, templates, and payment flows are migrated in a controlled order.",
    "Draft notes for: Short answer.": "A CRM for home service businesses is the system that keeps leads, customers, jobs, estimates, communication, and revenue workflows organized.",
    "Draft notes for: Detailed explanation.": "In this niche, a CRM often overlaps with field-service management because scheduling, dispatch, and invoicing matter as much as contact records.",
    "Draft notes for: Common questions.": "This section should answer the practical questions buyers ask before choosing a platform or switching tools.",
}


def main() -> None:
    content_dir = Path(__file__).resolve().parents[1] / "output" / "content"
    updated = 0
    for file in content_dir.glob("*.md"):
        text = file.read_text()
        before = text
        for old, new in REPLACEMENTS.items():
            text = text.replace(old, new)
        if text != before:
            file.write_text(text)
            updated += 1
    print(f"Refined {updated} files")


if __name__ == "__main__":
    main()
