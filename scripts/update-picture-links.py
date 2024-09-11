import re
import os
import argparse

def replace_articles_with_links(md_content, dir):
    pattern = r'\[\[([a-zA-Z]+)\]\]'
    def replace(match):
        print(f"match article: {match}")
        article_name = match.group(1)
        article_path = os.path.join(dir, article_name) + ".md"
        if os.path.exists(article_path):
            return f'[{article_name}](./{article_name})'
        else:
            print(f"Article not found: {article_path}")
            return match.group(0)
    updated_content = re.sub(pattern, replace, md_content)
    return updated_content

def replace_images_with_links(md_content, image_dir):
    """
    Replace Obsidian image links with HTML image tags.
    :param md_content: Content of the markdown file as a string.
    :param image_dir: Directory where images are stored.
    :return: Updated markdown content with HTML image tags.
    """
    pattern = r'!\[\[(Pasted image \d{14}\.(png|jpg))\]\]'
    def replace(match):
        print(f"match image: {match}")
        image_name = match.group(1)
        image_path = os.path.join(image_dir, image_name)
        if os.path.exists(image_path):
            return f'![](./{image_name})'
        else:
            print(f"Image not found: {image_path}")
            return match.group(0)
    updated_content = re.sub(pattern, replace, md_content)
    return updated_content

def main():
    parser = argparse.ArgumentParser(description='Replace Obsidian image links with HTML image tags.')
    parser.add_argument('markdown_file_path', type=str, help='Path to the markdown file.')
    parser.add_argument('image_directory', type=str, help='Directory where the images are stored.')
    
    args = parser.parse_args()
    
    with open(args.markdown_file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    updated_md_content = replace_images_with_links(md_content, args.image_directory)
    updated_md_content = replace_articles_with_links(updated_md_content, args.image_directory)
    
    with open(args.markdown_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_md_content)
    
    print(f"Images have been replaced with links: {args.markdown_file_path}")

if __name__ == "__main__":
    main()