---
layout: page
title: 페이트
permalink: /Fate/
---

<ul>
    {% assign sortedpost = site.posts | sort %}
    {%- for post in sortedpost -%}
    {%- if post.categories contains "Fate" -%}
    <li>
    {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
    <!-- <span class="post-meta">{{ post.date | date: date_format }}</span> -->
    <!-- <h3> -->
        <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
    <!-- </h3> -->
    {%- if site.show_excerpts -%}
        {{ post.excerpt }}
    {%- endif -%}
    </li>
    {%- endif -%}
    {%- endfor -%}
    
</ul>