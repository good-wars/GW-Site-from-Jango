import os
import markdown as md
import re
import asyncio

folder_md = 'mdnews/'
output_folder = 'templates/news/content/news/'

os.makedirs(output_folder, exist_ok=True)

md_files = [f for f in os.listdir(folder_md) if f.endswith('.md')]

async def add_id_to_h2(html_content):
    def replace_h2(match):
        h2_content = match.group(1)
        id_value = re.sub(r'\W+', '_', h2_content.lower())
        return f'<h2 id="{id_value}">{h2_content}</h2>'
   
    return re.sub(r'<h2>(.*?)</h2>', replace_h2, html_content)

async def convert_files():
    for md_file in md_files:
        input_file = os.path.join(folder_md, md_file)
        output_file = os.path.join(output_folder, os.path.splitext(md_file)[0] + '.html')
       
        with open(input_file, 'r', encoding='utf8') as f:
            md_content = f.read()
       
        html_content = md.markdown(md_content)
        html_content = await add_id_to_h2(html_content)
       
        template = f"""
{{% extends "news/content/news/news_example.html" %}}

{{% block title %}}Новости{{% endblock %}}

{{% block content %}}
{html_content}
{{% endblock %}}
"""
       
        with open(output_file, 'w', encoding='utf8') as f:
            f.write(template)

    print("Конвертация завершена.")

async def start():
    while True:
        await convert_files()
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(start())
