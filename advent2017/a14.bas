DECLARE SUB knothash (in$, hash())
SCREEN 12
CLS
in$ = "hfdlxzhv"
DIM arr(16)
p1 = 0
p2 = 0
FOR i = 1 TO 128
    CALL knothash(in$ + "-" + MID$(STR$(i - 1), 2), arr())
    FOR j = 0 TO 15
        v = arr(j + 1)
        FOR z = 0 TO 7
            bit = v MOD 2
            v = INT(v / 2)
            IF bit = 1 THEN
                PSET (i, j * 8 + 7 - z + 1)
                p1 = p1 + 1
            END IF
        NEXT
    NEXT
NEXT
FOR i = 1 TO 128
    FOR j = 1 TO 128
        IF POINT(i, j) THEN
            p2 = p2 + 1
        END IF
        PAINT (i, j), 0
    NEXT
NEXT
PRINT p1
PRINT p2

SUB knothash (in$, hash())
L = LEN(in$)
DIM lengths(L + 5)
DIM arr(256)
DIM scratch(256)
FOR i = 1 TO 256
    arr(i) = i - 1
NEXT
FOR i = 1 TO L
    lengths(i) = ASC(MID$(in$, i, 1))
NEXT
lengths(L + 1) = 17
lengths(L + 2) = 31
lengths(L + 3) = 73
lengths(L + 4) = 47
lengths(L + 5) = 23
cur = 0
skp = 0
FOR i = 1 TO 64
    FOR li = 1 TO UBOUND(lengths)
        L = lengths(li)
        FOR j = 0 TO L - 1
            scratch(j + 1) = arr((cur + j) MOD 256 + 1)
        NEXT
        FOR j = 0 TO L - 1
            arr((cur + L - j - 1) MOD 256 + 1) = scratch(j + 1)
        NEXT
        cur = (cur + L + skp) MOD 256
        skp = (skp + 1) MOD 256
    NEXT
NEXT

FOR i = 0 TO 15
    h = arr(1 + 16 * i)
    FOR j = 1 TO 15
        h = h XOR arr(1 + 16 * i + j)
    NEXT
    hash(i + 1) = h
NEXT
END SUB

