# Input and output path
import re
import os
import html
from datetime import datetime

SQL_FILE = "/Users/ilya/Downloads/vs3net-20251030145622/database.sql"
OUTPUT_DIR = "/Users/ilya/code/ivoytov-blog/src/content/blog"
POST_TYPE = "article"  # change to "post" for blog posts

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Extract INSERT blocks from SQL
with open(SQL_FILE, "r", encoding="utf-8", errors="ignore") as f:
    sql = f.read()

insert_blocks = re.findall(
    r"INSERT INTO [`\"]?wp_\d*_posts[`\"]?.*?VALUES\s*(.*?);", sql, re.DOTALL
)

entries = []

for block in insert_blocks:
    # Split block into value tuples
    for match in re.finditer(r"\((.*?)\)(?:,|$)", block, re.DOTALL):
        raw = match.group(1)

        # Split respecting quoted commas
        parts = re.findall(r"'((?:[^'\\]|\\.)*)'|([^,]+)", raw)
        values = [html.unescape(a or b or "") for a, b in parts]

        if len(values) < 22:
            continue

        try:
            (
                ID,
                post_author,
                post_date,
                post_date_gmt,
                post_content,
                post_title,
                post_excerpt,
                post_status,
                comment_status,
                ping_status,
                post_password,
                post_name,
                to_ping,
                pinged,
                post_modified,
                post_modified_gmt,
                post_content_filtered,
                post_parent,
                guid,
                menu_order,
                post_type,
                post_mime_type,
                comment_count,
            ) = values[:23]
        except ValueError:
            continue


        entries.append(
            {
                "id": ID,
                "name": post_name or f"id_{ID}",
                "title": post_title.strip(),
                "content": post_content.strip(),
                "modified": post_modified or post_date,
            }
        )

# Keep latest version per post_name
final_entries = {}
for e in entries:
    key = e["name"]
    # dt = datetime.fromisoformat(e["modified"]) if e["modified"] else datetime.min
    # if key not in final_entries or dt > datetime.fromisoformat(final_entries[key]["modified"]):
    final_entries[key] = e

# Write to Markdown
for idx, e in enumerate(final_entries.values()):
    filename = f"post_{idx}"
    path = os.path.join(OUTPUT_DIR, f"{filename}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {e['title']}\n\n{e['content']}")

print(f"✅ Exported {len(final_entries)} {POST_TYPE}s to '{OUTPUT_DIR}/'")