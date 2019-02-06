# EBCDIC

<!--
  |x0|x1|x2|x3|x4|x5|x6|x7|x8|x9|xA|xB|xC|xD|xE|xF
4x|  |  |  |  |  |  |  |  |  |  |¢ |. |< |( |+ |p
5x|& |  |  |  |  |  |  |  |  |  |! |$ |* |) |; |¬
6x|- |/ |  |  |  |  |  |  |  |  |  |, |% |_ |> |?
7x|  |  |  |  |  |  |  |  |  |  |: |# |@ |' |= |"
8x|  |a |b |c |d |e |f |g |h |i |
9x|  |j |k |l |m |n |o |p |q |r |
Ax|  |~ |s |t |u |v |w |x |y |z |
Bx|
Cx|  |A |B |C |D |E |F |G |H |I |
Dx|  |J |K |L |M |N |O |P |Q |R |
Ex|  |÷ |S |T |U |V |W |X |Y |Z |
Fx|0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |
-->


/   | x0  | x1  | x2  | x3  | x4  | x5  | x6  | x7  | x8  | x9  | xA  | xB  | xC  | xD  | xE  | xF
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
4x  |     |     |     |     |     |     |     |     |     |     | ¢   | .   | <   | (   | +   |\|
5x  | &   |     |     |     |     |     |     |     |     |     | !   | $   | *   | )   | ;   | ¬
6x  | -   | /   |     |     |     |     |     |     |     |     |     | ,   | %   | _   | >   | ?
7x  |     |     |     |     |     |     |     |     |     |     | :   | #   | @   | '   | =   | "
8x  |     | a   | b   | c   | d   | e   | f   | g   | h   | i   |     |     |     |     |     |
9x  |     | j   | k   | l   | m   | n   | o   | p   | q   | r   |     |     |     |     |     |
Ax  |     | ~   | s   | t   | u   | v   | w   | x   | y   | z   |     |     |     |     |     |
Bx  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
Cx  |     | A   | B   | C   | D   | E   | F   | G   | H   | I   |     |     |     |     |     |
Dx  |     | J   | K   | L   | M   | N   | O   | P   | Q   | R   |     |     |     |     |     |
Ex  |     | ÷   | S   | T   | U   | V   | W   | X   | Y   | Z   |     |     |     |     |     |
Fx  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |     |     |     |     |     |

# ASCII

**A**merican (National) **S**tandard **C**ode for **I**nformation **I**nterchange (`/'æski/.ass-kee`)

## in 1963
ASA standard X3.4-1963

 /  | -0  | -1  | -2  | -3  | -4  | -5  | -6  | -7  | -8  | -9  | -A  | -B  | -C  | -D  | -E  | -F
:-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-:
0x  | NUL | SOM | EOA | EOM | EOT | WRU | RU  | BELL| FE0 |HT/SK| LF  | Vtab| FF  | CR  | SO  | SI
1x  | DC0 | DC1 | DC2 | DC3 |DC4/STOP|ERR|SYNC| LEM |S0   | S1  | S2  | S3  | S4  | S5  | S6  | S7
    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
2x  | ƀ   | !   | "   | #   | $   | %   | &   | '   | (   | )   | *   | +   | ,   | -   | .   | /
3x  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | :   | ;   | <   | =   | >   | ?
    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
4x  | @   | A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O
5x  | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   | [   | \   | ]   | ↑   | ←
6x  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
7x  |     |     |     |     |     |     |     |     |     |     |     |     | ACK | ②   | ESC | DEL

.|.|.
:-:| ---     | ---
00 | NUL     | Null/Idle
01 | SOM     | Start of Message
02 | EOA     | End of Address
03 | EOM     | End Of Message
04 | EOT     | End of Transmission
05 | WRU     | "Who are you?"
06 | RU      | "Are you...?"
07 | BELL    | Audible signal
08 | FE0     | Format Effector
09 | HT      | Horizontal Tabulation
09 | SK      | Skip (punched card)
0A | LF      | Line feed
0B | VTAB    | Vertical Tabulation
0C | FF      | Form feed
0D | CR      | Carriage return
0E | SO      | Shift Out
0F | SI      | Shift in
10 | DC0     | Device Control reversed for data link escape
11-13| DC1-DC3 | Device Control
14 | DC4     | Device Control (stop)
15 | ERR     | Error
16 | SYNC    | synchronous idle
17 | LEM     | Logical End of Media
18-1F| S0-S7 | Separator (information)
   |         |
20 | ƀ       | Word separator (space, normally non-printing)
   |         |
5E | ↑       | Up arrow (exponentiation)
5F | ←       | Left Arrow (Implies/Replaced by)
5C | \       | Reverse Slant
   |         |
7C | ACK     | Acknowledge
7D | ②       | Unassigned control
7E | ESC     | Escape
7F | DEL     | Delete / Idle


## Printables

### Hexadecimal

<!--
  |-0|-1|-2|-3|-4|-5|-6|-7|-8|-9|-A|-B|-C|-D|-E|-F
2x|  |! |" |# |$ |% |& |' |( |) |* |+ |, |- |. |/
3x|0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |: |; |< |= |> |?
4x|@ |A |B |C |D |E |F |G |H |I |J |K |L |M |N |O
5x|P |Q |R |S |T |U |V |W |X |Y |Z |[ |\ |] |^ |_
6x|` |a |b |c |d |e |f |g |h |i |j |k |l |m |n |o
7x|p |q |r |s |t |u |v |w |x |y |z |{ |pi|} |~ |
-->

 /  | -0  | -1  | -2  | -3  | -4  | -5  | -6  | -7  | -8  | -9  | -A  | -B  | -C  | -D  | -E  | -F
:-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-:
2x  |     | !   | "   | #   | $   | %   | &   | '   | (   | )   | *   | +   | ,   | -   | .   | /
3x  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | :   | ;   | <   | =   | >   | ?
    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
4x  | @   | A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O
5x  | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   | [   | \   | ]   | ^   | _
    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
6x  | \`  | a   | b   | c   | d   | e   | f   | g   | h   | i   | j   | k   | l   | m   | n   | o
7x  | p   | q   | r   | s   | t   | u   | v   | w   | x   | y   | z   | {   | \|  | }   | ~   |


### Decimal

<!--
   |-0|-1|-2|-3|-4|-5|-6|-7|-8|-9
3x |  |  |  |! |" |# |$ |% |& |'
4x |( |) |* |+ |, |- |. |/ |0 |1
5x |2 |3 |4 |5 |6 |7 |8 |9 |: |;
6x |< |= |> |? |@ |A |B |C |D |E
7x |F |G |H |I |J |K |L |M |N |O
8x |P |Q |R |S |T |U |V |W |X |Y
9x |Z |[ |\ |] |^ |_ |` |a |b |c
10x|d |e |f |g |h |i |j |k |l |m
11x|n |o |p |q |r |s |t |u |v |w
12x|x |y |z |{ |pi|} |~
-->

/   | -0  | -1  | -2  | -3  | -4  | -5  | -6  | -7  | -8  | -9
:-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-:
3x  | ​    | ​    | ​    | !   | "   | #   | $   | %   | &   | '
4x  | (   | )   | *   | +   | ,   | -   | .   | /   | 0   | 1
5x  | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | :   | ;
6x  | <   | =   | >   | ?   | @   | A   | B   | C   | D   | E
7x  | F   | G   | H   | I   | J   | K   | L   | M   | N   | O
8x  | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y
9x  | Z   | [   | \   | ]   | ^   | _   | `   | a   | b   | c
10x | d   | e   | f   | g   | h   | i   | j   | k   | l   | m
11x | n   | o   | p   | q   | r   | s   | t   | u   | v   | w
12x | x   | y   | z   | {   | \   | }   | ~   |     |     |   
​    | -0  | -1  | -2  | -3  | -4  | -5  | -6  | -7  | -8  | -9

## Control codes

<!-- csvtable
/|-0|-1|-2|-3|-4|-5|-6|-7|-8|-9|-A|-B|-C|-D|-E|-F
0-|NUL|SOH|STX|ETX|EOT|ENQ|ACK|BEL|BS|HT|LF|VT|FF|CR|SO|SI|0-
1-|DLE|DC1|DC2|DC3|DC4|NAK|SYN|ETB|CAN|EM|SUB|ESC|FS|GS|RS|US|1-
|
2-|SP||||||||||||||||2-
|
7-||||||||||||||||DEL|7-
|-0|-1|-2|-3|-4|-5|-6|-7|-8|-9|-A|-B|-C|-D|-E|-F
-->

/   | -0  | -1  | -2  | -3  | -4  | -5  | -6  | -7  | -8  | -9  | -A  | -B  | -C  | -D  | -E  | -F  |  
:-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-:
0-  | NUL | SOH | STX | ETX | EOT | ENQ | ACK | BEL | BS  | HT  | LF  | VT  | FF  | CR  | SO  | SI  | 0-
1-  | DLE | DC1 | DC2 | DC3 | DC4 | NAK | SYN | ETB | CAN | EM  | SUB | ESC | FS  | GS  | RS  | US  | 1-
    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
2-  | SP  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 2-
    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
7-  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | DEL | 7-
    | -0  | -1  | -2  | -3  | -4  | -5  | -6  | -7  | -8  | -9  | -A  | -B  | -C  | -D  | -E  | -F  | 


- 00 `Ctrl-@`  `NUL` Null

transmission:
- 01 `Ctrl-A` `SOH` Start of Heading
- 02 `Ctrl-B` `STX` Start of Text
- 03 `Ctrl-C` `ETX` End of Text
- 04 `Ctrl-D` `EOT` End of Transmission
- 05 `Ctrl-E` `ENQ` Enquiry
- 06 `Ctrl-F` `ACK` Acknowledge


format:
- 08 `Ctrl-H` `BS` Backspace `\b`
- 09 `Ctrl-I` `HT` Horizontal Tab `\t`
- 0A `Ctrl-J` `LF` Line Feed `\n`
- 0B `Ctrl-K` `VT` Vertical Tab `\v`
- 0C `Ctrl-L` `FF` Form Feed / page break `\f`
- 0D `Ctrl-M` `CR` Carriage Return `\r`

code extension:
- 0E `Ctrl-N` `SI` Shift In
- 0F `Ctrl-O` `SO` Shift Out
- 1B `Ctrl-[` `ESC` Escape `\e`


Device Control:
- 11 `Ctrl-Q` `DC1` Device Control 1
- 12 `Ctrl-R` `DC2` Device Control 2
- 13 `Ctrl-S` `DC3` Device Control 3
- 14 `Ctrl-T` `DC4` Device Control 4

Transmission:
- 15 `Ctrl-U` `NAK` Negative Acknowledge
- 16 `Ctrl-V` `SYN` Synchronous idle
- 17 `Ctrl-W` `ETB` End of Transmission Block

Separators:
- 1C `Ctrl-\` `FS` File Separator
- 1D `Ctrl-]` `GS` Group Separator
- 1E `Ctrl-^` `RS` Record Separator
- 1F `Ctrl-_` `US` Unit Separator

- 07 `Ctrl-G` `BEL` Bell / beep `\a`

- 10 `Ctrl-P` `DLE` Data Link Escape

- 18 `Ctrl-X` `CAN` Cancel
- 19 `Ctrl-Y` `EM` End of Medium
- 1A `Ctrl-Z` `SUB` Substitute

- 20 `SP` Space

- `Ctrl-?` 7F `DEL` Delete


## DOS control glyphs

/  |x0 |x1 |x2 |x3 |x4 |x5 |x6 |x7 |x8 |x9 |xA |xB |xC |xD |xE |xF
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
0x |   | ☺ | ☻ | ♥ | ♦ | ♣ | ♠ | • | ◘ | ○ | ◙ | ♂ | ♀ | ♪ | ♫ | ☼
1x | ► | ◄ | ↕ | ‼ | ¶ | § | ▬ | ↨ | ↑ | ↓ | → | ← | ∟ | ↔ | ▲ | ▼
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
7x |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ⌂

## Code Pages

### DOS - cp437

 / |x0 |x1 |x2 |x3 |x4 |x5 |x6 |x7 |x8 |x9 |xA |xB |xC |xD |xE |xF
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
8x | Ç | ü | é | â | ä | à | å | ç | ê | ë | è | ï | î | ì | Ä | Å
9x | É | æ | Æ | ô | ö | ò | û | ù | ÿ | Ö | Ü | ¢ | £ | ¥ | ₧ | ƒ
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
Ax | á | í | ó | ú | ñ | Ñ | ª | º | ¿ | ⌐ | ¬ | ½ | ¼ | ¡ | « | »
Bx | ░ | ▒ | ▓ | │ | ┤ | ╡ | ╢ | ╖ | ╕ | ╣ | ║ | ╗ | ╝ | ╜ | ╛ | ┐
Cx | └ | ┴ | ┬ | ├ | ─ | ┼ | ╞ | ╟ | ╚ | ╔ | ╩ | ╦ | ╠ | ═ | ╬ | ╧
Dx | ╨ | ╤ | ╥ | ╙ | ╘ | ╒ | ╓ | ╫ | ╪ | ┘ | ┌ | █ | ▄ | ▌ | ▐ | ▀
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
Ex | α | ß | Γ | π | Σ | σ | μ | τ | Φ | Θ | Ω | δ | ∞ | φ | ε | ∩
Fx | ≡ | ± | ≥ | ≤ | ⌠ | ⌡ | ÷ | ≈ | ° | ∙ | · | √ | ⁿ | ² | ■
 \ |x0 |x1 |x2 |x3 |x4 |x5 |x6 |x7 |x8 |x9 |xA |xB |xC |xD |xE |xF

Box/blocks glyphs

```
 ░▒▓█
         ╔╒ ╦   ╤ ╕╗
         ╓┌ ╥   ┬ ┐╖
┌┬┐ ╓╥╖
├┼┤─╟╫╢  ╠╞ ╬ ═ ╪ ╡╣
└┴┘ ╙╨╜               ▐
 │   ║      ║   │    ▀█▄
╒╤╕ ╔╦╗               ▌
╞╪╡═╠╬╣  ╟├ ╫ ─ ┼ ┤╢
╘╧╛ ╚╩╝
         ╙└ ╨   ┴ ┘╜
         ╚╘ ╩   ╧ ╛╝
```

### Central European - cp852

modified characters from cp437

 / |x0 |x1 |x2 |x3 |x4 |x5 |x6 |x7 |x8 |x9 |xA |xB |xC |xD |xE |xF
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
8x |   |   |   |   |   | ů | ć |   | ł |   | Ő | ő |   | Ź |   | Ć
9x |   | Ĺ | ĺ |   |   | Ľ | ľ | Ś | ś |   |   | Ť | ť | Ł | × | č
Ax |   |   |   |   | Ą | ą | Ž | ž | Ę | ę |   | ź | Č | ş |   |  
Bx |   |   |   |   |   | Á | Â | Ě | Ş |   |   |   |   | Ż | ż |  
Cx |   |   |   |   |   |   | Ă | ă |   |   |   |   |   |   |   | ¤
Dx | đ | Đ | Ď | Ë | ď | Ň | Í | Î | ě |   |   |   |   | Ţ | Ů |  
Ex | Ó |   | Ô | Ń | ń | ň | Š | š | Ŕ | Ú | ŕ | Ű | ý | Ý | ţ | ´
Fx |   | ˝ | ˛ | ˇ | ˘ | § |   | ¸ |   | ¨ | ˙ | ű | Ř | ř |   |
\\ |x0 |x1 |x2 |x3 |x4 |x5 |x6 |x7 |x8 |x9 |xA |xB |xC |xD |xE |xF

### cp861 (Icelandic)

 / |x4 |x5 |x6 |x7 |x8 |x9 |xA |xB |xC |xD
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
8x | ä | à | å | ç | ê | ë | è | Ð | ð | Þ
9x | ö | þ | û | Ý | ý | Ö | Ü | ø | £ | Ø
Ax | Á | Í | Ó | Ú | ¿ | ⌐ | ¬ | ½ | ¼ | ¡

### Koi8-R
Код Обмена Информацией, 8 бит (Kod Obmena Informatsiey, 8 bit) / RFC 1489

 / |x0 |x1 |x2 |x3 |x4 |x5 |x6 |x7 |x8 |x9 |xA |xB |xC |xD |xE |xF
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
8x | ─ | │ | ┌ | ┐ | └ | ┘ | ├ | ┤ | ┬ | ┴ | ┼ | ▀ | ▄ | █ | ▌ | ▐
9x | ░ | ▒ | ▓ | ⌠ | ■ | ∙ | √ | ≈ | ≤ | ≥ |   | ⌡ | ° | ² | · | ÷
Ax | ═ | ║ | ╒ | ё | ╓ | ╔ | ╕ | ╖ | ╗ | ╘ | ╙ | ╚ | ╛ | ╜ | ╝ | ╞
Bx | ╟ | ╠ | ╡ | Ё | ╢ | ╣ | ╤ | ╥ | ╦ | ╧ | ╨ | ╩ | ╪ | ╫ | ╬ | ©
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
Cx | ю | а | б | ц | д | е | ф | г | х | и | й | к | л | м | н | о
Dx | п | я | р | с | т | у | ж | в | ь | ы | з | ш | э | щ | ч | ъ
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
Ex | Ю | А | Б | Ц | Д | Е | Ф | Г | Х | И | Й | К | Л | М | Н | О
Fx | П | Я | Р | С | Т | У | Ж | В | Ь | Ы | З | Ш | Э | Щ | Ч | Ъ

ASCII - Koi8-R:
```
4-                5-
`abcdefghijklmno  pqrstuvwxyz{|}~⌂
ЮАБЦДЕФГХИЙКЛМНО  ПЯРСТУЖВЬЫЗШЭЩЧЪ
C-                D-

6-                7-
@ABCDEFGHIJKLMNO  PQRSTUVWXYZ[\]^_
юабцдефгхийклмно  пярстужвьызшэщчъ
E-                F-
```

Examples:
```
kIRILLICA
Кириллица
```

```
Latin
лАТИН
```

### Windows - cp1252

 / |-0 |-1 |-2 |-3 |-4 |-5 |-6 |-7 |-8 |-9 |-A |-B |-C |-D |-E |-F
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
8- | € |   | ‚ | ƒ | „ | … | † | ‡ | ˆ | ‰ | Š | ‹ | O |   | Ž |
9- |   | ‘ | ’ | “ | ” | • | – | — | ˜ | ™ | š | › | o |   | ž | Ÿ
A- |`NBSP`|¡|¢ | £ | ¤ | ¥ | ¦ | § | ¨ | © | ª | « | ¬ |`SHY`|®| ¯
B- | ° | ± | ² | ³ | ´ | μ | ¶ | · | ¸ | ¹ | º | » | ¼ | ½ | ¾ | ¿
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
C- | À | Á | Â | Ã | Ä | Å | Æ | Ç | È | É | Ê | Ë | Ì | Í | Î | Ï
D- | Ð | Ñ | Ò | Ó | Ô | Õ | Ö | × | Ø | Ù | Ú | Û | Ü | Ý | Þ | ß
   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
E- | à | á | â | ã | ä | å | æ | ç | è | é | ê | ë | ì | í | î | ï
F- | ð | ñ | ò | ó | ô | õ | ö | ÷ | ø | ù | ú | û | ü | ý | þ | ÿ

- `NBSP` [Non-breakable space](https://en.wikipedia.org/wiki/Non-breaking_space) 00A0 ` `
- `SHY` [Soft Hyphen](https://en.wikipedia.org/wiki/Soft_hyphen) 00AD `­`
