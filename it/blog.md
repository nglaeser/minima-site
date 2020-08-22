---
layout: default
title: Blog
ref: blog
lang: it
order: 5
---

<div class="home">

  <div class="column-left">
      <ul class="post-list">
        {% assign posts=site.posts | where:"lang", page.lang %}
        {% for post in posts %}
          <li>
            <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

            <h2>
              <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
            </h2>
          </li>
        {% endfor %}
      </ul>

      <p class="rss-subscribe">Abbonarsi al <a href="{{ "/flux.xml" | prepend: site.baseurl }}">Feed RSS</a></p>
  </div>
  <div class="column-right">
      <ul>
          <h4>Tags:</h4>
          {% for tag in site.data.tags %}
            {% if tag.tag_name != "" and tag.tag_lang == page.lang %}
              <li>
                  <a href="{{ site.baseurl }}/tag/{{ tag.tag_name }}"><code class="highligher-rouge"><nobr>{{ tag.tag_name }}</nobr></code></a>&nbsp;
              </li>
            {% endif %}
          {% endfor %}
      </ul>
  </div>

</div>
