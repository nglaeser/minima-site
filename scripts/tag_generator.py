#!/usr/bin/env python

'''
tag_generator.py

Copyright 2017 Long Qian
Contact: lqian8@jhu.edu

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.

--------------------
Updated November 2019 Noemi Glaeser
Changelist:
    Collect tag languages
    Keep list of tag_name and tag_lang in _data/tags.yml

usage note by nglaeser:
    run this script from the root project directory
    lang must always be listed before tags in _posts/*.md
'''

import glob
import os

post_dir = '_posts/'
tag_dir = 'tag/'
tag_data_filename = '_data/tags.yml'

filenames = glob.glob(post_dir + '*md')

# list of tuples (tag, lang)
total_tags = list()
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'lang:':
                # assumes only one language per post
                language = current_tags[1]
            if current_tags[0] == 'tags:':
                new_tags = current_tags[1:]
                for tag in new_tags:
                    data = (tag, language)
                    total_tags.append(data)
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

# remove all existing tag files
old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

# remove existing tag data file, if present
old_tag_data = glob.glob(tag_data_filename)
for df in old_tag_data:
    os.remove(df)

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_name = tag[0]
    language = tag[1]

    # create tag file
    tag_filename = tag_dir + tag_name + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag_name + '\"\nlang: ' + language + '\ntag: ' + tag_name + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()

    # add tag to tag data file
    f = open(tag_data_filename, 'a')
    write_str = '- tag_name: ' + tag_name + '\n  tag_lang: ' + language + '\n'
    f.write(write_str)
    f.close()

print("Tags generated, count", total_tags.__len__())
