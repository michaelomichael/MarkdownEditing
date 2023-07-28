| SYNTAX TEST "Packages/MarkdownEditing/syntaxes/Morkdown.sublime-syntax"

# TEST: Tabs ##################################################################

## https://spec.commonmark.org/0.30/#example-4

  - foo

	bar
| <- markup.list.unnumbered.markdown.morkdown
|^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-6

>		foo
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^ markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown
| MO: Removed indented raw blocks 

## https://spec.commonmark.org/0.30/#example-7

-		foo
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown


## https://spec.commonmark.org/0.30/#example-8

    foo
	bar
| <- meta.paragraph.markdown.morkdown
|^^^^ meta.paragraph.markdown.morkdown
| MO: Removed indented raw blocks

## https://spec.commonmark.org/0.30/#example-9

 - foo
   - bar
	 - baz
|^ markup.list.unnumbered.markdown.morkdown
| ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|   ^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-10

#	Foo
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^ markup.heading.1.markdown.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-11

*	*	*	
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^ meta.separator.thematic-break.markdown.morkdown
| ^ punctuation.definition.thematic-break.markdown.morkdown
|   ^ punctuation.definition.thematic-break.markdown.morkdown

-	-	-	
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^ meta.separator.thematic-break.markdown.morkdown
| ^ punctuation.definition.thematic-break.markdown.morkdown
|   ^ punctuation.definition.thematic-break.markdown.morkdown

_	_	_	
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^ meta.separator.thematic-break.markdown.morkdown
| ^ punctuation.definition.thematic-break.markdown.morkdown
|   ^ punctuation.definition.thematic-break.markdown.morkdown


# TEST: LIGATURES #############################################################

this is a raw ampersand & does not require HTML escaping
|                       ^ - entity - illegal

this is a raw bracket < > does not require HTML escaping
|                     ^^^ - meta.tag - punctuation

these are raw ligatures << <<< <<<< <<<<< >>>>> >>>> >>> >>
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures <- <-- <--- <---- <-< <--< <---< <----<
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures -> --> ---> ----> >-> >--> >---> >---->
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures >- >-- >--- >---- ----< ---< --< -<
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures >< >-< >--< >---< <---> <--> <-> <>
|                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures <= <== <=== <==== <=< <==< <===< <====<
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures => ==> ===> ====> >=> >==> >===> >====>
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures >= >== >=== >==== ====< ===< ==< =<
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures >< >=< >==< >===< <===> <==> <=> <>
|                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures - -- --- ---- ----- ===== ==== === == =
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

-= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  - constant - keyword - variable

    -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
|   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  - constant - keyword - variable - punctuation
| MO: Removed indented raw blocks

>  -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - constant - keyword - variable

> > -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^ markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - constant - keyword - variable


# TEST: BACKSLASH ESCAPES #####################################################

## https://spec.commonmark.org/0.30/#example-12

\!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~
| <- constant.character.escape.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ constant.character.escape.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-13

\	\A\a\ \3\φ\«
| <- - constant.character.escape
|^^^^^^^^^^^^^ - constant.character.escape

## https://spec.commonmark.org/0.30/#example-14

\*not emphasized*
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown
|^^^^^^^^^^^^^^^^ - markup.italic

\<br/> not a tag
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown
|^^^^^ - markup.tag

\<br/\> not a tag
| <- constant.character.escape.markdown.morkdown
|^^^^^^ - meta.tag
|    ^^ constant.character.escape

\[not a link](/foo)
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown
|^^^^^^^^^^^^^^^^^^ - markup.link

\`not code`
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown
|^^^^^^^^^ - markup.raw

1\. not a list
|^^ constant.character.escape.markdown.morkdown
|^^^^^^^^^^^^^ - markup.list

\* not a list
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown
|^^^^^^^^^^^^ - markup.list

\# not a heading
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown
|^^^^^^^^^^^^^^^ - markup.heading

\[foo]: /url "not a reference"
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.link

\&ouml; not a character entity
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown
|^^^^^^ - entity

\~/.bashrc
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-15

\\*emphasis*
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown
| ^^^^^^^^^^ markup.italic.markdown.morkdown

\\_emphasis_
| <- constant.character.escape.markdown.morkdown
|^ constant.character.escape.markdown.morkdown
| ^^^^^^^^^^ markup.italic.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-16

foo\
|  ^ meta.hard-line-break.markdown.morkdown constant.character.escape.markdown.morkdown
|   ^ meta.hard-line-break.markdown.morkdown - constant
bar

## https://spec.commonmark.org/0.30/#example-17

`` \[\` ``
|^^^^^^^^^ markup.raw.inline.markdown.morkdown - constant.character.escape

## https://spec.commonmark.org/0.30/#example-19

~~~
\[\]
|^^^^ markup.raw.code-fence.markdown-gfm.morkdown - constant.character.escape
~~~

## https://spec.commonmark.org/0.30/#example-20

<http://example.com?find=\*>
|                        ^^ - constant.character.escape

## https://spec.commonmark.org/0.30/#example-21

<a href="/bar\/)">
|            ^^ - constant.character.escape

## https://spec.commonmark.org/0.30/#example-22

[foo](/bar\* "ti\*tle")
|         ^^ markup.underline.link.markdown.morkdown constant.character.escape
|               ^^ constant.character.escape

## https://spec.commonmark.org/0.30/#example-23

[foo]

[foo]: /bar\* "ti\*tle"
|          ^^ markup.underline.link.markdown.morkdown constant.character.escape
|                ^^ constant.character.escape

## https://spec.commonmark.org/0.30/#example-24

Note: current design doesn't support highlighting escapes in info strings
``` foo\+bar
|      ^^ - constant.character.escape
foo
```


# TEST: HTML ENTITIES #########################################################

## https://spec.commonmark.org/0.30/#example-25

  &nbsp; &amp; &copy; &AElig; &Dcaron;
| ^^^^^^ constant.character.entity.named.html
|       ^ - constant
|        ^^^^^ constant.character.entity.named.html
|             ^ - constant
|              ^^^^^^ constant.character.entity.named.html
|                    ^ - constant
|                     ^^^^^^^ constant.character.entity.named.html
|                            ^ - constant
|                             ^^^^^^^^ constant.character.entity.named.html
|                                     ^ - constant
  
  &frac34; &HilbertSpace; &DifferentialD;
| ^^^^^^^^ constant.character.entity.named.html
|         ^ - constant
|          ^^^^^^^^^^^^^^ constant.character.entity.named.html
|                        ^ - constant
|                         ^^^^^^^^^^^^^^^ constant.character.entity.named.html
|                                        ^ - constant

  &ClockwiseContourIntegral; &ngE;
| ^^^^^^^^^^^^^^^^^^^^^^^^^^ constant.character.entity.named.html
|                           ^ - constant
|                            ^^^^^ constant.character.entity.named.html
|                                 ^ - constant

## https://spec.commonmark.org/0.30/#example-26

  &#35; &#1234; &#992; &#0;
| ^^^^^ constant.character.entity.decimal.html
|      ^ - constant
|       ^^^^^^^ constant.character.entity.decimal.html
|              ^ - constant
|               ^^^^^^ constant.character.entity.decimal.html
|                     ^ - constant
|                      ^^^^ constant.character.entity.decimal.html
|                          ^ - constant

## https://spec.commonmark.org/0.30/#example-27

  &#X22; &#XD06; &#xcab;
| ^^^^^^ constant.character.entity.hexadecimal.html
|       ^ - constant
|        ^^^^^^^ constant.character.entity.hexadecimal.html
|               ^ - constant
|                ^^^^^^^ constant.character.entity.hexadecimal.html
|                       ^ - constant

## https://spec.commonmark.org/0.30/#example-28

  &
| ^ - constant - invalid

  &nbsp &x; &#; &#x;
| ^^^^^^ - constant
|       ^^^ constant.character.entity.named.html
|          ^^^^^^^^^ - constant

  &#87654321;

  &#abcdef0;
| ^^^^^^^^^^ - constant

  &hi?;
| ^^^^^ - constant

Note: ST's HTML or Markdown don't maintain a full list of valid html5 entities
      for simplicity reasons and therefore invalid entities are highlighted.

## https://spec.commonmark.org/0.30/#example-29

Although HTML5 does accept some entity references without a trailing semicolon
(such as &copy), these are not recognized here, because it makes the grammar
too ambiguous:

  &copy
| ^^^^^ - constant

## https://spec.commonmark.org/0.30/#example-30

Strings that are not on the list of HTML5 named entities are not recognized as
entity references either:

  &MadeUpEntity;
| ^^^^^^^^^^^^^^ constant.character.entity.named.html

Note: ST's HTML or Markdown don't maintain a full list of valid html5 entities
      for simplicity reasons and therefore invalid entities are highlighted.

## https://spec.commonmark.org/0.30/#example-31

<a href="&ouml;&ouml;.html">
|        ^^^^^^^^^^^^ constant.character.entity.named.html

## https://spec.commonmark.org/0.30/#example-32

[foo](/f&ouml;&ouml; "f&ouml;&ouml;")
|       ^^^^^^^^^^^^ constant.character.entity.named.html
|                      ^^^^^^^^^^^^ constant.character.entity.named.html

## https://spec.commonmark.org/0.30/#example-33

[foo]

[foo]: /f&ouml;&ouml; "f&ouml;&ouml;"
|        ^^^^^^^^^^^^ constant.character.entity.named.html
|                       ^^^^^^^^^^^^ constant.character.entity.named.html

## https://spec.commonmark.org/0.30/#example-34

``` f&ouml;&ouml;
foo
```
Note: current design doesn't support highlighting entities in info strings

## https://spec.commonmark.org/0.30/#example-35

`f&ouml;&ouml;`
|^^^^^^^^^^^^^ - constant.character.entity

## https://spec.commonmark.org/0.30/#example-37

&#42;foo&#42;
| <- meta.paragraph.markdown.morkdown constant.character.entity.decimal.html
|^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - markup.italic
|^^^^ constant.character.entity.decimal.html
|       ^^^^^ constant.character.entity.decimal.html

*foo*
| <- meta.paragraph.markdown.morkdown markup.italic.markdown.morkdown
|^^^^ meta.paragraph.markdown.morkdown markup.italic.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-38

&#42; foo
| <- meta.paragraph.markdown.morkdown constant.character.entity.decimal.html
|^^^^^^^^^ meta.paragraph.markdown.morkdown
|^^^^ constant.character.entity.decimal.html

* foo
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-39

foo&#10;&#10;bar
| <- meta.paragraph.markdown.morkdown
|^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown
|  ^^^^^^^^^^ constant.character.entity.decimal.html

## https://spec.commonmark.org/0.30/#example-40

&#9;foo
| <- meta.paragraph.markdown.morkdown constant.character.entity.decimal.html
|^^^ meta.paragraph.markdown.morkdown constant.character.entity.decimal.html
|   ^^^^ meta.paragraph.markdown.morkdown - constant

## https://spec.commonmark.org/0.30/#example-41

[a](url &quot;tit&quot;)
|       ^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - meta.link
|       ^^^^^^ constant.character.entity.named.html
|             ^^^ - constant
|                ^^^^^^ constant.character.entity.named.html


# TEST: THEMATIC BREAKS #######################################################

## https://spec.commonmark.org/0.30/#example-43

***
|^^^ meta.separator.thematic-break.markdown.morkdown
|^^ punctuation.definition.thematic-break.markdown.morkdown

---
|^^^ meta.separator.thematic-break.markdown.morkdown
|^^ punctuation.definition.thematic-break.markdown.morkdown

___
|^^^ meta.separator.thematic-break.markdown.morkdown
|^^ punctuation.definition.thematic-break.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-44

+++
| <- - meta.separator
|^^^ - meta.separator

## https://spec.commonmark.org/0.30/#example-45

===
| <- - meta.separator
|^^^ - meta.separator

## https://spec.commonmark.org/0.30/#example-46

**
| <- - meta.separator
|^ - meta.separator

--
| <- - meta.separator
|^ - meta.separator

__
| <- - meta.separator
|^ - meta.separator

## https://spec.commonmark.org/0.30/#example-47

 ***
|<- meta.separator.thematic-break.markdown.morkdown - punctuation
|^^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown

  ***
|<- meta.separator.thematic-break.markdown.morkdown - punctuation
|^ meta.separator.thematic-break.markdown.morkdown - punctuation
| ^^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown

   ***
|<- meta.separator.thematic-break.markdown.morkdown - punctuation
|^^ meta.separator.thematic-break.markdown.morkdown - punctuation
|  ^^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-48

    ***
|<- meta.separator.thematic-break.markdown.morkdown - punctuation
|^^^ meta.separator.thematic-break.markdown.morkdown - punctuation
|   ^^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
| MO: Removed indented raw blocks

## https://spec.commonmark.org/0.30/#example-49

Foo
    ***
| <- meta.separator.thematic-break.markdown.morkdown
|^^^^^^^ meta.separator.thematic-break.markdown.morkdown
| MO: Removed indented raw blocks

## https://spec.commonmark.org/0.30/#example-50

**************************************
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown

--------------------------------------
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown

_____________________________________
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-51

 * * *
| <- meta.separator.thematic-break.markdown.morkdown - punctuation
|^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^ punctuation.definition.thematic-break.markdown.morkdown
| ^ - punctuation
|  ^ punctuation.definition.thematic-break.markdown.morkdown
|   ^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown.morkdown
|     ^ - punctuation

 - - -
| <- meta.separator.thematic-break.markdown.morkdown - punctuation
|^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^ punctuation.definition.thematic-break.markdown.morkdown
| ^ - punctuation
|  ^ punctuation.definition.thematic-break.markdown.morkdown
|   ^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown.morkdown
|     ^ - punctuation

 _ _ _
| <- meta.separator.thematic-break.markdown.morkdown - punctuation
|^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^ punctuation.definition.thematic-break.markdown.morkdown
| ^ - punctuation
|  ^ punctuation.definition.thematic-break.markdown.morkdown
|   ^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown.morkdown
|     ^ - punctuation

## https://spec.commonmark.org/0.30/#example-52

 **  * ** * ** * **
| <- meta.separator.thematic-break.markdown.morkdown - punctuation
|^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^^ punctuation.definition.thematic-break.markdown.morkdown
|  ^^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown.morkdown
|     ^ - punctuation
|      ^^ punctuation.definition.thematic-break.markdown.morkdown
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break.markdown.morkdown
|          ^ - punctuation
|           ^^ punctuation.definition.thematic-break.markdown.morkdown
|             ^ - punctuation
|              ^ punctuation.definition.thematic-break.markdown.morkdown
|               ^ - punctuation
|                ^^ punctuation.definition.thematic-break.markdown.morkdown
|                  ^ - punctuation

 --  - -- - -- - --
| <- meta.separator.thematic-break.markdown.morkdown - punctuation
|^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^^ punctuation.definition.thematic-break.markdown.morkdown
|  ^^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown.morkdown
|     ^ - punctuation
|      ^^ punctuation.definition.thematic-break.markdown.morkdown
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break.markdown.morkdown
|          ^ - punctuation
|           ^^ punctuation.definition.thematic-break.markdown.morkdown
|             ^ - punctuation
|              ^ punctuation.definition.thematic-break.markdown.morkdown
|               ^ - punctuation
|                ^^ punctuation.definition.thematic-break.markdown.morkdown
|                  ^ - punctuation

 __  _ __ _ __ _ __
| <- meta.separator.thematic-break.markdown.morkdown - punctuation
|^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^^ punctuation.definition.thematic-break.markdown.morkdown
|  ^^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown.morkdown
|     ^ - punctuation
|      ^^ punctuation.definition.thematic-break.markdown.morkdown
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break.markdown.morkdown
|          ^ - punctuation
|           ^^ punctuation.definition.thematic-break.markdown.morkdown
|             ^ - punctuation
|              ^ punctuation.definition.thematic-break.markdown.morkdown
|               ^ - punctuation
|                ^^ punctuation.definition.thematic-break.markdown.morkdown
|                  ^ - punctuation

## https://spec.commonmark.org/0.30/#example-53

*     *      *      *
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^^^^^ - punctuation
|     ^ punctuation.definition.thematic-break.markdown.morkdown 
|      ^^^^^^ - punctuation
|            ^ punctuation.definition.thematic-break.markdown.morkdown 
|             ^^^^^^ - punctuation
|                   ^ punctuation.definition.thematic-break.markdown.morkdown 
|                    ^ - punctuation

-     -      -      -
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^^^^^ - punctuation
|     ^ punctuation.definition.thematic-break.markdown.morkdown 
|      ^^^^^^ - punctuation
|            ^ punctuation.definition.thematic-break.markdown.morkdown 
|             ^^^^^^ - punctuation
|                   ^ punctuation.definition.thematic-break.markdown.morkdown 
|                    ^ - punctuation

_     _      _      _
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^^^^^ - punctuation
|     ^ punctuation.definition.thematic-break.markdown.morkdown 
|      ^^^^^^ - punctuation
|            ^ punctuation.definition.thematic-break.markdown.morkdown 
|             ^^^^^^ - punctuation
|                   ^ punctuation.definition.thematic-break.markdown.morkdown 
|                    ^ - punctuation

## https://spec.commonmark.org/0.30/#example-54

* * * *
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^ - punctuation
| ^ punctuation.definition.thematic-break
|  ^ - punctuation
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation

- - - -
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^ - punctuation
| ^ punctuation.definition.thematic-break
|  ^ - punctuation
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation

_ _ _ _
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^^^ meta.separator.thematic-break.markdown.morkdown
|^ - punctuation
| ^ punctuation.definition.thematic-break
|  ^ - punctuation
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation

## https://spec.commonmark.org/0.30/#example-55

_ _ _ _ a
| <- meta.paragraph.markdown.morkdown - meta.separator
|^^^^^^^^^ meta.paragraph.markdown.morkdown - meta.separator

a------
| <- meta.paragraph.markdown.morkdown - meta.separator
|^^^^^^^ meta.paragraph.markdown.morkdown - meta.separator

---a---
| <- meta.paragraph.markdown.morkdown - meta.separator
|^^^^^^^ meta.paragraph.markdown.morkdown - meta.separator

## https://spec.commonmark.org/0.30/#example-56

 *-*
| <- meta.paragraph.markdown.morkdown - meta.separator
|^^^ meta.paragraph.markdown.morkdown - meta.separator

## https://spec.commonmark.org/0.30/#example-57

- foo
***
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
- bar
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-58

Foo
***
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
bar
| <- meta.paragraph.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-59

Foo
---
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
bar
| <- meta.paragraph.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-60

* Foo
* * *
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^^^ meta.separator.thematic-break.markdown.morkdown
| ^ punctuation.definition.thematic-break.markdown.morkdown
|   ^ punctuation.definition.thematic-break.markdown.morkdown
* Bar
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-61

- Foo
- * * *
| ^^^^^^ markup.list.unnumbered.markdown.morkdown meta.separator.thematic-break.markdown.morkdown


# TEST: ATX HEADINGS ##########################################################

## https://spec.commonmark.org/0.30/#example-62

# foo
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^ markup.heading.1.markdown.morkdown - punctuation

## foo
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^ markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
| ^^^^^ markup.heading.2.markdown.morkdown - punctuation

### foo
| <- markup.heading.3.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^ markup.heading.3.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|  ^^^^^ markup.heading.3.markdown.morkdown - punctuation

#### foo
| <- markup.heading.4.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^ markup.heading.4.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|   ^^^^^ markup.heading.4.markdown.morkdown - punctuation

##### foo
| <- markup.heading.5.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^ markup.heading.5.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|    ^^^^^ markup.heading.5.markdown.morkdown - punctuation

###### foo
| <- markup.heading.6.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^ markup.heading.6.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|     ^^^^^ markup.heading.6.markdown.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-63

####### foo
| <- meta.paragraph.markdown.morkdown - markup.heading
|^^^^^^^^^^^ meta.paragraph.markdown.morkdown - markup.heading

## https://spec.commonmark.org/0.30/#example-64

#5 bolt
| <- meta.paragraph.markdown.morkdown - markup.heading
|^^^^^^^ meta.paragraph.markdown.morkdown - markup.heading

#hashtag
| <- meta.paragraph.markdown.morkdown - markup.heading
|^^^^^^^^ meta.paragraph.markdown.morkdown - markup.heading

## https://spec.commonmark.org/0.30/#example-65

\## foo
| <- meta.paragraph.markdown.morkdown constant.character.escape.markdown.morkdown - markup
|^ meta.paragraph.markdown.morkdown constant.character.escape.markdown.morkdown - markup
| ^^^^^^ meta.paragraph.markdown.morkdown - constant - markup

## https://spec.commonmark.org/0.30/#example-66

# foo *bar* \*baz\*
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^ markup.heading.1.markdown.morkdown - entity.name - markup.italic
| ^^^^ markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown - markup.italic
|     ^^^^^ markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown markup.italic.markdown.morkdown
|          ^^^^^^^^ markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown - markup.italic

## https://spec.commonmark.org/0.30/#example-67

#                  foo                     
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^ markup.heading.1.markdown.morkdown - entity.name
|                  ^^^ markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown
|                     ^^^^^^^^^^^^^^^^^^^^^^ markup.heading.1.markdown.morkdown - entity.name

## https://spec.commonmark.org/0.30/#example-68

 ### foo
| <- markup.heading.3.markdown.morkdown
|^^^^^^^^ markup.heading.3.markdown.morkdown 
  ## foo
| <- markup.heading.2.markdown.morkdown
|^^^^^^^^ markup.heading.2.markdown.morkdown  
   # foo
| <- markup.heading.1.markdown.morkdown
|^^^^^^^^ markup.heading.1.markdown.morkdown   
          # foo
| <- markup.heading.1.markdown.morkdown
|^^^^^^^^^ markup.heading.1.markdown.morkdown   

## https://spec.commonmark.org/0.30/#example-69

    # foo
| <- markup.heading.1.markdown.morkdown - meta.paragraph.markdown.morkdown
|^^^^^^^^^ markup.heading.1.markdown.morkdown - meta.paragraph.markdown.morkdown
| MO: Removed indented raw code blocks

## https://spec.commonmark.org/0.30/#example-70

foo
    # bar
| <- markup.heading.1.markdown.morkdown - meta.paragraph.markdown.morkdown
|^^^^^^^^^ markup.heading.1.markdown.morkdown - meta.paragraph.markdown.morkdown
| MO: TODO: It would be nice if this was just treated as a paragraph

## https://spec.commonmark.org/0.30/#example-71

## foo ##
  ###   bar    ###
| <- markup.heading.3.markdown.morkdown
|^^^^^^^^^^^^^^^^^^ markup.heading.3.markdown.morkdown
| ^^^ punctuation.definition.heading.begin.markdown.morkdown
|    ^^^ - entity - punctuation 
|       ^^^ entity.name.section.markdown.morkdown
|          ^^^^ - entity - punctuation 
|              ^^^ punctuation.definition.heading.end.markdown.morkdown
|                 ^ - punctuation 

## https://spec.commonmark.org/0.30/#example-72

# foo ##################################
##### foo ##
| <- markup.heading.5.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^^^^^ markup.heading.5.markdown.morkdown
|^^^^ punctuation.definition.heading.begin.markdown.morkdown
|    ^ - entity - punctuation 
|     ^^^ entity.name.section.markdown.morkdown
|        ^ - entity - punctuation 
|         ^^ punctuation.definition.heading.end.markdown.morkdown
|           ^ - punctuation 

## https://spec.commonmark.org/0.30/#example-73

### foo ###     
| <- markup.heading.3.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^ markup.heading.3.markdown.morkdown
|^^ punctuation.definition.heading.begin.markdown.morkdown
|  ^ - entity - punctuation 
|   ^^^ entity.name.section.markdown.morkdown
|      ^ - entity - punctuation 
|       ^^^ punctuation.definition.heading.end.markdown.morkdown
|          ^^^^^^ - punctuation 

## https://spec.commonmark.org/0.30/#example-74

### foo ### b
| <- markup.heading.3.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^^^^^^ markup.heading.3.markdown.morkdown
|^^ punctuation.definition.heading.begin.markdown.morkdown
|  ^ - entity - punctuation 
|   ^^^^^^^^^ entity.name.section.markdown.morkdown
|            ^ - entity

## https://spec.commonmark.org/0.30/#example-75

# foo#
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^ markup.heading.1.markdown.morkdown
|^ - entity - punctuation 
| ^^^^ entity.name.section.markdown.morkdown
|     ^ - entity

# foo# #
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^ markup.heading.1.markdown.morkdown
|^ - entity - punctuation 
| ^^^^ entity.name.section.markdown.morkdown
|     ^ - entity - punctuation 
|      ^ punctuation.definition.heading.end.markdown.morkdown
|       ^ - punctuation

## https://spec.commonmark.org/0.30/#example-76

### foo \###
| <- markup.heading.3.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^^^^^ markup.heading.3.markdown.morkdown
|^^ punctuation.definition.heading.begin.markdown.morkdown
|   ^^^^^^^^ entity.name.section.markdown.morkdown
|       ^^ constant.character.escape.markdown.morkdown
|           ^ - constant - entity - punctuation

## foo #\##
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^^^^ markup.heading.2.markdown.morkdown
|^ punctuation.definition.heading.begin.markdown.morkdown
|  ^^^^^^^^ entity.name.section.markdown.morkdown
|       ^^ constant.character.escape.markdown.morkdown
|          ^ - constant - entity - punctuation

# foo \#
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^ markup.heading.1.markdown.morkdown
| ^^^^^^ entity.name.section.markdown.morkdown
|     ^^ constant.character.escape.markdown.morkdown
|       ^ - constant - entity - punctuation

## https://spec.commonmark.org/0.30/#example-77

****
## foo
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^ markup.heading.2.markdown.morkdown

****
## foo
****
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-78

Foo bar
# baz
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^ markup.heading.1.markdown.morkdown

Foo bar
# baz
Bar foo
| <- meta.paragraph.markdown.morkdown - markup.heading
|^^^^^^^ meta.paragraph.markdown.morkdown - markup.heading

Foo **bar
# baz
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown - markup.bold
|^^^^^ markup.heading.1.markdown.morkdown
this must not be bold**
| <- - meta.bold
|^^^^^^^^^^^^^^^^^^^^^^ - meta.bold

Foo *bar
# baz
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown - markup.italic
|^^^^ markup.heading.1.markdown.morkdown
this must not be italic*
| <- - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.italic

Foo ***bar
# baz
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown - markup.bold - markup.italic
|^^^^^ markup.heading.1.markdown.morkdown
this must not be bold italic***
| <- - meta.bold - markup.italic
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - markup.italic

## https://spec.commonmark.org/0.30/#example-79

#
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown

# #
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^ markup.heading.1.markdown.morkdown - entity.name.section
| ^ punctuation.definition.heading.end.markdown.morkdown

## 
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown - entity.name.section
|^ markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown - entity.name.section

## ##
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown - entity.name.section
|^^^^^ markup.heading.2.markdown.morkdown - entity.name.section
|^ punctuation.definition.heading.begin.markdown.morkdown
|  ^^ punctuation.definition.heading.end.markdown.morkdown

### ###
| <- markup.heading.3.markdown.morkdown  - entity.name.sectionpunctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^ markup.heading.3.markdown.morkdown - entity.name.section
|^^ punctuation.definition.heading.begin.markdown.morkdown
|   ^^^ punctuation.definition.heading.end.markdown.morkdown

# #### #
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^ markup.heading.1.markdown.morkdown
|^ - entity.name.section
| ^^^^ entity.name.section.markdown.morkdown
|     ^^ - entity.name.section
|      ^ punctuation.definition.heading.end.markdown.morkdown

## #### ##
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^^^ markup.heading.2.markdown.morkdown
|^ - entity.name.section
|  ^^^^ entity.name.section.markdown.morkdown
|      ^^^ - entity.name.section
|       ^^ punctuation.definition.heading.end.markdown.morkdown


# TEST: SETEXT HEADINGS #######################################################

SETEXT Heading Level 1
| <- markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown
=================
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^^^^^^^^^^^^^^ markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|                ^ markup.heading.1.markdown.morkdown meta.whitespace.newline.markdown.morkdown

SETEXT Heading Level 2
| <- markup.heading.2.markdown.morkdown entity.name.section.markdown.morkdown
------------------------------
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|                             ^ markup.heading.2.markdown.morkdown meta.whitespace.newline.markdown.morkdown - punctuation

underlined heading followed by a separator
-------------------
------
| <- meta.separator.thematic-break.markdown.morkdown - markup.heading

underlined heading followed by another one that should be treated as a normal paragraph
==================
=====
| <- meta.paragraph.markdown.morkdown - markup.heading

https://spec.commonmark.org/0.30/#example-80

Foo *bar*
| <- markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown
|^^^^^^^^^ markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown
|   ^^^^^ markup.italic.markdown.morkdown
=========
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^^^^^^ markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|        ^ markup.heading.1.markdown.morkdown meta.whitespace.newline.markdown.morkdown

Foo *bar*
| <- markup.heading.2.markdown.morkdown entity.name.section.markdown.morkdown
|^^^^^^^^^ markup.heading.2.markdown.morkdown entity.name.section.markdown.morkdown
|   ^^^^^ markup.italic.markdown.morkdown
---------
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^^^^^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|        ^ markup.heading.2.markdown.morkdown meta.whitespace.newline.markdown.morkdown

Foo *bar
| <- markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown
|^^^^^^^^^ markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown
|   ^^^^^ markup.italic.markdown.morkdown
=========
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown - markup.italic
|^^^^^^^^ markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown - markup.italic
|        ^ markup.heading.1.markdown.morkdown meta.whitespace.newline.markdown.morkdown - markup.italic

Foo *bar
| <- markup.heading.2.markdown.morkdown entity.name.section.markdown.morkdown
|^^^^^^^^^ markup.heading.2.markdown.morkdown entity.name.section.markdown.morkdown
|   ^^^^^ markup.italic.markdown.morkdown
---------
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown - markup.italic
|^^^^^^^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown - markup.italic
|        ^ markup.heading.2.markdown.morkdown meta.whitespace.newline.markdown.morkdown - markup.italic

https://spec.commonmark.org/0.30/#example-81

Foo *bar
baz*
| <- markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown markup.italic.markdown.morkdown
|^^^ markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown markup.italic.markdown.morkdown
|   ^ markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown - markup.italic
====
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^ markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|   ^ markup.heading.1.markdown.morkdown meta.whitespace.newline.markdown.morkdown

https://spec.commonmark.org/0.30/#example-82

  Foo *bar
baz*  
| <- markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown markup.italic.markdown.morkdown
|^^^ markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown markup.italic.markdown.morkdown
|   ^^ markup.heading.1.markdown.morkdown entity.name.section.markdown.morkdown - markup.italic
====
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^ markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|   ^ markup.heading.1.markdown.morkdown meta.whitespace.newline.markdown.morkdown

https://spec.commonmark.org/0.30/#example-83

Foo
=
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^ markup.heading.1.markdown.morkdown meta.whitespace.newline.markdown.morkdown

Foo
-
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^ markup.heading.2.markdown.morkdown meta.whitespace.newline.markdown.morkdown

https://spec.commonmark.org/0.30/#example-84

   Foo
---
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|  ^ markup.heading.2.markdown.morkdown meta.whitespace.newline.markdown.morkdown

  Foo
-----
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|    ^ markup.heading.2.markdown.morkdown meta.whitespace.newline.markdown.morkdown

  Foo
  ===
| <- markup.heading.1.markdown.morkdown - punctuation
|^ markup.heading.1.markdown.morkdown - punctuation
| ^^^ markup.heading.1.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|    ^ markup.heading.1.markdown.morkdown meta.whitespace.newline.markdown.morkdown

https://spec.commonmark.org/0.30/#example-85

    Foo
    ---
| <- markup.heading.2.markdown.morkdown - punctuation
|^^^ markup.heading.2.markdown.morkdown - punctuation
|   ^^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|      ^ markup.heading.2.markdown.morkdown meta.whitespace.newline.markdown.morkdown
| MO: Removed indented raw code blocks

    Foo
| <- markup.heading.2.markdown.morkdown - entity - punctuation
|   ^^^ markup.heading.2.markdown.morkdown entity.name.section.markdown.morkdown - punctuation
| MO: It would be nice if we could check the _level_ of indentation, but we don't seem to be able to do that.
---
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|  ^ markup.heading.2.markdown.morkdown meta.whitespace.newline.markdown.morkdown

https://spec.commonmark.org/0.30/#example-86

Foo
   ----      
|^^^^^^^^^^^^^ markup.heading.2.markdown.morkdown
|^^ - punctuation
|  ^^^^ punctuation.definition.heading.setext.markdown.morkdown
|      ^^^^^^^ - punctuation
|            ^ meta.whitespace.newline.markdown.morkdown

https://spec.commonmark.org/0.30/#example-87

Foo
    ---
|^^^^^^ markup.heading.2.markdown.morkdown
|^^^ - punctuation
|   ^^^ punctuation.definition.heading.setext.markdown.morkdown
|      ^ meta.whitespace.newline.markdown.morkdown
| MO: It would be nice if we could check the _level_ of indentation, but sublime 
| won't let us do that reliably, so it's easier to just allow the setext heading here

https://spec.commonmark.org/0.30/#example-88

Foo
= =
| <- meta.paragraph.markdown.morkdown - markup.heading
|^^^ meta.paragraph.markdown.morkdown - markup.heading

Foo
--- -
| <- meta.separator.thematic-break.markdown.morkdown - markup.heading
|^^^^^ meta.separator.thematic-break.markdown.morkdown - markup.heading

https://spec.commonmark.org/0.30/#example-89

Foo  
|  ^^ markup.heading.2.markdown.morkdown entity.name.section.markdown.morkdown - meta.hard-line-break
-----
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown

https://spec.commonmark.org/0.30/#example-90

Foo\
|  ^ markup.heading.2.markdown.morkdown entity.name.section.markdown.morkdown - meta.hard-line-break
----
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown

https://spec.commonmark.org/0.30/#example-91

`Foo
----
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown

`Foo`
----
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown

https://spec.commonmark.org/0.30/#example-92

> Foo
---
| <- meta.separator.thematic-break.markdown.morkdown - markup.heading
|^^^ meta.separator.thematic-break.markdown.morkdown - markup.heading

https://spec.commonmark.org/0.30/#example-93

> foo
bar
===
| <- markup.quote.markdown.morkdown - markup.heading
|^^^ markup.quote.markdown.morkdown - markup.heading

https://spec.commonmark.org/0.30/#example-94
- Foo
---
| <- meta.separator.thematic-break.markdown.morkdown - markup.heading
|^^^ meta.separator.thematic-break.markdown.morkdown - markup.heading

https://spec.commonmark.org/0.30/#example-95

Foo
Bar
---
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown

https://spec.commonmark.org/0.30/#example-96

---
Foo
---
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown

---
Foo
---
Bar
---
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
Baz

---
Foo
---
Bar
---
Baz
| <- meta.paragraph.markdown.morkdown
|^^^ meta.paragraph.markdown.morkdown

https://spec.commonmark.org/0.30/#example-97

====
| <- meta.paragraph.markdown.morkdown
|^^^^ meta.paragraph.markdown.morkdown

https://spec.commonmark.org/0.30/#example-98

---
---
| <- meta.separator.thematic-break.markdown.morkdown - markup.heading
|^^^ meta.separator.thematic-break.markdown.morkdown - markup.heading

https://spec.commonmark.org/0.30/#example-102

\> foo
------
| <- markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown
|^^^^^ markup.heading.2.markdown.morkdown punctuation.definition.heading.setext.markdown.morkdown

```
Fenced codeblocks are no no setext heading
```
---
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown
|^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown


# TEST: INDENTED CODE BLOCKS ##################################################

Code block below:

    this is code!
| <- meta.paragraph
| ^^^^^^^^^^^^^^^^ meta.paragraph
| MO: Removed indented raw code blocks

    more code
    spanning multiple lines
| <- meta.paragraph
| ^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph
| MO: Removed indented raw code blocks

paragraph
| <- meta.paragraph
| ^^^^^^^^^^^^^^^^^^ meta.paragraph


# TEST: FENCED CODE BLOCKS ####################################################

## https://spec.commonmark.org/0.30/#example-119

```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
<
| <- markup.raw.code-fence.markdown-gfm.morkdown - punctuation
 >
|^^ markup.raw.code-fence.markdown-gfm.morkdown - punctuation
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-120

~~~
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
<
| <- markup.raw.code-fence.markdown-gfm.morkdown - punctuation
 >
|^^ markup.raw.code-fence.markdown-gfm.morkdown - punctuation
~~~
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-121

``
foo
``
| <- - meta.code-fence - punctuation.definition.raw.code-fence
|^ - meta.code-fence - punctuation.definition.raw.code-fence

## https://spec.commonmark.org/0.30/#example-122

```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
aaa
~~~
| <- markup.raw.code-fence.markdown-gfm.morkdown - punctuation
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-123

~~~
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
aaa
```
| <- markup.raw.code-fence.markdown-gfm.morkdown - punctuation
~~~
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

~~~~ 
| <- punctuation.definition.raw.code-fence.begin
 ~~~~
| ^^^ punctuation.definition.raw.code-fence.end

## https://spec.commonmark.org/0.30/#example-124

````
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|   ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
aaa
```
| <- markup.raw.code-fence.markdown-gfm.morkdown - punctuation
``````
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|     ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-125

~~~~
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|   ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
|
aaa
~~~
| <- markup.raw.code-fence.markdown-gfm.morkdown - punctuation
~~~~
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|   ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-128

> ```
> aaa
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown - markup.raw
| ^^^^ markup.quote.markdown.morkdown markup.raw.code-fence.markdown-gfm.morkdown

bbb
| <- meta.paragraph.markdown.morkdown - markup.raw

## https://spec.commonmark.org/0.30/#example-129

```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation

  
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-130

```
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-131

 ```
 aaa
aaa
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-132

  ```
aaa
  aaa
aaa
  ```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
|^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
| ^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|    ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-133

   ```
   aaa
    aaa
  aaa
   ```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
|  ^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|     ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

    ```
    aaa
     aaa
    aaa
    ```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
|^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
|   ^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|      ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
| MO: Removed indented raw code blocks


## https://spec.commonmark.org/0.30/#example-135

```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
aaa
| <- markup.raw.code-fence.markdown-gfm.morkdown
  ```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
|^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
| ^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|    ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-136

   ```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
|  ^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|     ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
aaa
| <- markup.raw.code-fence.markdown-gfm.morkdown
  ```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
|^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
| ^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|    ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-137

```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
aaa
| <- markup.raw.code-fence.markdown-gfm.morkdown
    ```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
|^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation
|   ^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|      ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-138

``` ```
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^^^^ markup.raw.inline.markdown.morkdown

``` ```
aaa
| <- meta.paragraph.markdown.morkdown - meta.code-fence - markup
|^^ meta.paragraph.markdown.morkdown - meta.code-fence - markup

## https://spec.commonmark.org/0.30/#example-139

~~~~~~
aaa
~~~ ~~
| <- markup.raw.code-fence.markdown-gfm.morkdown - punctuation
|^^^^^^ markup.raw.code-fence.markdown-gfm.morkdown - punctuation

~~~~~~
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|     ^ meta.code-fence.definition.end.text.markdown-gfm.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-140

foo
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
bar
```
baz
| <- meta.paragraph.markdown.morkdown - meta.code-fence - markup
|^^ meta.paragraph.markdown.morkdown - meta.code-fence - markup

## https://spec.commonmark.org/0.30/#example-140-including-emphasis-termination

Paragraph is terminated by fenced code blocks.
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

Code blocks terminate **bold text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
this must not be bold**
| <- - meta.bold
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold

Code blocks terminate __bold text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
this must not be bold__
| <- - meta.bold
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold

Code blocks terminate *italic text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
this must not be italic*
| <- - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.italic

Code blocks terminate _italic text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
this must not be italic_
| <- - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - meta.italic

Code blocks terminate ***bold italic text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
this must not be bold italic***
| <- - meta.bold - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - meta.italic

Code blocks terminate ___bold italic text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
this must not be bold italic___
| <- - meta.bold - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - meta.italic

Code blocks terminate **_bold italic text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
this must not be bold italic_**
| <- - meta.bold - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - meta.italic

## https://spec.commonmark.org/0.30/#example-141

foo
---
~~~
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
bar
|^^^ markup.raw.code-fence.markdown-gfm.morkdown
~~~
# baz
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^ markup.heading.1.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-142

```ruby
| <- meta.code-fence.definition.begin.ruby.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.ruby.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|  ^^^^ meta.code-fence.definition.begin.ruby.markdown-gfm.morkdown constant.other.language-name.markdown.morkdown
|      ^ meta.code-fence.definition.begin.ruby.markdown-gfm.morkdown - constant
def foo(x)
| <- markup.raw.code-fence.ruby.markdown-gfm.morkdown source.ruby meta.function
  return 3
end
| <- markup.raw.code-fence.ruby.markdown-gfm.morkdown source.ruby keyword
```
| <- meta.code-fence.definition.end.ruby.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.ruby.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-143

~~~~    ruby startline=3 $%@#$
| <- meta.code-fence.definition.begin.ruby.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^^ meta.code-fence.definition.begin.ruby.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|   ^^^^ meta.code-fence.definition.begin.ruby.markdown-gfm.morkdown - punctuation - constant
|       ^^^^ meta.code-fence.definition.begin.ruby.markdown-gfm.morkdown constant.other.language-name.markdown.morkdown
|           ^^^^^^^^^^^^^^^^^^^ meta.code-fence.definition.begin.ruby.markdown-gfm.morkdown - constant
def foo(x)
| <- markup.raw.code-fence.ruby.markdown-gfm.morkdown source.ruby meta.function
  return 3
end
| <- markup.raw.code-fence.ruby.markdown-gfm.morkdown source.ruby keyword
~~~~~~~
| <- meta.code-fence.definition.end.ruby.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^^^^^ meta.code-fence.definition.end.ruby.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-144

````;
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|   ^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown
````
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-145

``` aa ```
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^^^^^^^ meta.paragraph.markdown.morkdown markup.raw.inline.markdown.morkdown
|^^ punctuation.definition.raw.begin.markdown.morkdown
|      ^^^ punctuation.definition.raw.end.markdown.morkdown
foo
| <- meta.paragraph.markdown.morkdown - markup

## https://spec.commonmark.org/0.30/#example-146

~~~ aa ``` ~~~
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|   ^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown constant.other.language-name.markdown.morkdown
|     ^^^^^^^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown - punctuation
foo
~~~
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

~~~~~foo~
|^^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|    ^^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown constant.other.language-name.markdown.morkdown

~~~~~
|^^^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-147

```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
``` aaa
| <- markup.raw.code-fence.markdown-gfm.morkdown - punctuation
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

## https://fenced-code-block-embedded-syntaxes-tests

```bash
# test
| ^^^^^ source.shell comment.line.number-sign
echo hello, \
|           ^^ punctuation.separator.continuation.line
echo This is a smiley :-\) \(I have to escape the parentheses, though!\)
|                       ^^ constant.character.escape
```
| <- meta.code-fence.definition.end.shell-script punctuation.definition.raw.code-fence.end
|^^ meta.code-fence.definition.end.shell-script.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```clojure
|^^^^^^^^^ meta.code-fence.definition.begin.clojure
|  ^^^^^^^ constant.other.language-name
 (/ 10 3.0)
| <- source.clojure
|^^^^^^^^^^ source.clojure
```
| <- meta.code-fence.definition.end.clojure.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.clojure.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```cmd

| <- markup.raw.code-fence.dosbatch.markdown-gfm.morkdown source.dosbatch
```
| <- meta.code-fence.definition.end.dosbatch.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.dosbatch.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```css

| <- markup.raw.code-fence.css.markdown-gfm.morkdown source.css
```
| <- meta.code-fence.definition.end.css.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.css.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```diff
+ inserted
| <- source.diff markup.inserted.diff punctuation.definition.inserted.diff
- deleted
| <- source.diff markup.deleted.diff punctuation.definition.deleted.diff
```
| <- meta.code-fence.definition.end.diff.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.diff.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```Graphviz
graph n {}
| ^^^ storage.type.dot
```
| <- meta.code-fence.definition.end.graphviz.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.graphviz.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```haskell

| <- markup.raw.code-fence.haskell.markdown-gfm.morkdown source.haskell
```
| <- meta.code-fence.definition.end.haskell.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.haskell.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```html
  <html>
| <- markup.raw.code-fence.html.markdown-gfm.morkdown text.html
| ^^^^^^ text.html meta.tag
```
| <- meta.code-fence.definition.end.html.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.html.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```html+php
<div></div>
|^^^ entity.name.tag.block.any.html
<?php
| <- markup.raw.code-fence.html-php.markdown-gfm.morkdown embedding.php text.html.php meta.embedded.php punctuation.section.embedded.begin.php
var_dump(expression);
| <- markup.raw.code-fence.html-php.markdown-gfm.morkdown embedding.php text.html.php meta.embedded.php source.php meta.function-call
```
| <- meta.code-fence.definition.end.html-php.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.html-php.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
| MO: Changed from `text.html.basic` to `text.html.php`. Presumably something's changed in the PHP parser since this was first written

```js
| <- punctuation.definition.raw.code-fence.begin
|  ^^ constant.other.language-name
for (var i = 0; i < 10; i++) {
| ^ source.js keyword.control.loop
    console.log(i);
}
```
| <- meta.code-fence.definition.end.javascript.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.javascript.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```jsx

| <- markup.raw.code-fence.jsx.markdown-gfm.morkdown
```
| <- meta.code-fence.definition.end.jsx.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.jsx.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```lisp

| <- markup.raw.code-fence.lisp.markdown-gfm.morkdown source.lisp
```
| <- meta.code-fence.definition.end.lisp.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.lisp.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```lua

| <- markup.raw.code-fence.lua.markdown-gfm.morkdown source.lua
```
| <- meta.code-fence.definition.end.lua.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.lua.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```matlab

| <- markup.raw.code-fence.matlab.markdown-gfm.morkdown source.matlab
```
| <- meta.code-fence.definition.end.matlab.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.matlab.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```ocaml

| <- markup.raw.code-fence.ocaml.markdown-gfm.morkdown source.ocaml
```
| <- meta.code-fence.definition.end.ocaml.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.ocaml.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```php
var_dump(expression);
| <- markup.raw.code-fence.php.markdown-gfm.morkdown source.php meta.function-call.identifier.php
```
| <- meta.code-fence.definition.end.php.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.php.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```python
|^^ punctuation.definition.raw.code-fence.begin
|^^^^^^^^^ meta.code-fence.definition.begin.python - markup
|  ^^^^^^ constant.other.language-name
def function():
    pass
|   ^^^^ keyword.control.flow
unclosed_paren = (
|                ^ meta.group.python punctuation.section.group.begin.python
```
| <- meta.code-fence.definition.end.python.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.python.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```regex
(?x)
\s+
| <- markup.raw.code-fence.regexp.markdown-gfm.morkdown source.regexp
```
| <- meta.code-fence.definition.end.regexp.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.regexp.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```scala

| <- markup.raw.code-fence.scala.markdown-gfm.morkdown source.scala
```
| <- meta.code-fence.definition.end.scala.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.scala.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```sh

| <- markup.raw.code-fence.shell-script.markdown-gfm.morkdown source.shell.bash
```
| <- meta.code-fence.definition.end.shell-script.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.shell-script.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```shell
function foo () {
| <- markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive.markdown meta.function.shell keyword.declaration.function.shell 
}
| <- markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive.markdown meta.function.shell meta.compound.shell punctuation.section.compound.end.shell

$ ls ~
| <- markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive comment.other.shell
| ^^ meta.function-call.identifier.shell variable.function.shell
|   ^^ meta.function-call.arguments.shell

output.txt
| <- markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive - meta.function-call - variable
|^^^^^^^^^ markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive - meta.function-call - variable

$ ls \
> /foo/
| <- markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive.markdown comment.other.shell
|^^^^^^^ markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive.markdown

$ ls \
> /foo/
bar
| <- markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive.markdown - meta.function-call
|^^^ markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive.markdown - meta.function-call

function foo () {}
| <- markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive.markdown - meta.function
|^^^^^^^^^^^^^^^^^^ markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive.markdown - meta.function
```
| <- meta.code-fence.definition.end.shell.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.shell.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

   ```shell
   $ ls
|  ^^^^^ markup.raw.code-fence.shell.markdown-gfm.morkdown source.shell.interactive.markdown
|  ^ comment.other.shell
|    ^^ meta.function-call.identifier.shell variable.function.shell
   ```

```shell-script

| <- markup.raw.code-fence.shell-script.markdown-gfm.morkdown source.shell.bash
```
| <- meta.code-fence.definition.end.shell-script.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.shell-script.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```sql
|^^^^^ meta.code-fence.definition.begin.sql
|  ^^^ constant.other.language-name
SELECT TOP 10 *
|^^^^^^^^^^^^^^^ markup.raw.code-fence.sql source.sql
FROM TableName
```
| <- meta.code-fence.definition.end.sql.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.sql.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```ts
declare type foo = 'bar'
| <- markup.raw.code-fence.typescript.markdown-gfm.morkdown source.ts
```
| <- meta.code-fence.definition.end.typescript.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.typescript.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```tsx

| <- markup.raw.code-fence.tsx.markdown-gfm.morkdown
```
| <- meta.code-fence.definition.end.tsx.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.tsx.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```xml
|^^^^^ meta.code-fence.definition.begin.xml
|  ^^^ constant.other.language-name
<?xml version="1.0" ?>
|^^^^^^^^^^^^^^^^^^^^^^ markup.raw.code-fence.xml
|     ^^^^^^^ meta.tag.preprocessor.xml entity.other.attribute-name.localname.xml
<example>
    <foobar />
</example>
```
| <- meta.code-fence.definition.end.xml.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
|^^ meta.code-fence.definition.end.xml.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

```R%&?! weired language name
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown
|  ^^^^^ constant.other.language-name.markdown.morkdown
|        ^^^^^^^^^^^^^^^^^^^^^ - constant
```

```{key: value}
|^^^^^^^^^^^^^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown
|  ^^^^^^^^^^^^ - constant
```

``` {key: value}
|^^^^^^^^^^^^^^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown
|   ^^^^^^^^^^^^ - constant
```


# TEST: HTML BLOCKS ###########################################################

## https://spec.commonmark.org/0.30/#example-148

<table><tr><td>
<pre>
**Hello**,
| ^^^^^^^^^ meta.disable-markdown - markup

_world_.
| ^^^^ markup.italic - meta.disable-markdown
</pre>
</td></tr></table>

## https://spec.commonmark.org/0.30/#example-149

<table>
  <tr>
    <td>
           hi
|^^^^^^^^^^^^^ meta.disable-markdown
    </td>
  </tr>
</table>

okay.
| <- meta.paragraph.markdown.morkdown
|^^^^^ meta.paragraph.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-150

 <div>
  *hello*
         <foo><a>
| <- meta.disable-markdown
|^^^^^^^^^^^^^^^^^ meta.disable-markdown
|        ^^^^^^^^ meta.tag

## https://spec.commonmark.org/0.30/#example-151

</div>
*foo*
| <- meta.disable-markdown - markup.italic
|^^^^^ meta.disable-markdown - markup.italic

## https://spec.commonmark.org/0.30/#example-152

<DIV CLASS="foo">
| ^^^^^^^^^^^^^^^^ meta.disable-markdown

*Markdown*
| ^^^^^^^ meta.paragraph markup.italic - meta.disable-markdown

</DIV>
| ^^^ meta.disable-markdown meta.tag.block.any.html

## https://spec.commonmark.org/0.30/#example-153

<div id="foo"
  class="bar">
|^^^^^^^^^^^^^ meta.disable-markdown meta.tag.block  
</div>
|^^^^^ meta.disable-markdown meta.tag.block

## https://spec.commonmark.org/0.30/#example-154

<div id="foo" class="bar
  baz">
|^^^^^^ meta.disable-markdown meta.tag.block  
</div>
|^^^^^ meta.disable-markdown meta.tag.block

## https://spec.commonmark.org/0.30/#example-155

<div>
*foo*
| <- meta.disable-markdown - markup.italic

<div>
*foo*

*bar*
| <- meta.paragraph.markdown.morkdown markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-159

<div><a href="bar">*foo*</a></div>
|                  ^^^^^ meta.disable-markdown - markup.italic

## https://spec.commonmark.org/0.30/#example-161

<div></div>
``` c
int x = 33;
```
|^^^ meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-162

<a href="foo">
*bar*
| <- meta.disable-markdown - markup.italic - punctuation
|^^^^^ meta.disable-markdown - markup.italic
</a>

## https://spec.commonmark.org/0.30/#example-163

<Warning>
*bar*
| <- meta.disable-markdown - markup.italic - punctuation
|^^^^^ meta.disable-markdown - markup.italic
</Warning>
| ^^^^^^^ meta.disable-markdown meta.tag.other.html entity.name.tag.other.html

## https://spec.commonmark.org/0.30/#example-164

<i class="foo">
*bar*
| <- meta.disable-markdown - markup.italic - punctuation
|^^^^^ meta.disable-markdown - markup.italic
</i>
| <- meta.disable-markdown meta.tag punctuation.definition.tag
|^^^ meta.disable-markdown meta.tag
|   ^ meta.disable-markdown - meta.tag

## https://spec.commonmark.org/0.30/#example-165

</ins>
*bar*
| <- meta.disable-markdown - markup.italic - punctuation
|^^^^^ meta.disable-markdown - markup.italic

## https://spec.commonmark.org/0.30/#example-166

<del>
*foo*
| <- meta.disable-markdown - markup.italic - punctuation
|^^^^^ meta.disable-markdown - markup.italic
</del>
| <- meta.disable-markdown meta.tag punctuation.definition.tag
|^^^^^ meta.disable-markdown meta.tag
|     ^ meta.disable-markdown - meta.tag

## https://spec.commonmark.org/0.30/#example-167

<del>
| <- meta.disable-markdown meta.tag punctuation.definition.tag
|^^^^ meta.disable-markdown meta.tag
|    ^ meta.disable-markdown - meta.tag

*foo*
| <- meta.paragraph.markdown.morkdown markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^ meta.paragraph.markdown.morkdown markup.italic.markdown.morkdown - punctuation
|   ^ meta.paragraph.markdown.morkdown markup.italic.markdown.morkdown punctuation.definition.italic.end.markdown.morkdown

</del>
| <- meta.disable-markdown meta.tag punctuation.definition.tag
|^^^^^ meta.disable-markdown meta.tag
|     ^ meta.disable-markdown - meta.tag

## https://spec.commonmark.org/0.30/#example-168

<del>*foo*</del>
|^^^^^^^^^^^^^^^ meta.paragraph - meta.disable-markdown
|^^^^ meta.tag.inline
|    ^^^^^ markup.italic
|         ^^^^^^ meta.tag.inline

## https://spec.commonmark.org/0.30/#example-169

<pre language="haskell"><code>
| ^^ meta.disable-markdown meta.tag.block.any.html entity.name.tag.block.any.html
import Text.HTML.TagSoup

main :: IO ()
| ^^^^^^^^^^^^ meta.disable-markdown
main = print $ parseTags tags
</code></pre>
| ^^^^^^^^^^^ meta.disable-markdown
|        ^^^ meta.tag.block.any.html entity.name.tag.block.any.html
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-170

<script type="text/javascript">
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown meta.tag.script.begin.html
// JavaScript example
| ^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown source.js.embedded.html comment.line.double-slash.js

document.getElementById("demo").innerHTML = "Hello JavaScript!";
| ^^^^^^ meta.disable-markdown source.js.embedded.html support.type.object.dom.js
</script>
| ^^^^^^ meta.disable-markdown meta.tag.script.end.html entity.name.tag.script.html
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-171

<style
  type="text/css">
| ^^^^^^^^^^^^^^^ meta.disable-markdown meta.tag.style.begin.html meta.attribute-with-value.html
h1 {color:red;}
|   ^^^^^ meta.disable-markdown source.css.embedded.html meta.property-list.css meta.property-name.css support.type.property-name.css

p {color:blue;}
|  ^^^^^ meta.disable-markdown source.css.embedded.html meta.property-list.css meta.property-name.css support.type.property-name.css
</style>
| ^^^^^ meta.disable-markdown meta.tag.style.end.html entity.name.tag.style.html
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-172

<style
  type="text/css">
h1 {color:red;}
| <- meta.disable-markdown source.css.embedded.html meta.selector.css entity.name.tag

p {color:blue;}
| <- meta.disable-markdown source.css.embedded.html meta.selector.css entity.name.tag
</style>
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-174

> <div>
> foo

bar
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-175

- <div>
- foo
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-176

<style>p{color:red;}</style>
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
*foo*
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-177

<!-- foo -->*bar*
| ^^^^^^^^^^ comment.block.html
|           ^^^^^ meta.disable-markdown
*baz*
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-178

<script>
foo
</script>1. *bar*
| ^^^^^^^^^^^^^^^^ meta.disable-markdown
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-179

<!-- Foo
| ^^ meta.disable-markdown comment.block.html punctuation.definition.comment

bar
   baz -->
| ^^^^^^^^ meta.disable-markdown comment.block.html
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-180

<?php
| ^^^^ meta.disable-markdown

  echo '>';

?>
|^^ meta.disable-markdown
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-181

<!DOCTYPE html>
| ^^^^^^^ meta.disable-markdown meta.tag.sgml.doctype.html
okay
| <- - meta.disable-markdown

<!ENTITY html>
| ^^^^^^^^^^^^^ meta.disable-markdown
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-182

<![CDATA[
| ^^^^^^^^ meta.disable-markdown meta.tag.sgml
function matchwo(a,b)
{
  if (a < b && a < 0) then {
    return 1;

  } else {

    return 0;
  }
}
]]>
|^^ meta.disable-markdown meta.tag.sgml
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-183

  <!-- foo -->
| ^^^^^^^^^^^^ meta.disable-markdown comment.block.html

    <!-- foo -->
|   ^^^^^^^^^^^^ meta.disable-markdown comment.block.html
| MO: Removed indented raw code blocks

## https://spec.commonmark.org/0.30/#example-184

  <div>

    <div>
|^^^^^^^^^ meta.disable-markdown - markup.raw.block.markdown.morkdown
| MO: Removed indented raw code blocks

## https://spec.commonmark.org/0.30/#example-188

<div>

*Emphasized* text.
|^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^^^^ markup.italic.markdown.morkdown

</div>
| <- meta.disable-markdown meta.tag.block
|^^^^^ meta.disable-markdown meta.tag.block

## https://spec.commonmark.org/0.30/#example-189

<div>
*Emphasized* text.
| <- meta.disable-markdown - markup.italic
|^^^^^^^^^^^^^^^^^^ meta.disable-markdown - markup.italic
</div>
| <- meta.disable-markdown meta.tag.block
|^^^^^ meta.disable-markdown meta.tag.block

## https://spec.commonmark.org/0.30/#example-190

<table>
| <- meta.disable-markdown meta.tag
|^^^^^^ meta.disable-markdown meta.tag

<tr>
| <- meta.disable-markdown meta.tag
|^^^ meta.disable-markdown meta.tag

<td>
Hi
</td>
| <- meta.disable-markdown meta.tag
|^^^^ meta.disable-markdown meta.tag

</tr>
| <- meta.disable-markdown meta.tag
|^^^^ meta.disable-markdown meta.tag

</table>
| <- meta.disable-markdown meta.tag
|^^^^^^^ meta.disable-markdown meta.tag

## https://spec.commonmark.org/0.30/#example-191

<table>
| <- meta.disable-markdown meta.tag
|^^^^^^ meta.disable-markdown meta.tag

  <tr>
| <- meta.disable-markdown
|^^^^^^^ meta.disable-markdown

    <td>
      Hi
    </td>
| <- meta.disable-markdown - markup.raw.block.markdown.morkdown
|^^^^^^^ meta.disable-markdown - markup.raw.block.markdown.morkdown
| MO: Removed indented raw code blocks

  </tr>
| <- meta.disable-markdown
|^^^^^^^ meta.disable-markdown

</table>
| <- meta.disable-markdown meta.tag
|^^^^^^^ meta.disable-markdown meta.tag

## https://custom-tests/html-blocks

<div>this is HTML until <span>there are two</span> blank lines</div>
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
disabled markdown
| <- meta.disable-markdown

non-disabled markdown
| <- - meta.disable-markdown

<div>this is HTML until there are two blank lines
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
still <span>HTML</span>
|      ^^^^ meta.tag.inline.any.html entity.name.tag.inline.any.html
</div>
| ^^^^ meta.disable-markdown

non-disabled markdown
| <- - meta.disable-markdown

<pre>nested tags don't count <pre>test</pre>
|                                     ^^^^^^ meta.disable-markdown meta.tag.block.any.html
non-disabled markdown
| <- - meta.disable-markdown

<div>nested tags don't count <div>test
|                                 ^^^^^ meta.disable-markdown
</div>
| ^^^ meta.disable-markdown entity.name.tag.block.any.html

non-disabled markdown
| <- - meta.disable-markdown

<div>two blank lines needed</div> to stop disabled markdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
disabled markdown
| <- meta.disable-markdown

non-disabled markdown
| <- - meta.disable-markdown

<div>another</div> <span>disable</span> test
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
|                  ^^^^^^ meta.tag.inline.any.html
disabled markdown
| <- meta.disable-markdown

non-disabled markdown
| <- - meta.disable-markdown

*a*
| ^ markup.italic
<p>*a*</p>
| ^^^^^^^^^ meta.disable-markdown - markup.italic
*a*
| ^^ meta.disable-markdown

non-disabled markdown
| <- - meta.disable-markdown


# TEST: LINK REFERENCE DEFINITIONS ############################################

## https://spec.commonmark.org/0.30/#example-192

[foo]: /url "title"
|^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|    ^ punctuation.separator.key-value
|      ^^^^ markup.underline.link
|           ^^^^^^^ string.quoted.double

## https://spec.commonmark.org/0.30/#example-193

   [foo]: 
      /url  
           'the title'  
|^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|          ^^^^^^^^^^^ string.quoted.single

## https://spec.commonmark.org/0.30/#example-194

 [Foo*bar\]]:my_(url) 'title (with parens)'
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|^ punctuation.definition.reference.begin.markdown.morkdown
| ^^^^^^^^^ entity.name.reference.link.markdown.morkdown - punctuation
|          ^ punctuation.definition.reference.end.markdown.morkdown
|           ^ punctuation.separator.key-value.markdown.morkdown
|            ^^^^^^^^ markup.underline.link
|                    ^ - markup - string
|                     ^^^^^^^^^^^^^^^^^^^^^ string.quoted.single

## https://spec.commonmark.org/0.30/#example-195

[Foo bar]:
<my url>
| <- meta.link.reference.def.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
|^^^^^^ meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown
|      ^ meta.link.reference.def.markdown.morkdown punctuation.definition.link.end.markdown.morkdown

[Foo bar]:
<my url>
'title'
| <- meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.single.markdown.morkdown
|^^^^^^ meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.single.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-196

[foo]: /url '
|           ^ meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.single.markdown.morkdown punctuation.definition.string.begin.markdown.morkdown
title
| <- meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.single.markdown.morkdown
|^^^^^ meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.single.markdown.morkdown
line1
| <- meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.single.markdown.morkdown
|^^^^^ meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.single.markdown.morkdown
line2
| <- meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.single.markdown.morkdown
|^^^^^ meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.single.markdown.morkdown
'
| <- meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.single.markdown.morkdown punctuation.definition.string.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-197

[foo]: /url 'title

with blank line'
| <- meta.paragraph.markdown.morkdown - meta.link
|^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - meta.link

## https://spec.commonmark.org/0.30/#example-198

[foo]:
/url
| <- meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown punctuation.separator.path.markdown.morkdown
|^^^ meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-199

[foo]:
| <- meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
|^^^ meta.link.reference.def.markdown.morkdown entity.name.reference.link.markdown.morkdown
|   ^ meta.link.reference.def.markdown.morkdown punctuation.definition.reference.end.markdown.morkdown
|    ^ meta.link.reference.def.markdown.morkdown punctuation.separator.key-value.markdown.morkdown
|     ^ meta.link.reference.def.markdown.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-200

[foo]: <>
|^^^^^^^^ meta.link.reference.def.markdown.morkdown
|    ^ punctuation.separator.key-value
|      ^ punctuation.definition.link.begin
|       ^ punctuation.definition.link.end

## https://spec.commonmark.org/0.30/#example-201

[foo]: <bar>(baz)
| <- meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|^^^ entity.name.reference.link.markdown.morkdown
|   ^ punctuation.definition.reference.end.markdown.morkdown
|    ^ punctuation.separator.key-value.markdown.morkdown
|      ^ punctuation.definition.link.begin.markdown.morkdown
|       ^^^ markup.underline.link.markdown.morkdown
|          ^ punctuation.definition.link.end.markdown.morkdown
|           ^^^^^ meta.string.title.markdown.morkdown string.quoted.other.markdown.morkdown
|           ^ punctuation.definition.string.begin.markdown.morkdown
|               ^ punctuation.definition.string.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-202

[foo]: /url\bar\*baz "foo\"bar\baz"
| <- meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|^^^ entity.name.reference.link.markdown.morkdown
|   ^ punctuation.definition.reference.end.markdown.morkdown
|    ^ punctuation.separator.key-value.markdown.morkdown
|      ^^^^^^^^^^^^^ markup.underline.link.markdown.morkdown
|      ^ punctuation.separator.path.markdown.morkdown
|          ^^ - constant.character.escape
|              ^^ constant.character.escape.markdown.morkdown
|                    ^^^^^^^^^^^^^^ meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown
|                    ^ punctuation.definition.string.begin.markdown.morkdown
|                        ^^ constant.character.escape.markdown.morkdown
|                             ^^ - constant.character.escape
|                                 ^ punctuation.definition.string.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-203

[foo]: url
| <- meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
|^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|^^^ entity.name.reference.link.markdown.morkdown
|   ^ punctuation.definition.reference.end.markdown.morkdown
|    ^ punctuation.separator.key-value.markdown.morkdown
|      ^^^ markup.underline.link.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-204

[foo]: first
[foo]: second
| <- meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
|^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|^^^ entity.name.reference.link.markdown.morkdown
|   ^ punctuation.definition.reference.end.markdown.morkdown
|    ^ punctuation.separator.key-value.markdown.morkdown
|      ^^^^^^ markup.underline.link.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-205

[FOO]: /url
| <- meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
|^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|^^^ entity.name.reference.link.markdown.morkdown
|   ^ punctuation.definition.reference.end.markdown.morkdown
|    ^ punctuation.separator.key-value.markdown.morkdown
|      ^^^^ markup.underline.link.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-206

[ΑΓΩ]: /φου
| <- meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
|^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|^^^ entity.name.reference.link.markdown.morkdown
|   ^ punctuation.definition.reference.end.markdown.morkdown
|    ^ punctuation.separator.key-value.markdown.morkdown
|      ^^^^ markup.underline.link.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-208

[
foo
]: /url
bar
| <- meta.paragraph.markdown.morkdown - meta.link
|^^^ meta.paragraph.markdown.morkdown - meta.link

## https://spec.commonmark.org/0.30/#example-209

This is not a link reference definition, because there are characters other than spaces or tabs after the title:

[foo]: /url "title" ok
|^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|                   ^^ invalid.illegal.expected-eol.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-210

This is a link reference definition, but it has no title:

[foo]: /url
"title" ok
|^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|       ^^ invalid.illegal.expected-eol.markdown.morkdown

[foo]: <bar> "baz" 
|^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|      ^ punctuation.definition.link.begin
|       ^^^ markup.underline.link
|          ^ punctuation.definition.link.end
|            ^^^^^ string.quoted.double
|                 ^ - invalid.illegal.expected-eol

[foo]: <bar>> "baz" 
|^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|      ^ punctuation.definition.link.begin
|       ^^^ markup.underline.link
|          ^ punctuation.definition.link.end
|           ^^^^^^^ invalid.illegal.expected-eol.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-211

MO: This is now a link reference definition, even though it is indented four spaces:

    [foo]: /url "title"
|^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown - markup.raw.block.markdown.morkdown
|        ^ punctuation.separator.key-value - markup.raw.block.markdown.morkdown
|          ^^^^ markup.underline.link - markup.raw.block.markdown.morkdown
|               ^^^^^^^ string.quoted.double - markup.raw.block.markdown.morkdown
| MO: Removed indented raw code blocks

## https://spec.commonmark.org/0.30/#example-212

This is not a link reference definition, because it occurs inside a code block:

```
[foo]: /url
| <- markup.raw.code-fence.markdown-gfm.morkdown - meta.link
|^^^^^^^^^^^ markup.raw.code-fence.markdown-gfm.morkdown - meta.link
```

## https://spec.commonmark.org/0.30/#example-213

A link reference definition cannot interrupt a paragraph.

Foo
[bar]: /baz
| <- meta.paragraph.markdown.morkdown meta.link.reference.description.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
|^^^^^^^^^^^ meta.paragraph.markdown.morkdown
|^^^^ meta.link.reference.description.markdown.morkdown
|    ^^^^^^^ - punctuation - markup.underline

## https://spec.commonmark.org/0.30/#example-214

### [Foo]
[foo]: /url
| <- meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
|^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown

### [Foo]
[foo]: /url
> bar
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-218

> [foo]: /url
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown - meta.link
| ^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown
| ^ punctuation.definition.reference.begin.markdown.morkdown
|  ^^^ entity.name.reference.link.markdown.morkdown
|     ^ punctuation.definition.reference.end.markdown.morkdown
|      ^ punctuation.separator.key-value.markdown.morkdown
|        ^^^^ markup.underline.link.markdown.morkdown

## https://custom-tests/link-reference-definitions/in-block-quotes

> [foo]: /url "description"
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown
| ^ punctuation.definition.reference.begin.markdown.morkdown
|  ^^^ entity.name.reference.link.markdown.morkdown
|     ^ punctuation.definition.reference.end.markdown.morkdown
|      ^ punctuation.separator.key-value.markdown.morkdown
|        ^^^^ markup.underline.link.markdown.morkdown
|             ^^^^^^^^^^^^^ meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown

> [foo]: 
> /url
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown - markup.underline
| ^^^^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown

> [foo]: 
> /url
> "description"
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown - meta.string - string
| ^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown

> [foo]:
> </url-with
> -continuation>
| <- markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown
|^^^^^^^^^^^^^^ markup.underline.link.markdown.morkdown
|              ^ punctuation.definition.link.end.markdown.morkdown

> [foo]: 
  /url
| <- markup.quote.markdown.morkdown - markup.underline - punctuation
|^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown - markup.underline
| ^^^^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown

> [foo]: 
  /url
  "description"
| <- markup.quote.markdown.morkdown - meta.string - string - punctuation
|^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown - meta.string - string
| ^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown

> [foo]:
  </url-with
  -continuation>
| <- markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown
|^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.markdown.morkdown
|^^^^^^^^^^^^^^ markup.underline.link.markdown.morkdown
|              ^ punctuation.definition.link.end.markdown.morkdown

## https://custom-tests/link-reference-definitions

[//]: # (This is a comment without a line-break.)
|     ^ meta.link.reference.def.markdown.morkdown markup.underline.link
|       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ string.quoted.other

[//]: # (This is a comment with a
|     ^ meta.link.reference.def.markdown.morkdown markup.underline.link
|       ^ punctuation.definition.string.begin
        line-break.)
|                  ^ punctuation.definition.string.end

[//]: # (testing)blah
|^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown.morkdown
|       ^ punctuation.definition.string.begin
|               ^ punctuation.definition.string.end
|                ^^^^ invalid.illegal.expected-eol
|                    ^ - invalid

[//]: # (testing
blah
| <- meta.link.reference.def.markdown.morkdown string.quoted.other

| <- invalid.illegal.non-terminated.link-title
text
| <- meta.paragraph - meta.link.reference.def.markdown.morkdown

## https://custom-tests/footnote-reference-definitions

 [^1]: And that's the footnote.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra.morkdown
|^ punctuation.definition.reference.begin.markdown.morkdown
| ^^ entity.name.reference.link.markdown.morkdown
|   ^ punctuation.definition.reference.end.markdown.morkdown
|    ^ punctuation.separator.key-value.markdown.morkdown

  [^1]: And that's the footnote.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra.morkdown
| ^ punctuation.definition.reference.begin.markdown.morkdown
|  ^^ entity.name.reference.link.markdown.morkdown
|    ^ punctuation.definition.reference.end.markdown.morkdown
|     ^ punctuation.separator.key-value.markdown.morkdown

   [^1]: And that's the footnote.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra.morkdown
|  ^ punctuation.definition.reference.begin.markdown.morkdown
|   ^^ entity.name.reference.link.markdown.morkdown
|     ^ punctuation.definition.reference.end.markdown.morkdown
|      ^ punctuation.separator.key-value.markdown.morkdown

     [^1]: And that's the footnote.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra.morkdown - markup.raw.block.markdown.morkdown
|    ^ punctuation.definition.reference.begin.markdown.morkdown - markup.raw.block.markdown.morkdown
|     ^^ entity.name.reference.link.markdown.morkdown - markup.raw.block.markdown.morkdown
|       ^ punctuation.definition.reference.end.markdown.morkdown - markup.raw.block.markdown.morkdown
|        ^ punctuation.separator.key-value.markdown.morkdown - markup.raw.block.markdown.morkdown
| MO: Removed indented raw code blocks

[^1]:
    And that's the footnote
with a *second* line.
|^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra.morkdown - markup.raw

[^1]:
    And that's the footnote.

    That's the *second* footnote paragraph.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra.morkdown - markup.raw
|              ^^^^^^^^ markup.italic

[^1]:
    And that's the footnote.

   Not a footnote paragraph.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - meta.link

[^1]:
    And that's the footnote
with a *second* line.
[^2]: second
| <- meta.link.reference.def.footnote.markdown-extra.morkdown punctuation.definition.reference.begin.markdown.morkdown
|^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra.morkdown
|^^ entity.name.reference.link.markdown.morkdown
|  ^ punctuation.definition.reference.end.markdown.morkdown
|   ^ punctuation.separator.key-value.markdown.morkdown

## https://custom-tests/footnote-reference-definitions/in-block-quotes

> [^1]: And that's the footnote.
|^ markup.quote.markdown.morkdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown
| ^ punctuation.definition.reference.begin.markdown.morkdown
|  ^^ entity.name.reference.link.markdown.morkdown
|    ^ punctuation.definition.reference.end.markdown.morkdown
|     ^ punctuation.separator.key-value.markdown.morkdown

>  [^1]: And that's the footnote.
|^ markup.quote.markdown.morkdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown
|  ^ punctuation.definition.reference.begin.markdown.morkdown
|   ^^ entity.name.reference.link.markdown.morkdown
|     ^ punctuation.definition.reference.end.markdown.morkdown
|      ^ punctuation.separator.key-value.markdown.morkdown

>   [^1]: And that's the footnote.
|^ markup.quote.markdown.morkdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown
|   ^ punctuation.definition.reference.begin.markdown.morkdown
|    ^^ entity.name.reference.link.markdown.morkdown
|      ^ punctuation.definition.reference.end.markdown.morkdown
|       ^ punctuation.separator.key-value.markdown.morkdown

>     [^1]: And that's no footnote.
|^ markup.quote.markdown.morkdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown - markup.raw
|     ^ punctuation.definition.reference.begin.markdown.morkdown - markup.raw
|      ^^ entity.name.reference.link.markdown.morkdown - markup.raw
|        ^ punctuation.definition.reference.end.markdown.morkdown - markup.raw
|         ^ punctuation.separator.key-value.markdown.morkdown - markup.raw
| MO: Removed indented raw code blocks

> [^1]: And that's the footnote.
> with a *second* line.
| <- markup.quote.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown

> [^1]:
>     And that's the footnote.
> 
>     That's the *second* paragraph.
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown
|                ^^^^^^^^ markup.italic

> [^1]:
>     And that's the footnote.
> 
>    Not a footnote paragraph.
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown - markup.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown - markup.link

>   [^1]: And that's the footnote.
> 
>     not a code block
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown - markup.link - markup.raw
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown - markup.link - markup.raw
| MO: Removed indented raw code blocks

> [^1]:
>     And that's the footnote.
> 
      That's a *second* paragraph.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - markup.raw
| MO: Removed indented raw code blocks

# TEST: TABLES ################################################################

| foo | bar |
|^^^^^^^^^^^^^ meta.table.header
| <- punctuation.separator.table-cell
|     ^ punctuation.separator.table-cell
|           ^ punctuation.separator.table-cell
| ^^^^ - punctuation.separator.table-cell

| foo | bar |
| --- | --- |
| baz | bim <kbd>Ctrl+C</kbd> |
| <- meta.table punctuation.separator.table-cell
|           ^^^^^ meta.tag.inline.any
|                             ^ punctuation.separator.table-cell

| <- - meta.table

| abc | defghi |
:-: | -----------:
|^^^^^^^^^^^^^^^^^ meta.table.header-separator
| <- punctuation.definition.table-cell-alignment
|^ punctuation.section.table-header
|   ^ punctuation.separator.table-cell
|     ^^^^^^^^^^^ punctuation.section.table-header
|                ^ punctuation.definition.table-cell-alignment - punctuation.section.table-header
bar | baz
|   ^ meta.table punctuation.separator.table-cell

| f\|oo  |
| <- meta.table punctuation.separator.table-cell
|  ^^ meta.table constant.character.escape - punctuation.separator.table-cell
|        ^ meta.table punctuation.separator.table-cell

| f\|oo  |
| ------ |
| b `|` az |
|   ^^^ meta.table markup.raw.inline - meta.table.header-separator
|          ^ meta.table punctuation.separator.table-cell
| b **|** im |
| <- meta.table punctuation.separator.table-cell
|   ^^^^^ meta.table markup.bold - punctuation.separator.table-cell
|            ^ meta.table punctuation.separator.table-cell

| abc | def |
| --- | --- |
| bar | baz |
|^^^^^^^^^^^^^ meta.table
test
|^^^^ meta.table
> bar
| <- markup.quote punctuation.definition.blockquote - meta.table

`|` this `|` example `|` is not a table `|`
| ^ punctuation.definition.raw.end - meta.table
| nor is this | because it is not at block level, it immediately follows a paragraph |
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph - meta.table

| First Header  | Second Header | Third Header         |
| :------------ | :-----------: | -------------------: |
| First row     | Data          | Very long data entry |
| Second row    | **Cell**      | *Cell*               |
| Third row     | Cell that spans across two columns  ||
| ^^^^^^^^^^^^^^ meta.table
|                                                     ^^ punctuation.separator.table-cell

 | table that doesn't start at column 0 |
  | ---- |
  | blah |
| ^^^^^^^^ meta.table
| ^ punctuation.separator.table-cell

not a table | 
| ^^^^^^^^^^^^^ - meta.table

 abc | def
 --- | ---
 --- | ---
| ^^^^ meta.table - meta.table.header

 a | b
 - | -
|^^^^^^ meta.table.header-separator.markdown-gfm.morkdown
|^ punctuation.section.table-header.markdown.morkdown
|  ^ punctuation.separator.table-cell.markdown.morkdown
|    ^ punctuation.section.table-header.markdown.morkdown
 - | -
|^^^^^^ meta.table.markdown-gfm.morkdown

 a | b
 -:| -
|^^^^^^ meta.table.header-separator.markdown-gfm.morkdown
|^ punctuation.section.table-header.markdown.morkdown
| ^ punctuation.definition.table-cell-alignment.markdown.morkdown
|  ^ punctuation.separator.table-cell.markdown.morkdown
|    ^ punctuation.section.table-header.markdown.morkdown
 - | -
|^^^^^^ meta.table.markdown-gfm.morkdown

| test | me |
|------|----|
|^^^^^^ punctuation.section.table-header
|*test | me |
|^^^^^^ - markup.bold
|      ^ punctuation.separator.table-cell
|           ^ punctuation.separator.table-cell
|`test | me |
|^ invalid.deprecated.unescaped-backticks
|      ^ punctuation.separator.table-cell

| table | followed by
paragraph
| <- meta.paragraph.markdown.morkdown
|^^^^^^^^^ meta.paragraph.markdown.morkdown

| table | followed by
https://foo.bar/baz
| <- meta.paragraph.markdown.morkdown meta.link.inet.markdown.morkdown markup.underline.link.markdown-gfm.morkdown
|^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown meta.link.inet.markdown.morkdown markup.underline.link.markdown-gfm.morkdown

| table | followed by
# heading
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^^ markup.heading.1.markdown.morkdown

| table | followed by
> quote
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^^ markup.quote.markdown.morkdown

| table | followed by
    quote
| <- meta.paragraph.markdown.morkdown - markup.raw
|^^^^^^^^^ meta.paragraph.markdown.morkdown - markup.raw
| MO: Removed indented raw code blocks

| table | followed by
```fenced
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown
|^^^^^^^^^ meta.code-fence.definition.begin.text.markdown-gfm.morkdown
code block
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown
|^^ meta.code-fence.definition.end.text.markdown-gfm.morkdown

A line without bolded |
|                     ^ - punctuation.separator.table-cell

A line with bolded **|**
|                    ^ - punctuation.separator.table-cell


# TEST: BLOCK QUOTES ##########################################################

## https://spec.commonmark.org/0.30/#example-228

> # Foo
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown - markup.heading
| ^^^^^^ markup.quote.markdown.morkdown markup.heading.1.markdown.morkdown
| ^ punctuation.definition.heading.begin.markdown.morkdown
|   ^^^ entity.name.section.markdown.morkdown

> # Foo
bar
| <- meta.paragraph.markdown.morkdown - markup.quote
|^^ meta.paragraph.markdown.morkdown - markup.quote

> # Foo
> bar
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^ markup.quote.markdown.morkdown

> # Foo
> bar
> baz
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-229

># Foo
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^ markup.quote.markdown.morkdown markup.heading.1.markdown.morkdown
|^ punctuation.definition.heading.begin.markdown.morkdown
|  ^^^ entity.name.section.markdown.morkdown

># Foo
>bar
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^ markup.quote.markdown.morkdown

># Foo
>bar
> baz
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-230

   > # Foo
| <- markup.quote.markdown.morkdown
|^^^^^^^^^^ markup.quote.markdown.morkdown
|  ^ punctuation.definition.blockquote.markdown.morkdown
|    ^^^^^^ markup.heading.1.markdown.morkdown
|    ^ punctuation.definition.heading.begin.markdown.morkdown
|      ^^^ entity.name.section.markdown.morkdown

   > # Foo
   > bar
| <- markup.quote.markdown.morkdown - punctuation
|^^ markup.quote.markdown.morkdown - punctuation
|  ^ markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|   ^^^^^ markup.quote.markdown.morkdown - punctuation

   > # Foo
   > bar
 > baz
| <- markup.quote.markdown.morkdown - punctuation
|^ markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
| ^^^^^ markup.quote.markdown.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-231

    > # Foo
    > bar
    > baz
|^^^ markup.quote.markdown.morkdown - punctuation - markup.raw
|   ^ markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown - markup.raw
|     ^^^^^ markup.quote.markdown.morkdown - punctuation - markup.raw
| MO: Removed indented raw code blocks

## https://spec.commonmark.org/0.30/#example-232

> # Foo
> bar
baz
| <- markup.quote.markdown.morkdown
|^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-233

> bar
baz
| <- markup.quote.markdown.morkdown
|^^^ markup.quote.markdown.morkdown
> foo
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^ markup.quote.markdown.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-234

> foo
***
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown - markup.quote
|^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown - markup.quote

> foo
---
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown - markup.quote
|^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown - markup.quote

> foo
___
| <- meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown - markup.quote
|^^ meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown - markup.quote

## https://spec.commonmark.org/0.30/#example-235

> - foo
- bar
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown - markup.quote
|^^^^^ markup.list.unnumbered.markdown.morkdown - markup.quote

## https://spec.commonmark.org/0.30/#example-236

>     foo
    bar
| <- markup.paragraph.markdown.morkdown - markup.raw
|^^^ markup.paragraph.markdown.morkdown - markup.raw
| MO: Removed indented raw code blocks
| MO: Why is it markup.paragraph.markdown.morkdown and not meta.paragraph.markdown?


## https://spec.commonmark.org/0.30/#example-237

> ```
foo
| <- meta.paragraph.markdown.morkdown - markup.quote - markup.raw
|^^^ meta.paragraph.markdown.morkdown - markup.quote - markup.raw

## https://spec.commonmark.org/0.30/#example-238

> foo
    - bar
|   ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown - markup.quote
|^^^ markup.list.unnumbered.markdown.morkdown - markup.quote - markup.raw
|    ^^^^ markup.list.unnumbered.markdown.morkdown - markup.quote - markup.raw
| MO: Lists are now allowed to be indented

## https://spec.commonmark.org/0.30/#example-239

>
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-240

>
>  
> 
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-241

>
> foo
>  
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-242

> foo

| <- - markup.quote
> foo

> bar
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-243

> foo
> bar
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-244

> foo
>
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
> bar
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-245

foo
> bar
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-246

> aaa
***
> bbb
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-247

> bar
baz
| <- markup.quote.markdown.morkdown
|^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-248

> bar

baz
| <- meta.paragraph.markdown.morkdown - markup.quote
|^^ meta.paragraph.markdown.morkdown - markup.quote

## https://spec.commonmark.org/0.30/#example-249

> bar
>
baz
| <- meta.paragraph.markdown.morkdown - markup.quote
|^^ meta.paragraph.markdown.morkdown - markup.quote

## https://spec.commonmark.org/0.30/#example-250

> > > foo
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^^^^ markup.quote.markdown.morkdown
| ^ punctuation.definition.blockquote.markdown.morkdown
|   ^ punctuation.definition.blockquote.markdown.morkdown
|    ^^^^^ - punctuation

> > > foo
bar
| <- markup.quote.markdown.morkdown
|^^^ markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-251

>>> foo
> bar
>>baz
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
| ^^^^ markup.quote.markdown.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-252

>     code
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown - markup.raw
| ^^^^^^^^^ markup.quote.markdown.morkdown - markup.raw
| MO: Removed indented raw code blocks

>    not code
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown - markup.raw
|^^^^^^^^^^^^^ markup.quote.markdown.morkdown - markup.raw

## https://custom-tests/block-quotes/block-quote-starts

>=
| <- punctuation.definition.blockquote.markdown.morkdown 

>==
| <- punctuation.definition.blockquote.markdown.morkdown

  >=
| ^ punctuation.definition.blockquote.markdown.morkdown
    >=
|   ^ punctuation.definition.blockquote.markdown.morkdown - markup.raw
| ^^^^^ markup.quote.markdown.morkdown - markup.raw
| MO: Removed indented raw code blocks
 
    >=
|   ^ punctuation.definition.blockquote.markdown.morkdown - markup.raw
| ^^^^^ markup.quote.markdown.morkdown - markup.raw
| MO: Removed indented raw code blocks

## https://custom-tests/block-quotes/block-quote-nesting

> > Nested block quote
| <- markup.quote punctuation.definition.blockquote
| ^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown
|^ - punctuation
| ^ punctuation.definition.blockquote
|  ^ - punctuation

> > Nested quote
> Followed by more quoted text that is not nested
| <- markup.quote punctuation.definition.blockquote - markup.quote markup.quote

>    > this is a nested quote but no code in a block quote
| <- punctuation.definition.blockquote
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown

>    > this is a nested quote but no code in a block quote
>     > with a second line of content
| <- punctuation.definition.blockquote
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown - markup.raw
|     ^ punctuation.definition.blockquote - markup.raw
| MO: Removed indented raw code blocks
> 
>     > this is NOT code in a block quote, it's a nested quote
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown - markup.raw
|       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.paragraph.markdown.morkdown 
|     ^ punctuation.definition.blockquote - markup.raw
| MO: Removed indented raw code blocks

## https://custom-tests/block-quotes/block-quote-terminations

> Block quote followed by heading
# heading
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
|^^^^^^^^^ markup.heading.1.markdown.morkdown - meta.quote
| ^^^^^^^ entity.name.section.markdown.morkdown

> Block quote followed by unordered list
* list item
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown - meta.quote

> Block quote followed by unordered list
+ list item
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown - meta.quote

> Block quote followed by unordered list
- list item
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown - meta.quote

> Block quote followed by ordered list
1. list item
| <- markup.list.numbered.bullet.markdown.morkdown - punctuation
|^ markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^^^^^^^^^^ markup.list.numbered.markdown.morkdown - meta.quote

> Block quote followed by ordered list
2. list item
| <- markup.list.numbered.bullet.markdown.morkdown - punctuation
|^ markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^^^^^^^^^^ markup.list.numbered.markdown.morkdown - meta.quote

> Block quote followed by invalid list
1234567890. no list item
| <- markup.quote.markdown.morkdown - markup.list
|^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown - markup.list

> Block quote followed by html block
<p>*no-markdown</p>
| <- meta.disable-markdown meta.tag.block
|^^^^^^^^^^^^^^^^^^^ meta.disable-markdown

## https://custom-tests/block-quotes/thematic-breaks

> * * *
paragraph
| <- meta.paragraph.markdown.morkdown - markup.quote

> - - -
paragraph
| <- meta.paragraph.markdown.morkdown - markup.quote

> _ _ _
paragraph
| <- meta.paragraph.markdown.morkdown - markup.quote

> paragraph
> * * *
| ^^^^^^ markup.quote.markdown.morkdown meta.separator.thematic-break.markdown.morkdown

> paragraph
> - - -
| ^^^^^^ markup.quote.markdown.morkdown meta.separator.thematic-break.markdown.morkdown

> paragraph
> _ _ _
| ^^^^^^ markup.quote.markdown.morkdown meta.separator.thematic-break.markdown.morkdown

## https://custom-tests/block-quotes/fenced-code-blocks

> Quoted fenced code block begin
> ```
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown - meta.code-fence
| ^^^^ markup.quote.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown
| ^^^ punctuation.definition.raw.code-fence.begin.markdown.morkdown

> Quoted fenced code block language identifier
> ```C++
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown - meta.code-fence
| ^^^^^^^ markup.quote.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown
|    ^^^ constant.other.language-name.markdown.morkdown

> Quoted fenced code block language identifier
> ```C++ info string
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown - meta.code-fence
| ^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown
|    ^^^ constant.other.language-name.markdown.morkdown
|       ^^^^^^^^^^^^^ - constant

> Quoted fenced code block content
> ```
> code block
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown - meta.code-fence
| ^^^^^^^^^^^ markup.quote.markdown.morkdown markup.raw.code-fence.markdown-gfm.morkdown

> Quoted fenced code block end
> ```
> ```
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown - meta.code-fence
| ^^^^ markup.quote.markdown.morkdown meta.code-fence.definition.end.text.markdown-gfm.morkdown
| ^^^ punctuation.definition.raw.code-fence.end.markdown.morkdown

> > 2nd level quoted fenced code block
> > ```
> > code block ```
|              ^^^ - punctuation

> > 2nd level quoted fenced code block
> > ```
> > code block ```
> > ```
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^ markup.quote.markdown.morkdown - meta.code-fence
|   ^^^ markup.quote.markdown.morkdown meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

> Block quote followed by fenced code block
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown - meta.quote
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown - meta.quote

> Quoted fenced code block is terminated by missing > at bol
> ```
no code block
| <- meta.paragraph.markdown.morkdown - meta.quote - meta.code-fence
|^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - meta.quote - meta.code-fence

> Quoted fenced code block is terminated by missing > at bol
> ```
> content
no code block
| <- meta.paragraph.markdown.morkdown - meta.quote - meta.code-fence
|^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - meta.quote - meta.code-fence

> Unterminated quoted fenced code block followed by unquoted fenced code block
> ```
```
| <- meta.code-fence.definition.begin.text.markdown-gfm.morkdown - markup.quote
```
| <- meta.code-fence.definition.end.text.markdown-gfm.morkdown - markup.quote

> > ```
> This is a paragraph highlight as code,
> because nested block quotes can't be counted.
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown

## https://custom-tests/block-quotes/list-blocks/basics

> Block quote with lists
> - list item 1
| ^ markup.quote punctuation.definition.list_item
> - list item 2
| ^ markup.list.unnumbered.bullet punctuation.definition.list_item
| ^^^^^^^^^^^^^^ markup.quote markup.list.unnumbered
>   1. sub list item
| <- markup.quote punctuation.definition.blockquote
|^^^^^^^^^^^^^^^^^^ markup.quote
| ^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered
|    ^ punctuation.definition.list_item
|   ^^ markup.list.numbered.bullet
> - list item 3
  continued
| ^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown

## https://custom-tests/block-quotes/list-blocks/items-with-line-continuation

> * list item
> second line
| <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
>   + subitem
> second line
| <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
>     - subitem
> second line
| <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
>       - subitem
> second line
| <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown

> * list item
second line
| <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown
>   + subitem
  second line
| <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown
>     - subitem
   second line
| <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown
>       - subitem
     second line
| <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown

> 1. list item
> second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
>    2. subitem
> second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
>       3. subitem
> second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
>          4. subitem
> second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown

> 1. list item
second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
>    2. subitem
  second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
>       3. subitem
   second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
>          4. subitem
    second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown

> 1. list item
> second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
>    + subitem
> second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
>      - subitem
> second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
>        - subitem
> second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown

> 1. list item
second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
>    + subitem
  second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
>      - subitem
   second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
>        - subitem
    second line
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown

## https://custom-tests/block-quotes/list-blocks/items-with-thematic-breaks

> - * * * * * * *
| ^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered
| ^ punctuation.definition.list_item.markdown.morkdown
|   ^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown.morkdown
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation
|       ^ punctuation.definition.thematic-break
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break
|          ^ - punctuation
|           ^ punctuation.definition.thematic-break
|            ^ - punctuation
|             ^ punctuation.definition.thematic-break
|              ^ - punctuation
|               ^ punctuation.definition.thematic-break
|                ^ - punctuation

> - * * * * * * *
>   still a list item
|   ^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown

> - - * * * * * *
| ^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered
| ^ punctuation.definition.list_item.markdown.morkdown
|   ^ punctuation.definition.list_item.markdown.morkdown
|    ^ - punctuation
|     ^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.separator.thematic-break.markdown.morkdown
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation
|       ^ punctuation.definition.thematic-break
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break
|          ^ - punctuation
|           ^ punctuation.definition.thematic-break
|            ^ - punctuation
|             ^ punctuation.definition.thematic-break
|              ^ - punctuation
|               ^ punctuation.definition.thematic-break
|                ^ - punctuation

> - - * * * * * *
>     still a list item
| <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown - meta.paragraph
| ^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown meta.paragraph.list.markdown.morkdown

> 1. * * * * * * *
| ^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered
| ^^ markup.list.numbered.bullet.markdown.morkdown
|    ^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.separator.thematic-break.markdown.morkdown
|    ^ punctuation.definition.thematic-break
|     ^ - punctuation
|      ^ punctuation.definition.thematic-break
|       ^ - punctuation
|        ^ punctuation.definition.thematic-break
|         ^ - punctuation
|          ^ punctuation.definition.thematic-break
|           ^ - punctuation
|            ^ punctuation.definition.thematic-break
|             ^ - punctuation
|              ^ punctuation.definition.thematic-break
|               ^ - punctuation
|                ^ punctuation.definition.thematic-break
|                 ^ - punctuation

> 1. * * * * * * *
>    still a list item
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown - meta.paragraph
| ^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.paragraph.list.markdown.morkdown

## https://custom-tests/block-quotes/list-blocks/unordered-items-with-atx-headings

> * list item
> # global heading
  | <- markup.quote.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown - markup.list
  |^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.heading.1.markdown.morkdown - markup.list
> 
> * list item
>  # global heading (matched as list item heading)
   | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
   |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown
>
> * list item
>   # list item heading
    | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
    |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown
> * list item
>   ## list item heading
    | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
    |^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown
>   + list item
>     ### list item heading
      | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.3.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.3.markdown.morkdown
>   + list item
>     ### list item heading
>     + list item
>       #### list item heading
        | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.4.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
        |^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.4.markdown.morkdown

> * 
>   # list item heading
    | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
    |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  
>   + 
>     # list item heading
      | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  
>   + 
>     # list item heading
>     - 
>       # list item heading 1
        | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
        |^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown   
>   + 
>     # list item heading
>     - 
>       # list item heading 1
>
>       ## list item heading 2
        | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
        |^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown

>       ## not a list item heading
        | <- markup.quote.markdown.morkdown - markup.raw
        |^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown - markup.raw
        | MO: Removed indented raw code blocks

> * 
> 
>   # list item heading
    | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
    |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  
> 
>   + 
> 
>     # list item heading
      | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  
>   + 
> 
>     # list item heading
> 
>     - 
> 
>       # list item heading 1
        | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
        |^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  
>   + 
> 
>     # list item heading
> 
>     - 
> 
>       # list item heading 1
> 
>       ## list item heading 2
        | <- markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
        |^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown

>       ## not a list item heading
        | <- markup.quote.markdown.morkdown - markup.raw
        |^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown - markup.raw
        | MO: Removed indented raw code blocks

## https://custom-tests/block-quotes/list-blocks/ordered-items-with-atx-headings

> 
> 1. list item
> # global heading
  | <- markup.quote.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown - markup.list
  |^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.heading.1.markdown.morkdown - markup.list
> 
> 2. list item
>  # global heading (matched as list item heading)
   | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
>  |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
> 
> 3. list item
>    # list item heading
     | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
     |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
>    1. list item
>       # list item heading
        | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
        |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
>    2. list item
>       # list item heading
>       1. list item
>          # list item heading
           | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
           |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
>    3. list item
>       # list item heading
        | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
        |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown

> 1. 
>    # list item heading
     | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
     |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
>    1. 
>       # list item heading
        | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
        |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
>    1. 
>       # list item heading
>       1. 
>          # list item heading
           | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
           |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
>    1. 
>       # list item heading
>       1. 
>          # list item heading
> 
>          ## list item heading 2
           | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
           |^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.2.markdown.morkdown
  
> 1. 
> 
>    # list item heading
     | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
     |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
> 
>    1. 
> 
>       # list item heading
        | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
        |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
>    1. 
> 
>       # list item heading
> 
>       1. 
> 
>          # list item heading 1
           | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
           |^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
>    1. 
> 
>       # list item heading
> 
>       1. 
> 
>          # list item heading 1
>
>          ## list item heading 2
           | <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
           |^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.2.markdown.morkdown

## https://custom-tests/block-quotes/list-blocks/items-with-fenced-code-blocks

> 1. item
>    + item
>      - item
>        ```C++
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown - meta.code-fence
| ^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown
|        ^^^ punctuation.definition.raw.code-fence.begin.markdown.morkdown
|           ^^^ constant.other.language-name.markdown.morkdown

> 1. item
>    + item
>      - item
>        ```C++
>        code
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown - meta.code-fence
| ^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.raw.code-fence.markdown-gfm.morkdown

> 1. item
>    + item
>      - item
>        ```C++
>        code
>        ```
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown - meta.code-fence
| ^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.code-fence.definition.end.text.markdown-gfm.morkdown
|        ^^^ punctuation.definition.raw.code-fence.end.markdown.morkdown

## https://custom-tests/block-quotes/list-blocks/unordered-items-with-reference-definitions

> * list item [ref]
    |         ^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.description.markdown.morkdown
>
>   + sub item [ref]
      |        ^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.description.markdown.morkdown
> 
>     [ref]: /url
      | <- markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
      |^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
      |^^^ entity.name.reference.link.markdown.morkdown
      |   ^ punctuation.definition.reference.end.markdown.morkdown
      |    ^ punctuation.separator.key-value.markdown.morkdown
      |      ^^^^ markup.underline.link.markdown.morkdown
>
>   + sub item [ref]
>     - sub item [ref]
        |        ^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.description.markdown.morkdown
>     
>       [ref]: /url
        | <- markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
        |^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
        |^^^ entity.name.reference.link.markdown.morkdown
        |   ^ punctuation.definition.reference.end.markdown.morkdown
        |    ^ punctuation.separator.key-value.markdown.morkdown
        |      ^^^^ markup.underline.link.markdown.morkdown
>
>   + sub item [ref]
>     - sub item [ref]
>     
>       [ref]: /url
>
>  [ref]: /url
   | <- markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
   |^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
   |^^^ entity.name.reference.link.markdown.morkdown
   |   ^ punctuation.definition.reference.end.markdown.morkdown
   |    ^ punctuation.separator.key-value.markdown.morkdown
   |      ^^^^ markup.underline.link.markdown.morkdown

## https://custom-tests/block-quotes/list-blocks/ordered-items-with-reference-definitions

> 1. list item [ref]
     |         ^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.description.markdown.morkdown
>
>    2. sub item [ref]
>       |        ^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.description.markdown.morkdown
>
>       [ref]: /url
        | <- markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
        |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
        |^^^ entity.name.reference.link.markdown.morkdown
        |   ^ punctuation.definition.reference.end.markdown.morkdown
        |    ^ punctuation.separator.key-value.markdown.morkdown
        |      ^^^^ markup.underline.link.markdown.morkdown
>
>    2. sub item [ref]
>       3. sub item [ref]
>          |        ^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.description.markdown.morkdown
>        
>          [ref]: /url
           | <- markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
           |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
           |^^^ entity.name.reference.link.markdown.morkdown
           |   ^ punctuation.definition.reference.end.markdown.morkdown
           |    ^ punctuation.separator.key-value.markdown.morkdown
           |      ^^^^ markup.underline.link.markdown.morkdown
>
>    2. sub item [ref]
>       3. sub item [ref]
>        
>          [ref]: /url
>          
>    [ref]: /url
     | <- markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
     |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
     |^^^ entity.name.reference.link.markdown.morkdown
     |   ^ punctuation.definition.reference.end.markdown.morkdown
     |    ^ punctuation.separator.key-value.markdown.morkdown
     |      ^^^^ markup.underline.link.markdown.morkdown

## https://custom-tests/block-quotes/list-blocks/items-with-reference-definitions

> 1. item
>    + item
>      - item [foo]
>
>        [foo]: /url "description"
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
|        ^ punctuation.definition.reference.begin.markdown.morkdown
|         ^^^ entity.name.reference.link.markdown.morkdown
|            ^ punctuation.definition.reference.end.markdown.morkdown
|             ^ punctuation.separator.key-value.markdown.morkdown
|               ^^^^ markup.underline.link.markdown.morkdown
|                    ^^^^^^^^^^^^^ meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
>        /url "description"
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
|        ^^^^ markup.underline.link.markdown.morkdown
|             ^^^^^^^^^^^^^ meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
>        /url
>        "description"
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
|        ^^^^^^^^^^^^^ meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
>        </url-with
>        -continuation>
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.markdown.morkdown
|                     ^ punctuation.definition.link.end.markdown.morkdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
         /url "description"
|<- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
|        ^^^^ markup.underline.link.markdown.morkdown
|             ^^^^^^^^^^^^^ meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
         /url
         "description"
| <- markup.quote.markdown.morkdown - meta.string - string - punctuation
|^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
|        ^^^^^^^^^^^^^ meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
         </url-with
         -continuation>
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.markdown.morkdown
|                     ^ punctuation.definition.link.end.markdown.morkdown

## https://custom-tests/block-quotes/list-blocks/items-with-footnote-definitions

> 1. list item
>    + sub item
>      - sub item [^1]
>      
>        [^1]:
>            This is a foot note
>            with a second line
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown

> 1. list item
>    + sub item
>      - sub item [^1]
>      
>        [^1]:
>            This is a foot note
>            with a second line
>        [^2]:
|        ^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown
|        ^ punctuation.definition.reference.begin.markdown.morkdown
|         ^^ entity.name.reference.link.markdown.morkdown
|           ^ punctuation.definition.reference.end.markdown.morkdown
|            ^ punctuation.separator.key-value.markdown.morkdown

> 1. list item
>    + sub item
>      - sub item [^1]
>      
>        [^1]:
>            This is a foot note
>            with a second line
>        # header
|^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown - markup.heading
| ^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown

> 1. list item
>    + sub item
>      - sub item [^1]
>      
>        [^1]:
>            This is a foot note
>            with a second line
>      - sub item
|^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
|      ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown

## https://custom-tests/block-quotes#gfm-tasks

> Block quote with GFM tasks
> * [ ] task
| ^^^^^^^^^^^ markup.quote.markdown.morkdown
| ^ markup.list.unnumbered.bullet.markdown.morkdown
|  ^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown
| ^ punctuation.definition.list_item.markdown.morkdown
|   ^ markup.checkbox.begin.markdown-gfm.morkdown punctuation.definition.checkbox.begin.markdown-gfm.morkdown
|    ^ markup.checkbox.mark.markdown-gfm.morkdown - punctuation
|     ^ markup.checkbox.end.markdown-gfm.morkdown punctuation.definition.checkbox.end.markdown-gfm.morkdown
> * [x] task
| ^^^^^^^^^^^ markup.quote.markdown.morkdown
| ^ markup.list.unnumbered.bullet.markdown.morkdown
|  ^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown
| ^ punctuation.definition.list_item.markdown.morkdown
|   ^ markup.checkbox.begin.markdown-gfm.morkdown punctuation.definition.checkbox.begin.markdown-gfm.morkdown
|    ^ markup.checkbox.mark.markdown-gfm.morkdown - punctuation
|     ^ markup.checkbox.end.markdown-gfm.morkdown punctuation.definition.checkbox.end.markdown-gfm.morkdown
> * [X] task
| ^^^^^^^^^^^ markup.quote.markdown.morkdown
| ^ markup.list.unnumbered.bullet.markdown.morkdown
|  ^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown
| ^ punctuation.definition.list_item.markdown.morkdown
|   ^ markup.checkbox.begin.markdown-gfm.morkdown punctuation.definition.checkbox.begin.markdown-gfm.morkdown
|    ^ markup.checkbox.mark.markdown-gfm.morkdown - punctuation
|     ^ markup.checkbox.end.markdown-gfm.morkdown punctuation.definition.checkbox.end.markdown-gfm.morkdown
> * [X] task
>   - [ ] task
| ^^^^^^^^^^^^^ markup.quote.markdown.morkdown
|   ^ markup.list.unnumbered.bullet.markdown.morkdown
|    ^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown
|   ^ punctuation.definition.list_item.markdown.morkdown
|     ^ markup.checkbox.begin.markdown-gfm.morkdown punctuation.definition.checkbox.begin.markdown-gfm.morkdown
|      ^ markup.checkbox.mark.markdown-gfm.morkdown - punctuation
|       ^ markup.checkbox.end.markdown-gfm.morkdown punctuation.definition.checkbox.end.markdown-gfm.morkdown

## https://custom-tests/block-quotes#emphasis

> Blcok quotes support markup,
> like *italics*, **bold**, ***bold italic*** and ~~strikethrough~~.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown
|      ^^^^^^^^^ markup.italic.markdown.morkdown
|                 ^^^^^^^^ markup.bold.markdown.morkdown
|                           ^^ markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|                             ^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|                              ^^^^^^^^^^^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown - punctuation
|                                         ^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown punctuation.definition.italic.end.markdown.morkdown
|                                          ^^ markup.bold.markdown.morkdown punctuation.definition.bold.end.markdown.morkdown
|                                                 ^^^^^^^^^^^^^^^^^ markup.strikethrough.markdown-gfm.morkdown


# TEST: LIST BLOCKS ###########################################################

## https://spec.commonmark.org/0.30/#example-253

A paragraph
with two lines.

    indented code

> A block quote.
| <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown - markup.raw
|^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown - markup.raw

## https://spec.commonmark.org/0.30/#example-254

1.  A paragraph
    with two lines.

        indented code

    > A block quote.
| <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown
|   ^ punctuation.definition.blockquote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-255

- one

 two
| <- markup.list.unnumbered.markdown.morkdown
|^^^^ markup.list.unnumbered.markdown.morkdown

> Note: `two` is not a part of the list item, but ST can't handle it!

## https://spec.commonmark.org/0.30/#example-256

- one

  two
| <- markup.list.unnumbered.markdown.morkdown
|^^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-257

 -    one

     two
| <- markup.list.unnumbered.markdown.morkdown
|^^^^^^^^ markup.list.unnumbered.markdown.morkdown

> Note: `two` is not a part of the list item, but ST can't handle it!

## https://spec.commonmark.org/0.30/#example-258

 -    one

      two
| <- markup.list.unnumbered.markdown.morkdown
|^^^^^^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-261

Note that at least one space or tab is needed between the list marker
and any following content, so these are not list items:

-one
| <- meta.paragraph.markdown.morkdown - markup.list
|^^^^ meta.paragraph.markdown.morkdown - markup.list

2.two
| <- meta.paragraph.markdown.morkdown - markup.list
|^^^^^ meta.paragraph.markdown.morkdown - markup.list

## https://spec.commonmark.org/0.30/#example-262

A list item may contain blocks that are separated by more than one blank line.

- foo


  bar
  | <- markup.list.unnumbered.markdown.morkdown
  |^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-263

1.  foo

    ```
    | <- markup.list.numbered.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
    bar
    | <- markup.list.numbered.markdown.morkdown markup.raw.code-fence.markdown-gfm.morkdown - punctuation
    ```
    | <- markup.list.numbered.markdown.morkdown meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

    baz
    | <- markup.list.numbered.markdown.morkdown

    > bam
    | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
    |^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-265

Note that ordered list start numbers must be nine digits or less:

123456789. ok
| <- markup.list.numbered.bullet.markdown.morkdown
|^^^^^^^^^ markup.list.numbered.bullet.markdown.morkdown
|         ^^^^ markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-266

1234567890. not ok
| <- meta.paragraph.markdown.morkdown - markup.list
|^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - markup.list

## https://spec.commonmark.org/0.30/#example-267

0. ok
| <- markup.list.numbered.bullet.markdown.morkdown
|^ markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^^^^ markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-268

003. ok
| <- markup.list.numbered.bullet.markdown.morkdown
|^^^ markup.list.numbered.bullet.markdown.morkdown
|  ^ punctuation.definition.list_item.markdown.morkdown
|   ^^^^ markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-269

-1. not ok
| <- meta.paragraph.markdown.morkdown - markup.list
|^^^^^^^^^^ meta.paragraph.markdown.morkdown - markup.list

## https://spec.commonmark.org/0.30/#example-282

- foo
-   
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^^ markup.list.unnumbered.markdown.morkdown

- foo
-   
- bar
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-283

1. foo
2.
| <- markup.list.numbered.bullet.markdown.morkdown
|^ markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^ markup.list.numbered.markdown.morkdown - punctuation

1. foo
2.
3. bar
| <- markup.list.numbered.bullet.markdown.morkdown
|^ markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^^^^^ markup.list.numbered.markdown.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-284

*
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^ markup.list.unnumbered.markdown.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-285

foo
*
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^ markup.list.unnumbered.markdown.morkdown - punctuation

foo
1.
| <- markup.list.numbered.bullet.markdown.morkdown
|^ markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^ markup.list.numbered.markdown.morkdown - punctuation 

## https://spec.commonmark.org/0.30/#example-286

 1.  A paragraph
     with two lines.
     |^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown

         indented code (but ST can't reliably highlight it!)
     |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown - markup.raw
     
     > A block quote.
     |^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-287

  1.  A paragraph
      with two lines.
      |^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown

          indented code (but ST can't reliably highlight it!)
      |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown - markup.raw

      > A block quote.
      | ^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-288

   1.  A paragraph
       with two lines.
       |^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown

            indented code (but ST can't reliably highlight it!)
       |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown - markup.raw

       > A block quote.
       |^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-289

    1.  A paragraph
        with two lines.
        |^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.paragraph.list.markdown.morkdown - markup.raw
        | MO: Removed indented raw code blocks

            indented code
        |^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.paragraph.list.markdown.morkdown - markup.raw
        | MO: Removed indented raw code blocks

        > A block quote.
        |^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown - markup.raw
        | ^^^^^^^^^^^^^^^ markup.paragraph.markdown.morkdown
        | MO: Removed indented raw code blocks

## https://spec.commonmark.org/0.30/#example-290

  1.  A paragraph
with two lines.
| <- markup.list.numbered.markdown.morkdown
|^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown

          indented code (but ST can't reliably highlight it!)
      |^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown - markup.raw

      > A block quote.
      | ^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-291

  1.  A paragraph
    with two lines.
    |^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-292

> 1. > Blockquote > text
|    ^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
|    ^ punctuation.definition.blockquote.markdown.morkdown
|                 ^ - punctuation

> 1. > Blockquote
continued here.
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
|^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-293

> 1. > Blockquote
> continued here.
| <- markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
|^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-294

So, in this case we need two spaces indent:

- foo
  - bar
    - baz
      - boo
| <- markup.list.unnumbered.markdown.morkdown
|^^^^^ markup.list.unnumbered.markdown.morkdown
|     ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|      ^^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-295

One is not enough:

- foo
 - bar
  - baz
   - boo
| <- markup.list.unnumbered.markdown.morkdown
|^^ markup.list.unnumbered.markdown.morkdown
|  ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|   ^^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-296

Here we need four, because the list marker is wider:

10) foo
    - bar
| <- markup.list.numbered.markdown.morkdown
|^^^ markup.list.numbered.markdown.morkdown
|   ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|    ^^^^^ markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-297

Three is not enough:

10) foo
   - bar
| <- markup.list.numbered.markdown.morkdown
|^^ markup.list.numbered.markdown.morkdown
|  ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|   ^^^^^ markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-298

A list may be the first block in a list item:

- - foo
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^ markup.list.unnumbered.markdown.morkdown
| ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|  ^^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-299

A list may be the first block in a list item:

1. - 2. foo 3. bar
| <- markup.list.numbered.bullet.markdown.morkdown
|^ markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^ markup.list.numbered.markdown.morkdown
|  ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|   ^ markup.list.unnumbered.markdown.morkdown
|    ^^ markup.list.numbered.bullet.markdown.morkdown
|      ^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown - punctuation

## https://spec.commonmark.org/0.30/#example-300

A list item can contain a heading:

- # Foo
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^^^^^ markup.list.unnumbered.markdown.morkdown
| ^^^^^^ markup.heading.1.markdown.morkdown
| ^ punctuation.definition.heading.begin.markdown.morkdown
|   ^^^ entity.name.section.markdown.morkdown


- Should be a setext heading!
  ---
| ^^^ markup.list.unnumbered.markdown.morkdown meta.separator.thematic-break.markdown.morkdown punctuation.definition.thematic-break.markdown.morkdown

- Bar
  ---
  baz
| <- markup.list.unnumbered.markdown.morkdown
|^^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-301

Changing the bullet or ordered list delimiter starts a new list:

- foo
- bar
+ baz
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-302

Changing the bullet or ordered list delimiter starts a new list:

1. foo
2. bar
3) baz
| <- markup.list.numbered.bullet.markdown.morkdown
|^ markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^^^^^ markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-303

In CommonMark, a list can interrupt a paragraph. 
That is, no blank line is needed to separate a paragraph from a following list:

Foo
- bar
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown

Foo
- bar
- baz
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-304

In order to solve of unwanted lists in paragraphs with hard-wrapped numerals, 
we allow only lists starting with 1 to interrupt paragraphs.

The number of windows in my house is
14.  The number of doors is 6.
| <- meta.paragraph.markdown.morkdown - markup.list
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - markup.list

## https://spec.commonmark.org/0.30/#example-305

We may still get an unintended result in cases like

The number of windows in my house is
1.  The number of doors is 6.
| <- markup.list.numbered.bullet.markdown.morkdown
|^ markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-306

There can be any number of blank lines between items:

- foo

- bar
  |^^^ markup.list.unnumbered.markdown.morkdown


- baz
  |^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-307

- foo
  - bar
    - baz


      bim
|^^^^^^^^ markup.list.unnumbered.markdown.morkdown - markup.raw
| MO: I'm not a fan of this, unless you can make it aware of the indentation levels. 
| I can see how, if 'bim' had started with '- ',
| it should be considered a continuation of the previous list; but, without
| the '- ', I think it should be a new paragraph. 
| How else are you supposed
| to "break out" of a list?


## https://spec.commonmark.org/0.30/#example-308

To separate consecutive lists of the same type,
you can insert a blank HTML comment:

- foo
- bar

<!-- -->
| <- meta.disable-markdown comment.block.html
|^^^^^^^ meta.disable-markdown comment.block.html

- baz
- bim

## https://spec.commonmark.org/0.30/#example-309

To separate a list from an indented code block that would otherwise 
be parsed as a subparagraph of the final list item,
you can insert a blank HTML comment:

-   foo

    notcode
    |^^^^^^^ markup.list.unnumbered.markdown.morkdown - markup.raw

-   foo

<!-- -->

    code
    |^^^^ meta.paragraph.markdown.morkdown - raw.block - markup.list
    | MO: Removed indented raw code blocks

## https://spec.commonmark.org/0.30/#example-311

List items need not be indented to the same level.

1. a
   | <- markup.list.numbered.markdown.morkdown - markup.raw

 2. b
    | <- markup.list.numbered.markdown.morkdown - markup.raw

  3. c
     | <- markup.list.numbered.markdown.morkdown - markup.raw

1) a
   | <- markup.list.numbered.markdown.morkdown - markup.raw

 2) b
    | <- markup.list.numbered.markdown.morkdown - markup.raw

  3) c
     | <- markup.list.numbered.markdown.morkdown - markup.raw

## https://spec.commonmark.org/0.30/#example-313

And here, `3. c` should be treated as in indented code block, 
because it is indented four spaces and preceded by a blank line.

1. a
   | <- markup.list.numbered.markdown.morkdown - markup.raw

  2. b
     | <- markup.list.numbered.markdown.morkdown - markup.raw

    3. c
       | <- markup.list.numbered.markdown.morkdown - markup.raw

1) a
   | <- markup.list.numbered.markdown.morkdown - markup.raw

  2) b
     | <- markup.list.numbered.markdown.morkdown - markup.raw

    3) c
       | <- markup.list.numbered.markdown.morkdown - markup.raw

> Note: ST's syntax engine and the implementation of this syntax don't support that.

## https://spec.commonmark.org/0.30/#example-314

This is a loose list, because there is a blank line between two of the list items:

- a
- b

- c
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-315

So is this, with a empty second item:

* a
*
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^ markup.list.unnumbered.markdown.morkdown
* c
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^ markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-317

- a
- b [ref]
  | ^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.description.markdown.morkdown

  [ref]: /url
  | <- markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
  |^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
  |^^^ entity.name.reference.link.markdown.morkdown
  |   ^ punctuation.definition.reference.end.markdown.morkdown
  |    ^ punctuation.separator.key-value.markdown.morkdown
  |      ^^^^ markup.underline.link.markdown.morkdown
- d
  | <- markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-318

- a
- ```
  | <- markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
  |^^ markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
  b
  | <- markup.list.unnumbered.markdown.morkdown markup.raw.code-fence.markdown-gfm.morkdown


  ```
  | <- markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
  |^^ markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

- a
- ```
  b


  ```
- c
  | <- markup.list.unnumbered.markdown.morkdown - markup.raw

## https://spec.commonmark.org/0.30/#example-319

- a
  - b

    c
    | <- markup.list.unnumbered.markdown.morkdown
- d
  | <- markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-320

* a
  > b
  >
  | <- markup.list.unnumbered.markdown.morkdown markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
  |^ markup.list.unnumbered.markdown.morkdown markup.quote.markdown.morkdown - punctuation

* a
  > b
  >
* c
  | <- markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-321

- a
  > b
  ```
  | <- markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
  |^^ markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
  c
  ```
  | <- markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
  |^^ markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

- a
  > b
  ```
  c
  ```
- d
  | <- markup.list.unnumbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-324

1. ```
   | <- markup.list.numbered.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
   |^^ markup.list.numbered.markdown.morkdown meta.code-fence.definition.begin.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
   foo
   | <- markup.list.numbered.markdown.morkdown markup.raw.code-fence.markdown-gfm.morkdown
   ```
   | <- markup.list.numbered.markdown.morkdown meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown
   |^^ markup.list.numbered.markdown.morkdown meta.code-fence.definition.end.text.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

   bar
   | <- markup.list.numbered.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-325

* foo
  * bar

  baz
  | <- markup.list.unnumbered.markdown.morkdown
  |^^^ markup.list.unnumbered.markdown.morkdown

## https://custom-tests/list-blocks/gfm-tasks

* [ ] Unticked GitHub-flavored-markdown checkbox
| ^ markup.checkbox.begin.markdown-gfm.morkdown punctuation.definition.checkbox.begin.markdown-gfm.morkdown
|  ^ markup.checkbox.mark.markdown-gfm.morkdown - punctuation
|   ^ markup.checkbox.end.markdown-gfm.morkdown punctuation.definition.checkbox.end.markdown-gfm.morkdown

* [x] Ticked GFM checkbox
| ^ markup.checkbox.begin.markdown-gfm.morkdown punctuation.definition.checkbox.begin.markdown-gfm.morkdown
|  ^ markup.checkbox.mark.markdown-gfm.morkdown - punctuation
|   ^ markup.checkbox.end.markdown-gfm.morkdown punctuation.definition.checkbox.end.markdown-gfm.morkdown

* [X] Another ticked checkbox
| ^ markup.checkbox.begin.markdown-gfm.morkdown punctuation.definition.checkbox.begin.markdown-gfm.morkdown
|  ^ markup.checkbox.mark.markdown-gfm.morkdown - punctuation
|   ^ markup.checkbox.end.markdown-gfm.morkdown punctuation.definition.checkbox.end.markdown-gfm.morkdown

* [X] Another ticked checkbox
    + [ ] Sub-item with checkbox
|     ^ markup.checkbox.begin.markdown-gfm.morkdown punctuation.definition.checkbox.begin.markdown-gfm.morkdown
|      ^ markup.checkbox.mark.markdown-gfm.morkdown - punctuation
|       ^ markup.checkbox.end.markdown-gfm.morkdown punctuation.definition.checkbox.end.markdown-gfm.morkdown

* [] Not a checkbox
| ^^ - markup.checkbox

* [/] Not a checkbox
| ^^^ - markup.checkbox

* Not [ ] a [x] checkbox [X]
| ^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup.checkbox

* [ ] [Checkbox][] with next word linked
| ^ markup.checkbox.begin.markdown-gfm.morkdown punctuation.definition.checkbox.begin.markdown-gfm.morkdown
|  ^ markup.checkbox.mark.markdown-gfm.morkdown - punctuation
|   ^ markup.checkbox.end.markdown-gfm.morkdown punctuation.definition.checkbox.end.markdown-gfm.morkdown
|     ^^^^^^^^^^^^ meta.link

## https://custom-tests/list-blocks/items-with-thematic-breaks

- * * * * * * *
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.separator.thematic-break.markdown.morkdown
| ^ punctuation.definition.thematic-break
|  ^ - punctuation
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation
|       ^ punctuation.definition.thematic-break
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break
|          ^ - punctuation
|           ^ punctuation.definition.thematic-break
|            ^ - punctuation
|             ^ punctuation.definition.thematic-break
|              ^ - punctuation

- * * * * * * *
  still a list item
| ^^^^^^^^^^^^^^^^^^ markup.list.unnumbered

- - * * * * * *
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|  ^ - punctuation
|   ^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.separator.thematic-break.markdown.morkdown
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation
|       ^ punctuation.definition.thematic-break
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break
|          ^ - punctuation
|           ^ punctuation.definition.thematic-break
|            ^ - punctuation
|             ^ punctuation.definition.thematic-break
|              ^ - punctuation

- - * * * * * *
    still a list item
|   ^^^^^^^^^^^^^^^^^^ markup.list.unnumbered

1. * * * * * * *
| <- markup.list.numbered.bullet.markdown.morkdown
|  ^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.separator.thematic-break.markdown.morkdown
|  ^ punctuation.definition.thematic-break
|   ^ - punctuation
|    ^ punctuation.definition.thematic-break
|     ^ - punctuation
|      ^ punctuation.definition.thematic-break
|       ^ - punctuation
|        ^ punctuation.definition.thematic-break
|         ^ - punctuation
|          ^ punctuation.definition.thematic-break
|           ^ - punctuation
|            ^ punctuation.definition.thematic-break
|             ^ - punctuation
|              ^ punctuation.definition.thematic-break
|               ^ - punctuation

1. * * * * * * *
   still a list item
|  ^^^^^^^^^^^^^^^^^^ markup.list.numbered

## https://custom-tests/list-blocks/items-with-atx-headings

* list item
# global heading
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown - markup.list
|^^^^^^^^^^^^^^^^ markup.heading.1.markdown.morkdown - markup.list

* list item
 # global heading (matched as list item heading)
 | <- markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
 |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown

* list item
  # list item heading
  | <- markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
  |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown
* list item
  ## list item heading
  | <- markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
  |^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown
  + list item
    ### list item heading
    | <- markup.list.unnumbered.markdown.morkdown markup.heading.3.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
    |^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.3.markdown.morkdown
    + list item
      #### list item heading
      | <- markup.list.unnumbered.markdown.morkdown markup.heading.4.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.4.markdown.morkdown

* 
  # list item heading
  | <- markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
  |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  
  + 
    # list item heading
    | <- markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
    |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  
    - 
      # list item heading 1
      | <- markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  

      ## list item heading 2
      | <- markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown

* 

  # list item heading
  | <- markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
  |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  

  + 

    # list item heading
    | <- markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
    |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  

    - 

      # list item heading 1
      | <- markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.1.markdown.morkdown  

      ## list item heading 2
      | <- markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown markup.heading.2.markdown.morkdown

1. list item
# global heading
| <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown - markup.list
|^^^^^^^^^^^^^^^^ markup.heading.1.markdown.morkdown - markup.list

2. list item
 # global heading (matched as list item heading)
 | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
 |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown

3. list item
   # list item heading
   | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
   |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
   1. list item
      # list item heading
      | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
      1. list item
         # list item heading
         | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
         |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
   2. list item
      # list item heading
      | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
      1. list item
         # list item heading
         | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
         |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown

1. 
   # list item heading
   | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
   |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
   1. 
      # list item heading
      | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown
      1. 
         # list item heading
         | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
         |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown

         ## list item heading 2
         | <- markup.list.numbered.markdown.morkdown markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
         |^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.2.markdown.morkdown

1. 

   # list item heading
   | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
   |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown

   1. 

      # list item heading
      | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
      |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown

      1. 

         # list item heading 1
         | <- markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
         |^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown

         ## list item heading 2
         | <- markup.list.numbered.markdown.morkdown markup.heading.2.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
         |^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.2.markdown.morkdown

## https://custom-tests/list-blocks/items-with-fenced-code-blocks-indented-by-tabs

  * foo
	```xml
|^^^ markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.begin.xml.markdown-gfm.morkdown punctuation.definition.raw.code-fence.begin.markdown.morkdown
|    ^^ markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.begin.xml.markdown-gfm.morkdown constant.other.language-name.markdown.morkdown
	<tag>
|^^^^^ markup.list.unnumbered.markdown.morkdown markup.raw.code-fence.xml.markdown-gfm.morkdown text.xml meta.tag.xml
	```
|^^^ markup.list.unnumbered.markdown.morkdown meta.code-fence.definition.end.xml.markdown-gfm.morkdown punctuation.definition.raw.code-fence.end.markdown.morkdown

## https://custom-tests/list-blocks/items-with-html-blocks

* list item
  
  <p>*no-markdown*</p>
  |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.disable-markdown - meta.paragraph
  |               ^^^^ meta.tag

  + sub item

    <p>*no-markdown*</p>
    |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.disable-markdown - meta.paragraph
    |               ^^^^ meta.tag

    <style>
        h1 {
            font-family: Helvetica;
        |^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.disable-markdown source.css.embedded.html meta.property-list.css
        }

        p {
            font-family: "Ubuntu Sans";
        |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.disable-markdown source.css.embedded.html meta.property-list.css
        }
    </style>
    | <- markup.list.unnumbered.markdown.morkdown meta.disable-markdown meta.tag.style.end.html punctuation.definition.tag.begin.html
    |^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.disable-markdown meta.tag.style.end.html
    |       ^ markup.list.unnumbered.markdown.morkdown meta.disable-markdown - mata.tag

    Further sub item text.
    | <- markup.list.unnumbered.markdown.morkdown
    |^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown

  + sub item
    <p>
    | <- markup.list.unnumbered.markdown.morkdown meta.disable-markdown meta.tag
    |^^ markup.list.unnumbered.markdown.morkdown meta.disable-markdown meta.tag
      *no-markodwn*
    |^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.disable-markdown - markup.italic
    </p>
    - not a list item
    | <- markup.list.unnumbered.markdown.morkdown meta.disable-markdown - punctuation
    |^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.disable-markdown - punctuation

## https://custom-tests/list-blocks/items-with-reference-definitions

* list item [ref]
  |         ^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.description.markdown.morkdown

  + sub item [ref]
    |        ^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.description.markdown.morkdown
  
    [ref]: /url
    | <- markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
    |^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
    |^^^ entity.name.reference.link.markdown.morkdown
    |   ^ punctuation.definition.reference.end.markdown.morkdown
    |    ^ punctuation.separator.key-value.markdown.morkdown
    |      ^^^^ markup.underline.link.markdown.morkdown

    - sub item [ref]
      |        ^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.description.markdown.morkdown
    
      [ref]: /url
      | <- markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
      |^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
      |^^^ entity.name.reference.link.markdown.morkdown
      |   ^ punctuation.definition.reference.end.markdown.morkdown
      |    ^ punctuation.separator.key-value.markdown.morkdown
      |      ^^^^ markup.underline.link.markdown.morkdown
 
      [ref]:
      /url
      | <- markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown
      |^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown

      [ref]: /url
      "title"
      | <- markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown
      |^^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown

      [ref]: /url
      no title
      | <- markup.list.unnumbered.markdown.morkdown meta.paragraph.list.markdown.morkdown - meta.link
      |^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.paragraph.list.markdown.morkdown - meta.link

  [ref]: /url
  | <- markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
  |^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
  |^^^ entity.name.reference.link.markdown.morkdown
  |   ^ punctuation.definition.reference.end.markdown.morkdown
  |    ^ punctuation.separator.key-value.markdown.morkdown
  |      ^^^^ markup.underline.link.markdown.morkdown

1. list item [ref]
   |         ^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.description.markdown.morkdown

   2. sub item [ref]
      |        ^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.description.markdown.morkdown
    
      [ref]: /url
      | <- markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
      |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
      |^^^ entity.name.reference.link.markdown.morkdown
      |   ^ punctuation.definition.reference.end.markdown.morkdown
      |    ^ punctuation.separator.key-value.markdown.morkdown
      |      ^^^^ markup.underline.link.markdown.morkdown

      3. sub item [ref]
         |        ^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.description.markdown.morkdown
       
         [ref]: /url
         | <- markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
         |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
         |^^^ entity.name.reference.link.markdown.morkdown
         |   ^ punctuation.definition.reference.end.markdown.morkdown
         |    ^ punctuation.separator.key-value.markdown.morkdown
         |      ^^^^ markup.underline.link.markdown.morkdown

         [ref]:
         /url
         | <- markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown
         |^^^ markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown markup.underline.link.markdown.morkdown

         [ref]: /url
         "title"
         | <- markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown
         |^^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown meta.string.title.markdown.morkdown string.quoted.double.markdown.morkdown

         [ref]: /url
         no title
         | <- markup.list.numbered.markdown.morkdown meta.paragraph.list.markdown.morkdown - meta.link
         |^^^^^^^^ markup.list.numbered.markdown.morkdown meta.paragraph.list.markdown.morkdown - meta.link

   [ref]: /url
   | <- markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown punctuation.definition.reference.begin.markdown.morkdown
   |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.def.markdown.morkdown
   |^^^ entity.name.reference.link.markdown.morkdown
   |   ^ punctuation.definition.reference.end.markdown.morkdown
   |    ^ punctuation.separator.key-value.markdown.morkdown
   |      ^^^^ markup.underline.link.markdown.morkdown

## https://custom-tests/list-blocks/items-with-footnote-definitions

1. list item
   + sub item
     - sub item [^1]
     
       [^1]:
           This is a foot note
           with a second line
| <- markup.list.numbered.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown

1. list item
   + sub item
     - sub item [^1]
     
       [^1]:
           This is a foot note
           with a second line
       [^2]:
       ^^^^^^ markup.list.numbered.markdown.morkdown meta.link.reference.def.footnote.markdown-extra.morkdown
       ^ punctuation.definition.reference.begin.markdown.morkdown
        ^^ entity.name.reference.link.markdown.morkdown
          ^ punctuation.definition.reference.end.markdown.morkdown
           ^ punctuation.separator.key-value.markdown.morkdown

1. list item
   + sub item
     - sub item [^1]
     
       [^1]:
           This is a foot note
           with a second line
       # header
|^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown

1. list item
   + sub item
     - sub item [^1]
     
       [^1]:
           This is a foot note
           with a second line
     - sub item
|^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown
|    ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown

## https://custom-tests/list-blocks/items-with-line-continuation

* list item
second line
| <- markup.list.unnumbered.markdown.morkdown
  + subitem
second line
| <- markup.list.unnumbered.markdown.morkdown
    - subitem
second line
| <- markup.list.unnumbered.markdown.morkdown
      - subitem
second line
| <- markup.list.unnumbered.markdown.morkdown

paragraph
| <- meta.paragraph.markdown.morkdown

1. list item
second line
| <- markup.list.numbered.markdown.morkdown
   2. subitem
second line
| <- markup.list.numbered.markdown.morkdown
      3. subitem
second line
| <- markup.list.numbered.markdown.morkdown
         4. subitem
second line
| <- markup.list.numbered.markdown.morkdown

paragraph
| <- meta.paragraph.markdown.morkdown

1. list item
second line
| <- markup.list.numbered.markdown.morkdown
   + subitem
second line
| <- markup.list.numbered.markdown.morkdown
     - subitem
second line
| <- markup.list.numbered.markdown.morkdown
       - subitem
second line
| <- markup.list.numbered.markdown.morkdown

paragraph
| <- meta.paragraph.markdown.morkdown

## https://custom-tests/list-blocks/items-with-block-quotes/basics

* list item

   > This is a blockquote.
   | <- markup.list.unnumbered markup.quote punctuation.definition.blockquote

  + subitem

    > This is a blockquote.
    | <- markup.list.unnumbered markup.quote punctuation.definition.blockquote

    - subitem
  
      > This is a blockquote.
      | <- markup.list.unnumbered markup.quote punctuation.definition.blockquote

      - subitem
    
        > This is a blockquote.
        | <- markup.list.unnumbered markup.quote punctuation.definition.blockquote

  This is a paragraph still part of the 
  list item
 |^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown - meta.paragraph meta.paragraph

1. list item

   > This is a blockquote.
   | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown

   2. subitem

      > This is a blockquote.
      | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
    
      3. subitem
    
         > This is a blockquote.
         | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown

   This is a paragraph still part of the 
   list item
   |^^^^^^^^^ markup.list.numbered.markdown.morkdown - meta.paragraph meta.paragraph

## https://custom-tests/list-blocks/items-with-block-quotes/block-quote-terminations

1. item
   + item
     - item
       > Block quote followed by heading
       # heading
       | <- markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
       |^^^^^^^^^ markup.heading.1.markdown.morkdown - meta.quote
       | ^^^^^^^ entity.name.section.markdown.morkdown

       > Block quote followed by unordered list
       * list item
       | <- markup.list.numbered.markdown.morkdown markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
       |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown - meta.quote

       > Block quote followed by unordered list
       + list item
       | <- markup.list.numbered.markdown.morkdown markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
       |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown - meta.quote

       > Block quote followed by unordered list
       - list item
       | <- markup.list.numbered.markdown.morkdown markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
       |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown - meta.quote

       > Block quote followed by ordered list
       1. list item
       | <- markup.list.numbered.markdown.morkdown markup.list.numbered.bullet.markdown.morkdown
       |^ markup.list.numbered.markdown.morkdown markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
       | ^^^^^^^^^^ markup.list.numbered.markdown.morkdown - meta.quote

       > Block quote followed by ordered list
       2. list item
       | <- markup.list.numbered.bullet.markdown.morkdown - punctuation
       |^ markup.list.numbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
       | ^^^^^^^^^^ markup.list.numbered.markdown.morkdown - meta.quote

       > Block quote followed by invalid list
       1234567890. no list item
       | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown
       |^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown

       > Block quote followed by html block
       <p>*no-markdown</p>
       | <- meta.disable-markdown meta.tag.block
       |^^^^^^^^^^^^^^^^^^^ meta.disable-markdown

## https://custom-tests/list-blocks/items-with-block-quotes/headings-and-paragraphs

1. item
   + item
     - item
       > # Foo
       | <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^ markup.quote.markdown.morkdown - markup.heading
       | ^^^^^^ markup.quote.markdown.morkdown markup.heading.1.markdown.morkdown
       | ^ punctuation.definition.heading.begin.markdown.morkdown
       |   ^^^ entity.name.section.markdown.morkdown
       
       > # Foo
       bar
       | <- meta.paragraph.list.markdown.morkdown - markup.quote
       |^^ meta.paragraph.list.markdown.morkdown - markup.quote
       
       > # Foo
       > bar
       | <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^^^^^ markup.quote.markdown.morkdown
       
       > # Foo
       > bar
       > baz
       | <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^^^^^ markup.quote.markdown.morkdown

       ># Foo
       | <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^^^^^^ markup.quote.markdown.morkdown markup.heading.1.markdown.morkdown
       |^ punctuation.definition.heading.begin.markdown.morkdown
       |  ^^^ entity.name.section.markdown.morkdown
       
       ># Foo
       >bar
       | <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^^^^ markup.quote.markdown.morkdown
       
       ># Foo
       >bar
       > baz
       | <- markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^^^^^ markup.quote.markdown.morkdown

## https://custom-tests/list-blocks/items-with-block-quotes/paragraphs-vs-codeblocks

1. item
   + item
     - item
       >foo 1
       >foo 2
       |^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown
       
       > foo 1
       > foo 2
       | ^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown
       
       >  foo 1
       >  foo 2
       | ^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown
       
       >   foo 1
       >   foo 2
       | ^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown

       >       foo 1
       >       foo 2
       | ^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown
       | MO: Removed indented raw code blocks

## https://custom-tests/list-blocks/items-with-nested-block-quotes

1. item
   + item
     - item
       > > Nested block quote
       | <- markup.quote punctuation.definition.blockquote
       | ^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown
       |^ - punctuation
       | ^ punctuation.definition.blockquote
       |  ^ - punctuation
       
       > > Nested quote
       > Followed by more quoted text that is not nested
       | <- markup.quote punctuation.definition.blockquote - markup.quote markup.quote
       
       >    > this is a nested quote but no code in a block quote
       | <- punctuation.definition.blockquote
       |    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown
       
       >    > this is a nested quote and no longer a code block
       >     > with a second line of content
       | <- punctuation.definition.blockquote
       |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown markup.paragraph.markdown.morkdown
       |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup.raw
       | MO: Removed indented raw code blocks
       
       >     > this is no longer code in a block quote, so it's still a nested quote
       | <- punctuation.definition.blockquote
       |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown.morkdown - markup.raw
       | MO: Removed indented raw code blocks

## https://custom-tests/list-blocks/items-with-block-quotes/list-blocks

1. item
   + item
     - item
       > Block
       > 1. item
       | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown
       | ^^ markup.list.numbered.bullet.markdown.morkdown

       > Block
       > 1. item
       >    + item
       | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
       |    ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown

       > Block
       > 1. item
       >    + item
       >      - item
       | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown
       |      ^ markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown

       > Block
       > 1. item
       >    + item
       >      - item
       >        > quote
       >        > quote
       | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown meta.paragraph.list.markdown.morkdown
       |        ^ punctuation.definition.blockquote.markdown.morkdown

       > Block
       > 1. item
       >    + item
       >      - item
       >      # heading
              | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.list.numbered.markdown.morkdown markup.heading.1.markdown.morkdown punctuation.definition.heading.begin.markdown.morkdown
       > # heading
       | <- markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown punctuation.definition.blockquote.markdown.morkdown
       |^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown - markup.heading
       | ^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.quote.markdown.morkdown markup.heading.1.markdown.morkdown
       | ^ punctuation.definition.heading.begin.markdown.morkdown
       |   ^^^^^^^ entity.name.section.markdown.morkdown

## https://custom-tests/list-blocks/items-with-code-spans

- `<foo>` | `<bar>` (foo/bar.baz)
- `<foo>` | `<my-bar>` | (foo/bar-baz.foo)
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown - markup.table

1. Open `Command Palette` using menu item `Tools → Command Palette...`
   |    ^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.raw.inline.markdown.morkdown
   |                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.raw.inline.markdown.morkdown
2. Choose `Package Control: Install Package`
   |      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown markup.raw.inline.markdown.morkdown

## https://custom-tests/list-blocks/items-with-emphasis

- test *testing
blah*
|   ^ markup.list.unnumbered markup.italic punctuation.definition.italic.end
- fgh
- *ghgh
| ^ markup.list.unnumbered markup.italic punctuation.definition.italic.begin
- fgfg
| <- markup.list.unnumbered.bullet punctuation.definition.list_item
- _test

| <- markup.list.unnumbered markup.italic invalid.illegal.non-terminated.bold-italic
  still a list item
| ^^^^^^^^^^^^^^^^^^ markup.list.unnumbered

## https://custom-tests/list-blocks/items-with-inline-html-tags

- `code` - <a name="demo"></a>
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown
| ^^^^^^ markup.raw.inline.markdown.morkdown
| ^ punctuation.definition.raw.begin.markdown.morkdown
|      ^ punctuation.definition.raw.end.markdown.morkdown
|        ^ - punctuation
|          ^^^^^^^^^^^^^^^^^^^ meta.tag.inline.a.html 

- list item

  <span>*no-markdown*</span>
  |^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.paragraph.list.markdown.morkdown
  |                  ^^^^^^^ meta.tag

  - list item
  
    <span>*no-markdown*</span>
    |^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.paragraph.list.markdown.morkdown
    |                  ^^^^^^^ meta.tag

    - list item
      
      <span>*no-markdown*</span>
      |^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown.morkdown meta.paragraph.list.markdown.morkdown
      |                  ^^^^^^^ meta.tag

## https://custom-tests/list-blocks/items-with-links-and-references

 1. [see `demo`](#demo "demo")
    | <- markup.list.numbered.markdown.morkdown meta.link.inline.description.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
    |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.inline.description.markdown.morkdown
    |           ^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.inline.metadata.markdown.morkdown
    |           ^ punctuation.definition.metadata.begin.markdown.morkdown
    |                  ^ punctuation.definition.string.begin.markdown.morkdown
    |                       ^ punctuation.definition.string.end.markdown.morkdown
    |                        ^ punctuation.definition.metadata.end.markdown.morkdown

    [see `demo`](#demo (demo))
    | <- markup.list.numbered.markdown.morkdown meta.link.inline.description.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
    |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.inline.description.markdown.morkdown
    |           ^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.inline.metadata.markdown.morkdown
    |           ^ punctuation.definition.metadata.begin.markdown.morkdown
    |                  ^ punctuation.definition.string.begin.markdown.morkdown
    |                       ^ punctuation.definition.string.end.markdown.morkdown
    |                        ^ punctuation.definition.metadata.end.markdown.morkdown

    [see `demo`](#demo 'demo')
    | <- markup.list.numbered.markdown.morkdown meta.link.inline.description.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
    |^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.inline.description.markdown.morkdown
    |           ^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.link.inline.metadata.markdown.morkdown
    |           ^ punctuation.definition.metadata.begin.markdown.morkdown
    |                  ^ punctuation.definition.string.begin.markdown.morkdown
    |                       ^ punctuation.definition.string.end.markdown.morkdown
    |                        ^ punctuation.definition.metadata.end.markdown.morkdown

    Here is a ![example image](https://test.com/sublime.png "A demonstration").
    |         ^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.image.inline.description.markdown.morkdown
    |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.image.inline.metadata.markdown.morkdown
    |                                                                         ^^ markup.list.numbered.markdown.morkdown - meta.image
    |         ^^ punctuation.definition.image.begin.markdown.morkdown
    |                        ^ punctuation.definition.image.end.markdown.morkdown
    |                         ^ punctuation.definition.metadata.begin.markdown.morkdown
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
    |                                                       ^^^^^^^^^^^^^^^^^ string.quoted.double.markdown.morkdown
    |                                                       ^ punctuation.definition.string.begin.markdown.morkdown
    |                                                                       ^ punctuation.definition.string.end.markdown.morkdown
    |                                                                        ^ punctuation.definition.metadata.end.markdown.morkdown

    Here is a ![example image](https://test.com/sublime.png 'A demonstration').
    |         ^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.image.inline.description.markdown.morkdown
    |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.image.inline.metadata.markdown.morkdown
    |                                                                         ^^ markup.list.numbered.markdown.morkdown - meta.image
    |         ^^ punctuation.definition.image.begin.markdown.morkdown
    |                        ^ punctuation.definition.image.end.markdown.morkdown
    |                         ^ punctuation.definition.metadata.begin.markdown.morkdown
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
    |                                                       ^^^^^^^^^^^^^^^^^ string.quoted.single.markdown.morkdown
    |                                                       ^ punctuation.definition.string.begin.markdown.morkdown
    |                                                                       ^ punctuation.definition.string.end.markdown.morkdown
    |                                                                        ^ punctuation.definition.metadata.end.markdown.morkdown

    Here is a ![example image](https://test.com/sublime.png (A demonstration)).
    |         ^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.image.inline.description.markdown.morkdown
    |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown.morkdown meta.image.inline.metadata.markdown.morkdown
    |                                                                         ^^ markup.list.numbered.markdown.morkdown - meta.image
    |         ^^ punctuation.definition.image.begin.markdown.morkdown
    |                        ^ punctuation.definition.image.end.markdown.morkdown
    |                         ^ punctuation.definition.metadata.begin.markdown.morkdown
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
    |                                                       ^^^^^^^^^^^^^^^^^ string.quoted.other.markdown.morkdown
    |                                                       ^ punctuation.definition.string.begin.markdown.morkdown
    |                                                                       ^ punctuation.definition.string.end.markdown.morkdown
    |                                                                        ^ punctuation.definition.metadata.end.markdown.morkdown


# TEST: CODE SPANS ############################################################

```testing``123```
| <- punctuation.definition.raw.begin
|         ^^ - punctuation
|              ^^^ punctuation.definition.raw.end

```testing``123````
| <- punctuation.definition.raw.begin
|        ^ - punctuation
|            ^^^^ - punctuation
```
| <- punctuation.definition.raw.end

``testing`123````
| <- punctuation.definition.raw.begin
|        ^ - punctuation
|            ^^^^ - punctuation
more text``
|        ^^ punctuation.definition.raw.end

``text

| <- invalid.illegal.non-terminated.raw
text
| <- - markup.raw

## https://spec.commonmark.org/0.30/#example-327

`hi`lo`
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^ markup.raw.inline.markdown.morkdown
|  ^ punctuation.definition.raw.end.markdown.morkdown
|   ^^ - markup.raw

## https://spec.commonmark.org/0.30/#example-328

`foo`
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^^ meta.paragraph.markdown.morkdown markup.raw.inline.markdown.morkdown
|   ^ punctuation.definition.raw.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-329

`` foo ` bar  ``
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^^^^^^^^^^^^^ markup.raw.inline.markdown.morkdown
|^ punctuation.definition.raw.begin.markdown.morkdown
|      ^ - punctuation
|             ^^ punctuation.definition.raw.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-330

` `` `
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^^^ markup.raw.inline.markdown.morkdown
| ^^ - punctuation
|    ^ punctuation.definition.raw.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-331

`  ``  `
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^^^^^ markup.raw.inline.markdown.morkdown
|  ^^ - punctuation
|      ^ punctuation.definition.raw.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-332

` a`
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^ markup.raw.inline.markdown.morkdown
|  ^ punctuation.definition.raw.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-333

` b `
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^^ markup.raw.inline.markdown.morkdown
|   ^ punctuation.definition.raw.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-334

` `
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^ markup.raw.inline.markdown.morkdown
| ^ punctuation.definition.raw.end.markdown.morkdown
|  ^ - markup 

`  `
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^ markup.raw.inline.markdown.morkdown
|  ^ punctuation.definition.raw.end.markdown.morkdown
|   ^ - markup 

## https://spec.commonmark.org/0.30/#example-335

``
foo
bar  
baz
``
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.end.markdown.morkdown
|^ markup.raw.inline.markdown.morkdown punctuation.definition.raw.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-336

``
foo 
``
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.end.markdown.morkdown
|^ markup.raw.inline.markdown.morkdown punctuation.definition.raw.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-337

`foo   bar
  baz`
|^^^^^ markup.raw.inline.markdown.morkdown
|    ^ punctuation.definition.raw.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-338

`foo\`bar`
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^^^ markup.raw.inline.markdown.morkdown
|     ^^^ - markup.raw

## https://spec.commonmark.org/0.30/#example-339

``foo`bar``
| <- meta.paragraph.markdown.morkdown markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^^^^^^^^ meta.paragraph.markdown.morkdown markup.raw.inline.markdown.morkdown
|^ punctuation.definition.raw.begin.markdown.morkdown
| ^^^^^^^ - punctuation
|        ^^ punctuation.definition.raw.end.markdown.morkdown

````bar```` baz
|^^^^^^^^^^ markup.raw.inline.markdown.morkdown
|          ^^^^^ - markup.raw

## https://spec.commonmark.org/0.30/#example-340

`foo `` bar`
| <- markup.raw.inline.markdown.morkdown punctuation.definition.raw.begin.markdown.morkdown
|^^^^^^^^^^ markup.raw.inline.markdown.morkdown - punctuation
|          ^ markup.raw.inline.markdown.morkdown punctuation.definition.raw.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-341

*foo`*`
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|   ^^^ markup.italic.markdown.morkdown markup.raw.inline.markdown.morkdown

| <- invalid.illegal.non-terminated.bold-italic

## https://spec.commonmark.org/0.30/#example-342

[not a `link](/foo`)
|^^^^^^^^^^^^^^^^^^^ - meta.link
|      ^^^^^^^^^^^^ markup.raw.inline.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-343

`<a href="`">`
|^^^^^^^^^^ markup.raw.inline.markdown.morkdown
|          ^^ - markup.raw

| <- invalid.illegal.non-terminated.raw

## https://spec.commonmark.org/0.30/#example-344

<a href="`">`
| ^^^^^^^^^ meta.tag.inline.a
|           ^ punctuation.definition.raw.begin

| <- invalid.illegal.non-terminated.raw

## https://spec.commonmark.org/0.30/#example-345

`<http://foo.bar.`baz>`
|^^^^^^^^^^^^^^^^^ markup.raw.inline
|                     ^ punctuation.definition.raw.begin

| <- invalid.illegal.non-terminated.raw

## https://spec.commonmark.org/0.30/#example-346

<http://foo.bar.`baz>`
|^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                    ^ punctuation.definition.raw.begin

| <- invalid.illegal.non-terminated.raw


# TEST: EMPHASIS ##############################################################

## https://spec.commonmark.org/0.30/#example-350

*foo bar*
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^ markup.italic.markdown.morkdown
|       ^ punctuation.definition.italic.end

## https://spec.commonmark.org/0.30/#example-351

This is not emphasis, because the opening `*` is followed by whitespace, and hence not part of a left-flanking delimiter run:

a * foo bar*
| ^^^^^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-352

a*"foo"*
| <- - markup.italic - punctuation
|^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-353

* a *
| <- markup.list.unnumbered.bullet.markdown.morkdown punctuation.definition.list_item.markdown.morkdown - markup.italic
|^^^^^ markup.list.unnumbered.markdown.morkdown - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-354

Intraword emphasis with `*` is permitted:

foo*bar*
| <- - markup.italic
|^^ - markup.italic
|  ^^^^^ markup.italic.markdown.morkdown
|  ^ punctuation.definition.italic.begin.markdown.morkdown
|      ^ punctuation.definition.italic.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-355

5*6*78
| <- - markup.italic
|^^^ markup.italic.markdown.morkdown
|^ punctuation.definition.italic.begin.markdown.morkdown
|  ^ punctuation.definition.italic.end.markdown.morkdown
|   ^^ - markup.italic

## https://spec.commonmark.org/0.30/#example-356

_foo bar_
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^ meta.paragraph.markdown.morkdown markup.italic.markdown.morkdown
|       ^ punctuation.definition.italic.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-357

This is not emphasis, because the opening `_` is followed by whitespace:

_ foo bar_
| <- - markup.italic - punctuation
|^^^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-358

This is not emphasis, because the opening `_` is preceded by an alphanumeric and followed by punctuation:

a_"foo"_
| <- - markup.italic - punctuation
|^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-359

Emphasis with `_` is not allowed inside words:

foo_bar_
| <- - markup.italic - punctuation
|^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-360

5_6_78
| <- - markup.italic - punctuation
|^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-361

пристаням_стремятся_
| <- - markup.italic - punctuation
|^^^^^^^^^^^^^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-362

Here `_` does not generate emphasis, because the first delimiter run is right-flanking
and the second left-flanking:

aa_"bb"_cc
| <- - markup.italic - punctuation
|^^^^^^ - markup.italic - punctuation

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-363

This is emphasis, even though the opening delimiter is both left- and right-flanking,
because it is preceded by punctuation:

foo-_(bar)_
| <- - markup.italic - punctuation
|^^^ - markup.italic - punctuation
|   ^^^^^^^ markup.italic.markdown.morkdown
|   ^ punctuation.definition.italic.begin.markdown.morkdown
|         ^ punctuation.definition.italic.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-365

This is not emphasis, because the closing `*` is preceded by whitespace:

*foo bar *
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^^^ markup.italic.markdown.morkdown

| <- markup.italic.markdown.morkdown invalid.illegal.non-terminated.bold-italic.markdown.morkdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-366

A line ending also counts as whitespace:

*foo bar *
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^^^ markup.italic.markdown.morkdown
|        ^ - punctuation
*
| <- markup.italic.markdown.morkdown - punctuation
abc*
| <- markup.italic.markdown.morkdown
|^^^ meta.paragraph.markdown.morkdown markup.italic.markdown.morkdown
|  ^ punctuation.definition.italic.end.markdown.morkdown
|   ^ - markup.italic

## https://spec.commonmark.org/0.30/#example-367

This is not emphasis, because the second `*` is preceded by punctuation and followed
by an alphanumeric (hence it is not part of a right-flanking delimiter run):

*(*foo)

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-368

The point of this restriction is more easily appreciated with this example:

*(*foo*)*

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-369

Intraword emphasis with `*` is allowed:

*foo*bar
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^ markup.italic.markdown.morkdown
|   ^ punctuation.definition.italic.end.markdown.morkdown
|    ^^^^ - markup.italic

## https://spec.commonmark.org/0.30/#example-370

This is not emphasis, because the closing `_` is preceded by whitespace:

_foo bar _
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^^^ markup.italic.markdown.morkdown
|        ^ - punctuation

| <- markup.italic.markdown.morkdown invalid.illegal.non-terminated.bold-italic.markdown.morkdown

> Note: Needs ST4's branching to get it right!

_foo bar _
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^^^ markup.italic.markdown.morkdown
|        ^ - punctuation
_
| <- markup.italic.markdown.morkdown - punctuation
abc_
| <- markup.italic.markdown.morkdown
|^^^ markup.italic.markdown.morkdown
|  ^ punctuation.definition.italic.end
|   ^ - markup.italic

## https://spec.commonmark.org/0.30/#example-371

This is not emphasis, because the second `_` is preceded by punctuation and followed
by an alphanumeric (hence it is not part of a right-flanking delimiter run):

_(_foo)

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-371

The point of this restriction is more easily appreciated with this example:

_(_foo_)_

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-373

Intraword emphasis is disallowed for `_`:

_foo_bar
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^ markup.italic.markdown.morkdown
|   ^ - punctuation
abc_
| <- markup.italic.markdown.morkdown
|^^^ markup.italic.markdown.morkdown
|  ^ punctuation.definition.italic.end.markdown.morkdown
|   ^ - markup.italic

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-374

Intraword emphasis is disallowed for `_`:

_пристаням_стремятся
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^ markup.italic.markdown.morkdown

| <- markup.italic.markdown.morkdown invalid.illegal.non-terminated.bold-italic.markdown.morkdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-375

_foo_bar_baz_
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^^^^^ markup.italic.markdown.morkdown
|   ^^^^^ - punctuation
|           ^ punctuation.definition.italic.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-376

This is emphasis, even though the closing delimiter is both left- and right-flanking,
because it is followed by punctuation:

_(bar)_.
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^ markup.italic.markdown.morkdown
|     ^ punctuation.definition.italic.end.markdown.morkdown
|      ^^ - markup.italic

## https://spec.commonmark.org/0.30/#example-377

**foo bar**
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown
|        ^^ punctuation.definition.bold.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-378

** foo bar**
| <- - markup - punctuation
|^^^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-379

This is not strong emphasis, because the opening `**` is preceded by an alphanumeric
and followed by punctuation, and hence not part of a left-flanking delimiter run:

a**"foo"**
| <- - markup - punctuation
|^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-380

Intraword strong emphasis with `**` is permitted:

foo**bar**
| <- - markup
|^^ - markup
|  ^^^^^^^ meta.paragraph.markdown.morkdown markup.bold.markdown.morkdown
|  ^^ punctuation.definition.bold.begin.markdown.morkdown
|       ^^ punctuation.definition.bold.end.markdown.morkdown
|         ^ - markup

## https://spec.commonmark.org/0.30/#example-381

__foo bar__
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown
|        ^^ punctuation.definition.bold.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-382

This is not strong emphasis, because the opening delimiter is followed by whitespace:
__ foo bar__
| <- - markup - punctuation
|^^^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-383

__
| <- - punctuation
|^ - punctuation

## https://spec.commonmark.org/0.30/#example-384

a__"foo"__
| <- - markup - punctuation
|^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-385

Intraword strong emphasis is forbidden with `__`:
foo__bar__
| <- - markup - punctuation
|^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-386

5__6__78
| <- - markup - punctuation
|^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-387

пристаням__стремятся__
| <- - markup - punctuation
|^^^^^^^^^^^^^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-389

foo-__(bar)__
| <- - markup
|^^^ - markup
|   ^^^^^^^^^ markup.bold.markdown.morkdown
|   ^^ punctuation.definition.bold.begin.markdown.morkdown
|          ^^ punctuation.definition.bold.end.markdown.morkdown
|            ^ - markup

## https://spec.commonmark.org/0.30/#example-390

**foo bar **
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^^^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown 
|         ^^ - punctuation

| <- markup.bold.markdown.morkdown invalid.illegal.non-terminated.bold-italic.markdown.morkdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-394

**foo "*bar*" foo**
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^ markup.bold.markdown.morkdown - markup.italic
|^ punctuation.definition.bold.begin.markdown.morkdown
|      ^^^^^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown
|      ^ punctuation.definition.italic.begin.markdown.morkdown
|          ^ punctuation.definition.italic.end.markdown.morkdown
|           ^^^^^^^ markup.bold.markdown.morkdown - markup.italic
|                ^^ punctuation.definition.bold.end.markdown.morkdown
|                  ^ - markup

## https://spec.commonmark.org/0.30/#example-395

Intraword emphasis:
 
**foo**bar
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^ markup.bold.markdown.morkdown
|    ^^ punctuation.definition.bold.end.markdown.morkdown
|      ^^^^ - markup

## https://spec.commonmark.org/0.30/#example-396

__foo bar __
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^^^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown 
|         ^^ - punctuation

| <- markup.bold.markdown.morkdown invalid.illegal.non-terminated.bold-italic.markdown.morkdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-397

This is not strong emphasis, because the second `__` 
is preceded by punctuation and followed by an alphanumeric:

__(__foo)

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-398

_(__foo__)_
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
| ^^^^^^^ markup.italic.markdown.morkdown markup.bold.markdown.morkdown
| ^^ punctuation.definition.bold.begin.markdown.morkdown
|      ^^ punctuation.definition.bold.end.markdown.morkdown
|         ^ punctuation.definition.italic.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-399

Intraword strong emphasis is forbidden with `__`:
__foo__bar
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown 
|    ^^ - punctuation

| <- markup.bold.markdown.morkdown invalid.illegal.non-terminated.bold-italic.markdown.morkdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-400

__пристаням__стремятся
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown 
|          ^^ - punctuation

| <- markup.bold.markdown.morkdown invalid.illegal.non-terminated.bold-italic.markdown.morkdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-401

__foo__bar__baz__
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown 
|    ^^^^^^^ - punctuation
|              ^^ punctuation.definition.bold.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-402

This is strong emphasis, even though the closing delimiter is both left- and right-flanking,
because it is followed by punctuation:

__(bar)__.
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown 
|      ^^ punctuation.definition.bold.end.markdown.morkdown
|        ^^ - markup

## https://spec.commonmark.org/0.30/#example-403

Any nonempty sequence of inline elements can be the contents of an emphasized span.

*foo [bar](/url)*
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^ markup.italic.markdown.morkdown
|    ^^^^^^^^^^^ meta.link.inline
|               ^ punctuation.definition.italic.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-404

*foo
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^ markup.italic.markdown.morkdown
bar*
| <- markup.italic.markdown.morkdown
|^^^ markup.italic.markdown.morkdown
|  ^ punctuation.definition.italic.end
|   ^ - markup

## https://spec.commonmark.org/0.30/#example-405

_foo __bar__ baz_
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^ markup.italic.markdown.morkdown - markup markup
|    ^^ punctuation.definition.bold.begin.markdown.morkdown
|    ^^^^^^^ markup.italic.markdown.morkdown markup.bold.markdown.morkdown
|         ^^ punctuation.definition.bold.end.markdown.morkdown
|           ^^^^^ markup.italic.markdown.morkdown - markup markup
|               ^ punctuation.definition.italic.end.markdown.morkdown
|                ^ - markup

## https://spec.commonmark.org/0.30/#example-418

*foo [*bar*](/url)*
| <-  markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^ markup.italic.markdown.morkdown - markup.italic markup.italic
|    ^^^^^^^^^^^^^ meta.link.inline
|     ^^^^^ markup.italic.markdown.morkdown markup.italic.markdown.morkdown
|          ^^^^^^^ markup.italic.markdown.morkdown - markup.italic markup.italic

*foo [_bar_](/url)*
| <-  markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^ markup.italic.markdown.morkdown - markup.italic markup.italic
|    ^^^^^^^^^^^^^ meta.link.inline
|     ^^^^^ markup.italic.markdown.morkdown markup.italic.markdown.morkdown
|          ^^^^^^^ markup.italic.markdown.morkdown - markup.italic markup.italic

_foo [_bar_](/url)_
| <-  markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^ markup.italic.markdown.morkdown - markup.italic markup.italic
|    ^^^^^^^^^^^^^ meta.link.inline
|     ^^^^^ markup.italic.markdown.morkdown markup.italic.markdown.morkdown
|          ^^^^^^^ markup.italic.markdown.morkdown - markup.italic markup.italic

_foo [**bar**](/url)_
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^ markup.italic.markdown.morkdown - markup.italic markup.bold
|    ^^^^^^^^^^^^^^^ meta.link.inline
|     ^^ punctuation.definition.bold.begin.markdown.morkdown
|     ^^^^^^^ markup.italic.markdown.morkdown markup.bold.markdown.morkdown
|          ^^ punctuation.definition.bold.end.markdown.morkdown
|            ^^^^^^^^ markup.italic.markdown.morkdown - markup.italic markup.bold
|                   ^ punctuation.definition.italic.end.markdown.morkdown

_foo [__bar__](/url)_
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^ markup.italic.markdown.morkdown - markup.italic markup.bold
|    ^^^^^^^^^^^^^^^ meta.link.inline
|     ^^ punctuation.definition.bold.begin.markdown.morkdown
|     ^^^^^^^ markup.italic.markdown.morkdown markup.bold.markdown.morkdown
|          ^^ punctuation.definition.bold.end.markdown.morkdown
|            ^^^^^^^^ markup.italic.markdown.morkdown - markup.italic markup.bold
|                   ^ punctuation.definition.italic.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-419

** is not an empty emphasis
| <- - punctuation
|^ - punctuation

## https://spec.commonmark.org/0.30/#example-420

**** is not an empty strong emphasis
| <- - punctuation
|^^^ - punctuation

## https://spec.commonmark.org/0.30/#example-421

**foo [bar](/url)**
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown
|     ^^^^^^^^^^^ meta.link.inline
|                ^^ punctuation.definition.bold.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-422

**foo
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown
bar**
| <- markup.bold.markdown.morkdown
|^^^^ markup.bold.markdown.morkdown
|  ^^ punctuation.definition.bold.end
|    ^ - markup

## https://spec.commonmark.org/0.30/#example-423

__foo _bar_ baz__
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^ markup.bold.markdown.morkdown - markup markup
|^ punctuation.definition.bold.begin.markdown.morkdown
|     ^ punctuation.definition.italic.begin.markdown.morkdown
|     ^^^^^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown
|         ^ punctuation.definition.italic.end.markdown.morkdown
|          ^^^^^^ markup.bold.markdown.morkdown - markup markup
|               ^ punctuation.definition.bold.end.markdown.morkdown
|                ^ - markup

## https://spec.commonmark.org/0.30/#example-432

**foo [*bar*](/url)**
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^ markup.bold.markdown.morkdown - markup.bold markup.italic
|     ^^^^^^^^^^^^^ meta.link.inline
|^ punctuation.definition.bold.begin.markdown.morkdown
|      ^ punctuation.definition.italic.begin.markdown.morkdown
|      ^^^^^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown
|          ^ punctuation.definition.italic.end.markdown.morkdown
|           ^^^^^^^^^ markup.bold.markdown.morkdown - markup.bold markup.italic
|                  ^^ punctuation.definition.bold.end.markdown.morkdown

**foo [_bar_](/url)**
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^ markup.bold.markdown.morkdown - markup.bold markup.italic
|     ^^^^^^^^^^^^^ meta.link.inline
|^ punctuation.definition.bold.begin.markdown.morkdown
|      ^ punctuation.definition.italic.begin.markdown.morkdown
|      ^^^^^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown
|          ^ punctuation.definition.italic.end.markdown.morkdown
|           ^^^^^^^^^ markup.bold.markdown.morkdown - markup.bold markup.italic
|                  ^^ punctuation.definition.bold.end.markdown.morkdown

## https://spec.commonmark.org/0.30/#example-433

__ is not an empty emphasis
| <- - markup - punctuation
|^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-434

____ is not an empty strong emphasis
| <- - markup - punctuation
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-435

foo ***
|   ^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-436

foo *\**
|^^^ - markup
|   ^^^^ markup.italic.markdown.morkdown
|   ^ punctuation.definition.italic.begin.markdown.morkdown
|    ^^ constant.character.escape.markdown.morkdown
|      ^ punctuation.definition.italic.end.markdown.morkdown
|       ^ - markup

## https://spec.commonmark.org/0.30/#example-437

foo *_*
|^^^ - markup
|   ^^^ markup.italic.markdown.morkdown
|   ^punctuation.definition.italic.begin.markdown.morkdown
|     ^ punctuation.definition.italic.end.markdown.morkdown
|      ^ - markup

## https://spec.commonmark.org/0.30/#example-439

foo **\***
|^^^ - markup
|   ^^^^^^ markup.bold.markdown.morkdown
|   ^^ punctuation.definition.bold.begin.markdown.morkdown
|     ^^ constant.character.escape.markdown.morkdown
|       ^^ punctuation.definition.bold.end.markdown.morkdown
|         ^ - markup

## https://spec.commonmark.org/0.30/#example-440

foo **_**
|^^^ - markup
|   ^^^^^ markup.bold.markdown.morkdown
|   ^^punctuation.definition.bold.begin.markdown.morkdown
|      ^^ punctuation.definition.bold.end.markdown.morkdown
|        ^ - markup

## https://spec.commonmark.org/0.30/#example-441

**foo*

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-442

*foo**

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-443

***foo**

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-444

****foo*

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-445

**foo***
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^^^^^^ markup.bold.markdown.morkdown
|^ punctuation.definition.bold.begin.markdown.morkdown
|    ^^ punctuation.definition.bold.end.markdown.morkdown
|      ^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-446

*foo****

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-447

foo ___
|   ^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-448

foo _\__
|^^^ - markup
|   ^^^^ markup.italic.markdown.morkdown
|   ^ punctuation.definition.italic.begin.markdown.morkdown
|    ^^ constant.character.escape.markdown.morkdown
|      ^ punctuation.definition.italic.end.markdown.morkdown
|       ^ - markup

## https://spec.commonmark.org/0.30/#example-449

foo _*_
|^^^ - markup
|   ^^^ markup.italic.markdown.morkdown
|   ^punctuation.definition.italic.begin.markdown.morkdown
|     ^ punctuation.definition.italic.end.markdown.morkdown
|      ^ - markup

## https://spec.commonmark.org/0.30/#example-450

foo _____
|   ^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-451

foo __\___
|^^^ - markup
|   ^^^^^^ markup.bold.markdown.morkdown
|   ^^ punctuation.definition.bold.begin.markdown.morkdown
|     ^^ constant.character.escape.markdown.morkdown
|       ^^ punctuation.definition.bold.end.markdown.morkdown
|         ^ - markup

## https://spec.commonmark.org/0.30/#example-452

foo __*__
|^^^ - markup
|   ^^^^^ markup.bold.markdown.morkdown
|   ^^punctuation.definition.bold.begin.markdown.morkdown
|      ^^ punctuation.definition.bold.end.markdown.morkdown
|        ^ - markup

## https://custom-tests/emphasis

This text is _italic_, but this__text__is neither bold_nor_italic
|            ^ punctuation.definition.italic
|             ^^^^^^ markup.italic
|                   ^ punctuation.definition.italic
|                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup.bold - markup.italic

the following is italic *and doesn't end here * but does end here*
|                       ^ punctuation.definition.italic.begin
|                                             ^ - punctuation.definition.italic
|                                                                ^ punctuation.definition.italic.end

the following is bold **and doesn't end here ** but does end here**
|                     ^^ punctuation.definition.bold.begin
|                                            ^^ - punctuation.definition.bold
|                                                                ^^ punctuation.definition.bold.end

the following is not bold ** test ****
|                         ^^ - punctuation.definition.bold.begin
|                                 ^^^^ - punctuation.definition.bold

the following is not italic _ test ____
|                           ^ - punctuation.definition.italic.begin
|                                  ^^^^ - punctuation.definition.italic

more **tests *** ** here**
|    ^^ punctuation.definition.bold.begin
|            ^^^^^^ - punctuation.definition
|                       ^^ punctuation.definition.bold.end

more __tests *** ** example __ here__
|    ^^ punctuation.definition.bold.begin
|            ^^^^^^^^^^^^^^^^^^^^^^ - punctuation.definition
|                                  ^^ punctuation.definition.bold.end

more _tests <span class="test_">here</span>_
|    ^ punctuation.definition.italic.begin
|                            ^ - punctuation.definition
|                                          ^ punctuation.definition.italic.end

more _tests <span class="test_">_here</span>_
|    ^ punctuation.definition.italic.begin
|                            ^ - punctuation.definition
|                               ^ - punctuation
|                                           ^ punctuation.definition.italic.end

_more `tests_` here_
| <- punctuation.definition.italic.begin
|     ^^^^^^^^ markup.raw.inline
|                  ^ punctuation.definition.italic.end

__more `tests__` here__
| <- punctuation.definition.bold.begin
|      ^^^^^^^^^ markup.raw.inline
|                    ^^ punctuation.definition.bold.end

**more `tests__` here**
| <- punctuation.definition.bold.begin
|      ^^^^^^^^^ markup.raw.inline
|                    ^^ punctuation.definition.bold.end

**more `tests**` here**
| <- punctuation.definition.bold.begin
|      ^^^^^^^^^ markup.raw.inline
|                    ^^ punctuation.definition.bold.end

*more `tests__` here**
| <- punctuation.definition.italic.begin
|                   ^^ - punctuation
abc*
|  ^ punctuation.definition.italic.end

This is ***bold italic***
|       ^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^ punctuation.definition.bold.end

This is ***bold italic* and just bold**
|       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^^^^^^^^^^^^^^^ - markup.italic
|                                    ^^ punctuation.definition.bold.end

The next scope overlap funny because we have to pick one order
to scope three indicators in a row
This is ***bold italic** and just italic*
|       ^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.italic
|         ^ punctuation.definition.italic.begin
|                     ^^ punctuation.definition.bold.end
|                       ^^^^^^^^^^^^^^^^^ - markup.bold
|                                       ^ punctuation.definition.italic.end

This is **_bold italic_**
|       ^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^ punctuation.definition.bold.end

This is __*bold italic*__
|       ^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^ punctuation.definition.bold.end

This is ___bold italic___
|       ^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^ punctuation.definition.bold.end

This is ___bold italic_ and just bold__
|       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^^^^^^^^^^^^^^^ - markup.italic
|                                    ^^ punctuation.definition.bold.end

The next scope overlap funny because we have to pick one order
to scope three indicators in a row
This is ___bold italic__ and just italic_
|       ^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.italic
|         ^ punctuation.definition.italic.begin
|                     ^^ punctuation.definition.bold.end
|                       ^^^^^^^^^^^^^^^^^ - markup.bold
|                                       ^ punctuation.definition.italic.end

This is _**italic bold**_
|       ^^^^^^^^^^^^^^^^^ markup.italic
|       ^ punctuation.definition.italic.begin
|        ^^^^^^^^^^^^^^^ markup.bold
|        ^^ punctuation.definition.bold.begin
|                     ^^ punctuation.definition.bold.end
|                       ^ punctuation.definition.italic.end

This is *__italic bold__*
|       ^^^^^^^^^^^^^^^^^ markup.italic
|       ^ punctuation.definition.italic.begin
|        ^^^^^^^^^^^^^^^ markup.bold
|        ^^ punctuation.definition.bold.begin
|                     ^^ punctuation.definition.bold.end
|                       ^ punctuation.definition.italic.end

**test!_test** Issue 1163
|^^^^^^^^^^^^^ markup.bold
|      ^ - punctuation.definition.italic
|           ^^ punctuation.definition.bold.end

__test!*test__ Issue 1163
|^^^^^^^^^^^^^ markup.bold
|      ^ - punctuation.definition.italic
|           ^^ punctuation.definition.bold.end

*test

| <- invalid.illegal.non-terminated.bold-italic
abc*
|  ^ - punctuation

_test

| <- invalid.illegal.non-terminated.bold-italic
abc_
|  ^ - punctuation

**test

| <- invalid.illegal.non-terminated.bold-italic
abc**
|  ^^ - punctuation

__test

| <- invalid.illegal.non-terminated.bold-italic
abc__
|  ^^ - punctuation

__test\
|     ^ meta.hard-line-break constant.character.escape
testing__

*italic text <span>HTML element</span> end of italic text*
| <- punctuation.definition.italic
|                                                        ^ punctuation.definition.italic
|            ^^^^^^ meta.tag.inline.any.html
|                              ^^^^^^^ meta.tag.inline.any.html

_italic text <SPAN>HTML element</SPAN> end of italic text_
| <- punctuation.definition.italic
|                                                        ^ punctuation.definition.italic
|            ^^^^^^ meta.tag.inline.any.html
|                              ^^^^^^^ meta.tag.inline.any.html

**bold text <span>HTML element</span> end of bold text**
| <- punctuation.definition.bold
|                                                     ^^ punctuation.definition.bold
|           ^^^^^^ meta.tag.inline.any.html
|                             ^^^^^^^ meta.tag.inline.any.html

__bold text <span>HTML element</span> end of bold text__
| <- punctuation.definition.bold
|                                                     ^^ punctuation.definition.bold
|           ^^^^^^ meta.tag.inline.any.html
|                             ^^^^^^^ meta.tag.inline.any.html

*italic text <span>HTML element</span> end of italic text*
| <- punctuation.definition.italic
|                                                        ^ punctuation.definition.italic
|            ^^^^^^ meta.tag.inline.any.html
|                              ^^^^^^^ meta.tag.inline.any.html

_italic text <span>HTML element</span> end of italic text_
| <- punctuation.definition.italic
|                                                        ^ punctuation.definition.italic
|            ^^^^^^ meta.tag.inline.any.html
|                              ^^^^^^^ meta.tag.inline.any.html

_test <span>text_ foobar</span>
| <- punctuation
|               ^ punctuation.definition.italic.end

__test <span>text__ not formatted</span>
| <- punctuation
|                ^^ punctuation.definition.bold.end

*test <span>text* not formatted</span>
| <- punctuation
|               ^ punctuation.definition.italic.end

**test <span>text** not formatted</span>
| <- punctuation
|                ^^ punctuation.definition.bold.end

_test <span>text **formatted**</span>_
| <- punctuation
|                ^^ punctuation
|                           ^^ punctuation
|                                    ^ punctuation

*test <span>text __formatted__</span>*
| <- punctuation
|                ^^ punctuation
|                           ^^ punctuation
|                                    ^ punctuation

*test <span>text __formatted__</span>* **more** _text_
| <- punctuation
|                ^^ punctuation
|                           ^^ punctuation
|                                    ^ punctuation
|                                      ^^ punctuation
|                                            ^^ punctuation
|                                               ^ punctuation
|                                                    ^ punctuation

*test <span>text* __formatted</span>__
| <- punctuation
|               ^ punctuation
|                 ^^ punctuation
|                                   ^^ punctuation

__test <span>text__ *formatted</span>*
| <- punctuation
|                ^^ punctuation
|                   ^ punctuation
|                                    ^ punctuation

# TEST: STRIKETHROUGH #########################################################

__~~bold striked~~__
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^ markup.bold.markdown.morkdown - markup.strikethrough
| ^^^^^^^^^^^^^^^^ markup.bold.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown
|                 ^^ markup.bold.markdown.morkdown - markup.strikethrough
|^ punctuation.definition.bold.begin.markdown.morkdown
| ^^ punctuation.definition.strikethrough.begin.markdown.morkdown
|               ^^ punctuation.definition.strikethrough.end.markdown.morkdown 
|                 ^^ punctuation.definition.bold.end.markdown.morkdown

**~~bold striked~~**
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^ markup.bold.markdown.morkdown - markup.strikethrough
| ^^^^^^^^^^^^^^^^ markup.bold.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown
|                 ^^ markup.bold.markdown.morkdown - markup.strikethrough
|^ punctuation.definition.bold.begin.markdown.morkdown
| ^^ punctuation.definition.strikethrough.begin.markdown.morkdown
|               ^^ punctuation.definition.strikethrough.end.markdown.morkdown 
|                 ^^ punctuation.definition.bold.end.markdown.morkdown

_~~italic striked~~_
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^ markup.italic.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown
|                  ^ markup.italic.markdown.morkdown - markup.strikethrough
|^^ punctuation.definition.strikethrough.begin.markdown.morkdown
|                ^^ punctuation.definition.strikethrough.end.markdown.morkdown 
|                  ^ punctuation.definition.italic.end.markdown.morkdown

*~~italic striked~~*
| <- markup.italic.markdown.morkdown punctuation.definition.italic.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^ markup.italic.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown
|                  ^ markup.italic.markdown.morkdown - markup.strikethrough
|^^ punctuation.definition.strikethrough.begin.markdown.morkdown
|                ^^ punctuation.definition.strikethrough.end.markdown.morkdown 
|                  ^ punctuation.definition.italic.end.markdown.morkdown

___~~bold italic striked~~___
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^ markup.bold.markdown.morkdown - markup.italic - markup.strikethrough
| ^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown - markup.strikethrough
|  ^^^^^^^^^^^^^^^^^^^^^^^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown
|                         ^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown - markup.strikethrough
|                          ^^ markup.bold.markdown.morkdown - markup.italic - markup.strikethrough
|^ punctuation.definition.bold.begin.markdown.morkdown
| ^ punctuation.definition.italic.begin.markdown.morkdown
|  ^^ punctuation.definition.strikethrough.begin.markdown.morkdown
|                       ^^ punctuation.definition.strikethrough.end.markdown.morkdown 
|                         ^ punctuation.definition.italic.end.markdown.morkdown
|                          ^^ punctuation.definition.bold.end.markdown.morkdown

***~~bold italic striked~~***
| <- markup.bold.markdown.morkdown punctuation.definition.bold.begin.markdown.morkdown
|^ markup.bold.markdown.morkdown - markup.italic - markup.strikethrough
| ^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown - markup.strikethrough
|  ^^^^^^^^^^^^^^^^^^^^^^^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown
|                         ^ markup.bold.markdown.morkdown markup.italic.markdown.morkdown - markup.strikethrough
|                          ^^ markup.bold.markdown.morkdown - markup.italic - markup.strikethrough
|^ punctuation.definition.bold.begin.markdown.morkdown
| ^ punctuation.definition.italic.begin.markdown.morkdown
|  ^^ punctuation.definition.strikethrough.begin.markdown.morkdown
|                       ^^ punctuation.definition.strikethrough.end.markdown.morkdown 
|                         ^ punctuation.definition.italic.end.markdown.morkdown
|                          ^^ punctuation.definition.bold.end.markdown.morkdown

~Hi~ Hello, world!
| <- - punctuation.definition.strikethrough
|^^^^^^^^^^^^^^^^^ meta.paragraph - markup
|  ^ - punctuation.definition.strikethrough

This ~text~~~~ is ~~~~curious~.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph - markup
|    ^ - punctuation.definition.strikethrough
|         ^^^^ - punctuation.definition.strikethrough
|                 ^^^^ - punctuation.definition.strikethrough
|                            ^ - punctuation.definition.strikethrough

This ~~text~~~~ is ~~~~curious~~.
|^^^^ meta.paragraph - markup
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph markup.strikethrough
|                               ^^ meta.paragraph - markup
|    ^^ punctuation.definition.strikethrough.begin
|          ^^^^ - punctuation.definition.strikethrough
|                  ^^^^ - punctuation.definition.strikethrough
|                             ^^ punctuation.definition.strikethrough.end

This ~~has a
|    ^^^^^^^^ meta.paragraph markup.strikethrough

| <- meta.paragraph markup.strikethrough invalid.illegal.non-terminated.bold-italic
new paragraph~~.
|            ^^ meta.paragraph markup.strikethrough punctuation.definition.strikethrough.begin

| <- invalid.illegal.non-terminated.bold-italic

A ~~[striked](https://link-url)~~
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown

A ~~![striked](https://image-url)~~
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown

A ~~[![striked](image-url)](link-url)~~
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown


# TEST: LINKS #################################################################

A [link](https://example.com){ :_attr = value }, *italic text* and **bold**.
| ^^^^^^ meta.link.inline.description.markdown.morkdown
| ^ punctuation.definition.link.begin
|      ^ punctuation.definition.link.end
|       ^ punctuation.definition.metadata
|        ^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                           ^ punctuation.definition.metadata
|                            ^ punctuation.definition.attributes.begin.markdown.morkdown
|                              ^^^^^^^^^^^^^^ meta.attribute-with-value.markdown.morkdown
|                              ^^^^^^ entity.other.attribute-name.markdown.morkdown
|                                     ^ punctuation.separator.key-value.markdown.morkdown
|                                       ^^^^^ string.unquoted.markdown.morkdown
|                                             ^ punctuation.definition.attributes.end.markdown.morkdown
|                                                ^^^^^^^^^^^^^ markup.italic
|                                                ^ punctuation.definition.italic
|                                                            ^ punctuation.definition.italic
|                                                                  ^^ punctuation.definition.bold
|                                                                  ^^^^^^^^ markup.bold
|                                                                        ^^ punctuation.definition.bold

Here is a [](https://example.com).
|         ^^ meta.link.inline
|         ^ punctuation.definition.link.begin
|          ^ punctuation.definition.link.end
|           ^ punctuation.definition.metadata
|            ^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                               ^ punctuation.definition.metadata

Here is a [](https://example.com){_attr="value"}.
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline
|         ^ punctuation.definition.link.begin
|          ^ punctuation.definition.link.end
|           ^ punctuation.definition.metadata
|            ^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                               ^ punctuation.definition.metadata
|                                ^ punctuation.definition.attributes.begin.markdown.morkdown
|                                 ^^^^^^^^^^^^^ meta.attribute-with-value.markdown.morkdown
|                                 ^^^^^ entity.other.attribute-name.markdown.morkdown
|                                      ^ punctuation.separator.key-value.markdown.morkdown
|                                       ^^^^^^^ string.quoted.double.markdown.morkdown
|                                              ^ punctuation.definition.attributes.end.markdown.morkdown

Here is a [link](#with_(parens/inside)_urls).
|         ^^^^^^ meta.link.inline.description.markdown.morkdown
|               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline.metadata.markdown.morkdown
|                                           ^^ - meta.link
|               ^ punctuation.definition.metadata.begin.markdown.morkdown
|                ^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.markdown.morkdown
|                                          ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a [link](\(foo\)).
|         ^^^^^^ meta.link.inline.description.markdown.morkdown
|               ^^^^^^^^^ meta.link.inline.metadata.markdown.morkdown
|                        ^^ - meta.link
|               ^ punctuation.definition.metadata.begin.markdown.morkdown
|                ^^^^^^^ markup.underline.link.markdown.morkdown
|                ^^ constant.character.escape.markdown.morkdown
|                     ^^ constant.character.escape.markdown.morkdown
|                       ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a [link](foo\)\:).
|         ^^^^^^ meta.link.inline.description.markdown.morkdown
|               ^^^^^^^^^ meta.link.inline.metadata.markdown.morkdown
|                        ^^ - meta.link
|               ^ punctuation.definition.metadata.begin.markdown.morkdown
|                ^^^^^^^ markup.underline.link.markdown.morkdown
|                   ^^ constant.character.escape.markdown.morkdown
|                       ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a [link](<foo(and(bar)>).
|         ^^^^^^ meta.link.inline.description.markdown.morkdown
|               ^^^^^^^^^^^^^^^^ meta.link.inline.metadata.markdown.morkdown
|                               ^^ - meta.link
|               ^ punctuation.definition.metadata.begin.markdown.morkdown
|                ^ punctuation.definition.link.begin.markdown.morkdown
|                 ^^^^^^^^^^^^ markup.underline.link.markdown.morkdown
|                             ^ punctuation.definition.link.end.markdown.morkdown
|                              ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a [link](http://example.com?foo=3#frag).
|         ^^^^^^ meta.link.inline.description.markdown.morkdown
|               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline.metadata.markdown.morkdown
|                                              ^^ - meta.link
|               ^ punctuation.definition.metadata.begin.markdown.morkdown
|                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.markdown.morkdown
|                    ^^^ punctuation.separator.path.markdown.morkdown
|                                  ^ punctuation.separator.path.markdown.morkdown
|                                        ^ punctuation.separator.path.markdown.morkdown
|                                             ^ punctuation.definition.metadata.end.markdown.morkdown

Not a [link] (url) due to space.
|     ^^^^^^ meta.link.reference.description.markdown.morkdown
|           ^^^^^^^^^^^^^^^^^^^^^ - meta.link

Here is a [reference link][name].
|         ^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown.morkdown
|                         ^^^^^^ meta.link.reference.metadata.markdown.morkdown
|         ^ punctuation.definition.link.begin.markdown.morkdown
|                        ^ punctuation.definition.link.end.markdown.morkdown
|                         ^ punctuation.definition.metadata.begin.markdown.morkdown
|                          ^^^^ markup.underline.link.markdown.morkdown
|                              ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a [reference link][name]{_attr='value' :att2}.
|         ^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown.morkdown
|                         ^^^^^^ meta.link.reference.metadata.markdown.morkdown
|                               ^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.attributes.markdown.morkdown
|                                ^^^^^^^^^^^^^ meta.attribute-with-value.markdown.morkdown
|                                             ^ - meta.attribute-with-value
|                                              ^^^^^ meta.attribute-with-value.markdown.morkdown
|         ^ punctuation.definition.link.begin.markdown.morkdown
|                        ^ punctuation.definition.link.end.markdown.morkdown
|                         ^ punctuation.definition.metadata.begin.markdown.morkdown
|                          ^^^^ markup.underline.link.markdown.morkdown
|                              ^ punctuation.definition.metadata.end.markdown.morkdown
|                               ^ punctuation.definition.attributes.begin.markdown.morkdown
|                                ^^^^^ entity.other.attribute-name.markdown.morkdown
|                                     ^ punctuation.separator.key-value.markdown.morkdown
|                                      ^^^^^^^ string.quoted.single.markdown.morkdown
|                                              ^^^^^ entity.other.attribute-name.markdown.morkdown
|                                                   ^ punctuation.definition.attributes.end.markdown.morkdown

Here is a [blank reference link][]{}.
|         ^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.literal.description.markdown.morkdown
|                               ^^ meta.link.reference.literal.metadata.markdown.morkdown
|                                 ^^ meta.link.reference.literal.attributes.markdown.morkdown
|         ^ punctuation.definition.link.begin.markdown.morkdown
|                              ^ punctuation.definition.link.end.markdown.morkdown
|                               ^ punctuation.definition.metadata.begin.markdown.morkdown
|                                ^ punctuation.definition.metadata.end.markdown.morkdown
|                                 ^ punctuation.definition.attributes.begin.markdown.morkdown
|                                  ^ punctuation.definition.attributes.end.markdown.morkdown

now you can access the [The Ever Cool Site: Documentation about Sites](
  www.thecoolsite.com.ca/documentations/about/cool ) for more information about...
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline markup.underline.link
|                                                 ^ - invalid
|                                                  ^ meta.link.inline punctuation.definition.metadata.end

now you can access the [The Ever Cool Site: Documentation about Sites](
  www.thecoolsite.com.ca /documentations/about/cool ) for more information about...
| ^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph meta.link.inline markup.underline.link
|                       ^ meta.paragraph meta.link.inline - markup.underline.link
|                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph - meta.link.inline

now you can access the [The Ever Cool Site: Documentation about Sites](
  www.thecoolsite.com.ca/documentations/about/cool
  (title)) for more information about...
| ^^^^^^^^ meta.paragraph meta.link.inline
|        ^ punctuation.definition.metadata.end
| ^^^^^^^ string.quoted.other.markdown.morkdown

link with a single underscore inside the text : [@_test](http://example.com)
|                                                ^^^^^^ meta.paragraph meta.link.inline.description - punctuation.definition
|                                                      ^ meta.paragraph meta.link.inline punctuation.definition.link.end

[foo]
|<- meta.link.reference punctuation.definition.link.begin
|^^^ meta.paragraph meta.link.reference
|   ^ meta.link.reference punctuation.definition.link.end

This is literal [Foo*bar\]] but [ref][Foo*bar\]]
|               ^^^^^^^^^^^ meta.link.reference.description.markdown.morkdown
|               ^ punctuation.definition.link.begin.markdown.morkdown
|                ^^^^^^^ - constant
|                       ^^ constant.character.escape.markdown.morkdown
|                         ^ punctuation.definition.link.end.markdown.morkdown
|                               ^^^^^ meta.link.reference.description.markdown.morkdown
|                                    ^^^^^^^^^^^ meta.link.reference.metadata.markdown.morkdown

[**Read more &#8594;**][details]
|^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown.morkdown
|                      ^^^^^^^^^ meta.link.reference.metadata.markdown.morkdown
|^^ punctuation.definition.bold.begin.markdown.morkdown
|            ^^^^^^^ constant.character.entity.decimal.html
|                   ^^ punctuation.definition.bold.end.markdown.morkdown
|                       ^^^^^^^ markup.underline.link.markdown.morkdown

[Read more &#8594;][details]
|^^^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown.morkdown
|                  ^^^^^^^^^ meta.link.reference.metadata.markdown.morkdown
|          ^^^^^^^ constant.character.entity.decimal.html
|                   ^^^^^^^ markup.underline.link

[Read more <span style="font-weight: bold;">&#8594;</span>][details]
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown.morkdown
|                                                          ^^^^^^^^^ meta.link.reference.metadata.markdown.morkdown
|          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag
|                       ^^^^^^^^^^^^^^^^^^ source.css
|                                           ^^^^^^^ constant.character.entity.decimal.html - meta.tag
|                                                  ^^^^^^^ meta.tag
|                                                           ^^^^^^^ markup.underline.link

[![Cool ★ Image - Click to Enlarge][img-example]][img-example]
| <- meta.link.reference.description.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
|^^ meta.link.reference.description.markdown.morkdown meta.image.reference.description.markdown.morkdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown.morkdown meta.image.reference.description.markdown.morkdown
|                                  ^^^^^^^^^^^^^^ meta.link.reference.description.markdown.morkdown
|                                                ^^^^^^^^^^^^^ meta.link.reference.metadata.markdown.morkdown
|^^ punctuation.definition.image.begin.markdown.morkdown
|                                 ^ punctuation.definition.image.end.markdown.morkdown
|                                  ^ punctuation.definition.metadata.begin.markdown.morkdown
|                                   ^^^^^^^^^^^ markup.underline.link
|                                              ^ punctuation.definition.metadata.end.markdown.morkdown
|                                               ^ punctuation.definition.link.end.markdown.morkdown
|                                                ^ punctuation.definition.metadata.begin.markdown.morkdown
|                                                 ^^^^^^^^^^^ markup.underline.link
|                                                            ^ punctuation.definition.metadata.end.markdown.morkdown

[![Cool ★ Image - Click to Enlarge](http://www.sublimetext.com/anim/rename2_packed.png)](http://www.sublimetext.com/anim/rename2_packed.png)
| <- meta.paragraph.markdown.morkdown meta.link.inline.description.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown meta.link.inline.description.markdown.morkdown meta.image.inline.description.markdown.morkdown
|                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown meta.link.inline.description.markdown.morkdown meta.image.inline.metadata.markdown.morkdown
|                                                                                      ^ meta.paragraph.markdown.morkdown meta.link.inline.description.markdown.morkdown
|                                                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown meta.link.inline.metadata.markdown.morkdown
|^^ punctuation.definition.image.begin.markdown.morkdown
|                                 ^ punctuation.definition.image.end.markdown.morkdown
|                                  ^ punctuation.definition.metadata.begin.markdown.morkdown
|                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
|                                                                                     ^ punctuation.definition.metadata.end.markdown.morkdown
|                                                                                      ^ punctuation.definition.link.end.markdown.morkdown
|                                                                                       ^ punctuation.definition.metadata.begin.markdown.morkdown
|                                                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.markdown.morkdown
|                                                                                                                                          ^ punctuation.definition.metadata.end.markdown.morkdown

[link [containing] [square] brackets](#backticks)
|<- punctuation.definition.link.begin
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline.description
|                                   ^ punctuation.definition.link.end

[link `containing square] brackets] in backticks`[]](#wow)
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline.description
|     ^ punctuation.definition.raw.begin
|                                               ^ punctuation.definition.raw.end
|                                                  ^ punctuation.definition.link.end

[link ``containing square]` brackets[[][] in backticks``](#wow)
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline.description
|     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.inline
|     ^^ punctuation.definition.raw.begin
|                                                     ^^ punctuation.definition.raw.end
|                                                       ^ punctuation.definition.link.end

This is a [reference] ()
|         ^^^^^^^^^^^ meta.link.reference
|                    ^^^^ - meta.link

This is a [reference] (followed by parens)
|         ^^^^^^^^^^^ meta.link.reference
|                    ^^^^^^^^^^^^^^^^^^^^^ - meta.link

This is a [reference] []
|         ^^^^^^^^^^^ meta.link.reference
|                    ^ - meta.link
|                     ^^ meta.link.reference

This is a ![reference] ()
|         ^^^^^^^^^^^^^^^ - meta.image
|          ^^^^^^^^^^^ meta.link.reference
|                     ^^^^ - meta.link

This is a ![reference] (followed by parens)
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.image
|          ^^^^^^^^^^^ meta.link.reference
|                     ^^^^^^^^^^^^^^^^^^^^^ - meta.link

This is a ![reference] []
|         ^^^^^^^^^^^^^^^ - meta.image
|          ^^^^^^^^^^^ meta.link.reference
|                     ^ - meta.link
|                      ^^ meta.link.reference


# TEST: IMAGES ################################################################

Here is a ![](https://example.com/cat.gif).
|         ^^^ meta.image.inline.description.markdown.morkdown
|            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline.metadata.markdown.morkdown
|                                         ^^ - meta.image
|         ^^ punctuation.definition.image.begin.markdown.morkdown
|           ^ punctuation.definition.image.end.markdown.morkdown - string
|            ^ punctuation.definition.metadata.begin.markdown.morkdown
|             ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
|                                        ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a ![](https://example.com/cat.gif){_at"r=value :att2}.
|         ^^^ meta.image.inline.description.markdown.morkdown
|            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline.metadata.markdown.morkdown
|                                         ^^^^^^^^^^^^^^^^^^^ meta.image.inline.attributes.markdown.morkdown
|                                                            ^^ - meta.image
|         ^^ punctuation.definition.image.begin.markdown.morkdown
|           ^ punctuation.definition.image.end.markdown.morkdown - string
|            ^ punctuation.definition.metadata.begin.markdown.morkdown
|             ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
|                                        ^ punctuation.definition.metadata
|                                         ^ punctuation.definition.attributes.begin.markdown.morkdown
|                                          ^^^^^ entity.other.attribute-name.markdown.morkdown
|                                             ^ invalid.illegal.attribute-name.markdown.morkdown
|                                               ^ punctuation.separator.key-value.markdown.morkdown
|                                                ^^^^^ string.unquoted.markdown.morkdown
|                                                      ^^^^^ entity.other.attribute-name.markdown.morkdown
|                                                           ^ punctuation.definition.attributes.end.markdown.morkdown

Here is a ![Image Alt Text](https://example.com/cat.gif).
|         ^^^^^^^^^^^^^^^^^ meta.image.inline.description.markdown.morkdown
|                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline.metadata.markdown.morkdown
|                                                       ^^ - meta.image
|         ^^ punctuation.definition.image.begin.markdown.morkdown
|                         ^ punctuation.definition.image.end.markdown.morkdown - string
|                          ^ punctuation.definition.metadata.begin.markdown.morkdown
|                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
|                                                      ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a ![Image Alt Text](  https://example.com/cat.gif  ).
|         ^^^^^^^^^^^^^^^^^ meta.image.inline.description.markdown.morkdown
|                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline.metadata.markdown.morkdown
|                                                           ^^ - meta.image
|         ^^ punctuation.definition.image.begin.markdown.morkdown
|                         ^ punctuation.definition.image.end - string
|                          ^ punctuation.definition.metadata.begin.markdown.morkdown
|                           ^^ - markup.underline
|                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
|                                                        ^^ - markup.underline
|                                                          ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a ![Image Alt Text](
  https://example.com/cat.gif  ).
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
|                              ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a ![Image Alt Text](
  https://example.com/cat.gif
 "hello"   ).
|^^^^^^^ meta.image.inline string.quoted.double
|       ^^^^ meta.image.inline
|          ^ punctuation.definition.metadata.end

Here is a ![Image Alt Text](
  <https://example.com/cat.gif> "hello"   ).
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown meta.image.inline.metadata.markdown.morkdown
|                                          ^^ meta.paragraph.markdown.morkdown - meta.image
| ^ punctuation.definition.link.begin.markdown.morkdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
|                             ^ punctuation.definition.link.end.markdown.morkdown
|                               ^^^^^^^ string.quoted.double.markdown.morkdown
|                               ^ punctuation.definition.string.begin.markdown.morkdown
|                                     ^ punctuation.definition.string.end.markdown.morkdown
|                                         ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a ![Image Alt Text](
  <https://example .com /cat.gif> (hello)   ).
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown meta.image.inline.metadata.markdown.morkdown
|                                            ^^ meta.paragraph.markdown.morkdown - meta.image
| ^ punctuation.definition.link.begin.markdown.morkdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown.morkdown
|                               ^ punctuation.definition.link.end.markdown.morkdown
|                                 ^^^^^^^ string.quoted.other.markdown.morkdown
|                                 ^ punctuation.definition.string.begin.markdown.morkdown
|                                       ^ punctuation.definition.string.end.markdown.morkdown
|                                           ^ punctuation.definition.metadata.end.markdown.morkdown

Here is a ![Image Alt Text](
  https://example .com /cat.gif (hello)   ).
|^ meta.paragraph.markdown.morkdown meta.image.inline.metadata.markdown.morkdown - markup.underline
| ^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown meta.image.inline.metadata.markdown.morkdown markup.underline.link.image.markdown.morkdown
|                ^ meta.paragraph.markdown.morkdown meta.image.inline.metadata.markdown.morkdown - markup.underline
|                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - meta.image - markup.underline

Here is a ![Image Ref Alt][1].
|         ^^^^^^^^^^^^^^^^ meta.image.reference.description.markdown.morkdown
|                         ^^^ meta.image.reference.metadata.markdown.morkdown
|         ^^ punctuation.definition.image.begin.markdown.morkdown
|                        ^ punctuation.definition.image.end.markdown.morkdown
|                         ^ punctuation.definition.metadata.begin.markdown.morkdown
|                          ^ markup.underline.link.markdown.morkdown
|                           ^ punctuation.definition.metadata.end.markdown.morkdown


# TEST: FOOTNOTES #############################################################

## https://michelf.ca/projects/php-markdown/extra/#footnotes

That's some text with a footnote.[^1]
|                                ^^^^ meta.paragraph meta.link.reference.footnote.markdown-extra.morkdown
|                                ^ punctuation.definition.link.begin
|                                 ^^ meta.link.reference.literal.footnote-id
|                                   ^ punctuation.definition.link.end

Here is a footnote[^1][link][] or long[^longnote][link][].
|                 ^^^^ meta.link.reference.footnote.markdown-extra.morkdown
|                     ^^^^^^ meta.link.reference.literal.description.markdown.morkdown
|                           ^^ meta.link.reference.literal.metadata.markdown.morkdown
|                                     ^^^^^^^^^^^ meta.link.reference.footnote.markdown-extra.morkdown
|                                                ^^^^^^^^ meta.link.reference.literal

Here is a footnote [^footnote](not_link_dest).
|                  ^^^^^^^^^^^ meta.paragraph.markdown.morkdown meta.link.reference.footnote.markdown-extra.morkdown
|                  ^ punctuation.definition.link.begin.markdown.morkdown
|                   ^^^^^^^^^ meta.link.reference.literal.footnote-id.markdown.morkdown
|                            ^ punctuation.definition.link.end.markdown.morkdown
|                             ^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown - meta.link


# TEST: COMMONMARK AUTOLINKS ##################################################

<mailto:test+test@test.com>
| <- meta.link.email.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown - markup.underline
|^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.email.markdown.morkdown markup.underline.link.markdown.morkdown
|                         ^ meta.link.email.markdown.morkdown - markup.underline
|      ^ punctuation.separator.path.markdown.morkdown
|                ^ punctuation.separator.path.markdown.morkdown
|                         ^ punctuation.definition.link.end.markdown.morkdown

<foo#bar?@mail.test.com>
| <- meta.link.email.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown - markup.underline
|^^^^^^^^^^^^^^^^^^^^^^ meta.link.email.markdown.morkdown markup.underline.link.markdown.morkdown
|                      ^ meta.link.email.markdown.morkdown - markup.underline
|        ^ punctuation.separator.path.markdown.morkdown
|                      ^ punctuation.definition.link.end.markdown.morkdown

<http://www.test.com/>
| <- meta.link.inet.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown - markup.underline
|^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link.markdown.morkdown
|                    ^ meta.link.inet.markdown.morkdown - markup.underline
|    ^^^ punctuation.separator.path.markdown.morkdown
|                   ^ punctuation.separator.path.markdown.morkdown
|                    ^ punctuation.definition.link.end.markdown.morkdown

<https://test.com/>
| <- meta.link.inet.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown - markup.underline
|^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link.markdown.morkdown
|                 ^ meta.link.inet.markdown.morkdown - markup.underline
|     ^^^ punctuation.separator.path.markdown.morkdown
|                ^ punctuation.separator.path.markdown.morkdown
|                 ^ punctuation.definition.link.end.markdown.morkdown

<ftp://test.com/>
| <- meta.link.inet.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown - markup.underline
|^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link.markdown.morkdown
|               ^ meta.link.inet.markdown.morkdown - markup.underline
|   ^^^ punctuation.separator.path.markdown.morkdown
|              ^ punctuation.separator.path.markdown.morkdown
|               ^ punctuation.definition.link.end.markdown.morkdown

<irc://foo%20bar.com:2233/baz>
| <- meta.link.inet.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown - markup.underline
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link.markdown.morkdown
|                            ^ meta.link.inet.markdown.morkdown - markup.underline
|   ^^^ punctuation.separator.path.markdown.morkdown
|         ^ constant.character.escape.url.markdown.morkdown punctuation.definition.escape.markdown.morkdown
|          ^^ constant.character.escape.url.markdown.morkdown - punctuation
|                        ^ punctuation.separator.path.markdown.morkdown

<a+b+c:d>
| <- meta.link.inet.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
|^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link.markdown.morkdown
|       ^ meta.paragraph.markdown.morkdown meta.link.inet.markdown.morkdown punctuation.definition.link.end.markdown.morkdown

<made-up-scheme://foo,bar>
| <- meta.paragraph.markdown.morkdown meta.link.inet.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown.morkdown meta.link.inet.markdown.morkdown markup.underline.link.markdown.morkdown
|                        ^ meta.paragraph.markdown.morkdown meta.link.inet.markdown.morkdown punctuation.definition.link.end.markdown.morkdown
|              ^^^ punctuation.separator.path.markdown.morkdown

<http://../>
| <- meta.link.inet.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
|^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link.markdown.morkdown
|          ^ meta.paragraph.markdown.morkdown meta.link.inet.markdown.morkdown punctuation.definition.link.end.markdown.morkdown
|    ^^^ punctuation.separator.path.markdown.morkdown
|         ^ punctuation.separator.path.markdown.morkdown

<localhost:5001/foo>
| <- meta.link.inet.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link.markdown.morkdown
|                  ^ meta.paragraph.markdown.morkdown meta.link.inet.markdown.morkdown punctuation.definition.link.end.markdown.morkdown
|         ^ punctuation.separator.path.markdown.morkdown
|              ^ punctuation.separator.path.markdown.morkdown

<http://foo.bar/baz bim>
| <- meta.link.inet.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link.markdown.morkdown
|                  ^^^^^^ - meta.link
|    ^^^ punctuation.separator.path.markdown.morkdown
|              ^ punctuation.separator.path.markdown.morkdown

<http://example.com/\[\>
| <- meta.link.inet.markdown.morkdown punctuation.definition.link.begin.markdown.morkdown
|^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link.markdown.morkdown
|                      ^ meta.paragraph.markdown.morkdown meta.link.inet.markdown.morkdown punctuation.definition.link.end.markdown.morkdown
|    ^^^ punctuation.separator.path.markdown.morkdown
|                  ^ punctuation.separator.path.markdown.morkdown


# TEST: GFM AUTOLINKS #########################################################

Visit ftp://intra%20net
|     ^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|        ^^^ punctuation.separator.path.markdown.morkdown
|               ^ - constant
|                ^ constant.character.escape.url.markdown.morkdown punctuation.definition.escape.markdown.morkdown
|                 ^^ constant.character.escape.url.markdown.morkdown - punctuation
|                   ^^^ - constant

Visit http://intra%20net
|     ^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|         ^^^ punctuation.separator.path.markdown.morkdown
|                ^ - constant
|                 ^ constant.character.escape.url.markdown.morkdown punctuation.definition.escape.markdown.morkdown
|                  ^^ constant.character.escape.url.markdown.morkdown - punctuation
|                    ^^^ - constant

Visit https://intra%20net
|     ^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|          ^^^ punctuation.separator.path.markdown.morkdown
|                 ^ - constant
|                  ^ constant.character.escape.url.markdown.morkdown punctuation.definition.escape.markdown.morkdown
|                   ^^ constant.character.escape.url.markdown.morkdown - punctuation
|                     ^^^ - constant

Visit www.intra%20net
|     ^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|             ^ - constant
|              ^ constant.character.escape.url.markdown.morkdown punctuation.definition.escape.markdown.morkdown
|               ^^ constant.character.escape.url.markdown.morkdown - punctuation
|                 ^^^ - constant

Visit www.commonmark.org/help for more information.
|     ^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|                       ^ punctuation.separator.path.markdown.morkdown
|                            ^^^^^^^^^^^^^^^^^^^^^^^ - markup.underline.link

Visit www.commonmark.org.
|     ^^^^^^^^^^^^^^^^^^ meta.paragraph meta.link.inet.markdown.morkdown markup.underline.link
|                       ^^ - markup.underline.link

Visit www.commonmark.org/a.b.
|     ^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph meta.link.inet.markdown.morkdown markup.underline.link
|                           ^ - markup.underline.link
|                       ^ punctuation.separator.path.markdown.morkdown

www.google.com/search?q=(business))+ok
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|             ^ punctuation.separator.path.markdown.morkdown
|                    ^ punctuation.separator.path.markdown.morkdown
|                                     ^ - markup.underline.link

www.google.com/search?q=Markup+(business)
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|             ^ punctuation.separator.path.markdown.morkdown
|                    ^ punctuation.separator.path.markdown.morkdown

www.commonmark.org/he<lp>
|^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|                 ^ punctuation.separator.path.markdown.morkdown
|                    ^ - markup.underline.link

http://commonmark.org
|^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|   ^^^ punctuation.separator.path.markdown.morkdown

www.google.com/search?q=commonmark&hl=en
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|             ^ punctuation.separator.path.markdown.morkdown
|                    ^ punctuation.separator.path.markdown.morkdown
|                                 ^ punctuation.separator.path.markdown.morkdown
|                                       ^ - markup.underline.link

www.google.com/search?q=commonmark&hl;
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|             ^ punctuation.separator.path.markdown.morkdown
|                    ^ punctuation.separator.path.markdown.morkdown
|                                 ^^^^ constant.character.entity.named.html - markup.underline.link

www.google.com/search?q=commonmark&hl;&hl;
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|             ^ punctuation.separator.path.markdown.morkdown
|                    ^ punctuation.separator.path.markdown.morkdown
|                                 ^^^^^^^^ constant.character.entity.named.html - markup.underline.link

www.google.com/search?q=commonmark&hl;!
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|                                 ^^^^^^ - meta.link
|             ^ punctuation.separator.path.markdown.morkdown
|                    ^ punctuation.separator.path.markdown.morkdown
|                                 ^^^^ constant.character.entity.named.html - markup.underline.link

www.google.com/search?q=commonmark&hl;f
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|                                      ^ - meta.link
|             ^ punctuation.separator.path.markdown.morkdown
|                    ^ punctuation.separator.path.markdown.morkdown
|                                 ^^^^ - constant.character

(Visit https://encrypted.google.com/search?q=Markup+(business))
|      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|           ^^^ punctuation.separator.path.markdown.morkdown
|                                  ^ punctuation.separator.path.markdown.morkdown
|                                         ^ punctuation.separator.path.markdown.morkdown
|                                                             ^^ - markup.underline.link

Anonymous FTP is available at ftp://foo.bar.baz.
|                             ^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|                                ^^^ punctuation.separator.path.markdown.morkdown
|                                              ^^ - markup.underline.link

(see http://www.google.com/search?q=commonmark&hl=en)
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown.morkdown markup.underline.link
|        ^^^ punctuation.separator.path.markdown.morkdown
|                         ^ punctuation.separator.path.markdown.morkdown
|                                ^ punctuation.separator.path.markdown.morkdown
|                                             ^ punctuation.separator.path.markdown.morkdown
|                                                   ^^ - markup.underline.link

foo@bar.baz
| <- meta.link.email.markdown.morkdown markup.underline.link.markdown.morkdown
|^^^^^^^^^^ meta.link.email.markdown.morkdown markup.underline.link.markdown.morkdown
|  ^ punctuation.separator.path.markdown.morkdown
|          ^ - meta.link - markup.underline.link

hello@mail+xyz.example isn't valid, but hello+xyz@mail.example is.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.link - markup.underline.link
|                                       ^^^^^^^^^^^^^^^^^^^^^^ meta.link.email.markdown.morkdown markup.underline.link.markdown.morkdown

 test@test.test.me
| <- - meta.link - markup.underline
|^^^^^^^^^^^^^^^^^ meta.link.email.markdown.morkdown markup.underline.link.markdown.morkdown
|    ^ punctuation.separator.path.markdown.morkdown
|                 ^ - meta.link - markup.underline.link

 a.b-c_d@a.b
| <- - meta.link - markup.underline
|^^^^^^^^^^^ meta.link.email.markdown.morkdown markup.underline.link.markdown.morkdown
|       ^ punctuation.separator.path.markdown.morkdown
|           ^ - meta.link - markup.underline.link

a.b-c_d@a.b.
|^^^^^^^^^^ markup.underline.link
|          ^^ - markup.underline.link

 a.b-c_d@a.b-
| <- - meta.link - markup.underline
|^^^^^^^^^^^^^ - meta.link - markup.underline.link

 a.b-c_d@a.b_
| <- - meta.link - markup.underline
|^^^^^^^^^^^^^ - meta.link - markup.underline.link


# TEST: HARD LINE BREAKS ######################################################

hard line break  
|              ^^ meta.hard-line-break punctuation.definition.hard-line-break
hard line break\
|              ^ meta.hard-line-break constant.character.escape
hard line break     
|              ^^^^^ meta.hard-line-break punctuation.definition.hard-line-break
soft line break 
|              ^^ - meta.hard-line-break
soft line break
|             ^^ - meta.hard-line-break

### foo  
|      ^^^ - meta.hard-line-break
### foo\
|      ^ - meta.hard-line-break

`inline code with trailing spaces  
|                                ^^^ - meta.hard-line-break
not a hard line break`


# TEST: CRITIC MARKUP #########################################################

This is an {++additional++} word in {++**bold**++}.
|          ^^^^^^^^^^^^^^^^ markup.critic.addition.markdown.morkdown
|          ^^^ punctuation.definition.critic.begin.markdown.morkdown - markup.inserted
|             ^^^^^^^^^^ markup.inserted.critic.markdown.morkdown
|                       ^^^ punctuation.definition.critic.end.markdown.morkdown - markup.inserted
|                                   ^^^ markup.critic.addition.markdown.morkdown - markup.inserted - markup.bold
|                                      ^^^^^^^^ markup.critic.addition.markdown.morkdown markup.inserted.critic.markdown.morkdown markup.bold.markdown.morkdown
|                                              ^^^ markup.critic.addition.markdown.morkdown - markup.inserted
|                                   ^^^ punctuation.definition.critic.begin.markdown.morkdown
|                                      ^^ punctuation.definition.bold.begin.markdown.morkdown
|                                            ^^ punctuation.definition.bold.end.markdown.morkdown 
|                                              ^^^ punctuation.definition.critic.end.markdown.morkdown

This is an {++ multiline
addition ++} test.
| <- markup.critic.addition.markdown.morkdown
|^^^^^^^^ markup.critic.addition.markdown.morkdown markup.inserted.critic.markdown.morkdown
|        ^^^ markup.critic.addition.markdown.morkdown - markup.inserted
|        ^^^ punctuation.definition.critic.end.markdown.morkdown
|           ^^^^^^ - markup.critic

Additional {++[Link](https://foo.bar)++} and {++![Image](images/image.png)++}.
| ^^^^^^^^^ - markup.critic
|          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.critic.addition.markdown.morkdown
|                                        ^^^^ - markup.critic
|                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.critic.addition.markdown.morkdown
|                                                                            ^^ - markup.critic
|          ^^^ punctuation.definition.critic.begin.markdown.morkdown
|             ^^^^^^ meta.link.inline.description.markdown.morkdown
|                   ^^^^^^^^^^^^^^^^^ meta.link.inline.metadata.markdown.morkdown
|                                    ^^^ punctuation.definition.critic.end.markdown.morkdown
|                                            ^^^ punctuation.definition.critic.begin.markdown.morkdown
|                                               ^^^^^^^^ meta.image.inline.description.markdown.morkdown
|                                                       ^^^^^^^^^^^^^^^^^^ meta.image.inline.metadata.markdown.morkdown
|                                                                         ^^^ punctuation.definition.critic.end.markdown.morkdown

This is a {-- deletion --} and {~~substitute~>with~~striked~~text~~} or {~~~~old~~~>~~new~~~~}.
|         ^^^^^^^^^^^^^^^^ markup.critic.deletion.markdown.morkdown
|         ^^^ punctuation.definition.critic.begin.markdown.morkdown - markup.deleted
|            ^^^^^^^^^^ markup.deleted.critic.markdown.morkdown
|                      ^^^ punctuation.definition.critic.end.markdown.morkdown - markup.deleted
|                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.critic.substitution.markdown.morkdown
|                                                                    ^^^ - markup.critic
|                                                                       ^^^^^^^^^^^^^^^^^^^^^^ markup.critic.substitution.markdown.morkdown
|                                                                                             ^^ - markup.critic
|                              ^^^ punctuation.definition.critic.begin.markdown.morkdown - markup.deleted
|                                 ^^^^^^^^^^ markup.deleted.critic.markdown.morkdown
|                                           ^^ punctuation.separator.critic.markdown.morkdown - markup.deleted - markup.inserted
|                                              ^^^^^^^^^^^^^^^^^^ markup.inserted.critic.markdown.morkdown
|                                                  ^^^^^^^^^^ markup.strikethrough.markdown-gfm.morkdown
|                                                                ^^^ punctuation.definition.critic.end.markdown.morkdown - markup.inserted
|                                                                       ^^^ punctuation.definition.critic.begin.markdown.morkdown
|                                                                          ^^ punctuation.definition.strikethrough.begin.markdown.morkdown
|                                                                          ^^^^^^^ markup.deleted.critic.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown
|                                                                               ^^ punctuation.definition.strikethrough.end.markdown.morkdown
|                                                                                 ^^ punctuation.separator.critic.markdown.morkdown
|                                                                                   ^^ punctuation.definition.strikethrough.begin.markdown.morkdown
|                                                                                   ^^^^^^^ markup.inserted.critic.markdown.morkdown markup.strikethrough.markdown-gfm.morkdown
|                                                                                        ^^ punctuation.definition.strikethrough.end.markdown.morkdown
|                                                                                          ^^^ punctuation.definition.critic.end.markdown.morkdown

No striked {~~~>~~} critics.
|          ^^^^^^^^ markup.critic.substitution.markdown.morkdown
|          ^^^ punctuation.definition.critic.begin.markdown.morkdown
|             ^^ punctuation.separator.critic.markdown.morkdown
|               ^^^ punctuation.definition.critic.end.markdown.morkdown
|                  ^^^^^^^^^^ - markup.critic

No striked {~~~~>~~~} critics.
|          ^^^^^^^^^^ markup.critic.substitution.markdown.morkdown
|          ^^^ punctuation.definition.critic.begin.markdown.morkdown
|             ^ - punctuation
|              ^^ punctuation.separator.critic.markdown.morkdown
|                ^ - punctuation
|                 ^^^ punctuation.definition.critic.end.markdown.morkdown
|                    ^^^^^^^^^^ - markup.critic

No striked {~~~~~>~~~~} critics.
|          ^^^^^^^^^^^^ markup.critic.substitution.markdown.morkdown
|          ^^^ punctuation.definition.critic.begin.markdown.morkdown
|             ^^ - punctuation
|               ^^ punctuation.separator.critic.markdown.morkdown
|                 ^^ - punctuation
|                   ^^^ punctuation.definition.critic.end.markdown.morkdown
|                      ^^^^^^^^^^ - markup.critic

No striked {~~~~~~>~~~~~} critics.
|          ^^^^^^^^^^^^^^ markup.critic.substitution.markdown.morkdown
|          ^^^ punctuation.definition.critic.begin.markdown.morkdown
|             ^^^ - punctuation
|                ^^ punctuation.separator.critic.markdown.morkdown
|                  ^^^ - punctuation
|                     ^^^ punctuation.definition.critic.end.markdown.morkdown
|                        ^^^^^^^^^^ - markup.critic

No striked {~~~~~~~>~~~~~~} critics.
|          ^^^^^^^^^^^^^^^^ markup.critic.substitution.markdown.morkdown
|          ^^^ punctuation.definition.critic.begin.markdown.morkdown
|             ^^^^ - punctuation
|                 ^^ punctuation.separator.critic.markdown.morkdown
|                   ^^^^ - punctuation
|                       ^^^ punctuation.definition.critic.end.markdown.morkdown
|                          ^^^^^^^^^^ - markup.critic

This is a {>> comment <<}.
|         ^^^^^^^^^^^^^^^ markup.critic.comment.markdown.morkdown
|         ^^^ punctuation.definition.critic.begin.markdown.morkdown - comment
|            ^^^^^^^^^ comment.critic.markdown.morkdown
|                     ^^^ punctuation.definition.critic.end.markdown.morkdown - comment
|                        ^ - markup.critic

This is an {== information ==}{>> comment <<}.
|          ^^^^^^^^^^^^^^^^^^^ markup.critic.highlight.markdown.morkdown
|                             ^^^^^^^^^^^^^^^ markup.critic.comment.markdown.morkdown
|          ^^^ punctuation.definition.critic.begin.markdown.morkdown -  markup.info
|             ^^^^^^^^^^^^^ markup.info.critic.markdown.morkdown
|                          ^^^ punctuation.definition.critic.end.markdown.morkdown -  markup.info
|                             ^^^ punctuation.definition.critic.begin.markdown.morkdown - comment
|                                ^^^^^^^^^ comment.critic.markdown.morkdown
|                                         ^^^ punctuation.definition.critic.end.markdown.morkdown - comment
|                                            ^^ - markup.critic

This is a [[wiki link]].
|         ^^^^^^^^^^^^^ meta.link.reference.wiki.description.markdown.morkdown
|         ^^ punctuation.definition.link.begin.markdown.morkdown
|                    ^^ punctuation.definition.link.end.markdown.morkdown
