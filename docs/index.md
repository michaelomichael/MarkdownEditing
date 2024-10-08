# MarkdownEditing

**Markdown plugin for Sublime Text**

![MarkdownEditing][preview]

with...

*   useful Markdown editing features for Sublime Text
*   color schemes optimized for writing
*   robust syntax definitions for
    *   Standard Markdown
    *   Github flavoured Markdown
    *   MultiMarkdown

ⓘ _See [configuration][] section to learn how to change the color scheme_.

!!!note "Most features are available through Command Palette."

    1.   Open Command Palette <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>P</kbd> (Windows, Linux) 
         or <kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> (on Mac)
    2.   Type `MarkdownEditing:` to display a list of available commands.

    ⓘ _They are only visible if a markdown file is open and focused._

## Features

### Folding and Navigation

*   displays headings in _Goto Symbol..._
*   displays headings in _Goto Symbol in Project..._
*   fold current section
*   fold by heading levels
*   navigate between adjacent headings with `Find Next/Previous Heading` command.

### Headings

*   automatic detection and maintenance of open or closed [atx headings][AtxHeadings] style while typing
*   change [headings levels][HeadingsLevels] via key bindings
*   auto-complete [Setext-style headings][SeHeadings] underlines
*   convert [Setext-style headings][SeHeadings] to ATX headings
*   new documents are named automatically based on first header

### Lists

*   At the end of a list item, pressing <kbd>Enter</kbd> will automatically insert the new list item bullet.
*   Pressing <kbd>Tab</kbd> on the blank list item will indent it and switch the list bullet to another one (Order is `*`, `-`, `+` in a cycle).
*   Pressing <kbd>Shift</kbd> + <kbd>Tab</kbd> on the blank list item will unindent it in the same way as above.
*   Sequential <kbd>Tab</kbd> s or <kbd>Shift</kbd> <kbd>Tab</kbd> s are supported.
*   You can disable automatic bullet switching or choose which bullets to be used, in your settings file (`mde.list_indent_bullets`).
*   If a list item contains a [GFM Task][], pressing 
    - <kbd>Enter</kbd> at the end of the line continues with a new blank task.
    - <kbd>Alt+X</kbd> in the line toggles the check mark.

### Blockquotes

*   At the end of a blockquote line, pressing <kbd>Enter</kbd> will automatically extend blockquote.
*   Selecting some text and pressing <kbd>&gt;</kbd> will convert it to blockquote. The first and the last line don't have to be fully selected; partial select works, too.

### Critic Markup

*   Syntax highlighting for inline critic markup
    -   `{++ addition ++}`
    -   `{>> comment <<}`
    -   `{-- deletion --}`
    -   `{== highlight==}{>> comment <<}`
    -   `{~~ substitution ~> by ~~}`
*   Reviewers can add critic via key bindings
*   Authors can accept or reject critic via key bindings

### Links and References

*   Left bracket pairing is modified to eliminate the selection and leave the cursor at a point where you can insert a `[]` or `()` pair for a link.
*   URL part of images, links and references is automatically folded if caret is not within brackets
*   Convert inline links to references
*   Jump between definitions and references
*   Organize references
*   Add or remove footnotes

### Text Formatting

*   Asterisks (<kbd>\*</kbd>), backticks (<kbd>\`</kbd>) and underscores (<kbd>\_</kbd>) are auto-paired and wrap selected text
*   <kbd>~</kbd> wraps selected text with `~~` (strike-through)
*   <kbd>Backspace</kbd> deletes an empty pair
*   <kbd>Space</kbd> or <kbd>Tab</kbd> deletes right element of empty pair of asterisks or underscores


[preview]: img/preview.png
[configuration]: config.md#change-color-scheme
[AtxHeadings]: usage.md#atx-style
[HeadingsLevels]: usage.md#headings-levels
[SeHeadings]: usage.md#setext-style
[GFM Task]: https://github.github.com/gfm/#task-list-items-extension-
