---
layout: page
title: 이벤트
permalink: /Event/
---

<ul>
    {% assign sortedpost = site.posts | sort %}
    {%- for post in sortedpost -%}
    {%- if post.categories contains "Event" -%}
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