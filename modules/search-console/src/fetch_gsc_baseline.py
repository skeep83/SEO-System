from __future__ import annotations

import json
import os
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

BASE = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE / 'output'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
SITE_URL = 'sc-domain:servicehub.md'
SITEMAP_URL = 'https://servicehub.md/sitemap.xml'
CREDENTIALS_PATH = os.environ.get(
    'GSC_CREDENTIALS_PATH',
    str(Path('/home/skeep/.openclaw/workspace/servicehub-search-console.json')),
)
SCOPES = ['https://www.googleapis.com/auth/webmasters']


def main() -> None:
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES)
    service = build('searchconsole', 'v1', credentials=creds, cache_discovery=False)

    sites = service.sites().list().execute()
    sitemaps = service.sitemaps().list(siteUrl=SITE_URL).execute()

    payload = {
        'site': SITE_URL,
        'sites': sites,
        'sitemaps': sitemaps,
        'target_sitemap': SITEMAP_URL,
    }
    (OUTPUT_DIR / 'baseline.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    lines = [
        f'# GSC Baseline for {SITE_URL}',
        '',
        '## Site access',
    ]
    for site in sites.get('siteEntry', []):
        lines.append(f"- {site.get('siteUrl')} | permission={site.get('permissionLevel')}")
    lines.append('')
    lines.append('## Sitemaps')
    if sitemaps.get('sitemap'):
        for sm in sitemaps['sitemap']:
            lines.append(
                f"- {sm.get('path')} | pending={sm.get('isPending')} | warnings={sm.get('warnings')} | errors={sm.get('errors')} | lastSubmitted={sm.get('lastSubmitted')}"
            )
    else:
        lines.append('- No sitemaps returned')
    lines.append('')
    (OUTPUT_DIR / 'baseline.md').write_text('\n'.join(lines))
    print((OUTPUT_DIR / 'baseline.md').read_text())


if __name__ == '__main__':
    main()
